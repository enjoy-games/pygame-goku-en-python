#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

# Variables.
personajeX = 45
personajeY = 45
salir = False

# Objetos
temporizador = pygame.time.Clock()

# Establezco la pantalla.
screen = pygame.display.set_mode((800,600))

# Establezco el título.
pygame.display.set_caption("Movimiento automático")

# Creo dos objetos surface.
fondo = pygame.image.load("Imagenes/fondo.jpg").convert()
personaje = pygame.image.load("Imagenes/goku.png").convert_alpha()
# .convert() convierten la superficie a un formato de color que permite imprimirlas mucho mas rápido.

# Imprimo las imágenes sobre la pantalla.
screen.blit(fondo, (0,0))
screen.blit(personaje, (personajeX,personajeY))
pygame.display.flip()


# Movimiento del personaje.
while not salir:
	personajeX += 10
        personajeY += 10

	if personajeX > 800:
		personajeX = -80

        if personajeY > 600:
		personajeY = -80

	screen.blit(personaje, (personajeX,personajeY))
	pygame.display.flip()
	temporizador.tick(60)

	screen.blit(fondo, (0,0))

	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			salir = True
