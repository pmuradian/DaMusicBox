#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import pygame

class Sound:
    id = ""
    path = ""
    speed = 0
    volume = 0

    def __init__(self, i, p, s, v):
        self.id = i
        self.path = p
        self.speed = s
        self.volume = v

path2 = "/home/pi/Documents/drum_2.wav"
path3 = "/home/pi/Documents/drum_3.wav"

soundList = [Sound(0, "/home/pi/Documents/drum_2.wav", 0.0, 2),
        Sound(1, "/home/pi/Documents/drum_2.wav", 0.0, 2),
        Sound(2, "/home/pi/Documents/drum_3.wav", 0.0, 3), 
        Sound(3, "/home/pi/Documents/drum_2.wav", 0.5, 2), 
        Sound(4, "/home/pi/Documents/drum_3.wav", 0.0, 2), 
        Sound(5, "/home/pi/Documents/drum_2.wav", 0.0, 3)]

speed1 = 0.2
speed2 = 0.5
speed3 = 0.8
speed4 = 1

pygame.mixer.init()

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)

channel1.set_volume(0.9)
channel2.set_volume(0.6)
channel3.set_volume(0.3)


while True:
    for s in soundList:
        snd = pygame.mixer.Sound(s.path)
        pygame.mixer.Channel(s.volume).play(snd)
        time.sleep(snd.get_length())
        #time.sleep(s.speed)
