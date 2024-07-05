import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from matplotlib.widgets import Slider, TextBox


def sin(x):
	return math.sin(x)

def cos(x):
	return math.cos(x)

class Arm:
	def __init__(self, ax):
		
		#length of each link in mm. Same letter as the angle up until the next joint.
		self.A1 = 40.86
		self.A2 = 44.83
		self.B = 123.0
		self.C1 = 17.5
		self.C2 = 131.34
		self.D1 = 20 #need to measure
		self.D2 = 20 #need to measure
		self.E1 = 20 #need to measure
		self.E2 = 10 #need to measure
		self.F1 = 10 #need to measure
		self.F2 = 10 #need to measure

		#angles in radians
		self.a = 0
		self.b = 0
		self.c = 0
		self.d = 0
		self.e = 0
		self.f = 0

		self.ax = ax

		
		
	def plot_segment(self, ax, start_point, end_point):
		segment = ax.plot3D([start_point[0], end_point[0]], 
					[start_point[1], end_point[1]], 
					[start_point[2], end_point[2]], color='black')
		return segment

	def draw(self):
		#easier to not have to write "self." all the time...
		A1 = self.A1 
		A2 = self.A2 
		B = self.B
		C1 = self.C1 
		C2 = self.C2 
		D1 = self.D1
		D2 = self.D2
		E1 = self.E1 
		E2 = self.E2 
		F1 = self.F1 
		F2 = self.F2 
		a = self.a
		b = self.b
		c = self.c
		d = self.d
		e = self.e
		f = self.f

		#The coordinate points for each joint in my drawing
		#Each point is named after the segment beginning in it. If a segment consist of several rigid parts numbered it has numbers 1,2,3 etc.
		pO = [0, 0, 0]
		pA =  np.array([         A1*sin(a),       A1*cos(a),  A2       ])
		pB =   B*np.array([  sin(b)*sin(a),   sin(b)*cos(a),  cos(b)   ]) + pA
		pC1 = C1*np.array([sin(b+c)*sin(a), sin(b+c)*cos(a),  cos(b+c) ]) + pB
		pC2 = C2*np.array([cos(b+c)*sin(a), cos(b+c)*cos(a), -sin(b+c) ]) + pC1
		pD1 = -D1*np.array([(cos(d) + cos(b+c)*sin(a)*cos(b+c)*sin(a)*(1-cos(d)))*sin(b+c)*sin(a) + (cos(b+c)*sin(a)*cos(b+c)*cos(a)*(1-cos(d))+sin(b+c)*sin(d))*sin(b+c)*cos(a) + (cos(b+c)*sin(a)*(-sin(b+c))*(1-cos(d))+cos(b+c)*cos(a)*sin(d))*cos(b+c), (cos(b+c)*cos(a)*cos(b+c)*sin(a)*(1-cos(d))+(-sin(b+c))*sin(d))*sin(b+c)*sin(a) + (cos(d) + cos(b+c)*cos(a)*cos(b+c)*cos(a)*(1-cos(d)))*sin(b+c)*cos(a) + (cos(b+c)*cos(a)*(-sin(b+c))*(1-cos(d))-cos(b+c)*sin(a)*sin(d))*cos(b+c), ((-sin(b+c))*cos(b+c)*sin(a)*(1-cos(d))-cos(b+c)*cos(a)*sin(d))*sin(b+c)*sin(a) + ((-sin(b+c))*cos(b+c)*cos(a)*(1-cos(d))+cos(b+c)*sin(a)*sin(d))*sin(b+c)*cos(a) + (cos(d) + (-sin(b+c))*(-sin(b+c))*(1-cos(d)))*cos(b+c)]) + pC2
		pD2 = pD1 + 10*np.array([cos(b+c)*sin(a), cos(b+c)*cos(a), -sin(b+c) ])
		

		#TODO
		#I want to rotate around vec_C2D1
		vec_C2D1 = pD1 - pC2
		#The vector I want to rotate is 
		vec_D1D2 = np.array([cos(b+c)*sin(a), cos(b+c)*cos(a), -sin(b+c) ])



		#Draw a cylinder between each joint.
		self.segment0 = self.plot_segment(self.ax, pO, pA)
		self.segment1 = self.plot_segment(self.ax, pA, pB)
		self.segment2 = self.plot_segment(self.ax, pB, pC1)
		self.segment3 = self.plot_segment(self.ax, pC1, pC2)
		self.segment4 = self.plot_segment(self.ax, pC2, pD1)
		self.segment5 = self.plot_segment(self.ax, pD1, pD2)
		


	def clear(self):
		self.segment0[0].remove()
		self.segment1[0].remove()
		self.segment2[0].remove()
		self.segment3[0].remove()
		self.segment4[0].remove()
		self.segment5[0].remove()


















#Rotation matrix around ux,uy,uz unit vector, angle t
	#[ cos(t) + ux*ux*(1-cos(t))  ,   ux*uy*(1-cos(t))-uz*sin(t) ,  ux*uz*(1-cos(t))+uy*sin(t)]
	#[ uy*ux*(1-cos(t))+uz*sin(t) ,   cos(t) + uy*uy*(1-cos(t))  ,  uy*uz*(1-cos(t))-ux*sin(t)]
	#[ uz*ux*(1-cos(t))-uy*sin(t) ,   uz*uy*(1-cos(t))+ux*sin(t) ,   cos(t) + uz*uz*(1-cos(t))]


#Rotation matrix around 
	#ux = cos(b+c)*sin(a)
	#uy = cos(b+c)*cos(a)
	#uz = -sin(b+c)
	#[ cos(t) + cos(b+c)*sin(a)*cos(b+c)*sin(a)*(1-cos(t))  ,   cos(b+c)*sin(a)*cos(b+c)*cos(a)*(1-cos(t))+sin(b+c)*sin(t) ,  cos(b+c)*sin(a)*(-sin(b+c))*(1-cos(t))+cos(b+c)*cos(a)*sin(t)]
	#[ cos(b+c)*cos(a)*cos(b+c)*sin(a)*(1-cos(t))+(-sin(b+c))*sin(t) ,   cos(t) + cos(b+c)*cos(a)*cos(b+c)*cos(a)*(1-cos(t))  ,  cos(b+c)*cos(a)*(-sin(b+c))*(1-cos(t))-cos(b+c)*sin(a)*sin(t)]
	#[ (-sin(b+c))*cos(b+c)*sin(a)*(1-cos(t))-cos(b+c)*cos(a)*sin(t) ,   (-sin(b+c))*cos(b+c)*cos(a)*(1-cos(t))+cos(b+c)*sin(a)*sin(t) ,   cos(t) + (-sin(b+c))*(-sin(b+c))*(1-cos(t))]





































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


