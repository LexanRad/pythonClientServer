import os
import socket
import sys
import json
sys.path.insert(0, os.path.join(os.getcwd(), '..'))
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, MESSAGE, MESSAGE_TEXT, PORT, SENDER,  RESPONDEFAULT_IP_ADDRESSSE
from common.utils import get_message, send_message
import errors_user as errors_user
import argparse
import logging
from decos import Log
import select
from collections import deque
import time


LOG_MAIN = logging.getLogger('server')


@Log(LOG_MAIN)
def process_client_msg(client_message, messages_list, client):
    if ACTION in client_message and TIME in client_message and USER in client_message and PORT in client_message:
        if client_message[ACTION] == PRESENCE and client_message[USER][ACCOUNT_NAME] == 'Vadim':
            send_message(client, {RESPONSE: 200})
            return
        if client_message[ACTION] == MESSAGE and MESSAGE_TEXT in client_message:
            messages_list.append((client_message[USER][ACCOUNT_NAME], client_message[MESSAGE_TEXT]))
            return
    send_message(client,
                 {
                     RESPONSE: 400,
                     ERROR: 'Bad Request'
                 })
    return


def server_main():
    print('Запуск сервера ...')
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-p', type=int, default=DEFAULT_PORT)
    arg_parser.add_argument('-a', type=str, default='')

    args = arg_parser.parse_args()
    try:
        listen_port = args.p
        if not (1024 < listen_port < 65535):
            raise errors_user.PortError
    except errors_user.PortError as port_error:
        LOG_MAIN.critical(f'Ошибка порта {args.listen_port}: Порт вне диапазона от 1024 до 65535. Закрытие соединения.')
        sys.exit(1)
    address_listen = args.a
    clients_list = []
    messages_deque = deque()
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((address_listen, listen_port))
    transport.listen(MAX_CONNECTIONS)

    while True:
        try:
            client, client_address = transport.accept()
        except OSError:
            pass
        else:
            LOG_MAIN.info(f'Установлено соединение с {client_address}')
            clients_list.append(client)

        receive_data_list = []
        send_data_list = []
        errors_list = []

        try:
            if clients_list:
                receive_data_list, send_data_list, errors_list = select.select(clients_list, clients_list, [], 0)
        except OSError:
            pass

        for client_with_message in receive_data_list:
            try:
                process_client_msg(get_message(client_with_message), messages_deque, client_with_message)
            except Exception:
                LOG_MAIN.info(f'Клиент {client_with_message.getpeername()} отключился от сервера.')
                clients_list.remove(client_with_message)

        if messages_deque and send_data_list:
            message_data = messages_deque.popleft()
            message = {
                ACTION: MESSAGE,
                SENDER: message_data[0],
                TIME: time.time(),
                MESSAGE_TEXT: message_data[1]
            }

            for waiting_client in send_data_list:
                try:
                    send_message(waiting_client, message)
                except Exception:
                    LOG_MAIN.info(f'Клиент {waiting_client.getpeername()} отключился от сервера.')
                    waiting_client.close()
                    clients_list.remove(waiting_client)


if __name__ == '__main__':
    server_main()
