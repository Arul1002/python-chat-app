🖧 Python Chat App (Server-Client GUI)
A simple Python-based chat application using sockets and Tkinter for GUI. This project demonstrates basic client-server communication over TCP with a graphical interface for sending and receiving messages.

📁 Project Structure
Code
chat-app/
├── server.py   # Server-side GUI application
├── client.py   # Client-side GUI application
└── README.md   # Project documentation
🚀 Features
Real-time message exchange between server and client

GUI interface built with Tkinter

Multi-threaded server to handle connections without freezing the UI

Simple and intuitive layout for chat interaction

🛠 Requirements
Python 3.x

No external libraries required (uses built-in socket, threading, and tkinter)

📦 Installation
Clone the repository:

bash
git clone https://github.com/your-username/chat-app.git
cd chat-app
Run the server:

bash
python server.py
Run the client (in a separate terminal or machine):

bash
python client.py
⚠️ Both server and client must run on the same network for successful connection.

🧠 How It Works
The server listens on a specified port (2468) and waits for a client to connect.

Once connected, both applications can send and receive messages using TCP sockets.

Messages are displayed in a listbox, and users can type and send messages using the entry field.

🐞 Known Issues
The xmlrpc.client import is unused and can be removed.

The client script incorrectly tries to accept() a connection after already connecting. This line should be removed:

python
Server = s.accept()[0]
Error handling for socket disconnection is not implemented.

Only one client can connect at a time.

✅ To Do
Add support for multiple clients

Improve error handling and connection feedback

Enhance UI with scrollbars and timestamps

Package as a standalone executable

📄 License
This project is licensed under the MIT License. Feel free to use and modify it.
