from bge import logic

cont = logic.getCurrentController()
own = cont.owner

mouse = logic.mouse

own.worldPosition = [mouse.position[0]*(own["amtx"]),mouse.position[1]*(own["amty"]),own.worldPosition.z]