import requests
import os
from colorama import Fore , init

init()

red = Fore.LIGHTRED_EX; yellow = Fore.LIGHTYELLOW_EX; green = Fore.LIGHTGREEN_EX; magenta = Fore.LIGHTMAGENTA_EX;

os.system('cls || clear')

bann = f'''{magenta}
▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄     ▄▄▄▄    ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌   ▓█████▄ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▒██▒ ▄██▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ▒██░█▀  ▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓    ░▓█  ▀█▓░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
 ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒    ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒    ▒░▒   ░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
 ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░     ░    ░ ░ ░ ░ ▒  ░      ░    ░    ░    ░     ░░   ░ 
   ░     ░        ░  ░ ░          ░ ░     ░        ░        ░          ░ ░         ░    ░         ░  ░   ░     
 ░                   ░                           ░               ░                           ░                 

                                    {red} Created By Yasin BM
'''

print(bann)

token = input(f'{red}[{yellow}+{red}] {green}PLS ENTER YOUR TOKEN {red}={yellow}>{green} ')
message = input(f'{red}[{yellow}+{red}] {green}PLS ENTER YOUR MESSAGE TO NEXT STEP {red}={yellow}>{green} ')
id_m = input(f'{red}[{yellow}+{red}] {green}PLS ENTER YOUR TARGET CHANNEL ID {red}={yellow}>{green} ')

payload = {
    'content' : message
}

header = {
    'authorization' : token
}

while True:
    req = requests.post(f'https://discord.com/api/v9/channels/{id_m}/messages', data=payload, headers=header)
    print(f'{red}[{yellow}+{red}] {green} MESSAGE SENT ==> {red}| {green}Response {yellow}: {magenta}{req}')