import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 5000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONECT_MSG = "!DISCONNECTED"


def handle_client(conn, addr):
  print(f"[NEW CONNECTION] {addr} connected")
  
  connected = True
  while connected:
    msg = conn.recv(SIZE).decode(FORMAT)
    print(msg)
    if msg == DISCONECT_MSG:
      connected = False
      
    print(f"[{addr}] {msg}")
    msg = f"Msg received: {msg}"
    conn.sendall(msg.encode(FORMAT))

def main():
  print("Server is starting...")
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(ADDR)
  server.listen()
  print(f"[LISTERNING] Server is listening on {IP}:{PORT}")
 
  while True:
    conn, addr = server.accept()
    thread = threading.Thread(target = handle_client, args = (conn,addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] (threading.activeCount() . 1)")

    
  
if __name__ == "__main__":
  main()
  
  


  