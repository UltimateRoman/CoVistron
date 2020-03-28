# **CoVistron**

### An all-in-one project for people under home-quarantine due to CoViD-19

*Project by Beta_Codinators for HomeHack. <br />
Our Web App services and devices are fully functional and are only intended for the benefit of society.*
<br /><br />
_**If you want to skip the description and go directly and setup CoVistron click here** - [setup:covistron](#Setup)_
<br />
## The Problem

The world is affected by the n-Cov virus and due to its highly contagious nature, many nations are forced to put their citizens under lockdown and confine them to their homes to curb this pandemic. But home-quarantine can be an unpleasant experience for many, especially for long periods involving several weeks. These people may also be compromising on the basic but important safety precautions advised by their respective health organistaions. All of these problems may lead to unprecedented consequences and would hamper the whole initiative.

## What is CoVistron?

Keeping in mind these issues, we have suitably devised CoVistron to be an umbrella intiative to help the quarantined people and make the whole process a satisfactory but safe affair. Powered by IoT, it can guide, accompany and entertain people in this crisis. CoVistron involves the following - 

- [CoVistron Smart Devices](#CoVistron-Arduino-powered-Intelligent-Devices)

- [CoVistron Web App](#CoVistron-Web-App)

- [CoVistron Home-Automation](#Covistron-Home-Automation)
<br />
The smart devices have been devised to help people follow safety precautions without fail in an innovative and fun way. Home-Automation is also deployed as a precaution to minimise the physical contact of people with their home appliances to prevent disease transmission to their housemates in that manner.
<br />
The Web App can be used to facilitate home-automation. In addition, it provides a real-time tracker of CoVid-19 cases around the world and in India. It has details of our smart devices and a small entertainment section providing hacks to overcome boredom. Moreover, it also has a section providing safety precautions to its users to promote awareness.

### CoVistron Arduino-powered Intelligent Devices

These devices are deployed to help you with safety precautions like washing your hands with soap/handwash for atleast 20 seconds, not touching your face and minimizing physical contact with shared objects like handwash dispensers. The devices currently available are - 
<br />
#### 1. CoVistron Smart Cap:
It helps you avoid touching your face by alerting you whenever you try to do so.
<br />
![Smart_Cap](Arduino/Smart_Cap/Cap_Plan.jpg?raw=true)

#### 2. CoVistron Hand-washing Tracker:
It promptly tracks your hand-washing time and cutely annoys you if you havent achieved the 20 seconds target.
<br />
![Smart_Tap](Arduino/Handwash_Tracker/Tap_Plan.jpg?raw=true)


#### 3. CoVistron Contactless Handwash/Sanitizer Dispenser:
It dispenses a suitable amount of handwash/sanitizer without physical contact by detecting the presence of your hands. It is useful in homes where multiple people share the same item.
<br />
![Safe_Dispenser](Arduino/Safe_Dispenser/Dispenser_Plan.jpg?raw=true)


### CoVistron Web App

The Web App has a state-of-the-art real-time CoViD-19 cases tracker providing details such as number of cases, active cases, recovered cases, deaths etc.. from India and the rest of the world. It also has the login page to execute home-automation for our registered users which is built with Bolt IoT.
<br />
Additional sections include 'About us', 'Precautions'(to spread awareness) and 'FeelingBored?'(Entertainment)...

### Covistron Home-Automation

Home-Automation is powered by Bolt IoT. A Bolt WiFi-Module is required for this purpose. The CoVistron Web App allows users to execute home automation by logging in using their Bolt device credentials.
  
  
## Setup

### 1. CoVistron-Arduino Devices:

To setup the CoVistron Arduino devices, check out the circuit and layout diagrams in the respective folders of each device at [Arduino-devices](Arduino) and assemble them. Upload the respective code of each device into your Arduinos using the Arduino IDE.

<br />

### 2. a) Web App:

The CoVistron Web-App is built using the flask python framework. To run the web app, you must have the flask and boltiot python modules installed in addition to python.  

#### For Linux users:

Step 1 - Install dependancies
<br />
```
$ sudo apt install python-pip
$ pip install flask
$ pip install boltiot
```
Step 2 - Clone the code into a fresh folder
<br />
```
$ git clone https://github.com/abelzach/CoVistron.git
$ cd Web_App
```
Step 3 - Run application.py to start the web app
<br />
```
$ python application.py
```
Step 4 - Visit localhost:5000 in your browser and enjoy the CoVistron Web-App experience.

#### For windows users:

Step 1 - Make sure you have the python interpreter installed on your system. Go to [python](https://www.python.org/) and install it if you don't have it already.

<br />
Step 2 - Go to the python installed folder in your system and into the 'Scripts' folder. Then, open command window there and run the following commands in it.
<br /> <br />
pip install flask
<br /><br />
pip install boltiot
<br /><br />
If this step didn't work properly, search and try out some other method online to install flask on windows and do the same for boltiot.

Step 3 - Download this repository as a zip file and extract it. Go to 'application.py' in the 'Web_App' folder and run it with the python interpreter to start the web app.
<br />

Step 4 - Visit localhost:5000 in your browser and enjoy the CoVistron Web-App experience.
<br />

### 2. b) Home-Automation with Bolt IoT

Home-Automation is only possible for users who have a Bolt Wi-Fi Module with them.
<br />
Step 1 - Assemble the home-automation circuit as given in [Bolt-circuit-layout](Images/HomeAutomation_Circuit.jpg). Pins 0-3 of the Bolt Module can be used to connect the appliances while Pin 4 is used for the alert buzzer.
<br />
Step 2 - Run the CoVistron web app and visit the login page.
<br />
Step 3 - Enter the credentials of your Bolt Module to login.
<br />
Step 4 - Use the panel controls provided and enjoy CoVistron home_automation.
<br />
We appreciate your valuable suggestions to improve your experience.
<br />
Stay Safe!
