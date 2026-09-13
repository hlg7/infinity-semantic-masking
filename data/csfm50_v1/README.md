# CSFM 衍生受控 prompt 集：50 × 6

截至 2026-09-14，300 条标注与真实 T5 校验、40 图预实验、7,800 图完整实验及评分汇总均已完成。无需访问原 STAR 目录。

| 文件 | 内容 |
|---|---|
| `source_prompts.json` | 原始 prompt、历史单词 spans、目标与子类型 |
| `prompts.json` | 300 条 id、prompt、target_semantic |
| `annotations.json` | 完整实验使用的最终分段标注 |
| `annotations_qwen3vl/` | 原始回答、逐词标签、校验及溯源 |
| `manual_corrections_v1.json` / `.md` | 14 条失败标注的人工修正 |
| `checks.json` | 原样迁移的 300 条编译评分任务与真值 |
| `source_manifest.json` / `checks_source.json` | 历史来源及 SHA256 |
| `pilot_*.json` | 10 prompt 预实验输入、评分任务及选取说明 |

六类各 50 条，每条只 mask 其 target_semantic 的全部片段。旧 spans 只作为已知目标的校验依据，不构造新版完整 mask。other 不 mask。

Qwen3-VL-8B-Instruct 使用文本输入，每批 8 条，返回六类的 [index, original_word] 列表；未列出词恢复为 other。模型提示与验证代码共享 [annotation_policy.json](../../configs/annotation_policy.json)。当前将 dark/pale/cloudy/tiled 等归为 other；这是有限的数据集策略，不是完备语言学分类。

286 条自动接受，其余 14 条经记录在案的人工修正。唯一词可依据原文修正错误索引；重复词的不明确位置不能这样修正。最终冻结输入见 [reports/csfm50_full/inputs](../../reports/csfm50_full/inputs)。

该集合来自既有实验的 CSFM 衍生受控模板，包含十个场景家族，不作为独立标准 benchmark 声称。改标注需要重新生成相应干预图片；更新评分器则可以重评已有图片。
