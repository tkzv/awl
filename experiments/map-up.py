#!/usr/bin/python3
import numpy as np
from PIL import Image

def fast_random( state ):
    state = state * 1664525 + 1013904223
    return state & 0x7fff

def fast_choice( state, sequence ): # в 3.9 раз быстрее random.choice()
    N = len( sequence )
    #value = (((state * 1664525 + 1013904223) & 0x7fff) * N) // 0x8000 # на 8% медленнее
    value = (((state * 1664525 + 1013904223) & 0x7fff) * N) >> 15
    #value = int((((state * 1664525 + 1013904223) & 0x7fff) * N) / 0x8000) # на 32% медленнее
    return sequence[value]

ar=[None]*8
ar[0] = np.asarray(Image.open('down1.png'))
#ar[0] = np.asarray(Image.open('down2.png'))

for p2 in range(1,8): #8
  ar[p2] = np.zeros( (ar[p2-1].shape[0]*2, ar[p2-1].shape[1]*2, ar[p2-1].shape[2] ), np.uint8 )
  # оригинал
  for x in   range(ar[p2-1].shape[0]):
    for y in range(ar[p2-1].shape[1]):
      ar[p2][x*2, y*2] = ar[p2-1][x,y]
  maxx, maxy = ar[p2].shape[:2]
  # центр
  for x in   range(1, maxx, 2):
    for y in range(1, maxy, 2):
      ar[p2][x,y] = fast_choice( x+y*maxy, (ar[p2][(x-1)%maxx,(y-1)%maxy], 
                                            ar[p2][(x+1)%maxx,(y-1)%maxy], 
                                            ar[p2][(x-1)%maxx,(y+1)%maxy], 
                                            ar[p2][(x+1)%maxx,(y+1)%maxy]) )
  # вертикальные рёбра
  for x in   range(0, maxx, 2):
    for y in range(1, maxy, 2):
      ar[p2][x,y] = fast_choice( x+y*maxy, (ar[p2][(x-1)%maxx,y], 
                                            ar[p2][(x+1)%maxx,y], 
                                            ar[p2][x,(y-1)%maxy], 
                                            ar[p2][x,(y+1)%maxy]) )
  # горизонтальные рёбра
  for x in   range(1, maxx, 2):
    for y in range(0, maxy, 2):
      ar[p2][x,y] = fast_choice( x+y*maxy, (ar[p2][(x-1)%maxx,y], 
                                            ar[p2][(x+1)%maxx,y], 
                                            ar[p2][x,(y-1)%maxy], 
                                            ar[p2][x,(y+1)%maxy]) )
  Image.fromarray( ar[p2], 'RGB' ).save( 'up-jan-' + str(p2) + '.png' )
  #Image.fromarray( ar[p2], 'RGB' ).save( 'up-jun-' + str(p2) + '.png' )
