from flask import Flask, render_template, url_for, request, redirect
from boltiot import Bolt
from globalrep import tcases , acases , rcases , dcases
from indrep import itcases , itoc , iacases , iccases , ircases , idcases , itod


app = Flask(__name__)

Device_ID = 'NULL'
API_KEY = 'NULL'

tc = tcases()
ac = acases()
rc = rcases()
dc = dcases()
itc = itcases()
iitoc = itoc()
iac = iacases()
irc = ircases()
icc = iccases()
idc = idcases()
iitod = itod()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/tracker")
def tracker():
    return render_template("tracker.html" , tc = tc , ac = ac , rc = rc ,
                           dc = dc , itc = itc , iitoc = iitoc , iac = iac,
                           irc = irc , icc = icc , idc = idc , iitod = iitod)

@app.route("/precautions")
def precautions():
    return render_template("precautions.html")

@app.route("/feelingbored")
def feelingbored():
    return render_template("feelingbored.html")

@app.route("/automate" , methods = ["GET" , "POST"])
def automate():
    if request.method == "GET":
        return "Automation is not here!"
    else:
        Device_ID = request.form.get("device")
        API_KEY = request.form.get("apikey")
        mybolt = Bolt(API_KEY , Device_ID)
        status = mybolt.isOnline()
        if status[11:17] == 'online':
            return render_template("control.html" , Device_ID = Device_ID , API_KEY = API_KEY)
        else:
            return 'Sorry, either your device is offline or you entered invalid credentials! Please try again later...'

if __name__ == "__main__":
    app.run()
        
