import time
from client import RobotClient
from inverse_kinematics import position_to_dof
from math import *

## Conectarse al robot

s = RobotClient(address="127.0.0.1")  # Recuerda usar una dirección válida
s.connect()
s.home()    # Revisa el archivo client.py para que veas qué hace esta función


## Función para mover el robot usando cartesianas
def move_robot_to_xyz(robot, x, y, z):
    q0, q1, q2 = position_to_dof(x, y, z)
    robot.set_joints(q0, q1, q2)

## Mover el robot (acá va tu código)

# move_robot_to_xyz(r, x=0, y=0, z=90) ORIGEN!

# EL CODIGO ES REFERENCIAL, SE MODIFICARAN LOS PARAMETROS CUANDO TENGAMOS EL CIRCUITO ARMADO UWU
# Ocupe como referencia el tip tap toe de 12x12cm, el centro de los
# primeros 3 espacios cuadrados representarian la posicion de los 3 botones
# El movimiento hacia abajo dependera de que tan largo sea el solenoide y que tan "alto" sea el boton
# Los movimientos de lado a lado y de adelante dependera de que tan grande sea el circuito

def PresionarBotonIzq(robot, x, y, z):
    move_robot_to_xyz(s, x=40, y=0, z=90) #Primer movimiento, hacia la izq
    move_robot_to_xyz(s, x=40, y=15, z=90) #Segundo movimiento, hacia adelante
    move_robot_to_xyz(s, x=40, y=15, z=130) #Tercer movimiento, hacia abajo (para presionar)

def PresionarBotonDer(robot, x, y, z):
    move_robot_to_xyz(s, x=-40, y=0, z=90) #Primer movimiento, hacia la der
    move_robot_to_xyz(s, x=-40, y=15, z=90) #Segundo movimiento, hacia adelante
    move_robot_to_xyz(s, x=-40, y=15, z=130) #Tercer movimiento, hacia abajo (para presionar)

def PresionarBotonCentro(robot, x, y, z):
    move_robot_to_xyz(s, x=50, y=10, z=90) #Primer movimiento, hacia adelante
    move_robot_to_xyz(s, x=50, y=10, z=130) #Segundo movimiento, hacia abajo (para presionar)
