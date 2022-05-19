import chardet
import subprocess
import platform


def site_ping(site):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '2', site]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in process.stdout:
        result = chardet.detect(line)
        print('result = ', result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


site_1 = 'yandex.ru'
site_ping(site_1)
site_2 = 'youtube.com'
site_ping(site_2)
