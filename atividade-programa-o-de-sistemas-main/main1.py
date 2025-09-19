import pygame

#inicializando o Pygame
pygame.init()

#Definindo o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.displayset_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Janela Simples")

#Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
#Atualizar a tela
    pygame.display.flip()

#Finalizar o pygame
pygame.QUIT()
