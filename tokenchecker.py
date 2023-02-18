import requests
import random
import json
import threading

req = requests.Session()

def tokenchecker(token):
    headers = {
        "authorization": token
    }
    proxy = open("./data/proxies.txt", "r").read().splitlines()
    proxy = random.choice(proxy)
    proxies = {
        "http://": f"http://{proxy}",
        "https://": f"http://{proxy}"
    }
    check_res = req.get('https://discord.com/api/v9/users/@me/library', headers=headers, proxies=proxies)
    if check_res.json() == []:
        print("Valid token | " + token)
        open('./data/availtokens.txt', 'a').write(token + '\n')
        exit()
    else:
        print("Invalid token | " + token)
        exit()

with open("./data/tokens.txt", "r") as f:
    for line in f:
        token = line.strip("\n")
        x = threading.Thread(target=tokenchecker, args=(token,))
        x.start()