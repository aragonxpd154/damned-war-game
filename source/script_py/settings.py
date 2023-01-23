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