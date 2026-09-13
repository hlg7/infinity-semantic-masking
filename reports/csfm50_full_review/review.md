# 300 prompt 完整实验汇总

全部 7,800 张图片已生成；7,800 项评分经明确的六项类别修正后完成，448 行曲线数据已独立重算核对。

## 六项修正

这是一项有记录的事后类别归一化，不是重新调用模型：silver（3 项）、gray（2 项）、octagonal（1 项）归入原有 allowed_answers 的 other。原始 JSON、两次模型回答、原始错误、SHA256 和修复说明均保留在 evaluation/scores/repairs/category_other_v1。六项最终均判 incorrect；另外 7,794 项评分文件哈希完全不变。标注、图片、问题、目标答案和评分函数未改变。

这里的 other 是评分答案类别，与 prompt 标注中的 other 是不同概念。

## Baseline

| Semantic | 正确数 / 50 | 成功率 |
|---|---:|---:|
| object | 48/50 | 96% |
| color | 47/50 | 94% |
| shape | 29/50 | 58% |
| texture | 44/50 | 88% |
| count | 28/50 | 56% |
| spatial_relation | 23/50 | 46% |

Retention 仅使用各类 baseline 正确的样本，分母分别为上表正确数。Missing、ambiguous 是现有协议下成功率为 0 的结果，不是执行错误。

## 验证与文件

- 7,800 条唯一评分、逐样本 baseline 配对、paired delta 已核对。
- 448 行成功率、retention、数量误差等聚合结果已重算核对。
- 无 evaluation_error 或 missing_output。
- 本地包含全部评分、生成清单、输入快照及六项修复备份；7,800 张原图仍保存在 Runpod，此轮没有完整下载图片。
- 图表是单 seed 的探索性自动评分结果，尚未进行完整图片人工审查。

![Success rate](success_rate.png)

![Retention](retention.png)
