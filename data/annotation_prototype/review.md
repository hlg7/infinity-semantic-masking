# 整类 semantic mask 清单

这是文本标注和 mask 目标的检查结果，不是生成实验或语义评分结果。
`other` 永不 mask；未出现的 semantic 跳过。字符位置采用左闭右开区间。

## all_six

Two red round smooth plates are to the left of three blue oval rough bowls.

标注说明：All six classes, with two disjoint mentions in each attribute/count class. Structural fixture only: plural attribute referents are ambiguous under the frozen evaluator.

- **object**：`plates` + `bowls`；位置 `[[21, 27], [69, 74]]`
- **color**：`red` + `blue`；位置 `[[4, 7], [53, 57]]`
- **shape**：`round` + `oval`；位置 `[[8, 13], [58, 62]]`
- **texture**：`smooth` + `rough`；位置 `[[14, 20], [63, 68]]`
- **count**：`Two` + `three`；位置 `[[0, 3], [47, 52]]`
- **spatial_relation**：`to the left of`；位置 `[[32, 46]]`

保留的 other：` ` + ` ` + ` ` + ` ` + ` are ` + ` ` + ` ` + ` ` + ` ` + ` ` + `.`

跳过：无

Token 映射：待接入实际 backbone tokenizer 后验证。

## repeated_color

A red car is behind a red truck, and a red bicycle is in front of the truck.

标注说明：All three red occurrences and both truck occurrences must be included. The repeated truck noun can refer to the same entity; masking is by mention, not deduplicated entity.

- **object**：`car` + `truck` + `bicycle` + `truck`；位置 `[[6, 9], [26, 31], [43, 50], [70, 75]]`
- **color**：`red` + `red` + `red`；位置 `[[2, 5], [22, 25], [39, 42]]`
- **spatial_relation**：`behind` + `in front of`；位置 `[[13, 19], [54, 65]]`

保留的 other：`A ` + ` ` + ` is ` + ` a ` + ` ` + `, and a ` + ` ` + ` is ` + ` the ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## compound_nouns

A black remote control is below a rectangular picture frame and above a blue pencil case.

标注说明：Lexicalized multiword object names stay whole; attributes remain separate.

- **object**：`remote control` + `picture frame` + `pencil case`；位置 `[[8, 22], [46, 59], [77, 88]]`
- **color**：`black` + `blue`；位置 `[[2, 7], [72, 76]]`
- **shape**：`rectangular`；位置 `[[34, 45]]`
- **spatial_relation**：`below` + `above`；位置 `[[26, 31], [64, 69]]`

保留的 other：`A ` + ` ` + ` is ` + ` a ` + ` ` + ` and ` + ` a ` + ` ` + `.`

跳过：texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## contextual_orange

An orange is above an orange cup.

标注说明：The first orange is an object, the second a color. Global string replacement would mask the wrong occurrence.

- **object**：`orange` + `cup`；位置 `[[3, 9], [29, 32]]`
- **color**：`orange`；位置 `[[22, 28]]`
- **spatial_relation**：`above`；位置 `[[13, 18]]`

保留的 other：`An ` + ` is ` + ` an ` + ` ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_and_material

A smooth wooden table is behind a striped fabric chair and a polka-dotted cushion.

标注说明：Texture includes surface and pattern. Material-only words wooden/fabric remain other under the existing six-semantic scope.

- **object**：`table` + `chair` + `cushion`；位置 `[[16, 21], [49, 54], [74, 81]]`
- **texture**：`smooth` + `striped` + `polka-dotted`；位置 `[[2, 8], [34, 41], [61, 73]]`
- **spatial_relation**：`behind`；位置 `[[25, 31]]`

保留的 other：`A ` + ` wooden ` + ` is ` + ` a ` + ` fabric ` + ` and a ` + ` ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## counts_and_containment

2 marbles are inside one bowl, and three coins are outside the bowl.

标注说明：Numeric and written explicit counts; repeated bowl; no inferred count from articles or plural endings.

- **object**：`marbles` + `bowl` + `coins` + `bowl`；位置 `[[2, 9], [25, 29], [41, 46], [63, 67]]`
- **count**：`2` + `one` + `three`；位置 `[[0, 1], [21, 24], [35, 40]]`
- **spatial_relation**：`inside` + `outside`；位置 `[[14, 20], [51, 58]]`

保留的 other：` ` + ` are ` + ` ` + ` ` + `, and ` + ` ` + ` are ` + ` the ` + `.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## legacy_scene_expanded

A dog is clearly visible in a grassy garden, with a low stone wall and distant trees visible under soft daylight.

标注说明：Original object_001 prompt. Whole-object mask now includes background entities garden, wall and trees as well as dog. Grassy/stone describe covering/material; low is size, distant is qualitative distance, and under soft daylight is illumination. These stay other in this provisional rule set.

- **object**：`dog` + `garden` + `wall` + `trees`；位置 `[[2, 5], [37, 43], [62, 66], [79, 84]]`
- **spatial_relation**：`in`；位置 `[[25, 27]]`

保留的 other：`A ` + ` is clearly visible ` + ` a grassy ` + `, with a low stone ` + ` and distant ` + ` visible under soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## only_other

Soft daylight, cinematic lighting.

标注说明：No intervention targets; preserve prompt for baseline handling by a future generator.


保留的 other：`Soft daylight, cinematic lighting.`

跳过：object, color, shape, texture, count, spatial_relation

Token 映射：待接入实际 backbone tokenizer 后验证。
