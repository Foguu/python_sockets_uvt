import random
import socket

def server_program():
    host = socket.gethostname()  # Get the hostname of the server
    port = 5000  # Use a port number above 1024 to avoid reserved ports

    server_socket = socket.socket()  # Create a socket object
    server_socket.bind((host, port))  # Bind the socket to the host and port

    server_socket.listen(2)  # Listen for incoming connections
    conn, addr = server_socket.accept()  # Accept a connection from a client
    print('Connection from: ' + str(addr))

    while True:
        data = conn.recv(1024).decode()  # Receive data from the client
        if not data:
            break
        if data == 'attack':
            random_number = random.randint(1, 10)
            data = "your attack did " + str(random_number) + " damage(s)"
        else:
            print('from connected user: ' + data)
            data = input(' -> ')  # Take input from the server
        conn.send(data.encode())  # Send the response back to the client

    conn.close()  # Close the connection

if __name__ == '__main__':
    server_program()