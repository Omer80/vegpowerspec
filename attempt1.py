#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  attempt1.py
#  
#  Copyright 2015 Ohm <ohm@ohm-S400CA>
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
__version__=1.0
__author__ = """Omer Tzuk (cliffon@gmail.com)"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)


def main():
	#space = np.random.randint(2, size=(1000,1000))
	N = int(10) 
	space = np.zeros((N, N), dtype=np.uint8)
	#print space
	x, y = np.random.randint(N, size=(2, 100))
	#print x,y
	space[x, y] += 1
	#print space
	
	# plot first frame (t=start)
	plt.ion()
	plt.clf()
	ext = [0,N,0,N]
	im=plt.imshow(space,origin='lower', interpolation='nearest', extent=ext, cmap='Greens')
	cbar=plt.colorbar()
	title=plt.title('Vegetation patches')
	plt.draw()
	
	while True:
		im.set_data(space)
		im.figure.canvas.draw()
		

	
	space_ps = np.abs(np.fft.fftn(space))
	space_ps *= space_ps
	space_ac = np.fft.ifftn(space_ps).real.round()
	space_ac /= space_ac[0, 0]
	
	dist = np.minimum(np.arange(N), np.arange(N, 0, -1))
	dist *= dist
	dist_2d = np.sqrt(dist[:, None] + dist)
	distances, _ = np.unique(dist_2d, return_inverse=True)
	values = np.bincount(_, weights=space_ac.ravel()) / np.bincount(_)
	
	#plt.plot(distances[1:], values[1:])
	#im.set_data(space)
	#im.figure.canvas.draw()
	

if __name__ == '__main__':
	main()

