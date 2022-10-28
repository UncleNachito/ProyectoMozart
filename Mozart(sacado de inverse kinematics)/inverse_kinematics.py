from math import *
def position_to_dof(x, y, z):
    """Acá va tu código para calcular la cinemática inversa
    
    La función debe recibir (x,y,z) en milimetros y retornar q0, q1 y q2 en grados"""
    q0 = atan(y/x)
    print(q0)
    q2 = acos(((((x / cos(q0)) - 66)**2) + (z - 94)**2 - (125**2) - ((147**2))) /(((2*125*147))))
    print(q2)
    q1 = atan(((z-94)/((x/cos(q0))-60.3))-(atan((147*sin(q2))/(125+(147*cos(q2))))))

    return int(q0), int(q1), int(q2)    # El robot solo entiende grados sexagesimales y enteros 


position_to_dof(60, 0, 94)
