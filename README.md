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

O script settings.py encontrado no diretório .~/source/script_py/settings.py inclui todos os dados registrados no menu.

It reads and writes game settings from a "Settings.dat" file. The "readSettings" function reads the settings from the file and stores them in properties of the "owner" object. The "writeSettings" function writes the "owner" object's settings back to the file.

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

Working here...

## 💻 Development Status

The project was to demonstrate the creation of a game menu model using only small snippets of code in python and logic from the blender game engine, an obsolete and discontinued suite of Blender3D.

## :memo: License

This project is under the GPL v3.0 license. See the [LICENSE](https://github.com/aragonxpd154/damned-war-game/blob/main/LICENSE) for more information.

---

Made with ♥ by Marcos (Obel) :wave: [Get in touch!](https://www.linkedin.com/in/marcosobel)
