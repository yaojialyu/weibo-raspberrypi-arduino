import pygame

import pygame.camera

from pygame.locals import *

pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()

image = cam.get_image()

pygame.image.save(image, 'image.jpg')

cam.stop()
