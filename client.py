from re import S
import socket
import threading
from pygame import*
import pygame
pygame.init()

IP = socket.gethostbyname(socket.gethostname())
PORT = 5000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONECT_MSG = "!DISCONNECTED"
dimention = (340, 260)

class SNAKE:
    def __init__(self,x ,y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.move_left = False
        self.move_right = False
        
    def update(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.move_left = True
                    self.move_right = False
                if event.key == K_RIGHT:
                    self.move_left = False
                    self.move_right = True
        if self.move_left:
            self.x -= 2
        if self.move_right:
            self.x += 2
            
    def draw(self, surf):
        pygame.draw.rect(surf, self.color, (self.x, self.y, self.w, self.h))
  
def main():
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  window = pygame.display.set_mode(dimention)
  clock = pygame.time.Clock()
  font = pygame.font.Font(None, 20)
  fps = 30
  posX = 100
  posY=100
  
  snake = SNAKE(posX, posY, 10, 10, 'black')
  
  client.connect(ADDR)
  print(f"[CONNECTED] client is connected to server on {IP}:{PORT}")
  
  connected = True
  while connected:
      clock.tick(fps)
      snake.update()
      
      window.fill("green")
      snake.draw(window)
      
      message = font.render(f"X:{snake.x}", 1, "red")
      window.blit(message, (0,0))
      
      pygame.display.flip()
      client.send(f"{snake.x}".encode(FORMAT))
    
    #if msg == DISCONECT_MSG:
     #   connected = False
        
    #else:
     #   msg = client.recv(SIZE).decode(FORMAT)
      #  print(f"[SERVER] {msg}")
        

if __name__ == "__main__":
  main()
    
  
  

  
  


  