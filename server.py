import socket
import pickle
socket_sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_sv.bind(("localhost", 8001))
socket_sv.listen(1)
socket_client, client_addr = socket_sv.accept()
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
    print("El jugador elijio el numero: "+ str(rta))
    resta = numero - int(rta)
    if resta<=0:
        resta = resta*-1

    if int(rta) > numero and (resta<= 1 or resta >=20):
        mensaje = "El numero es menor y estas muy cerca"
    elif int(rta) > numero and (resta <20 or resta >=60):
        mensaje = "El numero es menor"
    elif int(rta) > numero and (resta <60 or resta >=99):
        mensaje = "El numero es menor y estas lejos"
    elif int(rta) < numero and (resta<= 1 or resta >=20):
        mensaje = "El numero es mayor y estas muy cerca"
    elif int(rta) < numero and (resta <20 or resta >=60):
        mensaje = "El numero es mayor"
    elif int(rta) < numero and (resta <60 or resta >=99):
        mensaje = "El numero es mayor y estas lejos"
    elif int(rta) == numero:
        mensaje = f"Acertaste"
        socket_client.send(mensaje.encode())
        break
    else:
        print("Ninguno")

    socket_client.send(mensaje.encode())