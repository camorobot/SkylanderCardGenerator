import json
import re
import urllib.request
import logging

skylanderNameList = []
skylanderImgList = []

def skylanderSetPage():
    """
    It downloads the html files of the skylanders series from the website outcyders.net
    """
    currentSkylandersSerie = 0
    skylanderSet = ["spyrosadventure", "giants", "swapforce", "trapteam", "superchargers", "imaginators"]

    for i in range(len(skylanderSet)):
        skylanderSetLink = f"https://www.outcyders.net/skylanders/game-{skylanderSet[i]}-full-character-list"
        urllib.request.urlretrieve(skylanderSetLink, 'skylanderSerie/html/serie'+str(currentSkylandersSerie)+'.html')
        logging.debug(f"Downloading current skylander set: {skylanderSet[i]}")
        getSkylanderinfo("name",currentSkylandersSerie)
        getSkylanderinfo("img",currentSkylandersSerie)
        currentSkylandersSerie = currentSkylandersSerie+1
        createJson(currentSkylandersSerie)


# Get skylander name and image
def getSkylanderinfo(kind, currentSkylandersSerie):
    if kind == 'name':
        logging.debug(f"Setting vars for name info.")
        text ='"'
        number = 0
        skylanderList = skylanderNameList
    elif kind == 'img':
        logging.debug(f"Setting vars for img info.")
        text = 'data-src="'
        number = 2
        skylanderList = skylanderImgList
    word = 'data-src="/images/skylander'
    with open(f'skylanderSerie/html/serie{currentSkylandersSerie}.html', 'r') as fp:
        logging.info(f"Current skylander set number is {currentSkylandersSerie}")
        # read all lines in a list
        lines = fp.readlines()
        for line in lines:
            # check if string present on a current line
            if line.find(word) != -1:
                line = line.replace('"></div>','')
                line = line.replace('<div class="figurepic"><img alt="','')
                line = line.replace(' ','')
                line = line.replace('\n', '')
                line = line.replace('small', 'mid')
                line = line.replace('(Series2)','')
                line = line.replace('(Series3)','')
                left_text = line.partition(text)[number]
                if kind == "name":
                    left_text = (re.sub(r"(\w)([A-Z])", r"\1 \2", left_text))
                    skylanderList.append(left_text)
                    logging.info(f"Current skylander: {left_text}")
                else:
                    skylanderList.append(left_text)
    logging.debug(f"{len(skylanderNameList)}")
    logging.debug(f"{len(skylanderImgList)}")

def createJson(currentSkylandersSerie):
    global skylanderNameList
    global skylanderImgList
    if not skylanderNameList or not skylanderImgList:
        logging.error(f"Returned empty array..")
        exit()
    jsonList = []
    for i in range(len(skylanderNameList)):
        jsonList.append({"name" : skylanderNameList[i], "img" : "https://www.outcyders.net"+skylanderImgList[i]})

    with open(f'skylanderSerie/json/s{currentSkylandersSerie}.json', 'w', encoding='utf-8') as f:
        json.dump(jsonList, f, ensure_ascii=False, indent=4)
    # logging.debug(f(json.dumps(jsonList, indent = 1)))
    skylanderNameList = []
    skylanderImgList = []
# Getting the name and image of the skylanders and then creating a json file with the data.



def main():
    level = logging.DEBUG
    ftm = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=ftm)
    skylanderSetPage()

main()



# test()