from bge import render, logic

cont = logic.getCurrentController()
own = cont.owner

RES = [    
    "1920 x 1080",
    "1680 x 1050",
    "1600 x 900",
    "1440 x 900",
    "1400 x 1050",
    "1366 x 768",
    "1360 x 768",
    "1280 x 1024",
    "1280 x 960",
    "1280 x 800",
    "1280 x 768",
    "1280 x 720",
    "1280 x 600",
    "1152 x 864",
    "1024 x 768",
    "800 x 600",
    "640 x 480",
    "640 x 400",
    "512 x 384",
]

def setWindow():
    render.setFullScreen(False)

val = own["val"]

if val < 0:
    own["val"] = len(RES)-1
elif val == (len(RES)):
    own["val"] = 0

own.text = (RES[(own["val"])])

own["x"] = (own.text).rsplit(" x ",1)[0]
own["y"] = (own.text).rsplit(" x ",1)[1]

def setRes(cont):
    
    own = cont.owner
    
    x = own["x"]
    y = own["y"]

    render.setWindowSize(int(x),int(y))