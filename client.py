import socket
import pickle
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect(("localhost", 8001))
print("Esperando a que el jugador 1 elija un numero")
host_response = socket_client.recv(1024)
host_response = pickle.loads(host_response)
print("Intenta adivinar el numero elegido por el servidor")
while True:
    mensaje = str(input("Vos: "))
    socket_client.send(mensaje.encode())
    rta = socket_client.recv(1024).decode()
    print("Servidor: "+ str(rta))
    if str(rta) == "Acertaste":
        break
socket_client.close()