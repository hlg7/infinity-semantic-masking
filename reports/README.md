# 实验 01：结果与运行记录索引

本目录属于 **Infinity 整类 semantic mask 实验**。正式结果、早期验证与运行记录按下表查找；保留原路径以兼容已有脚本。

“GitHub 已收录”指该仓库提交的内容；“仅本地”指被 Git 忽略的辅助文件，在网页上不能直接打开。

## 1. 正式实验结果：优先看这里

300 个 prompt，六类各 50 条，seed 42，13 个 scale，7,800 张主实验图。

| 入口 | 内容 | 保存位置 |
|---|---|---|
| [csfm50_full_review/review.md](csfm50_full_review/review.md) | 正式实验核对报告 | GitHub 已收录 |
| [六类全 scale 对照图](csfm50_full_review/examples) | 每类一个 prompt，全部 prefix/suffix；156 张原图排成六张对照图，附来源和哈希清单 | GitHub 已收录 |
| [Retention 曲线](csfm50_full_review/retention.png) | 各类 baseline 正确样本的语义保留率 | GitHub 已收录，另有 PDF |
| [成功率曲线](csfm50_full_review/success_rate.png) | 全样本成功率与 baseline | GitHub 已收录，另有 PDF |
| [audit_summary.json](csfm50_full_review/audit_summary.json) | 7,800 项评分和 448 行聚合统计核对 | GitHub 已收录 |
| [曲线 CSV](csfm50_full/evaluation/scores/scale_curves.csv) | 全 scale、子类型、retention、paired delta、count MAE | GitHub 已收录 |
| [逐项评分 JSONL](csfm50_full/evaluation/scores/results.jsonl) | 7,800 项评分及原始观测 | GitHub 已收录 |
| [分组摘要](csfm50_full/evaluation/scores/summary.json) | 各类别、子类型和条件的汇总 | GitHub 已收录 |
| [输入快照](csfm50_full/inputs) | 本次运行冻结的 annotations、checks 与哈希 | GitHub 已收录 |
| [生成记录](csfm50_full/generation/runs.jsonl) | 图片 ID、SHA256、mask 条件、token 与审计路径 | GitHub 已收录 |
| [六项评分修复](csfm50_full/evaluation/scores/repairs/category_other_v1/repair_report.json) | 原始异常回答与 other 归一化记录 | GitHub 已收录 |

`csfm50_full/` 包含正式实验的输入与结果记录，**不包含全部 7,800 张原图**。原图和逐层 audit 文件保存在原实验 Runpod workspace；生成记录中的远端路径用于溯源。

## 2. 预实验与早期验证

| 目录 | 阶段 | 保存位置 |
|---|---|---|
| [pilot_review](pilot_review) | 10 prompt × 4 条件，40 图预实验的对照图、曲线和报告 | GitHub 已收录 |
| `csfm50_pilot/` | 上述预实验的完整本地图片及评分输出 | 仅本地 |
| [full_review](full_review) | 单个多语义 prompt、六类、全部 scale 的 151 图验证报告 | GitHub 已收录 |
| `runpod_full/` | 上述 151 图验证的完整本地图片及评分输出 | 仅本地 |
| `annotation_smoke/` | 早期标注接口验证输出 | 仅本地 |
| [annotation_responses](annotation_responses) | 本地测试使用的已保存 Qwen 响应 | GitHub 已收录 |
| `plan_smoke/`、`plan_full/` | 本地 plan-only 验证生成的计划 | 仅本地，可重新生成 |

注意：`runpod_full` / `full_review` 是**早期单 prompt 的全 scale 验证**；`csfm50_full` / `csfm50_full_review` 才是 **300 prompt 的正式实验**。

## 3. 数据验证与复现依赖

| 文件 | 用途 | 保存位置 |
|---|---|---|
| [t5_source.json](t5_source.json) | 下载脚本读取的固定 T5 版本 | GitHub 已收录，保留 |
| [infinity_scale_index.patch](infinity_scale_index.patch) | 源码初始化脚本应用的 scale_ind 补丁 | GitHub 已收录，保留 |
| [csfm50_repair_validation.json](csfm50_repair_validation.json) | 14 条标注修正及 300 条 T5 验证记录 | GitHub 已收录 |
| `csfm50_tokens.json` / `.md` | 300 prompt 的本地 T5 token 验证结果 | 仅本地 |
| `smoke_tokens.json` / `.md` | 单 prompt token 检查输出 | 仅本地，可重新生成 |
| `csfm50_preparation.json` | 当时的数据准备阶段记录 | 仅本地，历史状态 |
| `annotations_completed.tar` | 人工修正前的历史标注快照，与最终标注不同 | 仅本地，保留溯源 |

最终标注与标注原始回答在 [data/csfm50_v1](../data/csfm50_v1/README.md)。

## 4. 本地运行与传输记录

以下文件仅本地保留，不上传 GitHub：

- `runpod_deployment.json`、`runpod_deployment_previous.json`、`runpod_known_hosts`：当前及历史部署/连接信息。
- `csfm50_full_launch.md`：正式实验启动记录。
- `local_checks.log`、`local_status.json`：早期本地验证记录，不能当成当前实验状态。
- `runpod_bundle.tar.gz`、`dataset_pilot_update.tar`、`batch_annotation_update.tar`：历史传输包，暂保留。
- `readme_example_sources/`：README 六类样例的 156 张完整实验原始 PNG 与下载清单；排版后的对照图和来源清单收录于 `csfm50_full_review/examples/`。
- `organization_cleanup_20260914.json`：本次重复压缩包清理的校验记录。

## 5. 2026-09-14 整理记录

已逐文件比较，确认以下压缩包的所有文件都与现有解压目录完全一致后，删除了它们：

| 已删除压缩包 | 保留的解压目录 | 校验文件数 |
|---|---|---:|
| `runpod_full.tar` | `runpod_full/` | 573 |
| `csfm50_pilot.tar` | `csfm50_pilot/` | 140 |
| `csfm50_full_scores.tar.gz` | `csfm50_full/` | 20 |

释放约 **228 MB**（十进制）。结果目录未移动，标注历史、环境、缓存、模型源码及两份评分器均保留。
