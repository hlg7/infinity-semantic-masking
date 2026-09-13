# 整类 semantic mask 清单

这是文本标注和 mask 目标的检查结果，不是生成实验或语义评分结果。
`other` 永不 mask；未出现的 semantic 跳过。字符位置采用左闭右开区间。

## object_001

A dog is clearly visible in a grassy garden, with a low stone wall and distant trees visible under soft daylight.

- **object**：`dog` + `garden` + `wall` + `trees`；位置 `[[2, 5], [37, 43], [62, 66], [79, 84]]`
- **spatial_relation**：`in`；位置 `[[25, 27]]`

保留的 other：`A ` + ` is clearly visible ` + ` a grassy ` + `, with a low stone ` + ` and distant ` + ` visible under soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_002

A cat is clearly visible in a grassy garden, with a low stone wall and distant trees visible under soft daylight.

- **object**：`cat` + `garden` + `wall` + `trees`；位置 `[[2, 5], [37, 43], [62, 66], [79, 84]]`
- **spatial_relation**：`in`；位置 `[[25, 27]]`

保留的 other：`A ` + ` is clearly visible ` + ` a grassy ` + `, with a low stone ` + ` and distant ` + ` visible under soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_003

A bicycle is clearly visible in a grassy garden, with a low stone wall and distant trees visible under soft daylight.

- **object**：`bicycle` + `garden` + `wall` + `trees`；位置 `[[2, 9], [41, 47], [66, 70], [83, 88]]`
- **spatial_relation**：`in`；位置 `[[29, 31]]`

保留的 other：`A ` + ` is clearly visible ` + ` a grassy ` + `, with a low stone ` + ` and distant ` + ` visible under soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_004

A bench is clearly visible in a grassy garden, with a low stone wall and distant trees visible under soft daylight.

- **object**：`bench` + `garden` + `wall` + `trees`；位置 `[[2, 7], [39, 45], [64, 68], [81, 86]]`
- **spatial_relation**：`in`；位置 `[[27, 29]]`

保留的 other：`A ` + ` is clearly visible ` + ` a grassy ` + `, with a low stone ` + ` and distant ` + ` visible under soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_005

A wheelbarrow is clearly visible in a grassy garden, with a low stone wall and distant trees visible under soft daylight.

- **object**：`wheelbarrow` + `garden` + `wall` + `trees`；位置 `[[2, 13], [45, 51], [70, 74], [87, 92]]`
- **spatial_relation**：`in`；位置 `[[33, 35]]`

保留的 other：`A ` + ` is clearly visible ` + ` a grassy ` + `, with a low stone ` + ` and distant ` + ` visible under soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_006

A mug is clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`mug` + `table` + `chairs` + `window`；位置 `[[2, 5], [42, 47], [60, 66], [84, 90]]`
- **spatial_relation**：`on` + `in`；位置 `[[25, 27], [99, 101]]`

保留的 other：`A ` + ` is clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_007

A teapot is clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`teapot` + `table` + `chairs` + `window`；位置 `[[2, 8], [45, 50], [63, 69], [87, 93]]`
- **spatial_relation**：`on` + `in`；位置 `[[28, 30], [102, 104]]`

保留的 other：`A ` + ` is clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_008

A coffee pot is clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`coffee pot` + `table` + `chairs` + `window`；位置 `[[2, 12], [49, 54], [67, 73], [91, 97]]`
- **spatial_relation**：`on` + `in`；位置 `[[32, 34], [106, 108]]`

保留的 other：`A ` + ` is clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_009

A sugar bowl is clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`sugar bowl` + `table` + `chairs` + `window`；位置 `[[2, 12], [49, 54], [67, 73], [91, 97]]`
- **spatial_relation**：`on` + `in`；位置 `[[32, 34], [106, 108]]`

保留的 other：`A ` + ` is clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_010

A tray is clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`tray` + `table` + `chairs` + `window`；位置 `[[2, 6], [43, 48], [61, 67], [85, 91]]`
- **spatial_relation**：`on` + `in`；位置 `[[26, 28], [100, 102]]`

保留的 other：`A ` + ` is clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_011

A chair is clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`chair` + `library` + `bookshelves` + `walls` + `window`；位置 `[[2, 7], [38, 45], [52, 63], [74, 79], [118, 124]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[27, 29], [64, 69], [102, 109]]`

保留的 other：`A ` + ` is clearly visible ` + ` a quiet ` + `, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_012

A table is clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`table` + `library` + `bookshelves` + `walls` + `window`；位置 `[[2, 7], [38, 45], [52, 63], [74, 79], [118, 124]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[27, 29], [64, 69], [102, 109]]`

保留的 other：`A ` + ` is clearly visible ` + ` a quiet ` + `, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_013

A bookcase is clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`bookcase` + `library` + `bookshelves` + `walls` + `window`；位置 `[[2, 10], [41, 48], [55, 66], [77, 82], [121, 127]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[30, 32], [67, 72], [105, 112]]`

保留的 other：`A ` + ` is clearly visible ` + ` a quiet ` + `, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_014

A ladder is clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`ladder` + `library` + `bookshelves` + `walls` + `window`；位置 `[[2, 8], [39, 46], [53, 64], [75, 80], [119, 125]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[28, 30], [65, 70], [103, 110]]`

保留的 other：`A ` + ` is clearly visible ` + ` a quiet ` + `, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_015

A reading lamp is clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`reading lamp` + `library` + `bookshelves` + `walls` + `window`；位置 `[[2, 14], [45, 52], [59, 70], [81, 86], [125, 131]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[34, 36], [71, 76], [109, 116]]`

保留的 other：`A ` + ` is clearly visible ` + ` a quiet ` + `, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_016

A water bottle is clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`water bottle` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[2, 14], [43, 54], [66, 71], [84, 89], [116, 119]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[34, 40], [90, 97]]`

保留的 other：`A ` + ` is clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_017

A backpack is clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`backpack` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[2, 10], [39, 50], [62, 67], [80, 85], [112, 115]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[30, 36], [86, 93]]`

保留的 other：`A ` + ` is clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_018

An umbrella is clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`umbrella` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[3, 11], [40, 51], [63, 68], [81, 86], [113, 116]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[31, 37], [87, 94]]`

保留的 other：`An ` + ` is clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_019

A watering can is clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`watering can` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[2, 14], [43, 54], [66, 71], [84, 89], [116, 119]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[34, 40], [90, 97]]`

保留的 other：`A ` + ` is clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_020

A basket is clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`basket` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[2, 8], [37, 48], [60, 65], [78, 83], [110, 113]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[28, 34], [84, 91]]`

保留的 other：`A ` + ` is clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_021

A remote control is clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

- **object**：`remote control` + `floor` + `wall` + `window`；位置 `[[2, 16], [47, 52], [67, 71], [120, 126]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[36, 38], [72, 78], [113, 117]]`

保留的 other：`A ` + ` is clearly visible ` + ` a tiled ` + `, with a plain ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_022

A suitcase is clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

- **object**：`suitcase` + `floor` + `wall` + `window`；位置 `[[2, 10], [41, 46], [61, 65], [114, 120]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[30, 32], [66, 72], [107, 111]]`

保留的 other：`A ` + ` is clearly visible ` + ` a tiled ` + `, with a plain ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_023

A shoe is clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

- **object**：`shoe` + `floor` + `wall` + `window`；位置 `[[2, 6], [37, 42], [57, 61], [110, 116]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[26, 28], [62, 68], [103, 107]]`

保留的 other：`A ` + ` is clearly visible ` + ` a tiled ` + `, with a plain ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_024

A helmet is clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

- **object**：`helmet` + `floor` + `wall` + `window`；位置 `[[2, 8], [39, 44], [59, 63], [112, 118]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[28, 30], [64, 70], [105, 109]]`

保留的 other：`A ` + ` is clearly visible ` + ` a tiled ` + `, with a plain ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_025

A toy car is clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

- **object**：`toy car` + `floor` + `wall` + `window`；位置 `[[2, 9], [40, 45], [60, 64], [113, 119]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[29, 31], [65, 71], [106, 110]]`

保留的 other：`A ` + ` is clearly visible ` + ` a tiled ` + `, with a plain ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_026

A hourglass is clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 17, "resolved_index": 18}]

- **object**：`hourglass` + `desk` + `computer monitor` + `wall`；位置 `[[2, 11], [44, 48], [62, 78], [91, 95]]`
- **texture**：`plain`；位置 `[[85, 90]]`
- **spatial_relation**：`on` + `in`；位置 `[[31, 33], [104, 106]]`

保留的 other：`A ` + ` is clearly visible ` + ` an office ` + `, with a dark ` + ` and a ` + ` ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_027

A notebook is clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`notebook` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 10], [36, 47], [61, 77], [90, 94]]`
- **spatial_relation**：`on` + `in`；位置 `[[30, 32], [103, 105]]`

保留的 other：`A ` + ` is clearly visible ` + ` an ` + `, with a dark ` + ` and a plain ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_028

A stapler is clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`stapler` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 9], [35, 46], [60, 76], [89, 93]]`
- **spatial_relation**：`on` + `in`；位置 `[[29, 31], [102, 104]]`

保留的 other：`A ` + ` is clearly visible ` + ` an ` + `, with a dark ` + ` and a plain ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_029

A pencil case is clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`pencil case` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 13], [39, 50], [64, 80], [93, 97]]`
- **spatial_relation**：`on` + `in`；位置 `[[33, 35], [106, 108]]`

保留的 other：`A ` + ` is clearly visible ` + ` an ` + `, with a dark ` + ` and a plain ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_030

A calculator is clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`calculator` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 12], [38, 49], [63, 79], [92, 96]]`
- **spatial_relation**：`on` + `in`；位置 `[[32, 34], [105, 107]]`

保留的 other：`A ` + ` is clearly visible ` + ` an ` + `, with a dark ` + ` and a plain ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_031

A scarf is clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`scarf` + `worktable` + `cloth` + `window`；位置 `[[2, 7], [39, 48], [64, 69], [112, 118]]`
- **spatial_relation**：`on` + `through`；位置 `[[27, 29], [102, 109]]`

保留的 other：`A ` + ` is clearly visible ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_032

A hat is clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`hat` + `worktable` + `cloth` + `window`；位置 `[[2, 5], [37, 46], [62, 67], [110, 116]]`
- **spatial_relation**：`on` + `through`；位置 `[[25, 27], [100, 107]]`

保留的 other：`A ` + ` is clearly visible ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_033

A shirt is clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`shirt` + `worktable` + `cloth` + `window`；位置 `[[2, 7], [39, 48], [64, 69], [112, 118]]`
- **spatial_relation**：`on` + `through`；位置 `[[27, 29], [102, 109]]`

保留的 other：`A ` + ` is clearly visible ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_034

A glove is clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`glove` + `worktable` + `cloth` + `window`；位置 `[[2, 7], [39, 48], [64, 69], [112, 118]]`
- **spatial_relation**：`on` + `through`；位置 `[[27, 29], [102, 109]]`

保留的 other：`A ` + ` is clearly visible ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_035

A handbag is clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`handbag` + `worktable` + `cloth` + `window`；位置 `[[2, 9], [41, 50], [66, 71], [114, 120]]`
- **spatial_relation**：`on` + `through`；位置 `[[29, 31], [104, 111]]`

保留的 other：`A ` + ` is clearly visible ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_036

A plate is clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`plate` + `counter` + `wall` + `cabinet`；位置 `[[2, 7], [40, 47], [68, 72], [86, 93]]`
- **spatial_relation**：`on` + `in`；位置 `[[27, 29], [102, 104]]`

保留的 other：`A ` + ` is clearly visible ` + ` a kitchen ` + `, with a plain tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_037

A bowl is clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bowl` + `counter` + `wall` + `cabinet`；位置 `[[2, 6], [39, 46], [67, 71], [85, 92]]`
- **spatial_relation**：`on` + `in`；位置 `[[26, 28], [101, 103]]`

保留的 other：`A ` + ` is clearly visible ` + ` a kitchen ` + `, with a plain tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_038

A glass jar is clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`glass jar` + `kitchen counter` + `wall` + `cabinet`；位置 `[[2, 11], [36, 51], [72, 76], [90, 97]]`
- **texture**：`plain`；位置 `[[60, 65]]`
- **spatial_relation**：`on` + `in`；位置 `[[31, 33], [106, 108]]`

保留的 other：`A ` + ` is clearly visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_039

A kettle is clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`kettle` + `counter` + `wall` + `cabinet`；位置 `[[2, 8], [41, 48], [69, 73], [87, 94]]`
- **spatial_relation**：`on` + `in`；位置 `[[28, 30], [103, 105]]`

保留的 other：`A ` + ` is clearly visible ` + ` a kitchen ` + `, with a plain tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_040

A bread loaf is clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bread loaf` + `kitchen counter` + `wall` + `cabinet`；位置 `[[2, 12], [37, 52], [73, 77], [91, 98]]`
- **spatial_relation**：`on` + `in`；位置 `[[32, 34], [107, 109]]`

保留的 other：`A ` + ` is clearly visible ` + ` a ` + `, with a plain tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_041

A car is clearly visible beside a desert road, with dry shrubs nearby and distant mountains under a pale cloudy sky.

- **object**：`car` + `desert road` + `shrubs` + `mountains` + `sky`；位置 `[[2, 5], [34, 45], [56, 62], [82, 91], [112, 115]]`
- **spatial_relation**：`beside` + `nearby` + `under`；位置 `[[25, 31], [63, 69], [92, 97]]`

保留的 other：`A ` + ` is clearly visible ` + ` a ` + `, with dry ` + ` ` + ` and distant ` + ` ` + ` a pale cloudy ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_042

A truck is clearly visible beside a desert road, with dry shrubs nearby and distant mountains under a pale cloudy sky.

- **object**：`truck` + `desert road` + `shrubs` + `mountains` + `sky`；位置 `[[2, 7], [36, 47], [58, 64], [84, 93], [114, 117]]`
- **spatial_relation**：`beside` + `nearby` + `under`；位置 `[[27, 33], [65, 71], [94, 99]]`

保留的 other：`A ` + ` is clearly visible ` + ` a ` + `, with dry ` + ` ` + ` and distant ` + ` ` + ` a pale cloudy ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_043

A motorcycle is clearly visible beside a desert road, with dry shrubs nearby and distant mountains under a pale cloudy sky.

- **object**：`motorcycle` + `desert road` + `shrubs` + `mountains` + `sky`；位置 `[[2, 12], [41, 52], [63, 69], [89, 98], [119, 122]]`
- **spatial_relation**：`beside` + `nearby` + `under`；位置 `[[32, 38], [70, 76], [99, 104]]`

保留的 other：`A ` + ` is clearly visible ` + ` a ` + `, with dry ` + ` ` + ` and distant ` + ` ` + ` a pale cloudy ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_044

A road sign is clearly visible beside a desert road, with dry shrubs nearby and distant mountains under a pale cloudy sky.

- **object**：`road sign` + `road` + `shrubs` + `mountains` + `sky`；位置 `[[2, 11], [47, 51], [62, 68], [88, 97], [118, 121]]`
- **spatial_relation**：`beside` + `nearby` + `under`；位置 `[[31, 37], [69, 75], [98, 103]]`

保留的 other：`A ` + ` is clearly visible ` + ` a desert ` + `, with dry ` + ` ` + ` and distant ` + ` ` + ` a pale cloudy ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_045

A barrel is clearly visible beside a desert road, with dry shrubs nearby and distant mountains under a pale cloudy sky.

- **object**：`barrel` + `desert road` + `shrubs` + `mountains` + `sky`；位置 `[[2, 8], [37, 48], [59, 65], [85, 94], [115, 118]]`
- **spatial_relation**：`beside` + `nearby` + `under`；位置 `[[28, 34], [66, 72], [95, 100]]`

保留的 other：`A ` + ` is clearly visible ` + ` a ` + `, with dry ` + ` ` + ` and distant ` + ` ` + ` a pale cloudy ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_046

A vase is clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

- **object**：`vase` + `courtyard` + `wall` + `path`；位置 `[[2, 6], [37, 46], [61, 65], [79, 83]]`
- **spatial_relation**：`in`；位置 `[[26, 28]]`

保留的 other：`A ` + ` is clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_047

A flowerpot is clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

- **object**：`flowerpot` + `courtyard` + `wall` + `path`；位置 `[[2, 11], [42, 51], [66, 70], [84, 88]]`
- **spatial_relation**：`in`；位置 `[[31, 33]]`

保留的 other：`A ` + ` is clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_048

A statue is clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

- **object**：`statue` + `courtyard` + `wall` + `path`；位置 `[[2, 8], [39, 48], [63, 67], [81, 85]]`
- **spatial_relation**：`in`；位置 `[[28, 30]]`

保留的 other：`A ` + ` is clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_049

A fountain is clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

- **object**：`fountain` + `courtyard` + `wall` + `path`；位置 `[[2, 10], [41, 50], [65, 69], [83, 87]]`
- **spatial_relation**：`in`；位置 `[[30, 32]]`

保留的 other：`A ` + ` is clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## object_050

A stool is clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

- **object**：`stool` + `courtyard` + `wall` + `path`；位置 `[[2, 7], [38, 47], [62, 66], [80, 84]]`
- **spatial_relation**：`in` + `with`；位置 `[[27, 29], [49, 53]]`

保留的 other：`A ` + ` is clearly visible ` + ` a quiet ` + `, ` + ` a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_001

A red dog is clearly visible in a grassy garden, with a low stone wall and distant trees visible under soft daylight.

- **object**：`dog` + `garden` + `wall` + `trees`；位置 `[[6, 9], [41, 47], [66, 70], [83, 88]]`
- **color**：`red`；位置 `[[2, 5]]`
- **spatial_relation**：`in`；位置 `[[29, 31]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a grassy ` + `, with a low stone ` + ` and distant ` + ` visible under soft daylight.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_002

A green cat is clearly visible in a grassy garden, with a low stone wall and distant trees visible under soft daylight.

- **object**：`cat` + `garden` + `wall` + `trees`；位置 `[[8, 11], [43, 49], [68, 72], [85, 90]]`
- **color**：`green`；位置 `[[2, 7]]`
- **spatial_relation**：`in`；位置 `[[31, 33]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a grassy ` + `, with a low stone ` + ` and distant ` + ` visible under soft daylight.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_003

A purple bicycle is clearly visible in a grassy garden, with a low stone wall and distant trees visible under soft daylight.

- **object**：`bicycle` + `garden` + `wall` + `trees`；位置 `[[9, 16], [48, 54], [73, 77], [90, 95]]`
- **color**：`purple`；位置 `[[2, 8]]`
- **spatial_relation**：`in`；位置 `[[36, 38]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a grassy ` + `, with a low stone ` + ` and distant ` + ` visible under soft daylight.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_004

A pink bench is clearly visible in a grassy garden, with a low stone wall and distant trees visible under soft daylight.

- **object**：`bench` + `garden` + `wall` + `trees`；位置 `[[7, 12], [44, 50], [69, 73], [86, 91]]`
- **color**：`pink`；位置 `[[2, 6]]`
- **spatial_relation**：`in`；位置 `[[32, 34]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a grassy ` + `, with a low stone ` + ` and distant ` + ` visible under soft daylight.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_005

A black wheelbarrow is clearly visible in a grassy garden, with a low stone wall and distant trees visible under soft daylight.

- **object**：`wheelbarrow` + `garden` + `wall` + `trees`；位置 `[[8, 19], [51, 57], [76, 80], [93, 98]]`
- **color**：`black`；位置 `[[2, 7]]`
- **spatial_relation**：`in`；位置 `[[39, 41]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a grassy ` + `, with a low stone ` + ` and distant ` + ` visible under soft daylight.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_006

A red mug is clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`mug` + `table` + `chairs` + `window`；位置 `[[6, 9], [46, 51], [64, 70], [88, 94]]`
- **color**：`red`；位置 `[[2, 5]]`
- **spatial_relation**：`on` + `in`；位置 `[[29, 31], [103, 105]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_007

A green teapot is clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`teapot` + `table` + `chairs` + `window`；位置 `[[8, 14], [51, 56], [69, 75], [93, 99]]`
- **color**：`green`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `in`；位置 `[[34, 36], [108, 110]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_008

A purple coffee pot is clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`coffee pot` + `table` + `chairs` + `window`；位置 `[[9, 19], [56, 61], [74, 80], [98, 104]]`
- **color**：`purple`；位置 `[[2, 8]]`
- **spatial_relation**：`on` + `in`；位置 `[[39, 41], [113, 115]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_009

A pink sugar bowl is clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`bowl` + `table` + `chairs` + `window`；位置 `[[13, 17], [54, 59], [72, 78], [96, 102]]`
- **color**：`pink`；位置 `[[2, 6]]`
- **spatial_relation**：`on` + `in`；位置 `[[37, 39], [111, 113]]`

保留的 other：`A ` + ` sugar ` + ` is clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_010

A black tray is clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`tray` + `table` + `chairs` + `window`；位置 `[[8, 12], [49, 54], [67, 73], [91, 97]]`
- **color**：`black`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `in`；位置 `[[32, 34], [106, 108]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_011

A red chair is clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`chair` + `library` + `bookshelves` + `walls` + `window`；位置 `[[6, 11], [42, 49], [56, 67], [78, 83], [122, 128]]`
- **color**：`red`；位置 `[[2, 5]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[31, 33], [68, 73], [106, 113]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a quiet ` + `, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_012

A green table is clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`table` + `library` + `bookshelves` + `walls` + `window`；位置 `[[8, 13], [44, 51], [58, 69], [80, 85], [124, 130]]`
- **color**：`green`；位置 `[[2, 7]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[33, 35], [70, 75], [108, 115]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a quiet ` + `, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_013

A purple bookcase is clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`bookcase` + `library` + `bookshelves` + `walls` + `window`；位置 `[[9, 17], [48, 55], [62, 73], [84, 89], [128, 134]]`
- **color**：`purple`；位置 `[[2, 8]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[37, 39], [74, 79], [112, 119]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a quiet ` + `, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_014

A pink ladder is clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`ladder` + `library` + `bookshelves` + `walls` + `window`；位置 `[[7, 13], [44, 51], [58, 69], [80, 85], [124, 130]]`
- **color**：`pink`；位置 `[[2, 6]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[33, 35], [70, 75], [108, 115]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a quiet ` + `, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_015

A black reading lamp is clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`lamp` + `library` + `bookshelves` + `walls` + `window`；位置 `[[16, 20], [51, 58], [65, 76], [87, 92], [131, 137]]`
- **color**：`black`；位置 `[[2, 7]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[40, 42], [77, 82], [115, 122]]`

保留的 other：`A ` + ` reading ` + ` is clearly visible ` + ` a quiet ` + `, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_016

A red water bottle is clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`water bottle` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[6, 18], [47, 58], [70, 75], [88, 93], [120, 123]]`
- **color**：`red`；位置 `[[2, 5]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[38, 44], [94, 101]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_017

A green backpack is clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`backpack` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[8, 16], [45, 56], [68, 73], [86, 91], [118, 121]]`
- **color**：`green`；位置 `[[2, 7]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[36, 42], [92, 99]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_018

A purple umbrella is clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`umbrella` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[9, 17], [46, 57], [69, 74], [87, 92], [119, 122]]`
- **color**：`purple`；位置 `[[2, 8]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[37, 43], [93, 100]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_019

A pink watering can is clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`watering can` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[7, 19], [48, 59], [71, 76], [89, 94], [121, 124]]`
- **color**：`pink`；位置 `[[2, 6]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[39, 45], [95, 102]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_020

A black basket is clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`basket` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[8, 14], [43, 54], [66, 71], [84, 89], [116, 119]]`
- **color**：`black`；位置 `[[2, 7]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[34, 40], [90, 97]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_021

A red remote control is clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

- **object**：`remote control` + `floor` + `wall` + `window`；位置 `[[6, 20], [51, 56], [71, 75], [124, 130]]`
- **color**：`red`；位置 `[[2, 5]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[40, 42], [76, 82], [117, 121]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a tiled ` + `, with a plain ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_022

A green suitcase is clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

- **object**：`suitcase` + `floor` + `wall` + `window`；位置 `[[8, 16], [47, 52], [67, 71], [120, 126]]`
- **color**：`green`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[36, 38], [72, 78], [113, 117]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a tiled ` + `, with a plain ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_023

A purple shoe is clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

- **object**：`shoe` + `floor` + `wall` + `window`；位置 `[[9, 13], [44, 49], [64, 68], [117, 123]]`
- **color**：`purple`；位置 `[[2, 8]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[33, 35], [69, 75], [110, 114]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a tiled ` + `, with a plain ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_024

A pink helmet is clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

- **object**：`helmet` + `floor` + `wall` + `window`；位置 `[[7, 13], [44, 49], [64, 68], [117, 123]]`
- **color**：`pink`；位置 `[[2, 6]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[33, 35], [69, 75], [110, 114]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a tiled ` + `, with a plain ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_025

A black toy car is clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

- **object**：`car` + `floor` + `wall` + `window`；位置 `[[12, 15], [46, 51], [66, 70], [119, 125]]`
- **color**：`black`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[35, 37], [71, 77], [112, 116]]`

保留的 other：`A ` + ` toy ` + ` is clearly visible ` + ` a tiled ` + `, with a plain ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_026

A blue hourglass is clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`hourglass` + `office desk` + `computer monitor` + `wall`；位置 `[[7, 16], [42, 53], [67, 83], [96, 100]]`
- **color**：`blue`；位置 `[[2, 6]]`
- **spatial_relation**：`on` + `in`；位置 `[[36, 38], [109, 111]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` an ` + `, with a dark ` + ` and a plain ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_027

A yellow notebook is clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`notebook` + `desk` + `computer monitor` + `wall`；位置 `[[9, 17], [50, 54], [68, 84], [97, 101]]`
- **color**：`yellow`；位置 `[[2, 8]]`
- **spatial_relation**：`on` + `in`；位置 `[[37, 39], [110, 112]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` an office ` + `, with a dark ` + ` and a plain ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_028

An orange stapler is clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`stapler` + `desk` + `computer monitor` + `wall`；位置 `[[10, 17], [50, 54], [68, 84], [97, 101]]`
- **color**：`orange`；位置 `[[3, 9]]`
- **spatial_relation**：`on` + `in`；位置 `[[37, 39], [110, 112]]`

保留的 other：`An ` + ` ` + ` is clearly visible ` + ` an office ` + `, with a dark ` + ` and a plain ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_029

A white pencil case is clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`pencil case` + `office desk` + `computer monitor` + `wall`；位置 `[[8, 19], [45, 56], [70, 86], [99, 103]]`
- **color**：`white`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `in`；位置 `[[39, 41], [112, 114]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` an ` + `, with a dark ` + ` and a plain ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_030

A brown calculator is clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`calculator` + `office desk` + `computer monitor` + `wall`；位置 `[[8, 18], [44, 55], [69, 85], [98, 102]]`
- **color**：`brown`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `in`；位置 `[[38, 40], [111, 113]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` an ` + `, with a dark ` + ` and a plain ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_031

A blue scarf is clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`scarf` + `worktable` + `cloth` + `window`；位置 `[[7, 12], [44, 53], [69, 74], [117, 123]]`
- **color**：`blue`；位置 `[[2, 6]]`
- **spatial_relation**：`on` + `nearby` + `through`；位置 `[[32, 34], [75, 81], [107, 114]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a wooden ` + `, with a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_032

A yellow hat is clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`hat` + `worktable` + `cloth` + `window`；位置 `[[9, 12], [44, 53], [69, 74], [117, 123]]`
- **color**：`yellow`；位置 `[[2, 8]]`
- **spatial_relation**：`on` + `through`；位置 `[[32, 34], [107, 114]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_033

An orange shirt is clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`shirt` + `worktable` + `cloth` + `window`；位置 `[[10, 15], [47, 56], [72, 77], [120, 126]]`
- **color**：`orange`；位置 `[[3, 9]]`
- **spatial_relation**：`on` + `through`；位置 `[[35, 37], [110, 117]]`

保留的 other：`An ` + ` ` + ` is clearly visible ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_034

A white glove is clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`glove` + `worktable` + `cloth` + `window`；位置 `[[8, 13], [45, 54], [70, 75], [118, 124]]`
- **color**：`white`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `nearby` + `through`；位置 `[[33, 35], [76, 82], [108, 115]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a wooden ` + `, with a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_035

A brown handbag is clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`handbag` + `worktable` + `cloth` + `window`；位置 `[[8, 15], [47, 56], [72, 77], [120, 126]]`
- **color**：`brown`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `through`；位置 `[[35, 37], [110, 117]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_036

A blue plate is clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`plate` + `counter` + `wall` + `cabinet`；位置 `[[7, 12], [45, 52], [73, 77], [91, 98]]`
- **color**：`blue`；位置 `[[2, 6]]`
- **spatial_relation**：`on` + `in`；位置 `[[32, 34], [107, 109]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a kitchen ` + `, with a plain tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_037

A yellow bowl is clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bowl` + `counter` + `wall` + `cabinet`；位置 `[[9, 13], [46, 53], [74, 78], [92, 99]]`
- **color**：`yellow`；位置 `[[2, 8]]`
- **spatial_relation**：`on` + `in`；位置 `[[33, 35], [108, 110]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a kitchen ` + `, with a plain tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_038

An orange glass jar is clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`jar` + `counter` + `wall` + `cabinet`；位置 `[[16, 19], [52, 59], [80, 84], [98, 105]]`
- **color**：`orange`；位置 `[[3, 9]]`
- **spatial_relation**：`on` + `in`；位置 `[[39, 41], [114, 116]]`

保留的 other：`An ` + ` glass ` + ` is clearly visible ` + ` a kitchen ` + `, with a plain tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_039

A white kettle is clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`kettle` + `kitchen counter` + `wall` + `cabinet`；位置 `[[8, 14], [39, 54], [75, 79], [93, 100]]`
- **color**：`white`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `in`；位置 `[[34, 36], [109, 111]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a ` + `, with a plain tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_040

A brown bread loaf is clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bread loaf` + `kitchen counter` + `wall` + `cabinet`；位置 `[[8, 18], [43, 58], [79, 83], [97, 104]]`
- **color**：`brown`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `in`；位置 `[[38, 40], [113, 115]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a ` + `, with a plain tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_041

A blue car is clearly visible beside a desert road, with dry shrubs nearby and distant mountains under a pale cloudy sky.

- **object**：`car` + `desert road` + `shrubs` + `mountains` + `sky`；位置 `[[7, 10], [39, 50], [61, 67], [87, 96], [117, 120]]`
- **color**：`blue`；位置 `[[2, 6]]`
- **spatial_relation**：`beside` + `nearby` + `under`；位置 `[[30, 36], [68, 74], [97, 102]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a ` + `, with dry ` + ` ` + ` and distant ` + ` ` + ` a pale cloudy ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_042

A yellow truck is clearly visible beside a desert road, with dry shrubs nearby and distant mountains under a pale cloudy sky.

- **object**：`truck` + `desert road` + `shrubs` + `mountains` + `sky`；位置 `[[9, 14], [43, 54], [65, 71], [91, 100], [121, 124]]`
- **color**：`yellow`；位置 `[[2, 8]]`
- **spatial_relation**：`beside` + `under`；位置 `[[34, 40], [101, 106]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a ` + `, with dry ` + ` nearby and distant ` + ` ` + ` a pale cloudy ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_043

An orange motorcycle is clearly visible beside a desert road, with dry shrubs nearby and distant mountains under a pale cloudy sky.

- **object**：`motorcycle` + `desert road` + `shrubs` + `mountains` + `sky`；位置 `[[10, 20], [49, 60], [71, 77], [97, 106], [127, 130]]`
- **color**：`orange`；位置 `[[3, 9]]`
- **spatial_relation**：`beside` + `under`；位置 `[[40, 46], [107, 112]]`

保留的 other：`An ` + ` ` + ` is clearly visible ` + ` a ` + `, with dry ` + ` nearby and distant ` + ` ` + ` a pale cloudy ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_044

A white road sign is clearly visible beside a desert road, with dry shrubs nearby and distant mountains under a pale cloudy sky.

- **object**：`road sign` + `desert road` + `shrubs` + `mountains` + `sky`；位置 `[[8, 17], [46, 57], [68, 74], [94, 103], [124, 127]]`
- **color**：`white`；位置 `[[2, 7]]`
- **spatial_relation**：`beside` + `nearby` + `under`；位置 `[[37, 43], [75, 81], [104, 109]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a ` + `, with dry ` + ` ` + ` and distant ` + ` ` + ` a pale cloudy ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_045

A brown barrel is clearly visible beside a desert road, with dry shrubs nearby and distant mountains under a pale cloudy sky.

- **object**：`barrel` + `desert road` + `shrubs` + `mountains` + `sky`；位置 `[[8, 14], [43, 54], [65, 71], [91, 100], [121, 124]]`
- **color**：`brown`；位置 `[[2, 7]]`
- **spatial_relation**：`beside` + `under`；位置 `[[34, 40], [101, 106]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a ` + `, with dry ` + ` nearby and distant ` + ` ` + ` a pale cloudy ` + `.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_046

A blue vase is clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 13, "resolved_index": 14}, {"text": "path", "model_index": 17, "resolved_index": 18}]

- **object**：`vase` + `courtyard` + `wall` + `path`；位置 `[[7, 11], [42, 51], [66, 70], [84, 88]]`
- **color**：`blue`；位置 `[[2, 6]]`
- **spatial_relation**：`in`；位置 `[[31, 33]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_047

A yellow flowerpot is clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 13, "resolved_index": 14}, {"text": "path", "model_index": 17, "resolved_index": 18}]

- **object**：`flowerpot` + `courtyard` + `wall` + `path`；位置 `[[9, 18], [49, 58], [73, 77], [91, 95]]`
- **color**：`yellow`；位置 `[[2, 8]]`
- **spatial_relation**：`in`；位置 `[[38, 40]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_048

An orange statue is clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 13, "resolved_index": 14}, {"text": "path", "model_index": 17, "resolved_index": 18}]

- **object**：`statue` + `courtyard` + `wall` + `path`；位置 `[[10, 16], [47, 56], [71, 75], [89, 93]]`
- **color**：`orange`；位置 `[[3, 9]]`
- **spatial_relation**：`in`；位置 `[[36, 38]]`

保留的 other：`An ` + ` ` + ` is clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_049

A white fountain is clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 13, "resolved_index": 14}, {"text": "path", "model_index": 17, "resolved_index": 18}]

- **object**：`fountain` + `courtyard` + `wall` + `path`；位置 `[[8, 16], [47, 56], [71, 75], [89, 93]]`
- **color**：`white`；位置 `[[2, 7]]`
- **spatial_relation**：`in`；位置 `[[36, 38]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## color_050

A brown stool is clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 13, "resolved_index": 14}, {"text": "path", "model_index": 17, "resolved_index": 18}]

- **object**：`stool` + `courtyard` + `wall` + `path`；位置 `[[8, 13], [44, 53], [68, 72], [86, 90]]`
- **color**：`brown`；位置 `[[2, 7]]`
- **spatial_relation**：`in`；位置 `[[33, 35]]`

保留的 other：`A ` + ` ` + ` is clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_001

A round plate is shown with its outer outline clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`plate` + `kitchen counter` + `wall` + `cabinet`；位置 `[[8, 13], [67, 82], [103, 107], [121, 128]]`
- **shape**：`round`；位置 `[[2, 7]]`
- **texture**：`plain`；位置 `[[91, 96]]`
- **spatial_relation**：`on` + `in`；位置 `[[62, 64], [137, 139]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_002

A round mirror is shown with its outer outline clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`mirror` + `courtyard` + `wall` + `path`；位置 `[[8, 14], [74, 83], [98, 102], [116, 120]]`
- **shape**：`round`；位置 `[[2, 7]]`
- **spatial_relation**：`in`；位置 `[[63, 65]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_003

A round tray is shown with its outer outline clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`tray` + `table` + `chairs` + `window`；位置 `[[8, 12], [78, 83], [96, 102], [120, 126]]`
- **shape**：`round`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `in`；位置 `[[61, 63], [135, 137]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_004

A round rug is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`rug` + `bookshelves` + `window`；位置 `[[8, 11], [85, 96], [151, 157]]`
- **shape**：`round`；位置 `[[2, 7]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[60, 62], [97, 102], [135, 142]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_005

A round picture frame is shown with its outer outline clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`picture frame` + `office desk` + `computer monitor` + `plain wall`；位置 `[[8, 21], [76, 87], [101, 117], [124, 134]]`
- **shape**：`round`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `in`；位置 `[[70, 72], [143, 145]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` an ` + `, with a dark ` + ` and a ` + ` visible ` + ` the background.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_006

A round tabletop is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`tabletop` + `bookshelves` + `window`；位置 `[[8, 16], [90, 101], [156, 162]]`
- **shape**：`round`；位置 `[[2, 7]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[65, 67], [102, 107], [140, 147]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_007

A round cushion is shown with its outer outline clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}]

- **object**：`cushion` + `floor` + `wall` + `window`；位置 `[[8, 15], [75, 80], [95, 99], [148, 154]]`
- **shape**：`round`；位置 `[[2, 7]]`
- **texture**：`plain`；位置 `[[89, 94]]`
- **spatial_relation**：`behind` + `from`；位置 `[[100, 106], [141, 145]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible on a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_008

A round wall clock is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`wall clock` + `bookshelves` + `walls` + `window`；位置 `[[8, 18], [92, 103], [114, 119], [158, 164]]`
- **shape**：`round`；位置 `[[2, 7]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[67, 69], [104, 109], [142, 149]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_009

A round sign is shown with its outer outline clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`sign` + `courtyard` + `wall` + `path`；位置 `[[8, 12], [72, 81], [96, 100], [114, 118]]`
- **shape**：`round`；位置 `[[2, 7]]`
- **spatial_relation**：`in`；位置 `[[61, 63]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_010

A round floor mat is shown with its outer outline clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 19, "resolved_index": 20}]

- **object**：`floor mat` + `floor` + `wall` + `window`；位置 `[[8, 17], [77, 82], [97, 101], [150, 156]]`
- **shape**：`round`；位置 `[[2, 7]]`
- **texture**：`plain`；位置 `[[91, 96]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[66, 68], [102, 108], [143, 147]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_011

A square plate is shown with its outer outline clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`plate` + `kitchen counter` + `wall` + `cabinet`；位置 `[[9, 14], [68, 83], [104, 108], [122, 129]]`
- **shape**：`square`；位置 `[[2, 8]]`
- **texture**：`plain`；位置 `[[92, 97]]`
- **spatial_relation**：`on` + `in`；位置 `[[63, 65], [138, 140]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_012

A square mirror is shown with its outer outline clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`mirror` + `courtyard` + `wall` + `path`；位置 `[[9, 15], [75, 84], [99, 103], [117, 121]]`
- **shape**：`square`；位置 `[[2, 8]]`
- **spatial_relation**：`in`；位置 `[[64, 66]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_013

A square tray is shown with its outer outline clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`tray` + `table` + `chairs` + `window`；位置 `[[9, 13], [79, 84], [97, 103], [121, 127]]`
- **shape**：`square`；位置 `[[2, 8]]`
- **spatial_relation**：`on` + `in`；位置 `[[62, 64], [136, 138]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_014

A square rug is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`rug` + `bookshelves` + `window`；位置 `[[9, 12], [86, 97], [152, 158]]`
- **shape**：`square`；位置 `[[2, 8]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[61, 63], [98, 103], [136, 143]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_015

A square picture frame is shown with its outer outline clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`picture frame` + `office desk` + `computer monitor` + `wall`；位置 `[[9, 22], [77, 88], [102, 118], [131, 135]]`
- **shape**：`square`；位置 `[[2, 8]]`
- **texture**：`plain`；位置 `[[125, 130]]`
- **spatial_relation**：`on`；位置 `[[71, 73]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_016

A square tabletop is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`tabletop` + `bookshelves` + `window`；位置 `[[9, 17], [91, 102], [157, 163]]`
- **shape**：`square`；位置 `[[2, 8]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[66, 68], [103, 108], [141, 148]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_017

A square cushion is shown with its outer outline clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}]

- **object**：`cushion` + `floor` + `wall` + `window`；位置 `[[9, 16], [76, 81], [96, 100], [149, 155]]`
- **shape**：`square`；位置 `[[2, 8]]`
- **texture**：`plain`；位置 `[[90, 95]]`
- **spatial_relation**：`behind` + `from`；位置 `[[101, 107], [142, 146]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible on a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_018

A square wall clock is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`wall clock` + `bookshelves` + `walls` + `window`；位置 `[[9, 19], [93, 104], [115, 120], [159, 165]]`
- **shape**：`square`；位置 `[[2, 8]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[68, 70], [105, 110], [143, 150]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_019

A square sign is shown with its outer outline clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`sign` + `courtyard` + `wall` + `path`；位置 `[[9, 13], [73, 82], [97, 101], [115, 119]]`
- **shape**：`square`；位置 `[[2, 8]]`
- **spatial_relation**：`in`；位置 `[[62, 64]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_020

A square floor mat is shown with its outer outline clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 19, "resolved_index": 20}]

- **object**：`floor mat` + `floor` + `wall` + `window`；位置 `[[9, 18], [78, 83], [98, 102], [151, 157]]`
- **shape**：`square`；位置 `[[2, 8]]`
- **texture**：`plain`；位置 `[[92, 97]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[67, 69], [103, 109], [144, 148]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_021

A triangular plate is shown with its outer outline clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`plate` + `kitchen counter` + `wall` + `cabinet`；位置 `[[13, 18], [72, 87], [108, 112], [126, 133]]`
- **shape**：`triangular`；位置 `[[2, 12]]`
- **texture**：`plain`；位置 `[[96, 101]]`
- **spatial_relation**：`on` + `in`；位置 `[[67, 69], [142, 144]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_022

A triangular mirror is shown with its outer outline clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`mirror` + `courtyard` + `wall` + `path`；位置 `[[13, 19], [79, 88], [103, 107], [121, 125]]`
- **shape**：`triangular`；位置 `[[2, 12]]`
- **spatial_relation**：`in`；位置 `[[68, 70]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_023

A triangular tray is shown with its outer outline clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`tray` + `table` + `chairs` + `window`；位置 `[[13, 17], [83, 88], [101, 107], [125, 131]]`
- **shape**：`triangular`；位置 `[[2, 12]]`
- **spatial_relation**：`on` + `in`；位置 `[[66, 68], [140, 142]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_024

A triangular rug is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`rug` + `bookshelves` + `window`；位置 `[[13, 16], [90, 101], [156, 162]]`
- **shape**：`triangular`；位置 `[[2, 12]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[65, 67], [102, 107], [140, 147]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_025

A triangular picture frame is shown with its outer outline clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 24, "resolved_index": 25}]

- **object**：`picture frame` + `office desk` + `computer monitor` + `wall`；位置 `[[13, 26], [81, 92], [106, 122], [135, 139]]`
- **shape**：`triangular`；位置 `[[2, 12]]`
- **texture**：`plain`；位置 `[[129, 134]]`
- **spatial_relation**：`on` + `in`；位置 `[[75, 77], [148, 150]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible ` + ` the background.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_026

A triangular tabletop is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`tabletop` + `bookshelves` + `window`；位置 `[[13, 21], [95, 106], [161, 167]]`
- **shape**：`triangular`；位置 `[[2, 12]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[70, 72], [107, 112], [145, 152]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_027

A triangular cushion is shown with its outer outline clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}]

- **object**：`cushion` + `floor` + `wall` + `window`；位置 `[[13, 20], [80, 85], [100, 104], [153, 159]]`
- **shape**：`triangular`；位置 `[[2, 12]]`
- **texture**：`plain`；位置 `[[94, 99]]`
- **spatial_relation**：`behind` + `from`；位置 `[[105, 111], [146, 150]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible on a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_028

A triangular wall clock is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`wall clock` + `bookshelves` + `walls` + `window`；位置 `[[13, 23], [97, 108], [119, 124], [163, 169]]`
- **shape**：`triangular`；位置 `[[2, 12]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[72, 74], [109, 114], [147, 154]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_029

A triangular sign is shown with its outer outline clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`sign` + `courtyard` + `wall` + `path`；位置 `[[13, 17], [77, 86], [101, 105], [119, 123]]`
- **shape**：`triangular`；位置 `[[2, 12]]`
- **spatial_relation**：`in`；位置 `[[66, 68]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_030

A triangular floor mat is shown with its outer outline clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 19, "resolved_index": 20}]

- **object**：`floor mat` + `floor` + `wall` + `window`；位置 `[[13, 22], [82, 87], [102, 106], [155, 161]]`
- **shape**：`triangular`；位置 `[[2, 12]]`
- **texture**：`plain`；位置 `[[96, 101]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[71, 73], [107, 113], [148, 152]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_031

An oval plate is shown with its outer outline clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`plate` + `kitchen counter` + `wall` + `cabinet`；位置 `[[8, 13], [67, 82], [103, 107], [121, 128]]`
- **shape**：`oval`；位置 `[[3, 7]]`
- **texture**：`plain`；位置 `[[91, 96]]`
- **spatial_relation**：`on` + `in`；位置 `[[62, 64], [137, 139]]`

保留的 other：`An ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_032

An oval mirror is shown with its outer outline clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`mirror` + `courtyard` + `wall` + `path`；位置 `[[8, 14], [74, 83], [98, 102], [116, 120]]`
- **shape**：`oval`；位置 `[[3, 7]]`
- **spatial_relation**：`in`；位置 `[[63, 65]]`

保留的 other：`An ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_033

An oval tray is shown with its outer outline clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`tray` + `table` + `chairs` + `window`；位置 `[[8, 12], [78, 83], [96, 102], [120, 126]]`
- **shape**：`oval`；位置 `[[3, 7]]`
- **spatial_relation**：`on` + `in`；位置 `[[61, 63], [135, 137]]`

保留的 other：`An ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_034

An oval rug is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`rug` + `bookshelves` + `window`；位置 `[[8, 11], [85, 96], [151, 157]]`
- **shape**：`oval`；位置 `[[3, 7]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[60, 62], [97, 102], [135, 142]]`

保留的 other：`An ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_035

An oval picture frame is shown with its outer outline clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`picture frame` + `office desk` + `computer monitor` + `wall`；位置 `[[8, 21], [76, 87], [101, 117], [130, 134]]`
- **shape**：`oval`；位置 `[[3, 7]]`
- **texture**：`plain`；位置 `[[124, 129]]`
- **spatial_relation**：`on`；位置 `[[70, 72]]`

保留的 other：`An ` + ` ` + ` is shown with its outer outline clearly visible ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_036

An oval tabletop is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`tabletop` + `bookshelves` + `window`；位置 `[[8, 16], [90, 101], [156, 162]]`
- **shape**：`oval`；位置 `[[3, 7]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[65, 67], [102, 107], [140, 147]]`

保留的 other：`An ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_037

An oval cushion is shown with its outer outline clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}]

- **object**：`cushion` + `floor` + `wall` + `window`；位置 `[[8, 15], [75, 80], [95, 99], [148, 154]]`
- **shape**：`oval`；位置 `[[3, 7]]`
- **texture**：`plain`；位置 `[[89, 94]]`
- **spatial_relation**：`behind` + `from`；位置 `[[100, 106], [141, 145]]`

保留的 other：`An ` + ` ` + ` is shown with its outer outline clearly visible on a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_038

An oval wall clock is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`wall clock` + `bookshelves` + `walls` + `window`；位置 `[[8, 18], [92, 103], [114, 119], [158, 164]]`
- **shape**：`oval`；位置 `[[3, 7]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[67, 69], [104, 109], [142, 149]]`

保留的 other：`An ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_039

An oval sign is shown with its outer outline clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

- **object**：`sign` + `courtyard` + `wall` + `path`；位置 `[[8, 12], [72, 81], [96, 100], [114, 118]]`
- **shape**：`oval`；位置 `[[3, 7]]`
- **spatial_relation**：`in`；位置 `[[61, 63]]`

保留的 other：`An ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_040

An oval floor mat is shown with its outer outline clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 19, "resolved_index": 20}]

- **object**：`floor mat` + `floor` + `wall` + `window`；位置 `[[8, 17], [77, 82], [97, 101], [150, 156]]`
- **shape**：`oval`；位置 `[[3, 7]]`
- **texture**：`plain`；位置 `[[91, 96]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[66, 68], [102, 108], [143, 147]]`

保留的 other：`An ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_041

A rectangular plate is shown with its outer outline clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`plate` + `kitchen counter` + `wall` + `cabinet`；位置 `[[14, 19], [73, 88], [109, 113], [127, 134]]`
- **shape**：`rectangular`；位置 `[[2, 13]]`
- **texture**：`plain`；位置 `[[97, 102]]`
- **spatial_relation**：`on` + `in`；位置 `[[68, 70], [143, 145]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_042

A rectangular mirror is shown with its outer outline clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`mirror` + `courtyard` + `wall` + `path`；位置 `[[14, 20], [80, 89], [104, 108], [122, 126]]`
- **shape**：`rectangular`；位置 `[[2, 13]]`
- **spatial_relation**：`in`；位置 `[[69, 71]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_043

A rectangular tray is shown with its outer outline clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`tray` + `table` + `chairs` + `window`；位置 `[[14, 18], [84, 89], [102, 108], [126, 132]]`
- **shape**：`rectangular`；位置 `[[2, 13]]`
- **spatial_relation**：`on` + `in`；位置 `[[67, 69], [141, 143]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_044

A rectangular rug is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`rug` + `bookshelves` + `walls` + `window`；位置 `[[14, 17], [91, 102], [113, 118], [157, 163]]`
- **shape**：`rectangular`；位置 `[[2, 13]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[66, 68], [103, 108], [141, 148]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_045

A rectangular picture frame is shown with its outer outline clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 24, "resolved_index": 25}]

- **object**：`picture frame` + `office desk` + `computer monitor` + `wall`；位置 `[[14, 27], [82, 93], [107, 123], [136, 140]]`
- **shape**：`rectangular`；位置 `[[2, 13]]`
- **texture**：`plain`；位置 `[[130, 135]]`
- **spatial_relation**：`on` + `in`；位置 `[[76, 78], [149, 151]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible ` + ` the background.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_046

A rectangular tabletop is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`tabletop` + `bookshelves` + `window`；位置 `[[14, 22], [96, 107], [162, 168]]`
- **shape**：`rectangular`；位置 `[[2, 13]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[71, 73], [108, 113], [146, 153]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_047

A rectangular cushion is shown with its outer outline clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}]

- **object**：`cushion` + `floor` + `wall` + `window`；位置 `[[14, 21], [81, 86], [101, 105], [154, 160]]`
- **shape**：`rectangular`；位置 `[[2, 13]]`
- **texture**：`plain`；位置 `[[95, 100]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[70, 72], [106, 112], [147, 151]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_048

A rectangular wall clock is shown with its outer outline clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`wall clock` + `bookshelves` + `walls` + `window`；位置 `[[14, 24], [98, 109], [120, 125], [164, 170]]`
- **shape**：`rectangular`；位置 `[[2, 13]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[73, 75], [110, 115], [148, 155]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet library, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_049

A rectangular sign is shown with its outer outline clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`sign` + `courtyard` + `wall` + `path`；位置 `[[14, 18], [78, 87], [102, 106], [120, 124]]`
- **shape**：`rectangular`；位置 `[[2, 13]]`
- **spatial_relation**：`in`；位置 `[[67, 69]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_050

A rectangular floor mat is shown with its outer outline clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 19, "resolved_index": 20}]

- **object**：`floor mat` + `floor` + `wall` + `window`；位置 `[[14, 23], [83, 88], [103, 107], [156, 162]]`
- **shape**：`rectangular`；位置 `[[2, 13]]`
- **texture**：`plain`；位置 `[[97, 102]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[72, 74], [108, 114], [149, 153]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_001

A striped shirt is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`shirt` + `worktable` + `cloth` + `window`；位置 `[[10, 15], [70, 79], [95, 100], [143, 149]]`
- **texture**：`striped`；位置 `[[2, 9]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[58, 60], [81, 85], [101, 107], [133, 140]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_002

A striped scarf is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`scarf` + `worktable` + `cloth` + `window`；位置 `[[10, 15], [70, 79], [95, 100], [143, 149]]`
- **texture**：`striped`；位置 `[[2, 9]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[58, 60], [81, 85], [101, 107], [133, 140]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_003

A striped hat is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`hat` + `worktable` + `cloth` + `window`；位置 `[[10, 13], [68, 77], [93, 98], [141, 147]]`
- **texture**：`striped`；位置 `[[2, 9]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[56, 58], [79, 83], [99, 105], [131, 138]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_004

A striped handbag is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`handbag` + `worktable` + `cloth` + `window`；位置 `[[10, 17], [72, 81], [97, 102], [145, 151]]`
- **texture**：`striped`；位置 `[[2, 9]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[60, 62], [83, 87], [103, 109], [135, 142]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_005

A striped sock is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`sock` + `worktable` + `cloth` + `window`；位置 `[[10, 14], [69, 78], [94, 99], [142, 148]]`
- **texture**：`striped`；位置 `[[2, 9]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[57, 59], [80, 84], [100, 106], [132, 139]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_006

A striped blanket is shown with its surface clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

- **object**：`blanket` + `floor` + `wall` + `window`；位置 `[[10, 17], [71, 76], [91, 95], [144, 150]]`
- **texture**：`striped` + `plain`；位置 `[[2, 9], [85, 90]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[60, 62], [96, 102], [137, 141]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_007

A striped cushion is shown with its surface clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

- **object**：`cushion` + `floor` + `wall` + `window`；位置 `[[10, 17], [71, 76], [91, 95], [144, 150]]`
- **texture**：`striped` + `plain`；位置 `[[2, 9], [85, 90]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[60, 62], [96, 102], [137, 141]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_008

A striped curtain is shown with its surface clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`curtain` + `bookshelves` + `walls` + `window`；位置 `[[10, 17], [85, 96], [107, 112], [151, 157]]`
- **texture**：`striped`；位置 `[[2, 9]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[60, 62], [97, 102], [135, 142]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a quiet library, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_009

A striped tablecloth is shown with its surface clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

标注说明： Unique exact-word index repairs: [{"text": ",", "model_index": 14, "resolved_index": 15}]

- **object**：`tablecloth` + `chairs` + `window`；位置 `[[10, 20], [98, 104], [122, 128]]`
- **texture**：`striped`；位置 `[[2, 9]]`
- **spatial_relation**：`on` + `in`；位置 `[[63, 65], [137, 139]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden cafe table, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_010

A striped umbrella is shown with its surface clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`umbrella` + `garden path` + `reeds` + `trees`；位置 `[[10, 18], [70, 81], [93, 98], [111, 116]]`
- **texture**：`striped`；位置 `[[2, 9]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[61, 67], [117, 124]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded sky.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_011

A checkered shirt is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`shirt` + `worktable` + `cloth` + `window`；位置 `[[12, 17], [72, 81], [97, 102], [145, 151]]`
- **texture**：`checkered`；位置 `[[2, 11]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[60, 62], [83, 87], [103, 109], [135, 142]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_012

A checkered scarf is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`scarf` + `worktable` + `cloth` + `window`；位置 `[[12, 17], [72, 81], [97, 102], [145, 151]]`
- **texture**：`checkered`；位置 `[[2, 11]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[60, 62], [83, 87], [103, 109], [135, 142]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_013

A checkered hat is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`hat` + `worktable` + `cloth` + `window`；位置 `[[12, 15], [70, 79], [95, 100], [143, 149]]`
- **texture**：`checkered`；位置 `[[2, 11]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[58, 60], [81, 85], [101, 107], [133, 140]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_014

A checkered handbag is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`handbag` + `worktable` + `cloth` + `window`；位置 `[[12, 19], [74, 83], [99, 104], [147, 153]]`
- **texture**：`checkered`；位置 `[[2, 11]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[62, 64], [85, 89], [105, 111], [137, 144]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_015

A checkered sock is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`sock` + `worktable` + `cloth` + `window`；位置 `[[12, 16], [71, 80], [96, 101], [144, 150]]`
- **texture**：`checkered`；位置 `[[2, 11]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[59, 61], [82, 86], [102, 108], [134, 141]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_016

A checkered blanket is shown with its surface clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 17, "resolved_index": 18}]

- **object**：`blanket` + `floor` + `wall` + `window`；位置 `[[12, 19], [73, 78], [93, 97], [146, 152]]`
- **texture**：`checkered` + `plain`；位置 `[[2, 11], [87, 92]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[62, 64], [98, 104], [139, 143]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_017

A checkered cushion is shown with its surface clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 17, "resolved_index": 18}]

- **object**：`cushion` + `floor` + `wall` + `window`；位置 `[[12, 19], [73, 78], [93, 97], [146, 152]]`
- **texture**：`checkered` + `plain`；位置 `[[2, 11], [87, 92]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[62, 64], [98, 104], [139, 143]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_018

A checkered curtain is shown with its surface clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`curtain` + `bookshelves` + `window`；位置 `[[12, 19], [87, 98], [153, 159]]`
- **texture**：`checkered`；位置 `[[2, 11]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[62, 64], [99, 104], [137, 144]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a quiet library, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_019

A checkered tablecloth is shown with its surface clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`tablecloth` + `table` + `chairs` + `window`；位置 `[[12, 22], [82, 87], [100, 106], [124, 130]]`
- **texture**：`checkered`；位置 `[[2, 11]]`
- **spatial_relation**：`on` + `in`；位置 `[[65, 67], [139, 141]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_020

A checkered umbrella is shown with its surface clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`umbrella` + `garden path` + `reeds` + `trees`；位置 `[[12, 20], [72, 83], [95, 100], [113, 118]]`
- **texture**：`checkered`；位置 `[[2, 11]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[63, 69], [119, 126]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded sky.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_021

A polka-dotted shirt is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`shirt` + `worktable` + `cloth` + `window`；位置 `[[15, 20], [75, 84], [100, 105], [148, 154]]`
- **texture**：`polka-dotted`；位置 `[[2, 14]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[63, 65], [86, 90], [106, 112], [138, 145]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_022

A polka-dotted scarf is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`scarf` + `worktable` + `cloth` + `window`；位置 `[[15, 20], [75, 84], [100, 105], [148, 154]]`
- **texture**：`polka-dotted`；位置 `[[2, 14]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[63, 65], [86, 90], [106, 112], [138, 145]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_023

A polka-dotted hat is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`hat` + `worktable` + `cloth` + `window`；位置 `[[15, 18], [73, 82], [98, 103], [146, 152]]`
- **texture**：`polka-dotted`；位置 `[[2, 14]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[61, 63], [84, 88], [104, 110], [136, 143]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_024

A polka-dotted handbag is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`handbag` + `worktable` + `cloth` + `window`；位置 `[[15, 22], [77, 86], [102, 107], [150, 156]]`
- **texture**：`polka-dotted`；位置 `[[2, 14]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[65, 67], [88, 92], [108, 114], [140, 147]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_025

A polka-dotted sock is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 17, "resolved_index": 18}, {"text": "nearby", "model_index": 20, "resolved_index": 19}]

- **object**：`sock` + `worktable` + `cloth` + `window`；位置 `[[15, 19], [74, 83], [99, 104], [147, 153]]`
- **texture**：`polka-dotted`；位置 `[[2, 14]]`
- **spatial_relation**：`on` + `with` + `nearby` + `through`；位置 `[[62, 64], [85, 89], [105, 111], [137, 144]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_026

A polka-dotted blanket is shown with its surface clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 17, "resolved_index": 18}]

- **object**：`blanket` + `floor` + `wall` + `window`；位置 `[[15, 22], [76, 81], [96, 100], [149, 155]]`
- **texture**：`polka-dotted`；位置 `[[2, 14]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[65, 67], [101, 107], [142, 146]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a tiled ` + `, with a plain ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_027

A polka-dotted cushion is shown with its surface clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 17, "resolved_index": 18}]

- **object**：`cushion` + `floor` + `wall` + `window`；位置 `[[15, 22], [76, 81], [96, 100], [149, 155]]`
- **texture**：`polka-dotted` + `plain`；位置 `[[2, 14], [90, 95]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[65, 67], [101, 107], [142, 146]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_028

A polka-dotted curtain is shown with its surface clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`curtain` + `bookshelves` + `window`；位置 `[[15, 22], [90, 101], [156, 162]]`
- **texture**：`polka-dotted`；位置 `[[2, 14]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[65, 67], [102, 107], [140, 147]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a quiet library, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_029

A polka-dotted tablecloth is shown with its surface clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

标注说明： Unique exact-word index repairs: [{"text": ",", "model_index": 14, "resolved_index": 15}]

- **object**：`tablecloth` + `chairs` + `window`；位置 `[[15, 25], [103, 109], [127, 133]]`
- **texture**：`polka-dotted`；位置 `[[2, 14]]`
- **spatial_relation**：`on` + `in`；位置 `[[68, 70], [142, 144]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden cafe table, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_030

A polka-dotted umbrella is shown with its surface clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`umbrella` + `garden path` + `reeds` + `trees`；位置 `[[15, 23], [75, 86], [98, 103], [116, 121]]`
- **texture**：`polka-dotted`；位置 `[[2, 14]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[66, 72], [122, 129]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded sky.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_031

A rough vase is shown with its surface clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 17, "resolved_index": 18}, {"text": "path", "model_index": 21, "resolved_index": 22}]

- **object**：`vase` + `courtyard` + `wall` + `path`；位置 `[[8, 12], [66, 75], [90, 94], [108, 112]]`
- **texture**：`rough`；位置 `[[2, 7]]`
- **spatial_relation**：`in`；位置 `[[55, 57]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_032

A rough bowl is shown with its surface clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bowl` + `counter` + `wall` + `cabinet`；位置 `[[8, 12], [68, 75], [96, 100], [114, 121]]`
- **texture**：`rough` + `plain`；位置 `[[2, 7], [84, 89]]`
- **spatial_relation**：`on` + `in`；位置 `[[55, 57], [130, 132]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a kitchen ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_033

A rough plate is shown with its surface clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`plate` + `counter` + `wall` + `cabinet`；位置 `[[8, 13], [69, 76], [97, 101], [115, 122]]`
- **texture**：`rough` + `plain`；位置 `[[2, 7], [85, 90]]`
- **spatial_relation**：`on` + `in`；位置 `[[56, 58], [131, 133]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a kitchen ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_034

A rough stone is shown with its surface clearly visible in a grassy garden, with a low stone wall and distant trees visible under soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}]

- **object**：`garden` + `wall` + `trees`；位置 `[[68, 74], [93, 97], [110, 115]]`
- **texture**：`rough`；位置 `[[2, 7]]`
- **spatial_relation**：`in` + `with` + `and`；位置 `[[56, 58], [76, 80], [98, 101]]`

保留的 other：`A ` + ` stone is shown with its surface clearly visible ` + ` a grassy ` + `, ` + ` a low stone ` + ` ` + ` distant ` + ` visible under soft daylight.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_035

A rough flowerpot is shown with its surface clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 17, "resolved_index": 18}, {"text": "path", "model_index": 21, "resolved_index": 22}]

- **object**：`flowerpot` + `courtyard` + `wall` + `path`；位置 `[[8, 17], [71, 80], [95, 99], [113, 117]]`
- **texture**：`rough`；位置 `[[2, 7]]`
- **spatial_relation**：`in`；位置 `[[60, 62]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_036

A rough wooden box is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`box` + `worktable` + `cloth` + `window`；位置 `[[15, 18], [73, 82], [98, 103], [146, 152]]`
- **texture**：`rough`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `with` + `through`；位置 `[[61, 63], [84, 88], [136, 143]]`

保留的 other：`A ` + ` wooden ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_037

A rough ceramic tile is shown with its surface clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}]

- **object**：`tile` + `floor` + `wall` + `window`；位置 `[[16, 20], [74, 79], [94, 98], [147, 153]]`
- **texture**：`rough`；位置 `[[2, 7]]`
- **spatial_relation**：`behind` + `from`；位置 `[[99, 105], [140, 144]]`

保留的 other：`A ` + ` ceramic ` + ` is shown with its surface clearly visible on a tiled ` + `, with a plain ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_038

A rough sculpture is shown with its surface clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 17, "resolved_index": 18}, {"text": "path", "model_index": 21, "resolved_index": 22}]

- **object**：`sculpture` + `courtyard` + `wall` + `path`；位置 `[[8, 17], [71, 80], [95, 99], [113, 117]]`
- **texture**：`rough`；位置 `[[2, 7]]`
- **spatial_relation**：`in`；位置 `[[60, 62]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_039

A rough tray is shown with its surface clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`tray` + `table` + `chairs` + `window`；位置 `[[8, 12], [72, 77], [90, 96], [114, 120]]`
- **texture**：`rough`；位置 `[[2, 7]]`
- **spatial_relation**：`on` + `in`；位置 `[[55, 57], [129, 131]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_040

A rough statue is shown with its surface clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 17, "resolved_index": 18}, {"text": "path", "model_index": 21, "resolved_index": 22}]

- **object**：`statue` + `courtyard` + `wall` + `path`；位置 `[[8, 14], [68, 77], [92, 96], [110, 114]]`
- **texture**：`rough`；位置 `[[2, 7]]`
- **spatial_relation**：`in`；位置 `[[57, 59]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_041

A smooth vase is shown with its surface clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 17, "resolved_index": 18}, {"text": "path", "model_index": 21, "resolved_index": 22}]

- **object**：`vase` + `courtyard` + `wall` + `path`；位置 `[[9, 13], [67, 76], [91, 95], [109, 113]]`
- **texture**：`smooth`；位置 `[[2, 8]]`
- **spatial_relation**：`in`；位置 `[[56, 58]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_042

A smooth bowl is shown with its surface clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bowl` + `counter` + `wall` + `cabinet`；位置 `[[9, 13], [69, 76], [97, 101], [115, 122]]`
- **texture**：`smooth` + `plain`；位置 `[[2, 8], [85, 90]]`
- **spatial_relation**：`on` + `in`；位置 `[[56, 58], [131, 133]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a kitchen ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_043

A smooth plate is shown with its surface clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`plate` + `counter` + `wall` + `cabinet`；位置 `[[9, 14], [70, 77], [98, 102], [116, 123]]`
- **texture**：`smooth` + `plain`；位置 `[[2, 8], [86, 91]]`
- **spatial_relation**：`on` + `in`；位置 `[[57, 59], [132, 134]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a kitchen ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_044

A smooth stone is shown with its surface clearly visible in a grassy garden, with a low stone wall and distant trees visible under soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}]

- **object**：`garden` + `wall` + `trees`；位置 `[[69, 75], [94, 98], [111, 116]]`
- **texture**：`smooth`；位置 `[[2, 8]]`
- **spatial_relation**：`in` + `with` + `and`；位置 `[[57, 59], [77, 81], [99, 102]]`

保留的 other：`A ` + ` stone is shown with its surface clearly visible ` + ` a grassy ` + `, ` + ` a low stone ` + ` ` + ` distant ` + ` visible under soft daylight.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_045

A smooth flowerpot is shown with its surface clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 17, "resolved_index": 18}, {"text": "path", "model_index": 21, "resolved_index": 22}]

- **object**：`flowerpot` + `courtyard` + `wall` + `path`；位置 `[[9, 18], [72, 81], [96, 100], [114, 118]]`
- **texture**：`smooth`；位置 `[[2, 8]]`
- **spatial_relation**：`in`；位置 `[[61, 63]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_046

A smooth wooden box is shown with its surface clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 18, "resolved_index": 19}, {"text": "and", "model_index": 22, "resolved_index": 21}]

- **object**：`box` + `worktable` + `cloth` + `window`；位置 `[[16, 19], [74, 83], [99, 104], [147, 153]]`
- **texture**：`smooth`；位置 `[[2, 8]]`
- **spatial_relation**：`on` + `with` + `and` + `through`；位置 `[[62, 64], [85, 89], [112, 115], [137, 144]]`

保留的 other：`A ` + ` wooden ` + ` is shown with its surface clearly visible ` + ` a wooden ` + `, ` + ` a folded ` + ` nearby ` + ` soft daylight coming ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_047

A smooth ceramic tile is shown with its surface clearly visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

- **object**：`tile` + `floor` + `plain wall` + `window`；位置 `[[17, 21], [75, 80], [89, 99], [148, 154]]`
- **texture**：`smooth`；位置 `[[2, 8]]`
- **spatial_relation**：`behind` + `from`；位置 `[[100, 106], [141, 145]]`

保留的 other：`A ` + ` ceramic ` + ` is shown with its surface clearly visible on a tiled ` + `, with a ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_048

A smooth sculpture is shown with its surface clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 17, "resolved_index": 18}, {"text": "path", "model_index": 21, "resolved_index": 22}]

- **object**：`sculpture` + `courtyard` + `wall` + `path`；位置 `[[9, 18], [72, 81], [96, 100], [114, 118]]`
- **texture**：`smooth`；位置 `[[2, 8]]`
- **spatial_relation**：`in`；位置 `[[61, 63]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_049

A smooth tray is shown with its surface clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`tray` + `table` + `chairs` + `window`；位置 `[[9, 13], [73, 78], [91, 97], [115, 121]]`
- **texture**：`smooth`；位置 `[[2, 8]]`
- **spatial_relation**：`on` + `in`；位置 `[[56, 58], [130, 132]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## texture_050

A smooth statue is shown with its surface clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 17, "resolved_index": 18}, {"text": "path", "model_index": 21, "resolved_index": 22}]

- **object**：`statue` + `courtyard` + `wall` + `path`；位置 `[[9, 15], [69, 78], [93, 97], [111, 115]]`
- **texture**：`smooth`；位置 `[[2, 8]]`
- **spatial_relation**：`in`；位置 `[[58, 60]]`

保留的 other：`A ` + ` ` + ` is shown with its surface clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_001

Two mugs are arranged separately, with every item fully visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`mugs` + `table` + `chairs` + `window`；位置 `[[4, 8], [81, 86], [99, 105], [123, 129]]`
- **count**：`Two`；位置 `[[0, 3]]`
- **spatial_relation**：`on` + `in`；位置 `[[64, 66], [138, 140]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_002

Two bottles are arranged separately, with every item fully visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bottles` + `kitchen counter` + `wall` + `cabinet`；位置 `[[4, 11], [72, 87], [108, 112], [126, 133]]`
- **count**：`Two`；位置 `[[0, 3]]`
- **spatial_relation**：`separately` + `on` + `with` + `in`；位置 `[[25, 35], [67, 69], [89, 93], [142, 144]]`

保留的 other：` ` + ` are arranged ` + `, with every item fully visible ` + ` a ` + `, ` + ` a plain tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_003

Two books are arranged separately, with every item fully visible on a library reading table, with a plain wall and a closed storage cabinet visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "cabinet", "model_index": 24, "resolved_index": 25}]

- **object**：`books` + `table` + `wall` + `cabinet`；位置 `[[4, 9], [86, 91], [106, 110], [132, 139]]`
- **count**：`Two`；位置 `[[0, 3]]`
- **spatial_relation**：`on`；位置 `[[65, 67]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a library reading ` + `, with a plain ` + ` and a closed storage ` + ` visible in soft daylight.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_004

Two hourglasses are arranged separately, with every item fully visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 23, "resolved_index": 24}]

- **object**：`hourglasses` + `office desk` + `computer monitor` + `wall`；位置 `[[4, 15], [77, 88], [102, 118], [131, 135]]`
- **texture**：`plain`；位置 `[[125, 130]]`
- **count**：`Two`；位置 `[[0, 3]]`
- **spatial_relation**：`arranged separately` + `on` + `in the`；位置 `[[20, 39], [71, 73], [144, 150]]`

保留的 other：` ` + ` are ` + `, with every item fully visible ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible ` + ` background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_005

Two remote controls are arranged separately, with every item fully visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 19, "resolved_index": 20}]

- **object**：`remote controls` + `floor` + `wall` + `window`；位置 `[[4, 19], [86, 91], [106, 110], [159, 165]]`
- **texture**：`plain`；位置 `[[100, 105]]`
- **count**：`Two`；位置 `[[0, 3]]`
- **spatial_relation**：`behind` + `from`；位置 `[[111, 117], [152, 156]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible on a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_006

Two toy cars are arranged separately, with every item fully visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`cars` + `office desk` + `computer monitor` + `plain wall`；位置 `[[8, 12], [74, 85], [99, 115], [122, 132]]`
- **count**：`Two`；位置 `[[0, 3]]`
- **spatial_relation**：`on` + `in`；位置 `[[68, 70], [141, 143]]`

保留的 other：` toy ` + ` are arranged separately, with every item fully visible ` + ` an ` + `, with a dark ` + ` and a ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_007

Two hats are arranged separately, with every item fully visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 18, "resolved_index": 19}]

- **object**：`hats` + `worktable` + `cloth` + `window`；位置 `[[4, 8], [76, 85], [101, 106], [149, 155]]`
- **count**：`Two`；位置 `[[0, 3]]`
- **spatial_relation**：`separately` + `on` + `with` + `through`；位置 `[[22, 32], [64, 66], [87, 91], [139, 146]]`

保留的 other：` ` + ` are arranged ` + `, with every item fully visible ` + ` a wooden ` + `, ` + ` a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_008

Two bowls are arranged separately, with every item fully visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bowls` + `kitchen counter` + `wall` + `cabinet`；位置 `[[4, 9], [70, 85], [106, 110], [124, 131]]`
- **texture**：`plain`；位置 `[[94, 99]]`
- **count**：`Two`；位置 `[[0, 3]]`
- **spatial_relation**：`separately` + `on` + `with` + `in`；位置 `[[23, 33], [65, 67], [87, 91], [140, 142]]`

保留的 other：` ` + ` are arranged ` + `, with every item fully visible ` + ` a ` + `, ` + ` a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_009

Two flowerpots are arranged separately, with every item fully visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`flowerpots` + `courtyard` + `wall` + `path`；位置 `[[4, 14], [81, 90], [105, 109], [123, 127]]`
- **count**：`Two`；位置 `[[0, 3]]`
- **spatial_relation**：`separately` + `in`；位置 `[[28, 38], [70, 72]]`

保留的 other：` ` + ` are arranged ` + `, with every item fully visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_010

Two baskets are arranged separately, with every item fully visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`baskets` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[4, 11], [76, 87], [99, 104], [117, 122], [149, 152]]`
- **count**：`Two`；位置 `[[0, 3]]`
- **spatial_relation**：`separately` + `beside` + `beneath`；位置 `[[25, 35], [67, 73], [123, 130]]`

保留的 other：` ` + ` are arranged ` + `, with every item fully visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_011

Three mugs are arranged separately, with every item fully visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`mugs` + `table` + `chairs` + `window`；位置 `[[6, 10], [83, 88], [101, 107], [125, 131]]`
- **count**：`Three`；位置 `[[0, 5]]`
- **spatial_relation**：`on` + `in`；位置 `[[66, 68], [140, 142]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_012

Three bottles are arranged separately, with every item fully visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bottles` + `kitchen counter` + `wall` + `cabinet`；位置 `[[6, 13], [74, 89], [110, 114], [128, 135]]`
- **texture**：`plain`；位置 `[[98, 103]]`
- **count**：`Three`；位置 `[[0, 5]]`
- **spatial_relation**：`on` + `in`；位置 `[[69, 71], [144, 146]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_013

Three books are arranged separately, with every item fully visible on a library reading table, with a plain wall and a closed storage cabinet visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "cabinet", "model_index": 24, "resolved_index": 25}]

- **object**：`books` + `table` + `wall` + `cabinet`；位置 `[[6, 11], [88, 93], [108, 112], [134, 141]]`
- **count**：`Three`；位置 `[[0, 5]]`
- **spatial_relation**：`on`；位置 `[[67, 69]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a library reading ` + `, with a plain ` + ` and a closed storage ` + ` visible in soft daylight.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_014

Three hourglasses are arranged separately, with every item fully visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`hourglasses` + `office desk` + `computer monitor` + `wall`；位置 `[[6, 17], [79, 90], [104, 120], [133, 137]]`
- **texture**：`plain`；位置 `[[127, 132]]`
- **count**：`Three`；位置 `[[0, 5]]`
- **spatial_relation**：`on`；位置 `[[73, 75]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_015

Three remote controls are arranged separately, with every item fully visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 19, "resolved_index": 20}]

- **object**：`remote controls` + `floor` + `wall` + `window`；位置 `[[6, 21], [88, 93], [108, 112], [161, 167]]`
- **texture**：`plain`；位置 `[[102, 107]]`
- **count**：`Three`；位置 `[[0, 5]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[77, 79], [113, 119], [154, 158]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_016

Three toy cars are arranged separately, with every item fully visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`cars` + `office desk` + `computer monitor` + `plain wall`；位置 `[[10, 14], [76, 87], [101, 117], [124, 134]]`
- **count**：`Three`；位置 `[[0, 5]]`
- **spatial_relation**：`on` + `in`；位置 `[[70, 72], [143, 145]]`

保留的 other：` toy ` + ` are arranged separately, with every item fully visible ` + ` an ` + `, with a dark ` + ` and a ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_017

Three hats are arranged separately, with every item fully visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 18, "resolved_index": 19}]

- **object**：`hats` + `worktable` + `cloth` + `window`；位置 `[[6, 10], [78, 87], [103, 108], [151, 157]]`
- **count**：`Three`；位置 `[[0, 5]]`
- **spatial_relation**：`on` + `with` + `through`；位置 `[[66, 68], [89, 93], [141, 148]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a wooden ` + `, ` + ` a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_018

Three bowls are arranged separately, with every item fully visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bowls` + `kitchen counter` + `wall` + `cabinet`；位置 `[[6, 11], [72, 87], [108, 112], [126, 133]]`
- **texture**：`plain`；位置 `[[96, 101]]`
- **count**：`Three`；位置 `[[0, 5]]`
- **spatial_relation**：`on` + `in`；位置 `[[67, 69], [142, 144]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_019

Three flowerpots are arranged separately, with every item fully visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`flowerpots` + `courtyard` + `wall` + `path`；位置 `[[6, 16], [83, 92], [107, 111], [125, 129]]`
- **count**：`Three`；位置 `[[0, 5]]`
- **spatial_relation**：`in`；位置 `[[72, 74]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_020

Three baskets are arranged separately, with every item fully visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`baskets` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[6, 13], [78, 89], [101, 106], [119, 124], [151, 154]]`
- **count**：`Three`；位置 `[[0, 5]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[69, 75], [125, 132]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_021

Four mugs are arranged separately, with every item fully visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`mugs` + `table` + `chairs` + `window`；位置 `[[5, 9], [82, 87], [100, 106], [124, 130]]`
- **count**：`Four`；位置 `[[0, 4]]`
- **spatial_relation**：`on` + `in`；位置 `[[65, 67], [139, 141]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_022

Four bottles are arranged separately, with every item fully visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bottles` + `kitchen counter` + `wall` + `cabinet`；位置 `[[5, 12], [73, 88], [109, 113], [127, 134]]`
- **texture**：`plain`；位置 `[[97, 102]]`
- **count**：`Four`；位置 `[[0, 4]]`
- **spatial_relation**：`on` + `in`；位置 `[[68, 70], [143, 145]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_023

Four books are arranged separately, with every item fully visible on a library reading table, with a plain wall and a closed storage cabinet visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "cabinet", "model_index": 24, "resolved_index": 25}]

- **object**：`books` + `table` + `wall` + `cabinet`；位置 `[[5, 10], [87, 92], [107, 111], [133, 140]]`
- **count**：`Four`；位置 `[[0, 4]]`
- **spatial_relation**：`on`；位置 `[[66, 68]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a library reading ` + `, with a plain ` + ` and a closed storage ` + ` visible in soft daylight.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_024

Four hourglasses are arranged separately, with every item fully visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 23, "resolved_index": 24}]

- **object**：`hourglasses` + `office desk` + `computer monitor` + `wall`；位置 `[[5, 16], [78, 89], [103, 119], [132, 136]]`
- **texture**：`plain`；位置 `[[126, 131]]`
- **count**：`Four`；位置 `[[0, 4]]`
- **spatial_relation**：`separately` + `on` + `with` + `in`；位置 `[[30, 40], [72, 74], [91, 95], [145, 147]]`

保留的 other：` ` + ` are arranged ` + `, with every item fully visible ` + ` an ` + `, ` + ` a dark ` + ` and a ` + ` ` + ` visible ` + ` the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_025

Four remote controls are arranged separately, with every item fully visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 19, "resolved_index": 20}]

- **object**：`remote controls` + `floor` + `wall` + `window`；位置 `[[5, 20], [87, 92], [107, 111], [160, 166]]`
- **texture**：`plain`；位置 `[[101, 106]]`
- **count**：`Four`；位置 `[[0, 4]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[76, 78], [112, 118], [153, 157]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_026

Four toy cars are arranged separately, with every item fully visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`cars` + `office desk` + `computer monitor` + `plain wall`；位置 `[[9, 13], [75, 86], [100, 116], [123, 133]]`
- **count**：`Four`；位置 `[[0, 4]]`
- **spatial_relation**：`on` + `in`；位置 `[[69, 71], [142, 144]]`

保留的 other：` toy ` + ` are arranged separately, with every item fully visible ` + ` an ` + `, with a dark ` + ` and a ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_027

Four hats are arranged separately, with every item fully visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 18, "resolved_index": 19}]

- **object**：`hats` + `worktable` + `cloth` + `window`；位置 `[[5, 9], [77, 86], [102, 107], [150, 156]]`
- **count**：`Four`；位置 `[[0, 4]]`
- **spatial_relation**：`on` + `with` + `nearby` + `coming through`；位置 `[[65, 67], [88, 92], [108, 114], [133, 147]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a wooden ` + `, ` + ` a folded ` + ` ` + ` and soft daylight ` + ` a ` + `.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_028

Four bowls are arranged separately, with every item fully visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bowls` + `kitchen counter` + `wall` + `cabinet`；位置 `[[5, 10], [71, 86], [107, 111], [125, 132]]`
- **texture**：`plain`；位置 `[[95, 100]]`
- **count**：`Four`；位置 `[[0, 4]]`
- **spatial_relation**：`on` + `in`；位置 `[[66, 68], [141, 143]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_029

Four flowerpots are arranged separately, with every item fully visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`flowerpots` + `courtyard` + `wall` + `path`；位置 `[[5, 15], [82, 91], [106, 110], [124, 128]]`
- **count**：`Four`；位置 `[[0, 4]]`
- **spatial_relation**：`in`；位置 `[[71, 73]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_030

Four baskets are arranged separately, with every item fully visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`baskets` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[5, 12], [77, 88], [100, 105], [118, 123], [150, 153]]`
- **count**：`Four`；位置 `[[0, 4]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[68, 74], [124, 131]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_031

Five mugs are arranged separately, with every item fully visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`mugs` + `table` + `chairs` + `window`；位置 `[[5, 9], [82, 87], [100, 106], [124, 130]]`
- **count**：`Five`；位置 `[[0, 4]]`
- **spatial_relation**：`on` + `in`；位置 `[[65, 67], [139, 141]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_032

Five bottles are arranged separately, with every item fully visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bottles` + `kitchen counter` + `wall` + `cabinet`；位置 `[[5, 12], [73, 88], [109, 113], [127, 134]]`
- **texture**：`plain`；位置 `[[97, 102]]`
- **count**：`Five`；位置 `[[0, 4]]`
- **spatial_relation**：`on` + `in`；位置 `[[68, 70], [143, 145]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_033

Five books are arranged separately, with every item fully visible on a library reading table, with a plain wall and a closed storage cabinet visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "cabinet", "model_index": 24, "resolved_index": 25}]

- **object**：`books` + `table` + `wall` + `cabinet`；位置 `[[5, 10], [87, 92], [107, 111], [133, 140]]`
- **count**：`Five`；位置 `[[0, 4]]`
- **spatial_relation**：`on`；位置 `[[66, 68]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a library reading ` + `, with a plain ` + ` and a closed storage ` + ` visible in soft daylight.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_034

Five hourglasses are arranged separately, with every item fully visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 23, "resolved_index": 24}]

- **object**：`hourglasses` + `office desk` + `computer monitor` + `wall`；位置 `[[5, 16], [78, 89], [103, 119], [132, 136]]`
- **texture**：`plain`；位置 `[[126, 131]]`
- **count**：`Five`；位置 `[[0, 4]]`
- **spatial_relation**：`separately` + `on` + `with` + `in`；位置 `[[30, 40], [72, 74], [91, 95], [145, 147]]`

保留的 other：` ` + ` are arranged ` + `, with every item fully visible ` + ` an ` + `, ` + ` a dark ` + ` and a ` + ` ` + ` visible ` + ` the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_035

Five remote controls are arranged separately, with every item fully visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 19, "resolved_index": 20}]

- **object**：`remote controls` + `floor` + `wall` + `window`；位置 `[[5, 20], [87, 92], [107, 111], [160, 166]]`
- **texture**：`plain`；位置 `[[101, 106]]`
- **count**：`Five`；位置 `[[0, 4]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[76, 78], [112, 118], [153, 157]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a tiled ` + `, with a ` + ` ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_036

Five toy cars are arranged separately, with every item fully visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`cars` + `office desk` + `computer monitor` + `plain wall`；位置 `[[9, 13], [75, 86], [100, 116], [123, 133]]`
- **count**：`Five`；位置 `[[0, 4]]`
- **spatial_relation**：`on` + `in`；位置 `[[69, 71], [142, 144]]`

保留的 other：` toy ` + ` are arranged separately, with every item fully visible ` + ` an ` + `, with a dark ` + ` and a ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_037

Five hats are arranged separately, with every item fully visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 18, "resolved_index": 19}]

- **object**：`hats` + `worktable` + `cloth` + `window`；位置 `[[5, 9], [77, 86], [102, 107], [150, 156]]`
- **count**：`Five`；位置 `[[0, 4]]`
- **spatial_relation**：`on` + `with` + `coming through`；位置 `[[65, 67], [88, 92], [133, 147]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a wooden ` + `, ` + ` a folded ` + ` nearby and soft daylight ` + ` a ` + `.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_038

Five bowls are arranged separately, with every item fully visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bowls` + `kitchen counter` + `wall` + `cabinet`；位置 `[[5, 10], [71, 86], [107, 111], [125, 132]]`
- **texture**：`plain`；位置 `[[95, 100]]`
- **count**：`Five`；位置 `[[0, 4]]`
- **spatial_relation**：`on` + `in`；位置 `[[66, 68], [141, 143]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_039

Five flowerpots are arranged separately, with every item fully visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`flowerpots` + `courtyard` + `wall` + `path`；位置 `[[5, 15], [82, 91], [106, 110], [124, 128]]`
- **count**：`Five`；位置 `[[0, 4]]`
- **spatial_relation**：`in`；位置 `[[71, 73]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_040

Five baskets are arranged separately, with every item fully visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`baskets` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[5, 12], [77, 88], [100, 105], [118, 123], [150, 153]]`
- **count**：`Five`；位置 `[[0, 4]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[68, 74], [124, 131]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_041

Six mugs are arranged separately, with every item fully visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`mugs` + `table` + `chairs` + `window`；位置 `[[4, 8], [81, 86], [99, 105], [123, 129]]`
- **count**：`Six`；位置 `[[0, 3]]`
- **spatial_relation**：`on` + `in`；位置 `[[64, 66], [138, 140]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a wooden cafe ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_042

Six bottles are arranged separately, with every item fully visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bottles` + `kitchen counter` + `wall` + `cabinet`；位置 `[[4, 11], [72, 87], [108, 112], [126, 133]]`
- **count**：`Six`；位置 `[[0, 3]]`
- **spatial_relation**：`on` + `in`；位置 `[[67, 69], [142, 144]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a ` + `, with a plain tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_043

Six books are arranged separately, with every item fully visible on a library reading table, with a plain wall and a closed storage cabinet visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "cabinet", "model_index": 24, "resolved_index": 25}]

- **object**：`books` + `table` + `wall` + `cabinet`；位置 `[[4, 9], [86, 91], [106, 110], [132, 139]]`
- **count**：`Six`；位置 `[[0, 3]]`
- **spatial_relation**：`on`；位置 `[[65, 67]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a library reading ` + `, with a plain ` + ` and a closed storage ` + ` visible in soft daylight.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_044

Six hourglasses are arranged separately, with every item fully visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`hourglasses` + `office desk` + `computer monitor` + `plain wall`；位置 `[[4, 15], [77, 88], [102, 118], [125, 135]]`
- **count**：`Six`；位置 `[[0, 3]]`
- **spatial_relation**：`arranged` + `on` + `in`；位置 `[[20, 28], [71, 73], [144, 146]]`

保留的 other：` ` + ` are ` + ` separately, with every item fully visible ` + ` an ` + `, with a dark ` + ` and a ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_045

Six remote controls are arranged separately, with every item fully visible on a tiled floor, with a plain wall behind the scene and soft light entering from a window.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 19, "resolved_index": 20}]

- **object**：`remote controls` + `floor` + `wall` + `window`；位置 `[[4, 19], [86, 91], [106, 110], [159, 165]]`
- **count**：`Six`；位置 `[[0, 3]]`
- **spatial_relation**：`on` + `behind` + `from`；位置 `[[75, 77], [111, 117], [152, 156]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a tiled ` + `, with a plain ` + ` ` + ` the scene and soft light entering ` + ` a ` + `.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_046

Six toy cars are arranged separately, with every item fully visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`cars` + `office desk` + `computer monitor` + `plain wall`；位置 `[[8, 12], [74, 85], [99, 115], [122, 132]]`
- **count**：`Six`；位置 `[[0, 3]]`
- **spatial_relation**：`on` + `in`；位置 `[[68, 70], [141, 143]]`

保留的 other：` toy ` + ` are arranged separately, with every item fully visible ` + ` an ` + `, with a dark ` + ` and a ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_047

Six hats are arranged separately, with every item fully visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 18, "resolved_index": 19}]

- **object**：`hats` + `worktable` + `cloth` + `window`；位置 `[[4, 8], [76, 85], [101, 106], [149, 155]]`
- **count**：`Six`；位置 `[[0, 3]]`
- **spatial_relation**：`on` + `with` + `coming through`；位置 `[[64, 66], [87, 91], [132, 146]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a wooden ` + `, ` + ` a folded ` + ` nearby and soft daylight ` + ` a ` + `.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_048

Six bowls are arranged separately, with every item fully visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`bowls` + `kitchen counter` + `wall` + `cabinet`；位置 `[[4, 9], [70, 85], [106, 110], [124, 131]]`
- **count**：`Six`；位置 `[[0, 3]]`
- **spatial_relation**：`on` + `with` + `in`；位置 `[[65, 67], [87, 91], [140, 142]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a ` + `, ` + ` a plain tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_049

Six flowerpots are arranged separately, with every item fully visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 18, "resolved_index": 19}, {"text": "path", "model_index": 22, "resolved_index": 23}]

- **object**：`flowerpots` + `courtyard` + `wall` + `path`；位置 `[[4, 14], [81, 90], [105, 109], [123, 127]]`
- **count**：`Six`；位置 `[[0, 3]]`
- **spatial_relation**：`in`；位置 `[[70, 72]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_050

Six baskets are arranged separately, with every item fully visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`baskets` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[4, 11], [76, 87], [99, 104], [117, 122], [149, 152]]`
- **count**：`Six`；位置 `[[0, 3]]`
- **spatial_relation**：`beside` + `beneath`；位置 `[[67, 73], [123, 130]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_001

A mug is to the left of a coffee pot, with both objects separated and visible from the front on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`mug` + `coffee pot` + `cafe table` + `chairs` + `window`；位置 `[[2, 5], [26, 36], [105, 115], [128, 134], [152, 158]]`
- **spatial_relation**：`to the left of` + `on` + `in the`；位置 `[[9, 23], [93, 95], [167, 173]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` a wooden ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_002

A vase is to the left of a bowl, with both objects separated and visible from the front in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "path", "model_index": 30, "resolved_index": 31}]

- **object**：`vase` + `bowl` + `courtyard` + `wall` + `path`；位置 `[[2, 6], [27, 31], [99, 108], [123, 127], [141, 145]]`
- **spatial_relation**：`to the left of` + `in`；位置 `[[10, 24], [88, 90]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_003

A toy car is to the left of a wooden box, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`toy car` + `box` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 9], [37, 40], [103, 114], [128, 144], [157, 161]]`
- **texture**：`plain`；位置 `[[151, 156]]`
- **count**：`both`；位置 `[[47, 51]]`
- **spatial_relation**：`to the left of` + `on`；位置 `[[13, 27], [97, 99]]`

保留的 other：`A ` + ` is ` + ` a wooden ` + `, with ` + ` objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_004

A notebook is to the left of a pencil case, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`notebook` + `pencil case` + `office desk` + `computer` + `wall`；位置 `[[2, 10], [31, 42], [105, 116], [130, 138], [159, 163]]`
- **texture**：`plain`；位置 `[[153, 158]]`
- **spatial_relation**：`to the left of` + `on` + `in the`；位置 `[[14, 28], [99, 101], [172, 178]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` monitor and a ` + ` ` + ` visible ` + ` background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_005

A hat is to the left of a handbag, with both objects separated and visible from the front on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`hat` + `handbag` + `worktable` + `cloth` + `window`；位置 `[[2, 5], [26, 33], [102, 111], [127, 132], [175, 181]]`
- **spatial_relation**：`to the left of` + `on` + `through`；位置 `[[9, 23], [90, 92], [165, 172]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_006

A coffee pot is to the left of a mug, with both objects separated and visible from the front on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`coffee pot` + `mug` + `cafe table` + `chairs` + `window`；位置 `[[2, 12], [33, 36], [105, 115], [128, 134], [152, 158]]`
- **spatial_relation**：`to the left of` + `on` + `in the`；位置 `[[16, 30], [93, 95], [167, 173]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` a wooden ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_007

A bowl is to the left of a vase, with both objects separated and visible from the front in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "path", "model_index": 30, "resolved_index": 31}]

- **object**：`bowl` + `vase` + `courtyard` + `wall` + `path`；位置 `[[2, 6], [27, 31], [99, 108], [123, 127], [141, 145]]`
- **spatial_relation**：`to the left of` + `in`；位置 `[[10, 24], [88, 90]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_008

A wooden box is to the left of a toy car, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`box` + `toy car` + `office desk` + `computer monitor` + `wall`；位置 `[[9, 12], [33, 40], [103, 114], [128, 144], [157, 161]]`
- **texture**：`plain`；位置 `[[151, 156]]`
- **count**：`both`；位置 `[[47, 51]]`
- **spatial_relation**：`to the left of` + `on`；位置 `[[16, 30], [97, 99]]`

保留的 other：`A wooden ` + ` is ` + ` a ` + `, with ` + ` objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_009

A pencil case is to the left of a notebook, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`pencil case` + `notebook` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 13], [34, 42], [105, 116], [130, 146], [159, 163]]`
- **texture**：`plain`；位置 `[[153, 158]]`
- **count**：`both`；位置 `[[49, 53]]`
- **spatial_relation**：`to the left of` + `on`；位置 `[[17, 31], [99, 101]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with ` + ` objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_010

A handbag is to the left of a hat, with both objects separated and visible from the front on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`handbag` + `hat` + `worktable` + `cloth` + `window`；位置 `[[2, 9], [30, 33], [102, 111], [127, 132], [175, 181]]`
- **spatial_relation**：`to the left of` + `on` + `through`；位置 `[[13, 27], [90, 92], [165, 172]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_011

A mug is to the right of a coffee pot, with both objects separated and visible from the front on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`mug` + `coffee pot` + `cafe table` + `chairs` + `window`；位置 `[[2, 5], [27, 37], [106, 116], [129, 135], [153, 159]]`
- **spatial_relation**：`to the right of` + `on` + `in the`；位置 `[[9, 24], [94, 96], [168, 174]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` a wooden ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_012

A vase is to the right of a bowl, with both objects separated and visible from the front in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "path", "model_index": 30, "resolved_index": 31}]

- **object**：`vase` + `bowl` + `courtyard` + `wall` + `path`；位置 `[[2, 6], [28, 32], [100, 109], [124, 128], [142, 146]]`
- **spatial_relation**：`to the right of` + `in`；位置 `[[10, 25], [89, 91]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_013

A toy car is to the right of a wooden box, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`toy car` + `box` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 9], [38, 41], [104, 115], [129, 145], [158, 162]]`
- **texture**：`plain`；位置 `[[152, 157]]`
- **count**：`both`；位置 `[[48, 52]]`
- **spatial_relation**：`to the right of` + `on`；位置 `[[13, 28], [98, 100]]`

保留的 other：`A ` + ` is ` + ` a wooden ` + `, with ` + ` objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_014

A notebook is to the right of a pencil case, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`notebook` + `pencil case` + `office desk` + `computer` + `wall`；位置 `[[2, 10], [32, 43], [106, 117], [131, 139], [160, 164]]`
- **texture**：`plain`；位置 `[[154, 159]]`
- **spatial_relation**：`to the right of` + `on` + `in the`；位置 `[[14, 29], [100, 102], [173, 179]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` monitor and a ` + ` ` + ` visible ` + ` background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_015

A hat is to the right of a handbag, with both objects separated and visible from the front on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`hat` + `handbag` + `worktable` + `cloth` + `window`；位置 `[[2, 5], [27, 34], [103, 112], [128, 133], [176, 182]]`
- **spatial_relation**：`to the right of` + `on` + `through`；位置 `[[9, 24], [91, 93], [166, 173]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_016

A coffee pot is to the right of a mug, with both objects separated and visible from the front on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`coffee pot` + `mug` + `cafe table` + `chairs` + `window`；位置 `[[2, 12], [34, 37], [106, 116], [129, 135], [153, 159]]`
- **spatial_relation**：`to the right of` + `on` + `in the`；位置 `[[16, 31], [94, 96], [168, 174]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` a wooden ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_017

A bowl is to the right of a vase, with both objects separated and visible from the front in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "path", "model_index": 30, "resolved_index": 31}]

- **object**：`bowl` + `vase` + `courtyard` + `wall` + `path`；位置 `[[2, 6], [28, 32], [100, 109], [124, 128], [142, 146]]`
- **spatial_relation**：`to the right of` + `in`；位置 `[[10, 25], [89, 91]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_018

A wooden box is to the right of a toy car, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`box` + `toy car` + `office desk` + `computer monitor` + `wall`；位置 `[[9, 12], [34, 41], [104, 115], [129, 145], [158, 162]]`
- **texture**：`plain`；位置 `[[152, 157]]`
- **count**：`both`；位置 `[[48, 52]]`
- **spatial_relation**：`to the right of` + `on`；位置 `[[16, 31], [98, 100]]`

保留的 other：`A wooden ` + ` is ` + ` a ` + `, with ` + ` objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_019

A pencil case is to the right of a notebook, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`pencil case` + `notebook` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 13], [35, 43], [106, 117], [131, 147], [160, 164]]`
- **texture**：`plain`；位置 `[[154, 159]]`
- **count**：`both`；位置 `[[50, 54]]`
- **spatial_relation**：`to the right of` + `on`；位置 `[[17, 32], [100, 102]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with ` + ` objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_020

A handbag is to the right of a hat, with both objects separated and visible from the front on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`handbag` + `hat` + `worktable` + `cloth` + `window`；位置 `[[2, 9], [31, 34], [103, 112], [128, 133], [176, 182]]`
- **spatial_relation**：`to the right of` + `on` + `through`；位置 `[[13, 28], [91, 93], [166, 173]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects separated and visible from the front ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_021

A picture frame is mounted above a wall clock, with both objects fully visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`picture frame` + `wall clock` + `bookshelves` + `window`；位置 `[[2, 15], [35, 45], [104, 115], [170, 176]]`
- **spatial_relation**：`above` + `in` + `along` + `through`；位置 `[[27, 32], [79, 81], [116, 121], [154, 161]]`

保留的 other：`A ` + ` is mounted ` + ` a ` + `, with both objects fully visible ` + ` a quiet library, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_022

A shelf is mounted above a mirror, with both objects fully visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

- **object**：`shelf` + `mirror` + `courtyard` + `wall` + `path`；位置 `[[2, 7], [27, 33], [78, 87], [102, 106], [120, 124]]`
- **spatial_relation**：`above` + `in`；位置 `[[19, 24], [67, 69]]`

保留的 other：`A ` + ` is mounted ` + ` a ` + `, with both objects fully visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_023

A sign is mounted above a picture frame, with both objects fully visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`sign` + `picture frame` + `library` + `bookshelves` + `window`；位置 `[[2, 6], [26, 39], [84, 91], [98, 109], [164, 170]]`
- **spatial_relation**：`above` + `in` + `along` + `through`；位置 `[[18, 23], [73, 75], [110, 115], [148, 155]]`

保留的 other：`A ` + ` is mounted ` + ` a ` + `, with both objects fully visible ` + ` a quiet ` + `, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_024

A wall lamp is mounted above a shelf, with both objects fully visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`wall lamp` + `shelf` + `library` + `bookshelves` + `window`；位置 `[[2, 11], [31, 36], [81, 88], [95, 106], [161, 167]]`
- **spatial_relation**：`above` + `in` + `through`；位置 `[[23, 28], [70, 72], [145, 152]]`

保留的 other：`A ` + ` is mounted ` + ` a ` + `, with both objects fully visible ` + ` a quiet ` + `, with ` + ` along the walls and daylight entering ` + ` a large ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_025

A wall clock is mounted above a sign, with both objects fully visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

- **object**：`wall clock` + `sign` + `courtyard` + `wall` + `path`；位置 `[[2, 12], [32, 36], [81, 90], [105, 109], [123, 127]]`
- **spatial_relation**：`above` + `in`；位置 `[[24, 29], [70, 72]]`

保留的 other：`A ` + ` is mounted ` + ` a ` + `, with both objects fully visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_026

A picture frame is mounted below a wall clock, with both objects fully visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`picture frame` + `wall clock` + `bookshelves` + `window`；位置 `[[2, 15], [35, 45], [104, 115], [170, 176]]`
- **spatial_relation**：`below` + `in` + `along` + `through`；位置 `[[27, 32], [79, 81], [116, 121], [154, 161]]`

保留的 other：`A ` + ` is mounted ` + ` a ` + `, with both objects fully visible ` + ` a quiet library, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_027

A shelf is mounted below a mirror, with both objects fully visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

- **object**：`shelf` + `mirror` + `courtyard` + `wall` + `path`；位置 `[[2, 7], [27, 33], [78, 87], [102, 106], [120, 124]]`
- **spatial_relation**：`below` + `in`；位置 `[[19, 24], [67, 69]]`

保留的 other：`A ` + ` is mounted ` + ` a ` + `, with both objects fully visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_028

A sign is mounted below a picture frame, with both objects fully visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`sign` + `picture frame` + `library` + `bookshelves` + `window`；位置 `[[2, 6], [26, 39], [84, 91], [98, 109], [164, 170]]`
- **spatial_relation**：`below` + `in` + `along` + `through`；位置 `[[18, 23], [73, 75], [110, 115], [148, 155]]`

保留的 other：`A ` + ` is mounted ` + ` a ` + `, with both objects fully visible ` + ` a quiet ` + `, with ` + ` ` + ` the walls and daylight entering ` + ` a large ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_029

A wall lamp is mounted below a shelf, with both objects fully visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

- **object**：`wall lamp` + `shelf` + `bookshelves` + `window`；位置 `[[2, 11], [31, 36], [95, 106], [161, 167]]`
- **spatial_relation**：`below` + `in` + `through`；位置 `[[23, 28], [70, 72], [145, 152]]`

保留的 other：`A ` + ` is mounted ` + ` a ` + `, with both objects fully visible ` + ` a quiet library, with ` + ` along the walls and daylight entering ` + ` a large ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_030

A wall clock is mounted below a sign, with both objects fully visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

- **object**：`wall clock` + `sign` + `courtyard` + `wall` + `path`；位置 `[[2, 12], [32, 36], [81, 90], [105, 109], [123, 127]]`
- **spatial_relation**：`below` + `in`；位置 `[[24, 29], [70, 72]]`

保留的 other：`A ` + ` is mounted ` + ` a ` + `, with both objects fully visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_031

A mug is in front of a coffee pot, with both objects visible from an oblique viewing angle on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`mug` + `coffee pot` + `cafe table` + `chairs` + `window`；位置 `[[2, 5], [23, 33], [103, 113], [126, 132], [150, 156]]`
- **count**：`both`；位置 `[[40, 44]]`
- **spatial_relation**：`in front of` + `on` + `in the`；位置 `[[9, 20], [91, 93], [165, 171]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with ` + ` objects visible from an oblique viewing angle ` + ` a wooden ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` background.`

跳过：color, shape, texture

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_032

A vase is in front of a bowl, with both objects visible from an oblique viewing angle in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 25, "resolved_index": 26}, {"text": "path", "model_index": 29, "resolved_index": 30}]

- **object**：`vase` + `bowl` + `courtyard` + `wall` + `path`；位置 `[[2, 6], [24, 28], [97, 106], [121, 125], [139, 143]]`
- **spatial_relation**：`in front of` + `in`；位置 `[[10, 21], [86, 88]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects visible from an oblique viewing angle ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_033

A toy car is in front of a wooden box, with both objects visible from an oblique viewing angle on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明： Unique exact-word index repairs: [{"text": "monitor", "model_index": 28, "resolved_index": 29}, {"text": "wall", "model_index": 32, "resolved_index": 33}]

- **object**：`car` + `box` + `desk` + `monitor` + `wall`；位置 `[[6, 9], [34, 37], [108, 112], [135, 142], [155, 159]]`
- **texture**：`plain`；位置 `[[149, 154]]`
- **spatial_relation**：`in front of` + `on` + `in`；位置 `[[13, 24], [95, 97], [168, 170]]`

保留的 other：`A toy ` + ` is ` + ` a wooden ` + `, with both objects visible from an oblique viewing angle ` + ` an office ` + `, with a dark computer ` + ` and a ` + ` ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_034

A notebook is in front of a pencil case, with both objects visible from an oblique viewing angle on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`notebook` + `pencil case` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 10], [28, 39], [103, 114], [128, 144], [157, 161]]`
- **texture**：`plain`；位置 `[[151, 156]]`
- **count**：`both`；位置 `[[46, 50]]`
- **spatial_relation**：`in front of` + `on`；位置 `[[14, 25], [97, 99]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with ` + ` objects visible from an oblique viewing angle ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_035

A hat is in front of a handbag, with both objects visible from an oblique viewing angle on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 25, "resolved_index": 26}]

- **object**：`hat` + `handbag` + `worktable` + `cloth` + `window`；位置 `[[2, 5], [23, 30], [100, 109], [125, 130], [173, 179]]`
- **spatial_relation**：`in front of` + `on` + `through`；位置 `[[9, 20], [88, 90], [163, 170]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects visible from an oblique viewing angle ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_036

A mug is behind a coffee pot, with both objects visible from an oblique viewing angle on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`mug` + `coffee pot` + `cafe table` + `chairs` + `window`；位置 `[[2, 5], [18, 28], [98, 108], [121, 127], [145, 151]]`
- **spatial_relation**：`behind` + `on` + `in`；位置 `[[9, 15], [86, 88], [160, 162]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects visible from an oblique viewing angle ` + ` a wooden ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_037

A vase is behind a bowl, with both objects visible from an oblique viewing angle in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 23, "resolved_index": 24}, {"text": "path", "model_index": 27, "resolved_index": 28}]

- **object**：`vase` + `bowl` + `courtyard` + `wall` + `path`；位置 `[[2, 6], [19, 23], [92, 101], [116, 120], [134, 138]]`
- **spatial_relation**：`behind` + `in`；位置 `[[10, 16], [81, 83]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects visible from an oblique viewing angle ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_038

A toy car is behind a wooden box, with both objects visible from an oblique viewing angle on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`car` + `box` + `desk` + `computer` + `wall`；位置 `[[6, 9], [29, 32], [103, 107], [121, 129], [150, 154]]`
- **texture**：`plain`；位置 `[[144, 149]]`
- **spatial_relation**：`behind` + `on` + `in`；位置 `[[13, 19], [90, 92], [163, 165]]`

保留的 other：`A toy ` + ` is ` + ` a wooden ` + `, with both objects visible from an oblique viewing angle ` + ` an office ` + `, with a dark ` + ` monitor and a ` + ` ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_039

A notebook is behind a pencil case, with both objects visible from an oblique viewing angle on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`notebook` + `pencil case` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 10], [23, 34], [98, 109], [123, 139], [152, 156]]`
- **texture**：`plain`；位置 `[[146, 151]]`
- **count**：`both`；位置 `[[41, 45]]`
- **spatial_relation**：`behind` + `on`；位置 `[[14, 20], [92, 94]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with ` + ` objects visible from an oblique viewing angle ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_040

A hat is behind a handbag, with both objects visible from an oblique viewing angle on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

标注说明： Unique exact-word index repairs: [{"text": "cloth", "model_index": 23, "resolved_index": 24}]

- **object**：`hat` + `handbag` + `worktable` + `cloth` + `window`；位置 `[[2, 5], [18, 25], [95, 104], [120, 125], [168, 174]]`
- **spatial_relation**：`behind` + `on` + `through`；位置 `[[9, 15], [83, 85], [158, 165]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with both objects visible from an oblique viewing angle ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_041

A ball is inside a basket, with the object and container clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`ball` + `basket` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[2, 6], [19, 25], [82, 93], [105, 110], [123, 128], [155, 158]]`
- **spatial_relation**：`inside` + `beside` + `beneath`；位置 `[[10, 16], [73, 79], [129, 136]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with the object and container clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_042

An apple is inside a bowl, with the object and container clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`apple` + `bowl` + `kitchen counter` + `wall` + `cabinet`；位置 `[[3, 8], [21, 25], [78, 93], [114, 118], [132, 139]]`
- **texture**：`plain`；位置 `[[102, 107]]`
- **spatial_relation**：`inside` + `on` + `in`；位置 `[[12, 18], [73, 75], [148, 150]]`

保留的 other：`An ` + ` is ` + ` a ` + `, with the object and container clearly visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_043

A toy car is inside a open box, with the object and container clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明： Unique exact-word index repairs: [{"text": "wall", "model_index": 28, "resolved_index": 29}]

- **object**：`car` + `box` + `office desk` + `computer monitor` + `wall`；位置 `[[6, 9], [27, 30], [84, 95], [109, 125], [138, 142]]`
- **spatial_relation**：`inside` + `on` + `in`；位置 `[[13, 19], [78, 80], [151, 153]]`

保留的 other：`A toy ` + ` is ` + ` a open ` + `, with the object and container clearly visible ` + ` an ` + `, with a dark ` + ` and a plain ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_044

A spoon is inside a mug, with the object and container clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`spoon` + `mug` + `chairs` + `window`；位置 `[[2, 7], [20, 23], [106, 112], [130, 136]]`
- **spatial_relation**：`inside` + `on` + `in`；位置 `[[11, 17], [71, 73], [145, 147]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with the object and container clearly visible ` + ` a wooden cafe table, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_045

A hat is inside a basket, with the object and container clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`hat` + `basket` + `worktable` + `cloth` + `window`；位置 `[[2, 5], [18, 24], [84, 93], [109, 114], [157, 163]]`
- **spatial_relation**：`inside` + `on` + `through`；位置 `[[9, 15], [72, 74], [147, 154]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with the object and container clearly visible ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_046

A ball is outside a basket, with the object and container clearly visible beside a garden path, with tall reeds and distant trees beneath a lightly clouded sky.

- **object**：`ball` + `basket` + `garden path` + `reeds` + `trees` + `sky`；位置 `[[2, 6], [20, 26], [83, 94], [106, 111], [124, 129], [156, 159]]`
- **spatial_relation**：`outside` + `beside` + `beneath`；位置 `[[10, 17], [74, 80], [130, 137]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with the object and container clearly visible ` + ` a ` + `, with tall ` + ` and distant ` + ` ` + ` a lightly clouded ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_047

An apple is outside a bowl, with the object and container clearly visible on a kitchen counter, with a plain tiled wall and a closed cabinet visible in the background.

- **object**：`apple` + `bowl` + `kitchen counter` + `wall` + `cabinet`；位置 `[[3, 8], [22, 26], [79, 94], [115, 119], [133, 140]]`
- **texture**：`plain`；位置 `[[103, 108]]`
- **spatial_relation**：`outside` + `on` + `in`；位置 `[[12, 19], [74, 76], [149, 151]]`

保留的 other：`An ` + ` is ` + ` a ` + `, with the object and container clearly visible ` + ` a ` + `, with a ` + ` tiled ` + ` and a closed ` + ` visible ` + ` the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_048

A toy car is outside a open box, with the object and container clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

- **object**：`toy car` + `box` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 9], [28, 31], [85, 96], [110, 126], [139, 143]]`
- **texture**：`plain`；位置 `[[133, 138]]`
- **spatial_relation**：`outside` + `on`；位置 `[[13, 20], [79, 81]]`

保留的 other：`A ` + ` is ` + ` a open ` + `, with the object and container clearly visible ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_049

A spoon is outside a mug, with the object and container clearly visible on a wooden cafe table, with empty chairs and a softly lit window visible in the background.

- **object**：`spoon` + `mug` + `cafe table` + `chairs` + `window`；位置 `[[2, 7], [21, 24], [84, 94], [107, 113], [131, 137]]`
- **spatial_relation**：`outside` + `on` + `in`；位置 `[[11, 18], [72, 74], [146, 148]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with the object and container clearly visible ` + ` a wooden ` + `, with empty ` + ` and a softly lit ` + ` visible ` + ` the background.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_050

A hat is outside a basket, with the object and container clearly visible on a wooden worktable, with a folded cloth nearby and soft daylight coming through a window.

- **object**：`hat` + `basket` + `worktable` + `cloth` + `window`；位置 `[[2, 5], [19, 25], [85, 94], [110, 115], [158, 164]]`
- **spatial_relation**：`outside` + `on` + `through`；位置 `[[9, 16], [73, 75], [148, 155]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with the object and container clearly visible ` + ` a wooden ` + `, with a folded ` + ` nearby and soft daylight coming ` + ` a ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。
