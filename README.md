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


goinstall.sh 说明
----
```
golang 安装脚本
bash ./goinstall.sh
just run: lastest stable
version: --version 1.13.X
```