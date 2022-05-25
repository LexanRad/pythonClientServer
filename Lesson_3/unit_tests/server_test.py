import os
import sys
import unittest
sys.path.insert(0, os.path.join(os.getcwd(), '..'))
import common.variables as variables
from server_side import process_client_msg

ACTION_GOOD = variables.PRESENCE
USER_GOOD = 'Lexan'
PORT = variables.DEFAULT_PORT
TIME = 1.1
RESPONSE_GOOD = {variables.RESPONSE: 200}

USER_BAD = 'Andrey'
RESPONSE_BAD = {
    variables.RESPONSE: 400,
    variables.ERROR: 'УПС, ошибочка...'
}


class TestServer(unittest.TestCase):

    def test_process_client_msg_correct(self):
        client_message = {
            variables.ACTION: ACTION_GOOD,
            variables.TIME: TIME,
            variables.PORT: PORT,
            variables.USER: {
                variables.ACCOUNT_NAME: USER_GOOD
            }
        }
        self.assertEqual(process_client_msg(client_message), RESPONSE_GOOD)

    def test_process_client_msg_not_user(self):
        client_message = {
            variables.ACTION: ACTION_GOOD,
            variables.TIME: TIME,
            variables.PORT: PORT,
            variables.USER: {
                variables.ACCOUNT_NAME: USER_BAD
            }
        }
        self.assertEqual(process_client_msg(client_message), RESPONSE_BAD)

    def test_process_client_msg_not_port(self):
        client_message = {
            variables.ACTION: ACTION_GOOD,
            variables.TIME: TIME,
            variables.USER: {
                variables.ACCOUNT_NAME: USER_BAD
            }
        }
        self.assertEqual(process_client_msg(client_message), RESPONSE_BAD)

    def test_process_client_msg_port(self):
        client_message = {
            variables.ACTION: ACTION_GOOD,
            variables.TIME: TIME,
            variables.PORT: 8080,
            variables.USER: {
                variables.ACCOUNT_NAME: USER_BAD
            }
        }
        self.assertEqual(process_client_msg(client_message), RESPONSE_BAD)


if __name__ == '__main__':
    unittest.main()
