import requests

def getOffers():
    r = requests.get('https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=FI&allowCountries=FI')
    offers = r.json()['data']['Catalog']['searchStore']['elements']
    return offers
    

def filterFunct(offer):
    try:
        if(offer['promotions'] == None):
            return False
    except NameError:
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
    # end daten aikavyöhyke mysteeri, joten jää syssymmälle.
    # endDate = offer['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['endDate']
    return offer['title']

offers = getOffers()
free = list(filter(filterFunct, offers))
for offer in free:
    print(offerToString(offer))