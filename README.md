fabric部署脚本
====
step 1 安装依赖
----
首先确保本地有可使用的python3.7+环境
```
// 安装pip（一个python package controller）
python3 -m pip install --user --upgrade pip
// 安装虚拟环境package
pip3 install virtualenv
// 创建虚拟环境
virtualenv -p python3.7 venv
// 进入虚拟环境
source venv/bin/activate
// 安装依赖
pip3 install -r requirements.txt
```
step 2 填写配置文件
---
运行前请完成如下两个文件的信息填写
```
accounts.json: 出块帐号信息
hosts:json: 节点部署机器，按照示例填写即可
```
step 3 执行脚本
---
#### 部署节点
执行`fab -f main.py build`完成节点部署 <br>
如期间出现`[y/n]`选项只需要输入`y`回车即可

#### 监控节点运行日志
执行`fab -f main.py monitor`获取节点运行日志
##### 譬如
```shell script
[root@121.40.199.174:22] [http_port@8545] INFO [02-10|15:11:42.001] Mined new block                          candidate=fractal.founder number=18 hash=0x61a27fe0af4d1c905cadbc5e7d8e506d0cff9ddaa5ffc2191a25b80d5d6817eb time=1581318702000000000 txs=0 gas=0 diff=6901435 elapsed=832.984µs
[root@121.40.199.174:22] [http_port@8547] INFO [02-10|15:11:45.002] Mined new block                          candidate=fractal.founder number=17 hash=0x8dfd74c492a3cf529b5241cb74c64187a4f47ac23f1a31e6427de9f1b1a80d5f time=1581318705000000000 txs=0 gas=0 diff=6901436 elapsed=1.681ms
[root@121.40.199.174:22] [http_port@8549] INFO [02-10|15:11:51.001] Mined new block                          candidate=fractal.founder number=17 hash=0x1e82d77b708c3d4cc5b5e9db30f5a364bb131a560134342ba3e993a4f8661477 time=1581318711000000000 txs=0 gas=0 diff=6901438 elapsed=649.075µs
[root@121.40.199.174:22] [http_port@8551] INFO [02-10|15:11:57.001] Mined new block                          candidate=fractal.founder number=17 hash=0x8c5bc902334aefd8b85023b4ef0233ad2a2b5c5ee08e987b042f59e4c595a9ac time=1581318717000000000 txs=0 gas=0 diff=6901440 elapsed=699.016µs
```


goinstall.sh 说明
----
```
golang 安装脚本
bash ./goinstall.sh
just run: lastest stable
version: --version 1.13.X
```

节点端口说明
---

| debug_pprof_port | http_port | ws_port | p2p_listenaddr(string) |
| :-----| ----: | :----: |:----: |
| 6060 | 8545 | 8546 | :2018 |
| 6061 | 8547 | 8548 | :2019 |
| 6062 | 8549 | 8550 | :2020 |
| 6063 | 8551 | 8552 | :2021 |