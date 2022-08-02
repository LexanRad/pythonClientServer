import ipaddress
import os
from pprint import pprint
import subprocess

test_ip = ['77.88.55.55', '13', '64.233.165.104', '0.0.0.0', 'dkjojk', 'yandex.ru', 'google.com']
ip_list = []


def host_ping(str_list):
    for i in str_list:
        try:
            ip = ipaddress.ip_address(i)
            param = '-n' if os.name == 'nt' else '-c'
            response = subprocess.Popen(["ping", param, '1', str(i)], stdout=subprocess.PIPE)
            if response.wait() == 0:
                result = {'доступен': str(ip)}
            else:
                result = {'не доступен': str(ip)}
            ip_list.append(result)
        except Exception as err:
            print(err)
            param = '-n' if os.name == 'nt' else '-c'
            response = subprocess.Popen(["ping", param, '1', str(i)], stdout=subprocess.PIPE)
            if response.wait() == 0:
                result = 'узел доступен'
            else:
                result = 'узел не доступен'
            ip_list.append(f'{str(i)} Не является IP-адресом, {result}')
    return ip_list


if __name__ == '__main__':
    pprint(host_ping(test_ip))
