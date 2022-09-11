import socket
import pyttsx3

engine = pyttsx3.init()
soke = socket.socket()

soke.bind(("192.168.137.75", 8000))

soke.listen(5)

while True:
    conexion, addrs = soke.accept()
    engine.say("Conexion realizada en", str(addrs))
    engine.runAndWait()
    mensaje = "Saludo desde el servidor"
    conexion.send(mensaje.encode("utf-8"))
    recibido = conexion.recv(1024)
    print(recibido)
    print(type(recibido))
    conexion.close()
