import os

import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(os.getcwd())  # /home/lds/Desktop/Programs/leon_cpp/py_evan


if __name__ == '__main__':
    """
        print(Back.LIGHTBLACK_EX, math.floor(3.2))
        print(Fore.LIGHTMAGENTA_EX, 'hi')
        print(Style.RESET_ALL, '...')
    """

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    response = requests.get('https://missav.com', headers=headers)
    print(response.text)
