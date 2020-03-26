import requests, json, time
import config as c


response = requests.get(c.url)
data0 = json.loads(response.text)

cases = int(data0.get('cases' , 0))
recovered = int(data0.get('recovered' , 0))
deaths = int(data0.get('deaths' , 0))
active = (cases - recovered - deaths)

def tcases():
    return cases


def acases():
    return active


def rcases():
    return recovered


def dcases():
    return deaths
