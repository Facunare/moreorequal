    
resta = 70
print(resta<1 and resta<16)
if resta>= 1 and resta <=20:
    mensaje = "El numero es menor y estas muy cerca"
elif resta >20 and resta <=60:
    mensaje = "El numero es menor"
elif resta >60 and resta <=99:
    mensaje = "El numero es menor y estas lejos"
elif resta>= 1 and resta <=20:
    mensaje = "El numero es mayor y estas muy cerca"
elif resta >20 and resta <=60:
    mensaje = "El numero es mayor"
elif resta >60 and resta <=99:
    mensaje = "El numero es mayor y estas lejos"

print(mensaje)