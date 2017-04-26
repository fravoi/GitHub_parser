#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

name="fravoi"
requete = requests.get('https://github.com/'+name) #POST pour se logger
texte = requete.text
#print(texte)
infos = BeautifulSoup(requete.text, 'html.parser')
#infos.find(aria-label="Homepage")
#persos = infos.find_all("svg")

#persos=infos.find(itemprop="worksFor")
#fils=persos.findChildren()

#org=fils.find(class="user-mention")

org=infos.find(class_="user-mention").string

print(org)

nom=infos.find(itemprop="name").string
print(nom)

additionalName=infos.find(itemprop="additionalName").string
print(additionalName)

description= infos.find(class_="user-profile-bio").string
print(description)


#Il faut se logger en fait :/
email=infos.find(attrs={"aria-label":"Email"}).findChildren()
#email=infos.find(href="mailto\*")
print(email)
