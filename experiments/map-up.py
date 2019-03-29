#!/usr/bin/python3
import numpy as np
from PIL import Image
import random

ar=[None]*8
#ar[0] = np.asarray(Image.open('down1.png'))
ar[0] = np.asarray(Image.open('down2.png'))
#random.seed(1)

def pick( array, nodes ):
  sequence = []
  for n in nodes:
    try:
      sequence.append( array[n[0],n[1]] )
    except:
      continue
  return random.choice( sequence ) 
 
for p2 in range(1,8): #8
  random.seed(p2)
  ar[p2] = np.zeros( (ar[p2-1].shape[0]*2, ar[p2-1].shape[1]*2, ar[p2-1].shape[2] ), np.uint8 )
  # оригинал
  for x in range(ar[p2-1].shape[0]):
    for y in range(ar[p2-1].shape[1]):
      ar[p2][x*2, y*2] = ar[p2-1][x,y]
  # центр
  for x in range(1, ar[p2].shape[0]-1, 2):
    for y in range(1, ar[p2].shape[1]-1, 2):
      ar[p2][x,y] = random.choice( (ar[p2][x-1,y-1], ar[p2][x+1,y-1], ar[p2][x-1,y+1], ar[p2][x+1,y+1]) )
      #ar[p2][x,y] = pick( ar[p2], ( [x-1,y-1], [x+1,y-1], [x-1,y+1], [x+1,y+1] ) )
  # рёбра
  for x in range(0, ar[p2].shape[0], 2):
    for y in range(1, ar[p2].shape[1], 2):
      # ar[p2][x,y] = random.choice( ar[p2][x-1,y-1], ar[p2][x+1,y-1], ar[p2][x-1,y+1], ar[p2][x+1,y+1] )
      ar[p2][x,y] = pick( ar[p2], ([x-1,y], [x+1,y], [x,y+1], [x,y-1] ) )
  for x in range(1, ar[p2].shape[0], 2):
    for y in range(0, ar[p2].shape[1]-1, 2):
      #ar[p2][x,y] = random.choice( ar[p2][x-1,y-1], ar[p2][x+1,y-1], ar[p2][x-1,y+1], ar[p2][x+1,y+1] )
      ar[p2][x,y] = pick( ar[p2], ([x-1,y], [x+1,y], [x,y+1], [x,y-1] ) )
  #Image.fromarray( ar[p2], 'RGB' ).save( 'up-jan-' + str(p2) + '.png' )
  Image.fromarray( ar[p2], 'RGB' ).save( 'up-jun-' + str(p2) + '.png' )
