#!/usr/bin/python
#coding: utf-8
#

import requests
import json
import sys
import argparse as arg

#Banner
print(F''' 
    ____             __      _       __
   / __ \_________  / /_____| |     / /___ __   _____ 
  / /_/ / ___/ __ \/ __/ __ \ | /| / / __ `/ | / / _ \

 / ____/ /  / /_/ / /_/ /_/ / |/ |/ / /_/ /| |/ /  __/
/_/   /_/   \____/\__/\____/|__/|__/\__,_/ |___/\___/ 
 v1.0

[!] Desenvolvido por ./Cryptonking (B4l0x)
''')

#Menu
parser = arg.ArgumentParser(description="Procure sua falha...")
parser.add_argument("--cms", help="Aqui vai seu cms favorito ou falha por ex: wordpress,joomla,drupal,sqli,rce...", required=True)
x = parser.parse_args()

#Puxa os dados
try:
	site = requests.get('http://www.exploitalert.com/api/search-exploit?name='+str(x.cms)).text
	jsonsite = json.loads(site)

	for x in jsonsite:
		data = x['date']
		nome = x['name']
		mais = x['id']
		print(" [-] Nome: "+nome+"\n [-] Data: "+data+"\n [-] Sobre: http://www.exploitalert.com/view-details.html?id="+mais+"\n")
except:
		print("[!] Se voce esta vendo essa mensagem algo de errado aconteceu!")
