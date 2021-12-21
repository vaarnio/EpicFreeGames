import requests

def getOffers():
    r = requests.get('https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=FI&allowCountries=FI')
    offers = r.json()['data']['Catalog']['searchStore']['elements']
    return offers

def getFree():
    offers = getOffers()
    return list(filter(filterFunct, offers))

def filterFunct(offer):
    try:
        if(offer['promotions'] == None):
            #All freeGamePromotions don't have entries under 'promotions'
            return False
    except NameError:
        #Not sure if there are freeGamePromotions that don't have 'promotions' entry but the NameError check is here just to be safe.
        print('NameError')
        return False
    else:
        # filter out games with no promotions
        promotions = offer['promotions']['promotionalOffers']
        if(len(promotions) <= 0):
            return False
        
        # select only games that are 100% off
        discountPercentage = offer['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['discountSetting']['discountPercentage']
        if discountPercentage == 0:
            return True

def offerToString(offer):
    return offer['title']

def main():
    offers = getOffers()
    free = list(filter(filterFunct, offers))
    for offer in free:
        print(offerToString(offer))

if __name__ == "__main__":
    main()