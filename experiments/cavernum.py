#!/usr/bin/python3
from PIL import Image
from sys import argv
#import time

floor = [ l.split() for l in open( argv[1], 'rt' ).read().splitlines() ]
walls = [ l.split() for l in open( argv[2], 'rt' ).read().splitlines() ]
#objcs = [ l.split() for l in open( argv[3], 'rt' ).read().splitlines() ]
#peopl = [ l.split() for l in open( argv[4], 'rt' ).read().splitlines() ]

ip = '/home/user/caves/Graphics/'
d = {
'wallew'    : { 'fn': ip+'G2370.png', 'x':1,      'y':373, 'w':64, 'h':92 },
'wallns'    : { 'fn': ip+'G2370.png', 'x':66,     'y':373, 'w':64, 'h':92 },
'floor0'    : { 'fn': ip+'G1350.png', 'x':65*0+1, 'y':1,   'w':64, 'h':44 },
'floor1'    : { 'fn': ip+'G1350.png', 'x':65*1+1, 'y':1,   'w':64, 'h':44 },
'floor2'    : { 'fn': ip+'G1350.png', 'x':65*2+1, 'y':1,   'w':64, 'h':44 },
'floor3'    : { 'fn': ip+'G1350.png', 'x':65*3+1, 'y':1,   'w':64, 'h':44 },
'floor4'    : { 'fn': ip+'G1350.png', 'x':65*4+1, 'y':1,   'w':64, 'h':44 },
'floor5'    : { 'fn': ip+'G1350.png', 'x':65*5+1, 'y':1,   'w':64, 'h':44 },
'floor6'    : { 'fn': ip+'G1350.png', 'x':65*6+1, 'y':1,   'w':64, 'h':44 },
'empty'     : { 'fn': ip+'G2370.png', 'x':2,      'y':2,   'w':1,  'h':1  },
'_'         : { 'fn': ip+'G2370.png', 'x':2,      'y':2,   'w':1,  'h':1  }
}

#t0 = time.perf_counter()
usf = {} # unique sprite files
for e in d:
    ident = d[e]['fn'] + ' ' + str(d[e]['x']) + ' ' + str(d[e]['y']) + ' ' + str(d[e]['w']) + ' ' + str(d[e]['h'])
    d[e]['uid'] = ident
    usf[ ident ] = None
for uid in usf:
    for e in d:
        if d[e]['uid'] == uid:
            break
    usf[ uid ] = Image.open( d[e]['fn'], mode = 'r' ).crop( (d[e]['x'], d[e]['y'], d[e]['x']+d[e]['w'], d[e]['y']+d[e]['h']) )
for e in d:
    d[e]['image'] = usf[ d[e]['uid'] ]
#t1 = time.perf_counter()
#print( 'build buffer:', t1-t0 )

#t0 = time.perf_counter()
maxcol = max( max(len(row) for row in floor), max(len(row) for row in walls) )
maxrow = max( len( floor ), len( walls ) )
maxall = max( maxrow, maxcol )
maxh = max( d[e]['h'] for e in d )
#t1 = time.perf_counter()
#print( 'findmax:', t1-t0 )
cc, rc = maxcol//2, maxrow//2 # central tile
xs, ys = 32, 22    # step for sprite
xi, yi = 640, 480  # image size
xd, yd = 0, 0      # displace center

img = Image.new( 'RGBA', (xi, yi) )
'''
for row in range(len(floor)):
    for col in range(len(floor[row])):
        lc = floor[row][col].lower()
        img.alpha_composite( d[lc]['image'], ( xi//2 + ( col-cc)*xs + (row-rc)*xs + xd, yi//2 + (-col-cc)*ys + (row-rc)*ys + yd ) )
'''
for limit in range( maxall*2 + 2 ): 
    for e in range( limit + 1):
        col, row = maxcol - limit + e, e
        xd, yd = 0, maxh-44 #-44
        xy = ( xi//2 + ( col-cc)*xs + (row-rc)*xs + xd, 
               yi//2 + (-col-cc)*ys + (row-rc)*ys + yd )
        if (0 <= row < len(floor)) and (0 <= col < len(floor[row]) ):
            lc = floor[row][col].lower()
            #TODO: alpha_composite can't handle negative coordinates
            img.alpha_composite( d[lc]['image'], xy )
        xd, yd = 0, 0 # maxh-92 44-92
        xy = ( xi//2 + (col-cc)*xs + (row-rc)*xs + xd, yi//2 + (-col-cc)*ys + (row-rc)*ys + yd )
        if (0 <= row < len(walls) ) and (0 <= col < len(walls[row]) ):
            lc = walls[row][col].lower()
            img.alpha_composite( d[lc]['image'], xy )
img.show()
