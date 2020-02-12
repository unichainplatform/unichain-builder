from fabric.api import task, env, run, put, settings, cd, hide, execute
import fabric
from tools import host_parser, account_generater, account_reader
from termcolor import colored


hosts, passwords = host_parser()
public_key, private_key = account_reader()

env.hosts.extend(hosts)
env.passwords = passwords


def install_go():
    run('wget https://dl.google.com/go/go1.13.7.linux-amd64.tar.gz')
    with settings(
            hide('warnings', 'running', 'stdout', 'stderr'),
            warn_only=True
    ):
        run("tar -C /usr/local -zxvf  go1.13.7.linux-amd64.tar.gz")
    run("echo 'export GOROOT=/usr/local/go' >> /etc/profile")
    run("echo 'export PATH=$PATH:$GOROOT/bin' >> /etc/profile")
    run("source /etc/profile")
    run("go version")


def initial():
    run('apt update')
    run('apt install git jq moreutils screen')

    with settings(warn_only=True):
        result = run('go version')
    if result.return_code != 0:
        install_go()
    return


def unichain():
    run("git clone https://github.com/unichainplatform/unichain.git ~/uni")
    with cd('~/uni'):
        run("make fmt")
        run("make all")
        run("""jq '.allocAccounts[0].pubKey="{}"' build/genesis.json | sponge build/genesis.json""".format(public_key))
        run(
            """jq '.config.bootnodes=["fnode://a85ccab0374c60ddea0a63b521ae3f8475100ff4e116090d6798a8618ceea193f5b7deffc14627b2f61bc374336983f6a6c6ed979478590d49906e8ce6041a18@127.0.0.1:2018"]' ../genesis.json | sponge ../genesis.json""")
    with cd('~/uni/build/bin'):
        run("touch privateKey.txt")
        run("""echo {} > privateKey.txt""".format(private_key))
        # node 8545
        run("nohup ./uni --genesis=../genesis.json --datadir=./data/node1 --miner_start --contractlog --http_modules=fee,miner,dpos,account,txpool,uni &>node1.log & sleep 5; exit 0", warn_only=True)
        run("nohup ./uni --genesis=../genesis.json --datadir=./data/node2 --p2p_listenaddr :2019  --http_host 0.0.0.0 --http_port 8080 --ws_port 8081 --contractlog --http_modules=fee,miner,dpos,account,txpool,uni &> node2.log & sleep 5; exit 0", warn_only=True)
        run("nohup ./uni --genesis=../genesis.json --datadir=./data/node3 --p2p_listenaddr :2020  --http_host 0.0.0.0 --http_port 8090 --ws_port 8091 --contractlog --http_modules=fee,miner,dpos,account,txpool,uni &> node3.log & sleep 5; exit 0", warn_only=True)
        run('./uni miner -i ./data/node1/uni.ipc setcoinbase "unichain.founder" privateKey.txt')
        run('rm privateKey.txt')


@task
def build():
    initial()
    unichain()