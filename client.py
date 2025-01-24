import random
import socket

def client_program():
    host = socket.gethostname()  # Get the hostname of the server
    port = 5000  # Use a port number above 1024 to avoid reserved ports

    client_socket = socket.socket()  # Create a socket object
    client_socket.connect((host, port))  # Connect to the server

    message = input(" -> ")  # Take input from the user

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # Send the message to the server
        data = client_socket.recv(1024).decode()  # Receive the response from the server
        print('Received from server: ' + data)  # Print the response to the terminal
        message = input(" -> ")  # Take input again

    client_socket.close()  # Close the connection

if __name__ == '__main__':
    client_program()