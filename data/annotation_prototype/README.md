# 整类 semantic mask：第一步检查

## 自动入口（新增）

`annotate_semantics.py` 已接上原始 prompt → Qwen 词级类别标签 → 整类 mask 清单。程序对原文的词编号，模型只返回类别；位置和原文由程序恢复。默认使用 Runpod 公共 Qwen3-32B-AWQ，运行环境需设置 `RUNPOD_API_KEY`，不需要启动 GPU pod。

```bash
python3 annotate_semantics.py --prompt "An orange is above an orange cup." --output outputs/auto-semantic-smoke
```

输出为 `annotations.json`、`masks.json` 和 `review.md`。加 `--prepare-only` 可只生成请求，不调用模型。也支持 `--input` 输入 id/prompt JSON 列表，或 `--responses-dir` 导入通过 Runpod MCP 获取的原始 JSON 结果。

当前状态：2026-09-13 经用户授权，已通过 Runpod MCP 对 `An orange is above an orange cup.` 完成一次真实 Qwen 调用，并用 `--responses-dir` 将原始响应编译为三个整类 mask 目标。object=`orange + cup`，color=第二个 `orange`，spatial_relation=`above`，other 保留；费用 $0.0051。原始响应在 `outputs/auto-semantic-live-responses/p000.json`，清单在 `outputs/auto-semantic-smoke/review.md`。这是单条执行验证，不是分类准确率评估；Python 直连 HTTP 传输尚未实测，Infinity 图像生成尚未接入。

本目录是新实验的文本输入原型。六类沿用 `object`、`color`、`shape`、`texture`、`count`、`spatial_relation`；`other` 只保存剩余原文，永不作为干预目标。

已实现：Qwen 词级自动标注调用、完整标注的结构校验、字符位置计算、整类片段合并、可读 mask 清单，以及供实际 backbone 使用的 token 映射校验接口。**尚未接入 Infinity 生成。** 本目录原有 8 条样例由 Codex 逐条标注，用于检查接口，不是 Qwen 输出或正式实验集。实际模型指令位于 `annotate_semantics.py` 的 `SYSTEM` 常量；下方链接的指令草案是早期 segments 输出方案，仅供历史参考。

查看 [mask 清单](review.md)、[输入标注](annotations.json)、[编译结果](compiled.json)、[自动标注指令草案](annotation_instructions.md)。

## 现有实现核查

- `check_masking.py` 已对 `item['spans']` 中所有片段取 token 并集；底层支持多个片段。历史 `data/csfm50_v1/prompts.json` 只提供一个目标，没有完整六类标注。不能把旧数据里未标注的内容直接视为 `other`。
- `validate_prompts.py` 使用 STAR 的 CLIP slow/fast tokenizer 对照，并检查上下文长度和字符跨度。新代码将字符标注与 backbone tokenizer 分离，STAR 的 token 索引不进入新数据。
- 原干预是在选定 scale 的所有 cross-attention 层中，将目标文本 key 的 attention bias 设为负无穷；完整文本特征和全局条件保持固定。清单里的“mask”指这一目标集合，不是删除词、替换 prompt 或重新编码残缺文本。
- 原 `schedules(N)` 的 `k` 是边界：prefix=`1..k`，suffix=`k+1..N`，`k=0..N`。两端的 baseline/full-mask 复用，合计 `2N` 个独立 scale 条件。新数据不预设 Infinity 的 scale 数、分辨率或采样参数。
- `semantic-evaluators` 已独立于 backbone，接受 image/task JSONL；它不负责 prompt 划分和 scale mask。此次不修改该包和冻结评分规则。

## 当前标注约定（供检查）

每个字符只属于一个片段，每个片段只属于一类；片段顺序连接必须逐字符还原原 prompt。片段内不重写、不翻译、不改大小写。字符区间是 Python 字符索引 `[start, end)`，不是字节或 token 索引。

| 类别 | 标注范围 |
|---|---|
| object | 所有明确的实体/场景名词，包括背景和重复提及。保留原来的复数词形；`remote control`、`picture frame` 等复合名称整体标注。颜色、数量等修饰语单独分类。 |
| color | 明确的颜色表达；按上下文区分同形词，如水果 `orange` 和颜色 `orange`。 |
| shape | 明确的形状表达，如 `round`、`oval`、`rectangular`；不将大小词当形状。 |
| texture | 显式表面粗糙度和重复图案，包括 `smooth`、`rough`、`striped`、`polka-dotted`；纯材料词 `wooden`、`fabric` 暂归 other，不能由材料推断纹理。 |
| count | 明确的数量表达，包括数字和数词；`a/an` 作为冠词归 other，不从复数词尾推断额外数量片段。 |
| spatial_relation | 明确的位置、深度、包含关系短语，整体标注 `to the left of`、`in front of` 等；短语内部功能词也属于关系。照明用法 `under soft daylight` 不作为实体间位置关系。 |
| other | 冠词、连接词、系动词、片段外的空白和标点，以及不属于六类的动作、材料、大小、风格、照明等表达。 |

不确定的表达需要基于上下文检查，不能因为词典没收录就自动归 other。结构校验能防止漏字符、错位置，**不能证明语义分类正确**。这些约定应在扩展正式 prompt 集前固定。

新 mask 会包括所有属于该类的文本。因此旧样例中 object 从 `dog` 扩展为 `dog + garden + wall + trees`。同时，mask count 时名词复数仍保留，mask object 时颜色或数量仍保留；这些是文本层面整类干预的预期行为，不意味着模型中的全部语义信息都被消除了。

## 使用

在研究仓库根目录运行；纯文本模式仅需要 Python 标准库：

```bash
python3 semantic_masking.py \
  --input data/semantic_groups_v1/annotations.json \
  --output data/semantic_groups_v1/compiled.json \
  --review data/semantic_groups_v1/review.md

python3 -m unittest discover -s tests -p 'test_semantic_masking.py' -v
```

编译结果每个 prompt 保存六类加 other 的片段表，以及每个非空 semantic 的一条 `targets` 记录。记录含 `prompt_id`、`semantic`、全部 `spans` 和 `target_fragments`。同类重复词保留全部位置；空类跳过；只有 other 的 prompt 产生零条干预目标，可由后续生成器保留 baseline。

`--tokenizer`、`--locator`、`--context-length` 可选，用于本地 tokenizer 预检，需安装相应的 `transformers` 依赖并提供已下载的实际 tokenizer。CLI 对同一原文以 slow/fast tokenizer 无截断、无 padding 编码，核对完整 token ID；若 locator 不支持 offsets、两者 ID 不一致、超长、语义字符丢失或 token 横跨不同类别，则拒绝输出。特殊 token 不 mask；允许 token 吸收相邻空白，不允许连带其他类别的文字或标点。

该 CLI 的本地 tokenizer 预检不能代替生成器集成验证。Infinity 适配器需要检查其真实文本预处理、特殊 token、最大长度和条件分支布局，再将实际使用的无 padding token IDs 交给 `map_tokens`。若 backbone 改写或 strip prompt，必须显式核对字符映射，不能静默沿用原位置。若 tokenizer 无法分离两个类别，先检查标注/分词问题，不可偷偷扩大 mask 范围。

本次环境没有 `transformers`、Infinity tokenizer 或模型权重。提交的 `compiled.json` 因此明确标记 `pending_backbone_tokenizer`，不保存模拟 token 索引。单元测试用合成 offsets 检查选择逻辑，不声称它们是 Infinity 分词结果。

## 后续生成与评分接口

后续生成器按 `prompt_id + seed` 创建共享 baseline，按 `prompt_id + semantic + seed + scale condition` 创建干预图像；每一条件使用该类全部 token。跨类的 full-mask 不能复用同一图像；同类 prefix/suffix 的等价端点可以复用。

完整六类划分会暴露多个对象和多个属性，但旧冻结 evaluator 的一行只判断一个对象/属性/数量/有序对象对。接入评分时需给每条检查绑定明确的 referent 和 expected，再将多条检查关联到同一图像，保持原指标定义。不能将 `red + blue` 塞进单个 color expected，也不能把整类的文本片段直接当作 detector query。

现有属性/关系评分要求对象指代唯一。例如 `Two red plates` 的属性评分不能自行扩展成“所有 plate 都红”，必须按原规则保留 ambiguous，或在正式 prompt 设计时使用可唯一指代的不同对象。这里的复数样例仅检查分词/mask 结构。多目标如何汇总成每 prompt 的整类分数尚待正式实验协议定义，本次没有擅自改变指标或汇总权重。

本步骤未运行 GPU、生成图像、改写旧实验结果或推送 GitHub。
