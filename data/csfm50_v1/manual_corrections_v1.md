# 整类 semantic mask 清单

这是文本标注和 mask 目标的检查结果，不是生成实验或语义评分结果。
`other` 永不 mask；未出现的 semantic 跳过。字符位置采用左闭右开区间。

## object_015

A reading lamp is clearly visible in a quiet library, with bookshelves along the walls and daylight entering through a large window.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`reading lamp` + `library` + `bookshelves` + `walls` + `window`；位置 `[[2, 14], [45, 52], [59, 70], [81, 86], [125, 131]]`
- **spatial_relation**：`in` + `along` + `through`；位置 `[[34, 36], [71, 76], [109, 116]]`

保留的 other：`A ` + ` is clearly visible ` + ` a quiet ` + `, with ` + ` ` + ` the ` + ` and daylight entering ` + ` a large ` + `.`

跳过：color, shape, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_015

A square picture frame is shown with its outer outline clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`picture frame` + `office desk` + `computer monitor` + `wall`；位置 `[[9, 22], [77, 88], [102, 118], [131, 135]]`
- **shape**：`square`；位置 `[[2, 8]]`
- **texture**：`plain`；位置 `[[125, 130]]`
- **spatial_relation**：`on`；位置 `[[71, 73]]`

保留的 other：`A ` + ` ` + ` is shown with its outer outline clearly visible ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_035

An oval picture frame is shown with its outer outline clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`picture frame` + `office desk` + `computer monitor` + `wall`；位置 `[[8, 21], [76, 87], [101, 117], [130, 134]]`
- **shape**：`oval`；位置 `[[3, 7]]`
- **texture**：`plain`；位置 `[[124, 129]]`
- **spatial_relation**：`on`；位置 `[[70, 72]]`

保留的 other：`An ` + ` ` + ` is shown with its outer outline clearly visible ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## shape_039

An oval sign is shown with its outer outline clearly visible in a quiet courtyard, with a stone wall and a narrow path visible in soft daylight.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`sign` + `courtyard` + `wall` + `path`；位置 `[[8, 12], [72, 81], [96, 100], [114, 118]]`
- **shape**：`oval`；位置 `[[3, 7]]`
- **spatial_relation**：`in`；位置 `[[61, 63]]`

保留的 other：`An ` + ` ` + ` is shown with its outer outline clearly visible ` + ` a quiet ` + `, with a stone ` + ` and a narrow ` + ` visible in soft daylight.`

跳过：color, texture, count

Token 映射：待接入实际 backbone tokenizer 后验证。

## count_014

Three hourglasses are arranged separately, with every item fully visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`hourglasses` + `office desk` + `computer monitor` + `wall`；位置 `[[6, 17], [79, 90], [104, 120], [133, 137]]`
- **texture**：`plain`；位置 `[[127, 132]]`
- **count**：`Three`；位置 `[[0, 5]]`
- **spatial_relation**：`on`；位置 `[[73, 75]]`

保留的 other：` ` + ` are arranged separately, with every item fully visible ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_003

A toy car is to the left of a wooden box, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`toy car` + `box` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 9], [37, 40], [103, 114], [128, 144], [157, 161]]`
- **texture**：`plain`；位置 `[[151, 156]]`
- **count**：`both`；位置 `[[47, 51]]`
- **spatial_relation**：`to the left of` + `on`；位置 `[[13, 27], [97, 99]]`

保留的 other：`A ` + ` is ` + ` a wooden ` + `, with ` + ` objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_008

A wooden box is to the left of a toy car, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`box` + `toy car` + `office desk` + `computer monitor` + `wall`；位置 `[[9, 12], [33, 40], [103, 114], [128, 144], [157, 161]]`
- **texture**：`plain`；位置 `[[151, 156]]`
- **count**：`both`；位置 `[[47, 51]]`
- **spatial_relation**：`to the left of` + `on`；位置 `[[16, 30], [97, 99]]`

保留的 other：`A wooden ` + ` is ` + ` a ` + `, with ` + ` objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_009

A pencil case is to the left of a notebook, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`pencil case` + `notebook` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 13], [34, 42], [105, 116], [130, 146], [159, 163]]`
- **texture**：`plain`；位置 `[[153, 158]]`
- **count**：`both`；位置 `[[49, 53]]`
- **spatial_relation**：`to the left of` + `on`；位置 `[[17, 31], [99, 101]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with ` + ` objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_013

A toy car is to the right of a wooden box, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`toy car` + `box` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 9], [38, 41], [104, 115], [129, 145], [158, 162]]`
- **texture**：`plain`；位置 `[[152, 157]]`
- **count**：`both`；位置 `[[48, 52]]`
- **spatial_relation**：`to the right of` + `on`；位置 `[[13, 28], [98, 100]]`

保留的 other：`A ` + ` is ` + ` a wooden ` + `, with ` + ` objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_018

A wooden box is to the right of a toy car, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`box` + `toy car` + `office desk` + `computer monitor` + `wall`；位置 `[[9, 12], [34, 41], [104, 115], [129, 145], [158, 162]]`
- **texture**：`plain`；位置 `[[152, 157]]`
- **count**：`both`；位置 `[[48, 52]]`
- **spatial_relation**：`to the right of` + `on`；位置 `[[16, 31], [98, 100]]`

保留的 other：`A wooden ` + ` is ` + ` a ` + `, with ` + ` objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_019

A pencil case is to the right of a notebook, with both objects separated and visible from the front on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`pencil case` + `notebook` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 13], [35, 43], [106, 117], [131, 147], [160, 164]]`
- **texture**：`plain`；位置 `[[154, 159]]`
- **count**：`both`；位置 `[[50, 54]]`
- **spatial_relation**：`to the right of` + `on`；位置 `[[17, 32], [100, 102]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with ` + ` objects separated and visible from the front ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_034

A notebook is in front of a pencil case, with both objects visible from an oblique viewing angle on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`notebook` + `pencil case` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 10], [28, 39], [103, 114], [128, 144], [157, 161]]`
- **texture**：`plain`；位置 `[[151, 156]]`
- **count**：`both`；位置 `[[46, 50]]`
- **spatial_relation**：`in front of` + `on`；位置 `[[14, 25], [97, 99]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with ` + ` objects visible from an oblique viewing angle ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_039

A notebook is behind a pencil case, with both objects visible from an oblique viewing angle on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`notebook` + `pencil case` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 10], [23, 34], [98, 109], [123, 139], [152, 156]]`
- **texture**：`plain`；位置 `[[146, 151]]`
- **count**：`both`；位置 `[[41, 45]]`
- **spatial_relation**：`behind` + `on`；位置 `[[14, 20], [92, 94]]`

保留的 other：`A ` + ` is ` + ` a ` + `, with ` + ` objects visible from an oblique viewing angle ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape

Token 映射：待接入实际 backbone tokenizer 后验证。

## spatial_relation_048

A toy car is outside a open box, with the object and container clearly visible on an office desk, with a dark computer monitor and a plain wall visible in the background.

标注说明：Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.

- **object**：`toy car` + `box` + `office desk` + `computer monitor` + `wall`；位置 `[[2, 9], [28, 31], [85, 96], [110, 126], [139, 143]]`
- **texture**：`plain`；位置 `[[133, 138]]`
- **spatial_relation**：`outside` + `on`；位置 `[[13, 20], [79, 81]]`

保留的 other：`A ` + ` is ` + ` a open ` + `, with the object and container clearly visible ` + ` an ` + `, with a dark ` + ` and a ` + ` ` + ` visible in the background.`

跳过：color, shape, count

Token 映射：待接入实际 backbone tokenizer 后验证。
