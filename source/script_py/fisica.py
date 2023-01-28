#Esse código cria um carro com física simulada na engine Blender Game Engine (BGE), utilizando o módulo de PhysicsConstraints. Ele importa os módulos "bge" e "PhysicsConstraints", define as propriedades dos objetos-rodas (nome, posição, angulo, raio, direção, altura da suspensão) e cria uma constraint de carro no objeto da cena. Em seguida, as rodas são adicionadas ao carro. As propriedades da suspensão, a influência de rolamento e a rigidez da suspensão são ajustadas.

# importando os modules
from bge import logic as g
import PhysicsConstraints as pc

c = g.getCurrentController()


# obter a cena e os objetos da cena
s = g.getCurrentScene().objects

# nome das rodas
rd_0 = s["0"]
rd_1 = s["1"]
rd_2 = s["2"]
rd_3 = s["3"]

# posicao das rodas
rd_p_0 = [ 1.0, -1.4, 0.0]
rd_p_1 = [-1.0, -1.4, 0.0]
rd_p_2 = [-1.0,  1.4, 0.0]
rd_p_3 = [ 1.0,  1.4, 0.0]

# angulo da suspensao
rd_an_0 = [0.0, 0.0, -1.0]
rd_an_1 = [0.0, 0.0, -1.0]
rd_an_2 = [0.0, 0.0, -1.0]
rd_an_3 = [0.0, 0.0, -1.0]

# eixo
rd_e_0 =  [-1.0, 0.0, 0.0]
rd_e_1 =  [-1.0, 0.0, 0.0]
rd_e_2 =  [-1.0, 0.0, 0.0]
rd_e_3 =  [-1.0, 0.0, 0.0]

# altura da suspensao
rd_a_s_0 = 0.1
rd_a_s_1 = 0.1
rd_a_s_2 = 0.1
rd_a_s_3 = 0.1

# raio das rodas
rd_r_0 = 0.65
rd_r_1 = 0.65
rd_r_2 = 0.65
rd_r_3 = 0.65

# direcao
rd_d_0 = True
rd_d_1 = True
rd_d_2 = False
rd_d_3 = False

# obter o objeto conectado, o carro
o = c.owner

# criando a fisica
carro = pc.createConstraint(o.getPhysicsId(),0,11)
carro = carro.getConstraintId()
o["carro"] = carro = pc.getVehicleConstraint(carro)

# add as rodas no carro
carro.addWheel(rd_0, rd_p_0, rd_an_0, rd_e_0, rd_a_s_0, rd_r_0, rd_d_0)
carro.addWheel(rd_1, rd_p_1, rd_an_1, rd_e_1, rd_a_s_1, rd_r_1, rd_d_1)
carro.addWheel(rd_2, rd_p_2, rd_an_2, rd_e_2, rd_a_s_2, rd_r_2, rd_d_2)
carro.addWheel(rd_3, rd_p_3, rd_an_3, rd_e_3, rd_a_s_3, rd_r_3, rd_d_3)


######################################################################################

# preçao de decida

carro.setSuspensionCompression(1.0, 0)  # front driver's tire 
carro.setSuspensionCompression(1.0, 1)  # front passenger's tire 
carro.setSuspensionCompression(1.0, 2)  # rear driver's tire
carro.setSuspensionCompression(1.0, 3)  # rear passenger's tire 


######################################################################################

# limite da rotacao do carro, pra ele nao capota

carro.setRollInfluence(0.05,0)
carro.setRollInfluence(0.05,1)
carro.setRollInfluence(0.05,2)
carro.setRollInfluence(0.05,3)

######################################################################################

# rigides da suspençao
	
carro.setSuspensionStiffness(20.0, 0)
carro.setSuspensionStiffness(20.0, 1)
carro.setSuspensionStiffness(20.0, 2)
carro.setSuspensionStiffness(20.0, 3)

######################################################################################

# derrapagen

carro.setTyreFriction(5.0, 0)  # front driver's tire 
carro.setTyreFriction(5.0, 1)  # front passenger's tire 
carro.setTyreFriction(5.0, 2)  # rear driver's tire
carro.setTyreFriction(5.0, 3)  # rear passenger's tire

#######################################################################################

# preçao subida

carro.setSuspensionDamping(1.0, 0)  # front driver's tire 
carro.setSuspensionDamping(1.0, 1)  # front passenger's tire 
carro.setSuspensionDamping(1.0, 2)  # rear driver's tire
carro.setSuspensionDamping(1.0, 3)  # rear passenger's tire 