# mypkg

## ROS2
![test](https://github.com/RyoKozuka/mypkg/actions/workflows/test.yml/badge.svg)

ROS2のtalker,listenerの機能を用いたプログラム.
talker側で0.5秒につき１ずつ増加していく,0からの整数を送信する.
listener側でそれを受信し,ターミナル上に表示する.


## 必要なソフトウェア
* Python
テスト済み:22.04

### 利用コンテナ
Ubuntu22.04LTSにROS2があらかじめセットアップされている以下のコンテナを使用している.
https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2

## テスト環境
* Ubuntu22.04.2LTS

### 利用方法
#### 1.本リポジトリを使用ディレクトリにクローン.
```
git clone git@github.com:RyoKozuka/mypkg.git
```

#### 2.使用ディレクトリ内でtalkerを実行.
```
ros2 run mypkg talker
```
* talkerを実行後は何も表示されないのが正常です.  

#### 3.別ターミナルで使用ディレクトリを開き,listenerを実行し通信内容を確認.
```
ros2 run mypkg listener
```

#### 4.プログラムを終了する際は,talker,listener双方でCtrl+cで強制的に終了.
```
^C
```

## License
このソフトウェアパッケージは,三条項BSDLicenseの下,再頒布及び仕様が許可されます.  
このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．  
[ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

Copyright 2023 Ryo Kozuka
