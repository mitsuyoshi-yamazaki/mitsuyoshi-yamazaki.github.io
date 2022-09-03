+++
title = "Screepsドキュメンテーション超訳"
date = 2022-09-03T15:32:31+09:00
draft = true
tags = [
  "screeps",
]
+++

*※ この記事で単にScreepsと記載しているゲームはScreeps: Worldのことです*
*※※ この記事が参照している情報は2022年8月時点のものです*

Screepsのチュートリアルを終えるといよいよゲーム世界にデプロイできるようになりますが、実サーバーでうごくbotを実装するためにはゲーム世界の非機能要件を知っている必要があります。
これはScreepsのドキュメンテーションに記載されているのですが、それを読めというヒントはどこにも出てこないうえに英語で記載されているので、初心者に必要な部分を抜粋して日本語でまとめておきます。
[Docs - Screeps](https://docs.screeps.com)

---
## [Overview](https://docs.screeps.com/index.html)
botを実装するにあたって参考になるリンク集が載っています。

### 実装を安全に試したいプレイヤー向けのサンドボックス環境：Tutorial, Training, Custom
- [Tutorial](https://screeps.com/a/#!/sim/tutorial)
  - ステップバイステップでCreep, Spawn, Towerの使用方法とゲーム内エディタの使い方を学びます
- [Training](https://screeps.com/a/#!/sim/survival)
  - あらかじめ決められた地形で、実装したbotを検証するための環境です
- [Custom](https://screeps.com/a/#!/sim/custom)
  - 地形、RCL、Structureの数など、ほとんど全ての環境要因を自由にカスタムできる環境でbotの動作検証を行えます

### ドキュメンテーション
- https://docs.screeps.com
  - ここでまとめているドキュメンテーション本体
- https://docs.screeps.com/api/
  - ゲームが提供するAPIの仕様書

### コミュニティチャット
運営がDiscordサーバーを提供しており、ゲームと実装に関する話題/質問についてチャットできます
招待リンク：https://discord.com/invite/RjSS5fQuFx

主なDiscordチャンネル
- rules
  - Discordの使用ルールです。要するに大人としてふるまってくださいねということです。読んでください
- useful-links
  - お役立ちリンク集です
- world-help
  - 全般的な質問をする場所
- cpu-clinic
  - CPU使用時間に関する質問をする場所
- languages and technologiesのチャンネル群
  - 各プログラミング言語に関する話題を話す場所
- japanese-日本語
  - 日本語で質問ができる場所

---
## [Introduction](https://docs.screeps.com/introduction.html)
Roomの外に広がるゲーム世界の説明です。
ゲーム世界は50 x 50セルで構成されるRoom, 9 x 9Roomで構成されるSector, Sectorの集合であるShardという単位で構成されています。

### Room
- 50 x 50セルで構成される
- セルはそれぞれplain, swamp, wallのいづれかの状態をとり、これがRoomごと固有の地形をつくる
- Controllerをclaimすることで自分の支配下に置くことができ、Structureを設置できるようになる
- Roomは隣接するRoomと接続しており、Creepはその間を自由に移動できる

### Sector
- 9 x 9Roomで構成される
- Sectorの構造：
  - 中心の3x3RoomはControllerをもたずclaim不可だが、資源の豊富なSource Keeper's Room
  - Source Keeper's Room以外は通常のclaim可能なRoom
  - Sectorの間はこれもControllerをもたないHighway Roomが区切っており、claimされず妨害が少ないのでCreepの長距離移動に用いられる

![](/images/screeps_documentation_001.png)

### Shard
- 10 x 10程度のSectorで構成される
- shard0, shard1, shard2, shard3の4つのshardがあり、それぞれ独立して実行されるためtick速度が異なる
- shard3のみCPUに上限がかかっているため、CPU unlockの課金の有無に関わらず、全員平等なCPU量でプレイができる

初心者プレイヤーはshard3にデプロイするのが良いでしょう。
shard0,1,2は巨大な領土を擁する強プレイヤーが徘徊している魔境なのに対して、shard3は平等にCPU上限がかかっているため低レベル帯のプレイヤーが多く活発なshardとなっています。

---
## [Creeps](https://docs.screeps.com/creeps.html)
### Body parts
Creepは以下の7種類のbody partsの組み合わせでその能力が決まります。

- `WORK`: Energyの`harvest`, Structureの`build`と`repair`, `upgradeController`などを行う
- `MOVE`: Creepの移動
- `CARRY`: Energyやその他の資源の格納
- `ATTACK`: 近接攻撃
- `RANGED_ATTACK`: 遠隔攻撃
- `HEAL`: 回復
- `CLAIM`: Roomの確保（`claim`）
- `TOUGH`: CreepのHP増加

Body partsの種類ごとに、Creepをspawnする際の消費Energyと、能力値の増加分が異なります。それらの仕様はAPI仕様書に記載があります。
1Creepに積めるbody partsは最大50個までです。
https://docs.screeps.com/api/#Creep

### Creepの移動速度の仕組み
`MOVE`以外のbody partsは、Creepが隣のセルに移動したタイミングでCreepの疲労値（`Creep.fatigure`）を増加させます。
疲労値が1以上の場合、Creepはそのtickは動けません。
`MOVE`パーツひとつあたり、1tickで疲労値を2減少させます。
移動の最大速度は1セル/tickであり、これを超えることはありません。

疲労値の増加量は地面の状態により決まり、`MOVE`以外のbody partsひとつ当たり以下の量増加します。
- 地面がplain：2fatigure/tick
- 地面がswamp：10fatigure/tick
- 地面にRoadが敷いてある：1fatigure/tick

### Creepがダメージを受けた場合
CreepのHP総量はもっているbody partsの量で決まり、body parts数 x 100です。
Creepがダメージを受けると先頭のbody partsからHPがなくなっていき、HPが0になったbody partsはその能力を失います。

`MOVE,WORK,CARRY` Creepが150ダメージを負った場合は移動できなくなるものの`WORK`と`CARRY`に由来する能力は十全に利用できます。
それに対し、同じ構成のCreepでも `CARRY,WORK,MOVE` Creepが150ダメージを負った場合は移動と`WORK`系能力は使えるものの資源の格納ができなくなります。

### Body partsの組み合わせによるCreep能力値の例
```
[汎用] WORK,CARRY,MOVE
- HP: 300
- harvest: 2 Energy/tick
- carry capacity: 50
- move: CARRYパーツに資源を格納している場合は 1セル/2tick, CARRYパーツが空の場合は 1セル/tick

[エネルギー輸送] 4 x CARRY, 2 x MOVE
- HP: 600
- carry capacity: 200
- move: Road上で常に1セル/tick

[Creep迎撃用] 15 x RANGED_ATTACK, 10 x HEAL, 25 x MOVE
- HP: 5000
- heal: 120HP/tick
- ranged attack: 150HP/tick
- move: 1セル/tick
```

---
## [Control](https://docs.screeps.com/control.html)
ScreepsにはGCL（Global Cotrol Level）とRCL（Room Control Level）というふたつの指標があります。

### Room Control Level
確保しているRoomのControllerに、`Creep.upgradeController`APIを使ってエネルギーを注入することでレベルが上がります。
レベルが上がるごとに建てられるStructureの種類と数が増え（※ [原文](https://docs.screeps.com/control.html#Available-structures-per-RCL)を参照のこと）、それによりRoomで行える行動が増えます。

序盤の優先順位としては、RCLが上がったら新たにアンロックされたStructureを一通り建て、それが終わったらまたRCLが上がるまで`upgradeController`にエネルギーを費やすというものになります。

RCLは一定期間`upgradeController`が行われない、もしくは他プレイヤーから`attackController`を受けることで下がってしまい、アンロックされていた機能が使えなくなってしまうため注意が必要です。

### Global Control Level
プレイを開始してから`upgradeController`で費やしたEnergyの累積でGCLが上がります。
GCLはリセットされないため、全滅してリスポーンしても持ち越されます。
GCLは確保できるRoomの数とCPU上限に影響します。

各プレイヤーはGCLの分だけRoomを確保（`claim`）できます。
多くのRoomがあればGCLの増加率が増え、また全滅しにくくなるためGCLが上がったら新たな部屋の確保に動きましょう。
GCLが最初に上がるのは、最初の部屋がおおよそRCL6に上がる前後のタイミングです。

GCLの上昇によりCPU上限が10ずつ増えます。
CPU上限の詳細は後述

---
## [Defense](https://docs.screeps.com/defense.html)
疲れたので今日はここまでにします

## その他ドキュメントに記載されていない内容
### 課金
Screepsではゲームの購入時と、ゲーム購入者向けのCPUアンロックで課金が発生します。

それぞれ行える内容：
- 無課金
  - チュートリアル
- ゲーム購入
  - ゲーム世界へのデプロイ
  - 使用可能なCPU上限は20に制限
- CPUアンロック
  - 消費型の一時的にCPU上限を増やすアイテム、一定期間CPU上限が撤廃されるサブスクリプション、一度の購入で無期限にCPU上限が撤廃されるライフタイムサブスクリプションなどがある

