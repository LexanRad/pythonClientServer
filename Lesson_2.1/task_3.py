from tabulate import tabulate
import os
import sys

sys.path.insert(0, os.path.join(os.getcwd(), '..'))
from task_2 import host_range_ping, last_oct


def host_range_ping_tab():

    res_dict = host_range_ping(last_oct)

    print(tabulate(res_dict, headers='keys', tablefmt='grid', stralign='center'))


if __name__ == "__main__":
    host_range_ping_tab()
