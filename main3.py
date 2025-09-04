import pygame
import os

#Inicializando o Pygame
pygame.init()

#Definindo o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mover imagem com as setas")

#Definindo a cor de fundo
BG_COLOR = (30,30,40) #cor de fundo (preto)

#Carregar a imagem
image_file = "burro-removebg-preview.png" #coloque o nome da foto aqui
if os.path.exists(image_file):
  img = pygame.image.load(image_file).convert_alpha() 
  img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2)) #Centraliza a imagem
else:
    print("Imagem não encontrada!")

#Velocidade do movimento
speed = 1

#Loop principal do jogo
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = FALSE

#pega as teclas pressionadas
keys = pygame.key.get_pressed()

#movimentação da imagem
 # tem que adicionar as keys aqui !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Preencher o fundo
screen.fill(BG_COLOR)

#Desenhar a imagem na tela
screen.blit(img, img_rect.topleft)

#Atualizar a tela
pygame.display.flip()

#Finalizar o game
pygame.quit()

      
  
