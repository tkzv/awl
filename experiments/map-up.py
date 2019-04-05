#!/usr/bin/python3
import numpy as np
from PIL import Image
import random

ar=[None]*8
#ar[0] = np.asarray(Image.open('down1.png'))
ar[0] = np.asarray(Image.open('down2.png'))
#random.seed(1)

for p2 in range(1,8): #8
  #random.seed(p2)
  ar[p2] = np.zeros( (ar[p2-1].shape[0]*2, ar[p2-1].shape[1]*2, ar[p2-1].shape[2] ), np.uint8 )
  # оригинал
  for x in   range(ar[p2-1].shape[0]):
    for y in range(ar[p2-1].shape[1]):
      ar[p2][x*2, y*2] = ar[p2-1][x,y]
  maxx, maxy = ar[p2].shape[:2]
  # центр
  for x in   range(1, maxx, 2):
    for y in range(1, maxy, 2):
      random.seed( x+y*maxy )
      ar[p2][x,y] = random.choice( (ar[p2][(x-1)%maxx,(y-1)%maxy], 
                                    ar[p2][(x+1)%maxx,(y-1)%maxy], 
                                    ar[p2][(x-1)%maxx,(y+1)%maxy], 
                                    ar[p2][(x+1)%maxx,(y+1)%maxy]) )
  # вертикальные рёбра
  for x in   range(0, maxx, 2):
    for y in range(1, maxy, 2):
      random.seed( x+y*maxy )
      ar[p2][x,y] = random.choice( (ar[p2][(x-1)%maxx,y], 
                                    ar[p2][(x+1)%maxx,y], 
                                    ar[p2][x,(y-1)%maxy], 
                                    ar[p2][x,(y+1)%maxy]) )
  # горизонтальные рёбра
  for x in   range(1, maxx, 2):
    for y in range(0, maxy, 2):
      random.seed( x+y*maxy )
      ar[p2][x,y] = random.choice( (ar[p2][(x-1)%maxx,y], 
                                    ar[p2][(x+1)%maxx,y], 
                                    ar[p2][x,(y-1)%maxy], 
                                    ar[p2][x,(y+1)%maxy]) )
  #Image.fromarray( ar[p2], 'RGB' ).save( 'up-jan-' + str(p2) + '.png' )
  Image.fromarray( ar[p2], 'RGB' ).save( 'up-jun-' + str(p2) + '.png' )
