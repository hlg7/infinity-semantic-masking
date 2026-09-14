# 实验 01：整类 semantic 标注原型

本目录保留 Infinity 实验早期的 8 条人工标注样例，用于检查完整分段、整类片段合并和字符跨度接口。它不是正式实验集，也不是自动标注准确率评估。

正式实验已完成：300 条 prompt、真实 T5 校验、7,800 张生成图片和评分汇总。当前入口见 [实验 README](../../README.md)、[正式数据集](../csfm50_v1/README.md) 和 [共享标注规则](../../configs/annotation_policy.json)。本目录的 `compiled.json` 是 tokenizer 接入前的接口快照，不用于完整实验生成。

## 输入与输出

输入为原文 prompt 及逐段 semantic 标签，输出为六类加 `other` 的片段表，以及每个非空 semantic 的全部字符跨度。同类分散或重复的片段合并为一个 mask 目标；`other` 不参与 mask。

- [输入标注](annotations.json)
- [编译结果](compiled.json)
- [可读 mask 清单](review.md)
- [早期 segments 输出指令草案](annotation_instructions.md)

每个字符只属于一个片段；片段连接必须逐字符还原原文。字符区间为 Python 索引 `[start, end)`。片段内不重写、翻译或改变大小写。结构校验不等于语义分类正确。

六类为 `object`、`color`、`shape`、`texture`、`count`、`spatial_relation`。实际生成使用最终标注和 FLAN-T5-XL 的真实 token 映射，完整文本 embedding 与 global conditioning 保持固定。

## 编译这些样例

在实验根目录运行：

```bash
python3 semantic_masking.py \
  --input data/annotation_prototype/annotations.json \
  --output outputs/annotation_prototype/compiled.json \
  --review outputs/annotation_prototype/review.md
```

自动标注入口是 `annotate_semantics.py`；正式数据集的批量标注入口是 `scripts/annotate_dataset_gpu.py`。标注、生成与评分分别维护，评分目标与整类 mask 片段通过 prompt ID 对接。
