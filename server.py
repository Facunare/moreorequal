import socket
import pickle
socket_sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_sv.bind(("localhost", 8001))
socket_sv.listen(1)
socket_client, client_addr = socket_sv.accept()
intentos = 5
while True:
    numero = int(input("Elija un numero del 1 al 100: "))
    if numero == "" or numero <= 0 or numero >100:
        print("Numero invalido")
        continue
    else:
        print(f"El cliente tendra que adivinar el numero {numero}")
        host_response = pickle.dumps(numero)
        socket_client.send(host_response)
        break

while True:
    rta = socket_client.recv(1024).decode()
    print("El jugador elijio el numero: "+ f"\033[94m{str(rta)}\033[0m" )
    resta = numero - int(rta)
    if resta<=0:
        resta = resta*-1
    if int(rta) == numero:
        mensaje = f"\033[94mAcertaste\033[0m" 
        socket_client.send(mensaje.encode())
        break
    else:
        print("hola")
        intentos-=1
        if intentos == 0:
            sinIntentos = f"\033[91mEl client se quedo sin intentos!!\033[0m" 
            print(sinIntentos)
            break
        
    if int(rta) > numero and (resta>= 1 and resta <=20):
        mensaje = f"\033[91mEl numero es menor y estas muy cerca\033[0m" 
    elif int(rta) > numero and (resta >20 and resta <=60):
        mensaje = f"\033[91mEl numero es menor\033[0m" 
    elif int(rta) > numero and (resta >60 and resta <=99):
        mensaje = f"\033[91mEl numero es menor y estas lejos\033[0m" 
    elif int(rta) < numero and (resta>= 1 and resta <=20):
        mensaje = f"\033[91mEl numero es mayor y estas muy cerca\033[0m" 
    elif int(rta) < numero and (resta >20 and resta <=60):
        mensaje = f"\033[91mEl numero es mayor\033[0m" 
    elif int(rta) < numero and (resta >60 and resta <=99):
        mensaje = f"\033[91mEl numero es mayor y estas lejos\033[0m" 
    
    
    socket_client.send(mensaje.encode())