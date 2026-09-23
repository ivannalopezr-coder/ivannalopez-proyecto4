from whalesbot import *

patrol_integrated_initialization(A,100,B,-100) #inicia ajustes para seguimientos de linea en el PLC 1s
"""
parametro1 : puerto de llanta izquierda (A,B,C,D)
parametro2 : velocidad de llanta izquierda (-100 a 100)
parametro3 : puerto de la llanta derecha (A,B,C,D)
parametro4 : velocidad de la llanta derecha (-100 a 100)
"""
patrol_single_initialization(A,100,B,-100,P1,P2,P3,P4,P5) # inicia ajustes para seguimientos de linea en el PLC 5s
"""
parametro1 : puerto de llanta izquierda (A,B,C,D)
parametro2 : velocidad de llanta izquierda (-100 a 100)
parametro3 : puerto de la llanta derecha (A,B,C,D)
parametro4 : velocidad de la llanta derecha (-100 a 100)
parametro5 : puertos de los sensores (P1 a P10)
"""
patrol_time(30,0.5) #realiza seguimientos de linea por tiempo
"""
parametro1 : velocidad de seguimiento (0 - 100)
parametro2 : tiempo de rastreo (0 - 60)
"""

patrol_road(intersection_right,30,0) #realiza seguimiento de linea y se detiene en la interseccion que le indiques
"""
parametro1 : tipo de interseccion (intersection_left, intersection_right, intersection_T)
parametro2 : velocidad de seguimiento (0 - 100)
parametro3 : tiempo de cruce (0 - 60)
"""

start_motor_angle(20,20,360) # mueve el robot a la direccion deseada por grados
"""
parametro1 : velocidad del motor izquierdo (-100 a 100)
parametro2 : velocidad del motor derecho (-100 a 100)
parametro3 : grados que rotaran ambos motores ( >0 )
""" 

set_motor_angle(C,30,200) #mueve la garra a la direccion deseada por grados
"""
parametro1 : puerto del motor que tiene la garra (A,B,C,D)
parametro2 : velocidad del motor (-100 a 100)
parametro3 : grados que rotaran ambos motores ( >0 )
"""

color_detected(P1,0) #funcion para detectar colores 
"""
parametro1 : puerto donde va conectado el sensor (P1 - P5)
parametro2 : color a detectar, valores:
0 = rojo
1 = naranja
2 = amarillo
3 = verde
4 = cyan
5 = azul
6 = morado 
7 = blanco
8 = negro
"""