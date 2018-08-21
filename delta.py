#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test.py
#  
#  Copyright 2018 redbobcat <redbobcat@yandex.ru>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import argparse, sys, math

#parse arguments, very usefull module
parser=argparse.ArgumentParser(description='Buld deltas .nec files.')
parser.add_argument('-f', '--freq', help='Destination freq to build antenna in MHz', \
    required=True, type=float)
parser.add_argument('-m', '--mast', help='Top point of antenna, mast hight in meters', \
    default=6, type=float)
parser.add_argument('-o', '--out', help='Filename to output .nec file', required=True)
parser.add_argument('-a', '--angle', help='Top wire angle in degs', default=90, type=int)
parser.add_argument('--shorten', help='Coefficent of wire shortening', default=1.00)
args=parser.parse_args()

#errors check
if args.freq>30:
    print ('Max freq is 30MHz now')
    sys.exit(1)
if args.mast>150:
    print ('How can you build such a tall mast??? Mail me, pls')
    sys.exit(1)
if args.angle>180:
    print ('This is not a delta anymore')
    sys.exit(1)

#calculate lambda
vlight=299792458
freq=args.freq*1000000
lambda1=vlight*args.shorten/freq

lambda4=lambda1/4

#calculate lenght of the 
side_short=lambda4*1.24
top_angle_rad=math.radians(args.angle)

x=side_short*math.sin(top_angle_rad/2)
y=0
z=side_short*math.cos(top_angle_rad/2)



x=round(x,3)
z=round(z,3)

#
point_top=[]
point_left=[]
point_right=[]
point_top=[0,0,z]
point_left=[x,0,0]
point_right=[-x,0,0]

#tight up antenna to the top of the mast
add_hight=round((args.mast-z),3)

point_top[2]+=add_hight
point_left[2]+=add_hight
point_right[2]+=add_hight

#feedpoint in 1/4 wavelenght, aprox 4/5 from top end
#50 segments, and EX is 40 segs from the top
segments=51
feedpint=11

#let's look to the points
print (point_top)
print (point_left)
print (point_right)



