import socket
import threading
from tkinter import *
from xmlrpc import client

def send(listv, entry):
    message = entry.get()
    listv.insert(END, "Server : " + message)
    entry.delete(0, END)
    client.send(bytes(message, "utf-8"))
    receive(listv)

def receive(listv):
    from_client = client.recv(50)
    listv.insert(END, "Client : " + from_client.decode("utf-8"))
    print(from_client.decode("utf-8"))

def handle_connection():
    global client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST_NAME = socket.gethostname()
    PORT = 2468
    s.bind((HOST_NAME, PORT))
    s.listen(4)
    client, address = s.accept()
    print("Connected to", address)

root = Tk()

entry = Entry()
entry.pack(side = BOTTOM)

listv = Listbox(root)
listv.pack()

button = Button(root, text="Send", command=lambda: send(listv, entry))
button.pack(side=BOTTOM)

rbutton = Button(root, text="Receive", command=lambda: receive(listv))
rbutton.pack(side=BOTTOM)

root.title("Server")
root.geometry("300x300")

# Start socket connection in a separate thread
threading.Thread(target=handle_connection, daemon=True).start()

root.mainloop()