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