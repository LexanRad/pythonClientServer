import os
import socket
import sys
import json
sys.path.insert(0, os.path.join(os.getcwd(), '..'))
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, RESPONDEFAULT_IP_ADDRESSSE
from common.utils import get_message, send_message
import argparse
import logging

LOG_MAIN = logging.getLogger('server')


def process_client_msg(client_message):
    if ACTION in client_message and client_message[ACTION] == PRESENCE and TIME in client_message \
            and USER in client_message and client_message[USER][ACCOUNT_NAME] == 'Vadim':
        return {RESPONSE: 200}
    return {
        RESPONDEFAULT_IP_ADDRESSSE: 400,
        ERROR: 'Bad Request'
    }


def server_main():
    print('Запуск сервера ...')
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-p', type=int, default=DEFAULT_PORT)
    arg_parser.add_argument('-a', type=str, default='')

    args = arg_parser.parse_args()
    try:
        listen_port = args.p
        if not (1024 < listen_port < 65535):
            raise ValueError
    except ValueError:
        LOG_MAIN.critical(f'Ошибка порта {args.listen_port}: Порт вне диапазона от 1024 до 65535. Закрытие соединения.')
        sys.exit(1)
    address_listen = args.a
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((address_listen, listen_port))
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        LOG_MAIN.info(f'Установлено соединение с {client_address}')
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            LOG_MAIN.debug(f'Получено сообщение {message_from_client} от  {client_address}')
            response = process_client_msg(message_from_client)
            send_message(client, response)
            LOG_MAIN.info(f'Отправлено сообщение {response} клиенту {client_address}')
            client.close()
        except (ValueError, json.JSONDecodeError):
            LOG_MAIN.error(f'Не удалось декодировать сообщение клиента {client_address}.')
            client.close()


if __name__ == '__main__':
    server_main()
