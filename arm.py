import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from matplotlib.widgets import Slider, TextBox


class Arm:
	def __init__(self, ax):
		#length of each link in mm.
		self.m_o = 123.0
		self.m_p = 40.86
		self.m_q = 44.83
		self.m_n = 17.5
		self.m_m = 131.34

		

		#angles in radians
		self.m_theta = 0
		self.m_a = 0
		self.m_b = 0
		self.m_psi = 0
		self.m_omega = 0
		self.m_gamma = 0

		self.ax = ax

		self.segment0 = self.plot_segment(self.ax, [0,0,0], [0,0,1])
		self.segment1 = self.plot_segment(self.ax, [0,0,0], [0,0,1])
		self.segment2 = self.plot_segment(self.ax, [0,0,0], [0,0,1])
		self.segment3 = self.plot_segment(self.ax, [0,0,0], [0,0,1])

		
	def plot_segment(self, ax, start_point, end_point):
		segment = ax.plot3D([start_point[0], end_point[0]], 
					[start_point[1], end_point[1]], 
					[start_point[2], end_point[2]], color='black')
		return segment

#		radius = 10
#		# Calculate the height and direction of the cylinder
#		direction = np.array(end_point) - np.array(start_point)
#		height = np.linalg.norm(direction)
#		direction = direction / height
#
#		# Create a grid for the cylinder
#		theta = np.linspace(0, 2 * np.pi, 100)
#		z = np.linspace(0, height, 100)
#		theta, z = np.meshgrid(theta, z)
#		x = radius * np.cos(theta)
#		y = radius * np.sin(theta)
#
#		# Calculate the rotation matrix
#		if direction[2] == 1:  # Special case where the direction is along z-axis
#		    R = np.eye(3)
#		else:
#		    a = np.cross([0, 0, 1], direction)
#		    a = a / np.linalg.norm(a)
#		    angle = np.arccos(direction[2])
#		    A = np.array([
#		        [0, -a[2], a[1]],
#		        [a[2], 0, -a[0]],
#		        [-a[1], a[0], 0]
#		    ])
#		    R = np.eye(3) + np.sin(angle) * A + (1 - np.cos(angle)) * np.dot(A, A)
#
#		# Rotate and translate the cylinder
#		xyz = np.array([x.flatten(), y.flatten(), z.flatten()])
#		rotated_xyz = np.dot(R, xyz).T
#		x_rot, y_rot, z_rot = rotated_xyz[:,0], rotated_xyz[:,1], rotated_xyz[:,2]
#
#		x_rot += start_point[0]
#		y_rot += start_point[1]
#		z_rot += start_point[2]
#
#		x_rot = x_rot.reshape(x.shape)
#		y_rot = y_rot.reshape(y.shape)
#		z_rot = z_rot.reshape(z.shape)
#
#		ax.plot_surface(x_rot, y_rot, z_rot, color='b', alpha=0.6, label='Cylinder')








	def draw(self):

		#The coordinate points for each joint in my drawing
		origin = [0, 0, 0]
		i = np.array([self.m_p*math.sin(self.m_theta)                               , self.m_p*math.cos(self.m_theta)                                , self.m_q                ])
		j = np.array([self.m_m*math.sin(self.m_a)*math.sin(self.m_theta)            , self.m_m*math.sin(self.m_a)*math.cos(self.m_theta)             , self.m_m*math.cos(self.m_a)    ]) + i
		k = np.array([self.m_n*math.sin(self.m_a+self.m_b)*math.sin(self.m_theta)   , self.m_n*math.sin(self.m_a+self.m_b)*math.cos(self.m_theta)    , self.m_n*math.cos(self.m_a+self.m_b)  ]) + j
		d = np.array([self.m_o*math.cos(self.m_a+self.m_b)*math.sin(self.m_theta)   , self.m_o*math.cos(self.m_a+self.m_b)*math.cos(self.m_theta)    , -self.m_o*math.sin(self.m_a+self.m_b) ]) + k

		#Draw a cylinder between each joint.
		self.segment0 = self.plot_segment(self.ax, origin, i)
		self.segment1 = self.plot_segment(self.ax, i, j)
		self.segment2 = self.plot_segment(self.ax, j, k)
		self.segment3 = self.plot_segment(self.ax, k, d)
		


	def clear(self):
		if self.segment0:
			self.segment0[0].remove()
		if self.segment1:
			self.segment1[0].remove()
		if self.segment2:
			self.segment2[0].remove()
		if self.segment3:
			self.segment3[0].remove()





