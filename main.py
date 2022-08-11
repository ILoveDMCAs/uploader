import sys
import time
import random
from requests import post, get
import requests
from os import name as os_name, system
import codecs
import json
import secrets
import os
import random
from colorama import Fore, Back, Style
from xml.dom import minidom
from xml.etree import ElementTree as etree
"""
Requirements for the uploader to function are above (libraries)

"""

def main(cookie):

    token = post("https://auth.roblox.com/v2/logout", #logout, this way we generate a free ROBLOSECURITY token specifically for viewing IDs
                 cookies={
                     ".ROBLOSECURITY": cookie
                 }).headers['X-CSRF-TOKEN']
    userId = requests.get("https://users.roblox.com/v1/users/authenticated", # Authentication
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox/WinINet',
                                "Connection": "keep-alive"
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["id"]
    print(f" [DATA] {userId}- UserID")
    gameId = requests.get("https://inventory.roblox.com/v2/users/" + # In order to find our game ID, we need to go through our inventory.
                          str(userId) + "/inventory/9?limit=10&sortOrder=Asc", # Specifically the "Places" section of the inventory
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox/WinINet'
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["data"][0]["assetId"] # Now we have the game ID!
    print(f" [DATA] {gameId} - GameID") # Print the game ID for easy access
    myfiles = open("latest.rbxl", "rb").read() # Read the file that's going to be uploaded
    unvid = get(
        "https://api.roblox.com/universes/get-universe-containing-place?placeid="
        + str(gameId)).json()["UniverseId"] # Universe ID, contains our *game*, not *place* configuration. It's weird complex shit, fuck you roblox.
    print(f" [DATA] {unvid} - UniverseID") # Print universe ID
    url = f"https://data.roblox.com/Data/Upload.ashx?assetid={str(gameId)}"

    url2 = f"https://develop.roblox.com/v2/universes/{str(unvid)}/configuration" # This is so that we're able to configure data like game name, description, private servers, etc.

    avatartype = "MorphToR15" # Do we want R6 or R15?
    allowprivateservers = False # Do we want to allow Private Servers to be made? If Yes, set to "True". If not, set to "False". (Capitilization of the first letter is REQUIRED!)
# LG (Life's Good) Hub!

    gamedata = {
        "name": "Brilliant, the learning platform. ", # Game Name Ruggable Rugs
        "description": "Visit to get started learning STEM for free, and the first 200 people will get 20 percent off their annual premium subscription. Please enter .gg/lostgames for early access to the Air Force Base!", # Game description Ruggable is an Amazon based brand  easy-to-use eletronics, such as a Type-C to -C connection. Speaking of which, I  bought one! LOL! LG made this! Please enter .gg/lostgames for early access to the Air  Base! Tags: LTT, Technology, Linus Tech Tips, Framework
        "universeAvatarType": avatartype, # Our avatar type, R15 or R6, refrenced in L55 (above)
        "universeAnimationType": "Standard", # Animations count as "Clothes" for some reason, basically it's saying "We don't use custom clothing"
        "maxPlayerCount": 1, # The maximum amount of players that can join 1 server, max is 100.
        "allowPrivateServers": allowprivateservers, # L56
        "privateServerPrice": 0, # If we set allowprivateservers to True, what price to we want it to be set at? (max = 1000, lowest = 0 [free] )
        "permissions": {
            "IsThirdPartyPurchaseAllowed": True # Are we allowed to buy gamepasses/assets from this game that are from different games? Usually, this should be set to True. However, setting it to False won't affect anything.
        }
    }
    # _|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_364675868C576ED352DD8F76B1257ACD6EAAFA4558BD29A3C4461CD4BEEBD3D35DE8E86B2297062AD8EA4C7C187756AE7A630BCE6FA1E6BC25383C1FC6C0156B7158D0A2686BFE0E3A032F016A9DA7C06BD3EB45283187D20C8237E41DD1A85FE9F30EC8CAEEF748DABA9E2B182A5C88FA7F96A834CCC1DC399BD892225F0537991147F9AB3AADEA29771CA31AB9851387834A4E12F8F1024BA52901D410B4FC861413FEE2CAE17290722CBCA333D1F9FC8827197FE4D188A0D9FE5B9FFDDE11BAAE72463671D69F62F1FACF4ED61597C8A0B5139C93467A0B6B5372E0E705506CDE343877FAF2684AA907C41B8ABE383E9F1F22AF39D95A25A9B8F68E35604A8EDF66392AD9A8794192A09A318D14F294A886B2CA39CED51DE24CB50F35FA90B6668FFCDFEA49E0A4891653620DC22F7E8BE2C7BBBC8A9067019436D2AADB3942CFE9A4DC85E78AF654A9DC0920459E8D71944F88E3F441B9FD93B244A298433262068E483C0DA834FE020922758596BBE93DB9EB9CAF4AD7261F358517E1867359E91C3EDC773AB14648B36A2BF082BC57F66F
    gamedata = json.dumps(gamedata)
    gameData = requests.patch(
        url2,
        headers={
            'Content-Type': 'application/json',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36', # The headers we want to use for logging in 
            'x-csrf-token': token
        },
        cookies={'.ROBLOSECURITY': cookie},
        data=gamedata)
    gameData2 = {
        "maxPlayerCount": 2,
    }
    gameData = requests.patch(
        url2,
        headers={
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'x-csrf-token': token
        },
        cookies={'.ROBLOSECURITY': cookie},
        data=gameData2)

    print(f" [DATA] {gameData.status_code} - Successful upload") # I like to print this BEFORE uploading, just because.
    upload = post(url,
                  headers={
                      'Content-Type': 'application/xml',
                      'User-Agent': 'Roblox/WinINet', # Headers to upload the game, impersonates official ROBLOX headers
                      'x-csrf-token': token
                  },
                  cookies={'.ROBLOSECURITY': cookie},
                  data=myfiles)
    if upload.status_code == 200: # If the upload is a sucess (code 200), then 
     print(f" [DATA] https://roblox.com/games/{gameId}/zelenskyy-will-win - Game Link") # We'll print the link.
    while True:
        time.sleep(60)
        cookie2 = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_A8D5F916CE211AF798092DCFF5D2BB971B93F35FB1C162441BE8755443CA395A12E5D643C5CA6CD809542E97453C6274A0A3E6F28E69DDD375BD5FF739681C9B89AD4D301177870F45545377163FCFF9CA42473A2EC79DF4559F08BB7B5162807527222E548646E252CC82ED889487CFBEFB906D5CF2596100D21339BB6B9DCAF40CEDC25D37217A04C8A6C4FB9069825D92A059BC06A6351A64C2295ABD1F5E4A396F64F3FD821404E19FBEBF3860B4C30CCB09C1480B7EF17F667C42486A841831D4EDA9E63CCD0F736D8BFA3DABBA0761ED5EC92A69B8CD666ADE202A6A1E213744C29167E59847C7D04CC8BD861CC27BA9967B6E471C968962AED9F1ED29E0E49AB1BA8A44BDEA8B3893B8A9D9BFF01B27B448688C71B101773740C1C749CB0D5C21AD862190CAF179528F31A463F25D488000A459B7F0AD903C97F0039B57800FA7C93A0F13C8948A4BCAB37F377B7D7239"
        sheesh = get(f"https://games.roblox.com/v1/games/multiget-playability-status?universeIds={unvid}",headers={'x-csrf-token': token,'User-Agent': 'Roblox/WinINet'},cookies={'.ROBLOSECURITY': cookie2 }).json()
        sheesh = sheesh[0]['playabilityStatus']
        if sheesh == 'UnderReview':
            def start():
                k = 1
                filename = 'cookies.txt'
                with open(filename) as file:
                    lines = file.read().splitlines()

                if len(lines) > k:
                    random_lines = random.sample(lines, k)
                    with open(filename, 'w') as output_file:
                        output_file.writelines(line + "\n"
                        for line in lines if line not in random_lines)
                    main("\n".join(random_lines))
                elif lines: # file is too small
                    print("\n".join(lines)) # print all lines
                    with open(filename, 'wb', 0): # empty the file
                                pass 
                """
                All the stuff above does is check to make sure your cookies are valid.
                """

            start()

if __name__ == "__main__":
    clear = lambda: system('cls')
    def sendmsg():
        clear()
        print(Fore.RED + '''                                                                     
            ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗
            
                                                 Aimee's...
                                  ▒█░▒█ ▒█▀▀█ ▒█░░░ ▒█▀▀▀█ ░█▀▀█ ▒█▀▀▄ ▒█▀▀▀ ▒█▀▀█ 
                                  ▒█░▒█ ▒█▄▄█ ▒█░░░ ▒█░░▒█ ▒█▄▄█ ▒█░▒█ ▒█▀▀▀ ▒█▄▄▀ 
                    　            ░▀▄▄▀ ▒█░░░ ▒█▄▄█ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▀ ▒█▄▄▄ ▒█░▒█
                                        Making copyright abuse easier for everyone ;)
                             
                                         [1] Unblacklist/Unpatch         [2] Upload Game 
               v7.2.4                                                                           Remake by Aimee
            ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════╝

        ''')
        input22 = input(" \n    Enter Task (1 or 2):  ")
        if input22 == "2":
           stuff = input("Please Insert Account Cookie: ")
           main(stuff) # Start the uploading process using the supplied ROBLOSECURITY cookie.
           time.sleep(1) # Wait for a second
           sendmsg() # Then send the message to console
        elif input22 == "1":
            print("This doesn't work") # This hasn't been implemented because I haven't found any good methods. If there are any new methods, feel free to include them here.
            time.sleep(2)
            print("\n Error")
            time.sleep(1)
            sendmsg()
        elif input22 == "3":
            req = requests.Session()
            cookiefilefolder = os.path.dirname(__file__)
            cookiefile = (cookiefilefolder + "\cookies.txt")
            cookie = open(cookiefile).read().splitlines()
            validcount = 0
            invalidcount = 0
               # Cookie stuff
            if len(cookie) > 0:
                print(str(len(cookie)) + " Cookie(s) Found")
                print(" ")
       
                for line in cookie:
                    check = req.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(line)})
                    if check.status_code == 200:
                        validcount += 1
                    else:
                        invalidcount += 1
                print(" Valid Cookie(s): " + str(validcount) + "\n Invalid Cookie(s):" + str(invalidcount))
                time.sleep(5)
                sendmsg()

            else:
                print(" No cookies found.")

    sendmsg()
