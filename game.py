#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from pygame.sprite import Sprite

class Personaje(Sprite):
	def __init__(self):
		self.image = personaje = pygame.image.load("Imagenes/goku.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(50, 300)
	def update(self):
		teclas = pygame.key.get_pressed()
		if teclas[K_SPACE]:
			self.image = personaje = pygame.image.load("Imagenes/gokukamehameha.png").convert_alpha()
		elif kamehameha.rect.x > 860:
			self.image = personaje = pygame.image.load("Imagenes/goku.png").convert_alpha()

		if teclas[K_LEFT]:
			self.image = personaje = pygame.image.load("Imagenes/gokuleft.png").convert_alpha()
			if self.rect.x > 0:
				self.rect.x -= 10
		elif teclas[K_RIGHT]:
			self.image = personaje = pygame.image.load("Imagenes/gokuright.png").convert_alpha()
			if self.rect.x < 740:
				self.rect.x += 10

		if teclas[K_UP]:
			self.image = personaje = pygame.image.load("Imagenes/gokuup.png").convert_alpha()
			if self.rect.y > 0:
				self.rect.y -= 10
		elif teclas[K_DOWN]:
			if self.rect.y < 530:
				self.image = personaje = pygame.image.load("Imagenes/gokudown.png").convert_alpha()
				self.rect.y += 10

class Kamehameha(Sprite):
	def __init__(self):
		self.image = kamehameha = pygame.image.load("Imagenes/kamehameha.gif").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(900, 700)
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.rect.x > 840:
			if teclas[K_SPACE]:
				self.rect.x = (personaje.rect.x + 60)
				self.rect.y = (personaje.rect.y + 14)
		if self.rect.x < 870:
			self.rect.x += 20
			

if __name__ == '__main__':
	# Variables.
	salir = False

	# Establezco la pantalla.
	screen = pygame.display.set_mode((800,600))

	# Establezco el título.
	pygame.display.set_caption("Mejor kamehameha")

	# Creo do objeto surface.
	fondo = pygame.image.load("Imagenes/fondo.jpg").convert()
	# .convert() convierten la superficie a un formato de color que permite imprimirlas mucho mas rápido.

	# Objetos
	temporizador = pygame.time.Clock()
	personaje = Personaje()
	kamehameha = Kamehameha()

	# Movimiento del personaje.
	while not salir:
		personaje.update()
		kamehameha.update()

		# actualizacion grafica
		screen.blit(fondo, (0, 0))
		screen.blit(personaje.image, personaje.rect)
		screen.blit(kamehameha.image, kamehameha.rect)
		pygame.display.flip()

		temporizador.tick(60)
		# gestion de eventos
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				salir = True
