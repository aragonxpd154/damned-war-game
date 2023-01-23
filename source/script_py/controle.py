# importando os modules
from bge import logic as g, events

# obter o controle
c = g.getCurrentController()

# obter o objeto conectado o carro
o = c.owner

# obter o teclado
tc = g.keyboard.events

# variaveis
freio = 0.0
virar = 0.0
acelerador = 0.0

# as teclas que vai muda os valor das variaveis
if tc[events.SKEY]: acelerador -= 2500.0
if tc[events.WKEY]: acelerador  = 2200.0
if tc[events.AKEY]: virar = 0.5
if tc[events.DKEY]: virar -= 0.5
if tc[events.SPACEKEY]: freio = 90.0

# obter a fisica do carro que esta no outro script
carro = o["carro"]

# obter aceleracao nas rodas 0,1,2,3
#carro.applyEngineForce(acelerador,0)
#carro.applyEngineForce(acelerador,1)
carro.applyEngineForce(acelerador,2)
carro.applyEngineForce(acelerador,3)

# virar roda 0.1
carro.setSteeringValue(virar,0)
carro.setSteeringValue(virar,1)

# freia rodas 0,1,2,3
#carro.applyBraking(freio,0)
#carro.applyBraking(freio,1)
carro.applyBraking(freio,2)
carro.applyBraking(freio,3)