<h1 align="center">
<img alt="damned-war-game" src="https://raw.githubusercontent.com/aragonxpd154/damned-war-game/main/icone/DAMNED%20WAR_free-file.png"/>
<br>
</h1>

<h4 align="center">

In mid-2016, I started an in-depth study of the Blender 3D game development engine, version 2.77 was operating at the time and the software included new features with the cycles rendering engine, in light of this desire to develop new skills in oriented programming lines. three-dimensional objects and the sum of previous knowledge of panda3d, I started to develop the menu and a physics simulation of a jeep that would be used for academic purposes and personal studies. Unfortunately the BGE engine (blender 3d) is no longer available in the latest versions, however you can run the project by downloading a version prior to 2.77 from the Blender Foundation website. I leave this project available for study purposes and the script source code and the .blend file for posterity

</h4>

<p align="center">
<img alt="Github top language" src="https://img.shields.io/github/languages/top/aragonxpd154/damned-war-game">
<img alt="Github laguage count" src="https://img.shields.io/github/languages/count/aragonxpd154/damned-war-game">
<img alt="Repository size" src="https://img.shields.io/github/repo-size/aragonxpd154/damned-war-game">
<img alt="Github last commit" src="https://img.shields.io/github/last-commit/aragonxpd154/damned-war-game">
<a href="https://github.com/aragonxpd154/damned-war-game/issues">
<img alt="Repository issues" src="https://img.shields.io/github/issues/aragonxpd154/damned-war-game"> 
</a>
<img alt="Github license" src="https://img.shields.io/github/license/aragonxpd154/damned-war-game">
</a>
</p>

<p align="center">
<a href="#rocket-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#information_source">How To Use</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#do-it-yourself">Do It Yourself</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#status">Development Status</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
<a href="#memo-license">License</a>
</p>

<p align="center">
<img alt="Demo on Photo" src="https://github.com/aragonxpd154/damned-war-game/blob/main/icone/apresentation.gif">
</p>

## :rocket: Technologies

This project is still in the development stage and using the following technologies

- [Blender3D](https://www.blender.org/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Python3.1 and Python2.9](https://www.python.org/)

## :information_source: How To Use

This project was carried out using the Blender 3D software and its internal suite of functionality specific to the BGE (Blender Game Engine), to open this project it is necessary to install version 2.77 or earlier, this [link](https://download.blender.org/release/) you will find all the repositories with compilations and binaries of Blender 3D.

To clone and download all project directories you can use [Git](https://git-scm.com), or any other specific program.

To clone the current directory use the command:

```bash
# Clone this repository
$ git clone https://github.com/aragonxpd154/damned-war-game
```

## ☕ Do It Yourself

In the .~/source directory, you will find the .blend files in the source_blend folder which can be opened with Blender V2.77 or earlier.

```bash
INTRO.blend file, includes description animation
MENU_INICIAL.blend file includes the original menu that accesses the guide.
```

The settings.py script found in the .~/source/script_py/settings.py directory includes all the data recorded in the menu and saved according to the readSettings and whiteSettings functions, below which the Settings.dat file is generated in the parent directory. For more information on the methods used, see the blender guide at this link.

```bash
from bge import logic

fileName = "Settings.dat"

def readSettings(cont):
    own = cont.owner
    with open(fileName) as reading:
        data = [line.split()[0] for line in reading]
        reading.close()

    own["val"] = int(data[0])
    own["bright"] = int(data[1])
    own["playerName"] = data[2]
    own["audio"] = int(data[3])

def writeSettings(cont):
    own = cont.owner
    with open(fileName, 'w') as writing:
        writing.write(str(own["val"])+"\n")
        writing.write(str(own["bright"])+"\n")
        writing.write(own["playerName"]+"\n")
        writing.write(str(own["audio"]+"\n"))
        writing.close()
```

This code makes screen resolution adjustment in a game made with Blender Game Engine (BGE) game engine. It defines a list of available screen resolutions and assigns one of those resolutions to an object in the scene. It uses the render library's setWindowSize method to adjust the screen resolution according to the (x, y) dimensions defined in the resolution list. The "val" value of the selected resolution is stored as a property of the object in the scene and can be changed by the player. Which can be found in the script_py repository

```bash
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
```

And finally the code that controls the position of an object in the world according to the position of the mouse cursor. The object's position is defined by multiplying the mouse cursor position by the "amtx" and "amty" variables. The object's position is updated every frame.

```bash
from bge import logic

cont = logic.getCurrentController()
own = cont.owner

mouse = logic.mouse

own.worldPosition = [mouse.position[0]*(own["amtx"]),mouse.position[1]*(own["amty"]),own.worldPosition.z]
```

The code takes the current controller of the "own" object and loads the dialog file specified in the variable "dialogFile1" this file is found in ~/DATA/DATA/direct.1. Then the file is read and the content is stored in the "dialog" variable. At each iteration, the value of the "count" variable is incremented by 1, and the displayed text is trimmed to the size of the "count" variable. Thus, the text of the dialog is displayed little by little with each iteration.

```bash
from bge import logic

cont = logic.getCurrentController()
own = cont.owner

dialogFile = own["dialogFile1"]
dialogFile = logic.expandPath("//"+dialogFile)

with open(dialogFile) as d:
    dialog = d.read()
    d.close()

own["count"] += 1
count = own["count"]

own.text = dialog[:count]
```

## 💻 Development Status

The project was to demonstrate the creation of a game menu model using only small snippets of code in python and logic from the blender game engine, an obsolete and discontinued suite of Blender3D.

## :memo: License

This project is under the GPL v3.0 license. See the [LICENSE](https://github.com/aragonxpd154/damned-war-game/blob/main/LICENSE) for more information.

---

Made with ♥ by Marcos (Obel) :wave: [Get in touch!](https://www.linkedin.com/in/marcosobel)
