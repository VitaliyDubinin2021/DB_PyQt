from ipaddress import ip_address
from platform import system
from socket import gethostbyname
from subprocess import Popen, PIPE


def host_ping(list_hosts):
    args = ['ping', '-n', '2']
    os_name = system().lower()

    if os_name == 'windows':
        pass
    else:
        args.pop(1)
        args.insert(1, '-c')

    for itm in list_hosts:
        try:
            ip_adr = str(ip_address(itm))
        except ValueError:
            ip_adr = gethostbyname(itm)
        args.append(ip_adr)
        ping_host_proc = Popen(args, stdout=PIPE, shell=False)
        ping_host_proc.wait()
        args.pop()

        if ping_host_proc.returncode == 0:
            print(f'{itm}     Адрес доступен')
        else:
            print(f'{itm}     Адрес не доступен')


if __name__ == '__main__':
    hosts = ['osu.ru', 'youtube.com']
    host_ping(hosts)