+++
title = "2023-02-21_alife_workshop06"
date = 2023-02-21T09:06:16+09:00
draft = false
tags = [
    "alife",
    "alife-workshop",
]
+++

[第6回人工生命研究会](https://alife-japan.org/archives/event/workshop006)

# Evolving soft robots in neighboring environments
- "neighbourhood model"
- 共通祖先からさまざまなニッチに適応したフィンチ
- グリッド状に異なる環境を並べて、進化計算をする際に近隣のグリッドのエージェントを一定混ぜて一緒に評価する
  - つまり、ニッチな環境に特化した形質に対して全く異なる環境に適用したエージェントを競争相手に入れる
- エージェントの混合は隣り合ったグリッド間でしか起きないので、ある形質が広がるかどうかにはグリッドの配置が影響する
- このモデルの特色
  - 大きな空間的広がりを使わずに、同等の効果を得られる
  - 進化的アルゴリズムにかける形質は、それ自体が移動できなくても良い

# ピクセル単位で年齢推定するニューラルセルオートマトンの考案
- Neural CAと同じアーキテクチャを使用
- ピクセル単位で推定が行われるため画像の欠けなどに対してロバスト
- 学習させると、与えられた顔画像の各部分（目元、口元など）に対してそれぞれ異なる年齢が推定されて、その後計算を進めるにつれてどれかが優勢になり全体に広がる
- 異なる推定年齢が衝突した際にどちらが優勢になるのか、そのプロセスはまだわかっていない

# EvoJAX Tutorial

> We will also have a hands-on tutorial from Bert Chan, Yujin Tang and Yingtao Tian from Google Brain about EvoJax. EvoJax is a NeuroEvolution ToolKit improved by hardware acceleration technologies, that is also used for evolutionary computation and alife simulations.

- What is EvoJAX
  - can solve problems involving non-differentiable systems
  - with hardware acceleration 
- How can EvoJAX help alife research
- [evojax - GitHub](https://github.com/google/evojax)
- [EvoJAX: Hardware-Accelerated Neuroevolution - arXiv](https://arxiv.org/abs/2202.05008)


---

- Multiagent city expansion incorporating land use and transport
  - Road generation 
    - L-Systemなどのアルゴリズムを使う
  - トップダウン（都市計画）とボトムアップ（自然な発展）の両面を含む都市プラニング
- Integrated indirect reciprocity and the evolution of cooperation
  - 共生、共存、多様性をどのように行うか
  - 利他的行動にもいくつかの種類がある
    - 相互に
    - 受けた分を他者に（upstream reciprocity
    - 与えた後で受ける（downstream reciprocity
  - 数理モデルをつくると裏切りにアトラクタがきやすい
- The effects of inter-player competition on the evolution of Theory of Mind in the cooperative card game Hanabi
  - 協力ゲームHanabiにおける心の理論の進化へのプレイヤー間競合の影響

