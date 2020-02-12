from eth_bip44 import EtherCommon
import json


def account_reader():
    with open('accounts.json', 'r') as data:
        json_data = json.loads(data.read())
        return json_data['public_key'], json_data['private_key']


def host_parser():
    """
    从settings文件中解析服务器信息

    :return:
        hosts: 服务器列表
        passwords: 密码列表
    """
    with open('hosts.json', 'r') as data:
        json_data = json.loads(data.read())
        hosts = list(json_data.keys())
        _hosts = [''.join([json_data[host]['user'], '@', host, ':22']) for host in hosts]
        passwords = {''.join([json_data[host]['user'], '@', host, ':22']) : json_data[host]['password'] for host in hosts}
        return _hosts, passwords


def account_generater():
    """
    生成eth帐号
    :return:
    """
    ec_obj = EtherCommon.generate_eth_mnemonic()

    mnemonic_codes = ec_obj.mnemonic_codes
    address = ec_obj.address
    public_key = ec_obj.public_key
    private_key = ec_obj.private_key
    # print(address, '\n', mnemonic_codes, '\n', public_key, '\n', private_key)
    return {
        "mnemonic_codes": mnemonic_codes, "address": address,
        "public_key": public_key, "private_key": private_key
    }