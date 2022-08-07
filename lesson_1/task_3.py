from ipaddress import ip_address
from platform import system
from socket import gethostbyname
from subprocess import Popen, PIPE
from re import match
from tabulate import tabulate


def host_range_ping_tab():

    def host_ping(host):
        args = ['ping', '-n', '2']
        os_name = system().lower()

        if os_name == 'windows':
            pass
        else:
            args.pop(1)
            args.insert(1, '-c')

        try:
            ip_adr = str(ip_address(host))
        except ValueError:
            ip_adr = gethostbyname(host)
        args.append(ip_adr)
        ping_host_proc = Popen(args, stdout=PIPE, shell=False)
        ping_host_proc.wait()
        args.pop()

        if ping_host_proc.returncode == 0:
            result = (host, 'Адрес доступен')
        else:
            result = (host, 'Адрес недоступен')
        return result

    while True:
        begin_ip = input('Введите начальный адрес: ')
        if match(r'\d{0,255}\.\d{0,255}\.\d{0,255}\.\d{0,255}', begin_ip):
            tail = int(begin_ip.split('.')[3])
            break
        else:
            print('Неправильно введены данные, введите в формате '
                  'ХХХ.ХХХ.ХХХ.ХХХ, где ХХХ - от 0 до 255 !\n')

    while True:
        count_ip = input('Введите количество ip для проверки: ')
        if (int(count_ip) + tail) > 256:
            print('Проверка адресов только последнего октета, он не должен '
                  'превышать 255')
        elif not count_ip.isnumeric():
            print(' Введите число!')
        else:
            end_result = [('Host', 'Result'), ]
            count_ip = int(count_ip)
            begin_ip = ip_address(begin_ip)
            end_ip = begin_ip + count_ip
            print('Подождите, выполняется операция...')
            for i in range(0, count_ip):
                end_ip = begin_ip + i
                end_result.append(host_ping(end_ip))
            print('Готово!\n')
            print(tabulate(end_result, headers='firstrow', tablefmt='presto',
                           stralign="center"))
            break


if __name__ == '__main__':
    host_range_ping_tab()
