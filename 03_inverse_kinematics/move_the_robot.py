import time
from client import RobotClient
from inverse_kinematics import position_to_dof

## Conectarse al robot
"192.168.0.13"
s = RobotClient(address="192.168.0.13")  # Recuerda usar una dirección válida
s.connect()


## Función para mover el robot usando cartesianas
def move_robot_to_xyz(robot, x, y, z):
    q0, q1, q2 = position_to_dof(x, y, z)
    robot.set_joints(q0, q1, q2)
# move_robot_to_xyz(r, x=230, y=0, z=243) ORIGEN!


def home():#x:
    move_robot_to_xyz(s, x=180, y=0, z=230)


def move_to_button2(vector):
    x_home = 130
    y_home = 0
    z_home = 230
    z_button = 120

    path = []

    if vector[0] == x_home:
        path.append((x_home, y_home, z_home))
    else:
        for i in range(10):
            x = x_home + (vector[0] - x_home) * float(i) / 10
            y = y_home
            z = z_home
            path.append((x, y, z))

    if vector[1] == y_home:
        path.append((vector[0], y_home, z_home))
    else:
        for i in range(10):
            x = x_home + (vector[0] - x_home)
            y = y_home + (vector[1] - y_home) * float(i) / 10
            z = z_home
            path.append((x, y, z))

    for i in range(10):
        x = x_home + (vector[0] - x_home)
        y = y_home + (vector[1] - y_home)
        z = z_home + (z_button - z_home) * float(i) / 10
        path.append((x, y, z))

    path.append((x_home, y_home, z_home))

    for x, y, z in path:
        move_robot_to_xyz(s, x, y, z)
        time.sleep(0.1)


home()
