import socket

socket_sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_sv.bind(("localhost", 8001))
socket_sv.listen(1)
socket_client, client_addr = socket_sv.accept()
while True:
    numero = int(input("Elija un numero del 1 al 100: "))
    if numero == "" or numero <= 0:
        continue
    else:
        break
while True:
    rta = socket_client.recv(1024).decode()
    print("El jugador elijio el numero: "+ str(rta))
    if int(rta) > numero:
        mensaje = "El numero es menor"
    elif int(rta) < numero:
        mensaje = "El numero es mayor"
    else:
        mensaje = f"Acertaste"
        socket_client.send(mensaje.encode())
        break

    socket_client.send(mensaje.encode())