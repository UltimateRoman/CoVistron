import requests, json
import config as c


response = requests.get(c.url1)
data1 = json.loads(response.text)


cases = int(data1.get('cases' , 0))
todaycases = int(data1.get('todayCases' , 0))
active = int(data1.get('active' , 0))
critical = int(data1.get('critical' , 0))
recovered = int(data1.get('recovered' , 0))
deaths = int(data1.get('deaths' , 0))
todaydeaths = int(data1.get('todayDeaths' , 0))


def itcases():
    return cases

def itoc():
    return todaycases

def iacases():
    return active

def iccases():
    return critical

def ircases():
    return recovered

def idcases():
    return deaths

def itod():
    return todaydeaths

