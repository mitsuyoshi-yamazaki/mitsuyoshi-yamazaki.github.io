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

## 記事生成
### テンプレート
`Archetypes` と呼ばれる
記事生成時に対応するArchetypeが探索され、マッチしたものが適用される
https://gohugo.io/content-management/archetypes/

### Archetypes
Archethypeの動的値の設定はfunctionsという機能が司っている
https://gohugo.io/functions/

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