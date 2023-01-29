https://mitsuyoshi-yamazaki.github.io

## Usage
### Scripts
```sh
$ cd docs
$ python ../scripts/create_post.py <post file name>
```

## Hugo
### 全般
https://zenn.dev/mitsuyoshi/scraps/355eebf05d4f2f

Hugoプロジェクトのは `docs/` なので `$ cd docs` で作業する必要がある

```sh
# コンテンツの追加
$ hugo new <CATEGORY>/<FILE>.<FORMAT>

# ビルド
# -D: 下書きを含める
$ hugo 

# ローカル実行
# -D: 下書きを含める
$ hugo server
```

### Documentation
- [config項目一覧](https://gohugo.io/getting-started/configuration/)
- [テンプレート適用順序/Archetypes](https://gohugo.io/content-management/archetypes/)
