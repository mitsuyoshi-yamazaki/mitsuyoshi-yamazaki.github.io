+++
title = "JSのガベージコレクションを攻略したい"
date = 2022-09-12T15:33:57+09:00
draft = true
tags = [
  "javascript",
  "programming_language",
  "gabage_collection",
]
+++

## 概要
ScreepsでランダムなタイミングでCPU使用時間のスパイクがあり、Discordで質問してみたところ「JSのガベージコレクションを喰らっているのでは？」という意見をもらいました。

> create less ad-hoc objects i'd say ?
> less objects in less scopes



## 経緯

## 根本対応

## 対処療法
- JSのGCの仕様を調べ、簡単に行える対処法がないか調べる
  - https://developer.mozilla.org/ja/docs/Web/JavaScript/Memory_Management
- とりあえずimportの循環を解消する

### Google Closure Compiler
https://developers.google.com/closure/compiler/docs/gettingstarted_app
コマンドラインから利用するにはjar

[macOSでjavaを使いたい。](https://zenn.dev/satokazur222/articles/66568417b291d8)

https://rollupjs.org/guide/en/#writebundle


```js
    {
      name: "Compile with Google Closure Compiler",
      writeBundle: {
        sequential: true,
        order: null,
        async handler(options, bundle) {
          const filename = options.file;
          const tempFilename = "temp/temp.js";

          // ワーキングディレクトリはルート
          fs.rename(filename, tempFilename, (error) => {
            if (error == null) {
              console.log("file renamed to: " + tempFilename);
              return;
            }
            console.log("file rename error: " + error);
          });

          console.log("compile " + tempFilename);
          const compileCommand = "java -jar compiler.jar --js " + tempFilename + " --js_output_file " + filename;
          exec.exec(compileCommand,
            function (error, stdout, stderr) {
              console.log('stdout: ' + stdout);
              console.log('stderr: ' + stderr);
              if (error != null) {
                console.log('exec error: ' + error);
              }
            });
          console.log("writeBundle finished");
        }
      }
    },
```

```
[!] (plugin Compile with Google Closure Compiler) Error: Error running plugin hook writeBundle for Compile with Google Closure Compiler, expected a function hook.
```

https://github.com/rollup/rollup/issues/703

---

- minifyで改善することがあるか？
  - Discordではないらしいという話題になっていた
- https://yosuke-furukawa.hatenablog.com/entry/2017/12/05/125517#どこの処理に時間がかかっているのかを確認する

### `FinalizationRegistry`
Screepsにはない

`FinalizationRegistry` にオブジェクトを登録しておくと、そのオブジェクトがガベージコレクトされた際に処理が走るようになる
https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry

### Weak Reference
Screepsにはない

https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/WeakRef