import pygame
import sys
pygame.init()
#size
pantalla_x=800
pantalla_y=600
size = (pantalla_x,pantalla_y)
punto_x_circulo=250
punto_y_circulo=80
punto_x_cuadrado=pantalla_x//2
punto_y_cuadrado=400
clock= pygame.time.Clock()
#creas ventana de juegos

screen = pygame.display.set_mode(size)
color_rojo=(255,0,0)
color_verde=(0,255,0)
color_azul=(0,0,255)
color_blanco=(255,255,255)

while True:
    for  event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            sys.exit()

    screen.fill(color_azul)
    pygame.draw.line(screen,color_blanco,[0,0],[pantalla_x,pantalla_y],5)
    pygame.draw.rect(screen,color_verde,(pantalla_x//2,400,180,100))
    pygame.draw.circle(screen,color_azul,(punto_x_circulo,punto_y_circulo),50)
    punto_x_circulo += 5
    punto_y_cuadrado -= 5
    pygame.display.flip()
    #cantidad de fps
    clock.tick(20)
    pass
