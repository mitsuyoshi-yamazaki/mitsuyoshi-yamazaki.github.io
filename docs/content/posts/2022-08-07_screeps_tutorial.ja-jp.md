+++
title = "Screepsチュートリアル"
date = 2022-08-07T17:50:58+09:00
draft = true
tags = [
  "screeps",
  "alife",
]
+++

[screeps.com](https://screeps.com)

## Open-Endedなマルチエージェントゲーム世界


## Screeps世界


# memo
- why screeps for ALifers
- what is it
- getting started
- open-endedness
  - how
    - world imports open-endedness from the real world
    - competing battleground
  - how to survive
    - 参考文献
- future
  - これは何？
- references
  - https://note.com/_mitsuyoshi/n/nf2ec6fd8a72f
  - https://note.com/_mitsuyoshi/n/n7201a8478ac1


---

```
チュートリアルで話してからScreepsと人工生命を関連づけて考えてきたけど、決定論的なScreeps世界上で生きるbotがOpen-Endedな点がいちばん面白くて人工生命的なんだな

この系のよくできている点は、十分にプリミティブな世界を設計しているので、現実世界の計算機科学をそのまま適用できるところ

現実世界のOpen-Endednessを輸入しているということ。ずるいけれど簡単で有効。

現実から輸入したOpen-Endednessをもつ世界で、人間のプレイヤー（の実装したbot）同士が戦うので、まあ収束しない

数年前から最強の座を譲らず戦争でほぼ全勝しているbotや、居を構えた土地を要塞化して防衛し続けているbotはいるが、世界の仕組み上絶対に敗れないということはないし、そのような最適解はありそうにない
```

```
Screepsは小さい適当なコードで始められるものの、高度なふるまいを実装しようとすると相応に高度なアーキテクチャが求められるようになる

制御対象と状況の増加で動的なプログラム実行が必要になったときは処理をプロセス単位でまとめてプロセス管理をするOSを書いた

今は人間がバグ取りをするとジリ貧な状況にいるので汎用問題解決器を書いてる

人間が　問題-原因-解決法　のセットを定義すれば機械が勝手に解決するというのが目標

問題の原因を推定して解決法を試すという仕組みは十分単純なものの、動的な環境で動かすのがムズくてすでに何度か失敗してる
```