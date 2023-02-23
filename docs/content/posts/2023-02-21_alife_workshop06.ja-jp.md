+++
title = "第6回人工生命研究会"
date = 2023-02-21T09:06:16+09:00
draft = false
tags = [
    "alife",
    "alife-workshop",
    "neighbourhood-model",
    "evojax",
]
+++

[第6回人工生命研究会](https://alife-japan.org/archives/event/workshop006)

人工生命研究会の6回目はリアルとオンラインのハイブリッドで、リアル会場はつくば駅前のco-enスペースで行われました。

# Evolving soft robots in neighboring environments
提案するNeighbourhood Modelという手法が面白かったです。
これは共通祖先からさまざまな環境ニッチに適応したフィンチのように、人工生命のエージェントがどのように環境に適応するか・適応した形態がどのように近隣の環境に進出するかを観察できるモデルです。

![](/images/alifeworkshop6_001.png)

このモデルの骨子は通常の遺伝的アルゴリズムです。
一般的な遺伝的アルゴリズムと異なるのは、異なる環境をグリッド状に並べて、遺伝的アルゴリズムによる個体評価をする際に、近隣のグリッドのエージェントを一定数混ぜて一緒に評価するという部分です。
それにより、近隣に異なる環境がある場合はひとつの形態の独占状態が生まれにくく、逆に近隣に同質の環境が多い場合はひとつの形態が多くのグリッドを寡占するという状態が生まれます。

面白いのは、エージェントの混合は隣り合ったグリッド間でしか起きないので、ある形質が広がるかどうかにはグリッドの配置が影響するという点です。
発表では適応困難な環境をロの字型に配置することにより、外側の環境に対して適応して複数のグリッドに広がった形質が、ブロックしているロの字部分を越えられずに中央グリッドに進出できない様子がありました（↓ 赤枠部分が同種の支配種）

![](/images/alifeworkshop6_002.png)

このモデルの特色としては、
- 大きな空間的広がりを使わずに、同等の効果を得られる
- 遺伝的アルゴリズムにかける内容は、それ自体が移動できなくても良い

という部分になると思います。
特にエージェントそれ自体に移動能力がなくとも"移動"による影響を導入できるのは応用範囲を広くしてとても面白いですね。

# ピクセル単位で年齢推定するニューラルセルオートマトンの考案
- Neural CAと同じアーキテクチャを使用
- ピクセル単位で推定が行われるため画像の欠けなどに対してロバスト
- 学習させると、与えられた顔画像の各部分（目元、口元など）に対してそれぞれ異なる年齢が推定されて、その後計算を進めるにつれてどれかが優勢になり全体に広がる
- 異なる推定年齢が衝突した際にどちらが優勢になるのか、そのプロセスはまだわかっていない

# EvoJAX Tutorial

![](/images/alifeworkshop6_003.png)

EvoJAXはPythonで書いた計算をJust In Time CompilerでCUDA実行形式に自動で直し、CPU/GPU/TPUで計算してくれるフレームワークです。
コードを適合させるための制約は副作用のない純粋関数にすることだけで、GPU利用の計算をとても簡単に書けるらしい。

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

