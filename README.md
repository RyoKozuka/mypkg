# mypkg
![test](https://github.com/RyoKozuka/mypkg/actions/workflows/test.yml/badge.svg)

## 概要
ROS2のテストプログラム.  
パブリッシャを持つノードであるtalker.pyで0.5秒につき１ずつ増加していく,0からの整数を送信する.  
サブスクライバを持つノードであるlistener.pyでそれを受信し,ターミナル上に表示する.  

## 利用方法
1. リポジトリをクローン. 
```
$git clone https://github.com/RyoKozuka/mypkg.git
```

2. ディレクトリ内でtalkerを実行. 
```
$ros2 run mypkg talker
```
* talkerを実行後は何も表示されないのが正常です.    

3. 別ターミナルで使用ディレクトリを開き,listenerを実行し通信内容を確認. 
```
$ros2 run mypkg listener
[INFO] [1703932798.329942192] [listener]: Listen: 96
[INFO] [1703932798.822123681] [listener]: Listen: 97
[INFO] [1703932799.322318519] [listener]: Listen: 98
[INFO] [1703932799.822438724] [listener]: Listen: 99
[INFO] [1703932800.322442596] [listener]: Listen: 100
```

4. プログラムを終了する際は,talker,listener双方でCtrl+cで強制的に終了. 
```
^C
```

## 必要なソフトウェア/テスト環境
* Python 3.10.12
* Ubuntu22.04.2LTS
* ROS2 Humble

また,GitHubActionsでのテスト環境構築に以下のコンテナを使用した.  
https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2

## License
* このソフトウェアパッケージは,三条項BSDLicenseの下,再頒布及び仕様が許可されます.   
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです. 
  - [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
　　
Copyright 2023 Ryo Kozuka
