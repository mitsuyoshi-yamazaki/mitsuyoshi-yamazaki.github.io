---
title: "Hugoチートシート"
date: 2022-07-05T17:41:39+09:00
draft: false
tags:
- programming
- hugo
---

テスト記事兼Hugoチートシート

[Hugoを使用したGitHub Pages用の静的HTML生成 - Zenn](https://zenn.dev/mitsuyoshi/scraps/355eebf05d4f2f)

## サイト内リンク
[サイト内リンクを貼ろう - なかけんのHugoノート](https://hugo.nakaken88.com/use/internal-link/)
生成後のHTMLファイルへのパスではなく、生成前のMarkdownのパスを指定すると生成時に変換してくれるらしい。
便利ですね

## Markdownコンテンツ
### Front Matter(トップのあれ
- フォーマットはyml/toml/json
- https://gohugo.io/content-management/front-matter/

```yml
title: "Hugoチートシート"
date: 2022-07-05T17:41:39+09:00
draft: false
tags:
- programming
- hugo
```