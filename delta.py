#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# test.py
#  
#  Copyright 2018 username <username@zvorikin>
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
parser=argparse.ArgumentParser(description='Buld deltas .nec files.')
parser.add_argument('-f', '--freq', help='Destination freq to build antenna in MHz', \
    required=True, type=float)
parser.add_argument('-m', '--mast', help='Top point of antenna, mast hight in meters', \
    default=6, type=int)
parser.add_argument('-o', '--out', help='Filename to output .nec file', required=True)

args=parser.parse_args()

if args.freq>30:
    print 'Max freq is 30MHz now'
    sys.exit(1)
if args.mast>150:
    print 'How can you build such a tall mast??? Mail me, pls'
    sys.exit(1)

vlight=299792458
freq=args.freq*1000000
lambda1=vlight/freq
lambda4=lambda1/4

top_angle=90 #this will be in args in future
side_short=lambda4*1.24
top_angle_rad=math.radians(top_angle)

x=side_short*sin(top_angle_rad/2)
y=0
z=side_short*cos(top_angle_rad/2)

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

x=toFixed(x,3)
z=toFixed(z,3)

point_top[3]=[0,0,z]
point_side_left[3]=[x,0,0]
point_side_right[3]=[-x,0,0]




