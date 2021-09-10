import requests
import json
from pathlib import Path


with open(Path('verification/key.txt'), 'r') as file:
    key = file.read()

def getcataLevel(ign):
    catalvls = [0,50,125,235,395,625,955,1425,2095,3045,4385,6275,8940,12700,17960,25340,35640,50040,70040,97640,135640,188140,259640,356640,488640,668640,911640,1239640,1684640,2284640,3084640,4149640,5559640,7459640,9959640,13259640,17559640,23159640,30359640,39559640,51559640,66559640,85559640,109559640,139559640,177559640,225559640,285559640,360559640,453559640,569809640]
    try:
        uuid = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()['id']
    except:
        return None
    profiles = requests.get(f'https://api.hypixel.net/skyblock/profiles?key={key}&uuid={uuid}').json()['profiles']
    catalvl = 0
    cataxp = 0


    for profile in profiles:
        try:
            cata = profile['members'][uuid]['dungeons']['dungeon_types']['catacombs']['experience']
                
            if cata > cataxp:
                cataxp = cata

        except KeyError:
            continue


    for lvl in catalvls:

        if catalvls.index(lvl) == 50:
            catalvl = 50
            return catalvl
        if lvl < cataxp:
            continue
        else:
            catalvl = catalvls.index(lvl)-1
            if(catalvl == float('nan') or catalvl == None or catalvl < 0):
                catalvl = 0
            return catalvl

def disc(ign):
    try:
        uuid = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()['id']
        discord = requests.get(f'https://api.hypixel.net/player?key={key}&uuid={uuid}').json()['player']['socialMedia']['links']['DISCORD']
        return discord
    except:
        return None
