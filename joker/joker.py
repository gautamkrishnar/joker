import json
import requests
try:
    from urllib.parse import quote_plus
    from urllib.parse import urlencode
except ImportError:
    from urllib import quote_plus
    from urllib import urlencode
from random import randrange

def getrequest(url):
    return requests.get(url)
def postrequest(url,data):
    return requests.post(url,data)
def checkstatus(response):
    if response.status_code not in iter(200,404):
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

"""
#    XKCD API:

If  @param img == True the function will return image url (string) of the meme.
    Else will return:
    tittle : string (Tittle of the meme)
    meme : string (Meme text)
"""
def xkcd(img=False):
    response = getrequest("http://xkcd.com/info.0.json")
    #checkstatus(response)
    data = response.json()
    maxno = data['num']
    while 1:
        num = randrange(1,maxno)
        response = getrequest("http://xkcd.com/" + str(num) + "/info.0.json")
        data = response.json()
        if img == True:
            return data['img']
        if data['transcript'] != '':
            break
    meme, junk, title = data['transcript'].partition("{{")
    meme = meme.replace("[[", "[").replace("]]", "]").replace("((","(").replace("))",")")\
        .replace("{{","{").replace("}}","]")
    try :
        title = title[title.index(":") + 1:]
    except:
        title = ""
        return title,meme
    title = title.split('}}')[0]
    while 1:
        if title[0] == " ":
            title = title[1:]
        else: break
    return title,meme


"""
#   Chuck Norris API
If @param cat is given, it will return jokes related to the given categories.
List of categories: https://api.chucknorris.io/jokes/categories
"""
def ChuckNorris(cat=""):
    if cat == "":
        response = getrequest("https://api.chucknorris.io/jokes/random")
    else:
        response = getrequest("https://api.chucknorris.io/jokes/random?category="+cat)
        if response.status_code == 404:
            return "Wrong category! / Please check your internet conection,"
    data = response.json()
    return data['value']

"""
#   Be Like Bill API

Returns the belikebill image url for the parameters specified
@param name: peron's name
@param sex: person's sex
@param text: custom meme (Newline as "\n"
If no parameter is given then it will return the default image url
"""
def belikebill(name="",sex="",text=""):
    if name !="":
        if sex!="":
            return "http://belikebill.azurewebsites.net/billgen-API.php?default=1&sex="+sex+"&name="+name
        else:
            return "http://belikebill.azurewebsites.net/billgen-API.php?default=1&name="+name
    elif text!="":
        text.replace("\n","%0D%")
        return "http://belikebill.azurewebsites.net/billgen-API.php?text="+text
    else:
        return "http://belikebill.azurewebsites.net/billgen-API.php?default=1"
"""
#   Phteven English API
@:param inp: text to translate
todo: Under construction
"""
def phteven(inp):
    header = {"Host": "api.phteven.io/",
                "Cache-Control": "no-cache",
                "Content-Type": "application/x-www-form-urlencoded"
              }
    data ={"text":inp}
    response = postrequest("http://api.phteven.io/translate/",urlencode(data).encode())
    data = response.json()
    return


"""
#   Ron Swanson Quotes API
Returns random Ron Swanson quotes if no param is given
@param count: Number of quotes, Will return the specified number of quotes as list
"""
def RonSwansonQuotes(count=1):
    if count > 1:
        response = getrequest("http://ron-swanson-quotes.herokuapp.com/v2/quotes/"+str(count))
        data = response.json()
        return data
    else:
        response = getrequest("http://ron-swanson-quotes.herokuapp.com/v2/quotes/1")
    data = response.json()
    return data[0]

"""
#   Yes or No API
Returns random yes or no as a string if no parameter is passed
@:param img: Booleam if it is specified, then it will return a yes or now and a image url of random meme with that choice
@:param forced: Values("yes","no") if any of it is given, the result will be forced to  =v=be the given input
"""
def YesOrNo(img=False,forced=""):
    if forced in ["yes","no"]:
        response = getrequest("https://yesno.wtf/api/?force="+forced)
    else:
        response = getrequest("https://yesno.wtf/api/")
    data = response.json()
    if img:
        return data['answer'],data['image']
    else:
        return data['answer']


"""
#   Cat Facts API
The Cat Facts API is a web service able to deliver random cat facts sourced from a variety of open web pages.
@:param count: no of facts to recieve. default is 1. If more than one, function returns a list
"""
def catFacts(count=1):
    if count > 1:
        result = getrequest("http://catfacts-api.appspot.com/api/facts?number="+str(count))
        data = result.json()
        return data['facts']
    else:
        result = getrequest("http://catfacts-api.appspot.com/api/facts?number=" + str(count))
        data = result.json()
        return data['facts'][0]

if __name__ == '__main__':
    print(catFacts(3))