# Infinity 单 prompt 完整实验检查

结论：生成、整类 semantic mask、六类评分和曲线汇总已跑通。自动评分存在检测误差，不能把本样例的曲线直接视为语义因果结论。

## 完整性与实现核对

- 1 个 prompt，seed 42，13 个 scale，六类 semantic 的全部前缀／后缀边界。
- 151 张实验图片已下载，全部 SHA256 与远端生成记录一致。
- 151 × 32 层 × 13 scale = 62,816 条审计记录全部通过：每层每 scale 恰好一条；只有指定 scale 删除指定 semantic 的全部 token。
- object 一起 mask plate/cup/spoons；color 一起 mask red/blue；texture 一起 mask smooth/striped。shape 为 round，count 为 two，spatial_relation 为 to the left of；other 保留。
- 前缀为 1..k，后缀为 k+1..13。基线、全程 mask 的重复边界复用同一图片。
- 六类全程 mask 重复生成一致，无 mask 与原始推理一致。
- 260 项评分都有结果，包含 correct 179、incorrect 68、missing 13。missing 是目标缺失判断，不是执行失败。
- 364 行曲线数据已生成（包含语义总分与子类型）。六类总分共 168 个边界点均重新从逐项评分计算，与 CSV 一致。

## 图片和评分抽查

查看了六类在 baseline、prefix_06、suffix_06、full_mask 下的对照图（19 张不同图片），并进一步查看基线原图及检测框。

1. color：前 6 个 scale 或全部 scale 屏蔽 red/blue 后，图中变为白色盘子且杯子缺失；对应颜色错误／目标缺失与图像相符。后 7 个 scale 屏蔽时仍保留红盘、蓝杯。
2. texture：前段 mask 后杯子条纹弱化或消失，而盘子仍光滑；两项合并后为 0.5，需同时查看 surface 与 pattern 子类型。
3. spatial_relation：前段 mask 后杯子与盘子更多呈重叠居中，后段 mask 仍保留盘子在左、杯子在右的布局。
4. shape：所有条件下盘子都被评为 round；抽查图中盘子确实仍圆，不能据此判断 mask 未生效，审计记录显示 round token 已按计划删除。
5. count：基线提示 two spoons，但图中有一件双头勺状畸形物及杯子中的两件餐具，数量本身有歧义。DINO 保留三处独立检测框，并非简单重复框。基线 count 失败，不能据此测量“原本正确的数量在 mask 后是否保留”；count retention 为空是正确处理，应看原始成功率和 MAE。
6. object：发现明确的 cup 检测误差。object full_mask 的 cup 检测框覆盖红色盘子（置信度约 0.412），导致 cup 被记为存在。保留原始评分，未针对本例修改阈值或重写评分标准；正式数据集应继续抽查检测结果。

## 下一轮数据准备

已将原始 csfm50_v1 数据复制到独立实验目录 data/csfm50_v1。核对为 300 条、六类各 50 条，并保存来源 SHA256。数据内容保持不变。

已生成 300 条完整 semantic 分组的标注请求，尚未提交模型标注。旧的单词 spans 仅保留用于溯源，不作为新版 mask 输入。

接下来完成分组标注和 T5 token 检查、迁移逐 prompt 评分配置、按所属 semantic 为每条 prompt 生成全 scale 计划；先抽每类少量 prompt 跑通，再启动 300 条数据集实验。当前尚未启动数据集 GPU 实验。

## 文件

- [六类评分曲线](semantic_curves.png) / [PDF](semantic_curves.pdf)
- [图片对照表](image_contact_sheet.jpg)
- [count 基线检测框](baseline_count_boxes.png)
- [cup 检测误差](object_cup_false_positive.png)
- [机器核对结果](audit_summary.json)
- 完整生成／评分记录：../runpod_full
