#!/usr/bin/python3
from PIL import Image
import numpy as np
scale = 100

jan = Image.open('world.topo.bathy.200401.3x5400x2700.png')
jul = Image.open('world.topo.bathy.200407.3x5400x2700.png')
print(jan, jul)
ar1 = np.asarray(jan)
ar2 = np.asarray(jul)

sieved1 = ar1[ [ i for i in range(0, ar1.shape[0], scale) ] ] [ :, [ j for j in range(0, ar1.shape[1], scale)] ]
sieved2 = ar2[ [ i for i in range(0, ar2.shape[0], scale) ] ] [ :, [ j for j in range(0, ar2.shape[1], scale)] ]

#pic1 = Image.frombuffer( 'RGB', (sieved1.shape[0], sieved1.shape[1]), sieved1, 'raw', 'RGB', 0, 1 )
pic1 = Image.fromarray( sieved1, 'RGB' )
pic2 = Image.fromarray( sieved2, 'RGB' )

pic1.save('down1.png')
pic2.save('down2.png')
