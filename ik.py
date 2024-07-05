import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_cylinder(ax, start_point, end_point, radius):
    # Calculate the height and direction of the cylinder
    direction = np.array(end_point) - np.array(start_point)
    height = np.linalg.norm(direction)
    direction = direction / height
    
    # Create a grid for the cylinder
    theta = np.linspace(0, 2 * np.pi, 100)
    z = np.linspace(0, height, 100)
    theta, z = np.meshgrid(theta, z)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    # Calculate the rotation matrix
    if direction[2] == 1:  # Special case where the direction is along z-axis
        R = np.eye(3)
    else:
        a = np.cross([0, 0, 1], direction)
        a = a / np.linalg.norm(a)
        angle = np.arccos(direction[2])
        A = np.array([
            [0, -a[2], a[1]],
            [a[2], 0, -a[0]],
            [-a[1], a[0], 0]
        ])
        R = np.eye(3) + np.sin(angle) * A + (1 - np.cos(angle)) * np.dot(A, A)
    
    # Rotate and translate the cylinder
    xyz = np.array([x.flatten(), y.flatten(), z.flatten()])
    rotated_xyz = np.dot(R, xyz).T
    x_rot, y_rot, z_rot = rotated_xyz[:,0], rotated_xyz[:,1], rotated_xyz[:,2]
    
    x_rot += start_point[0]
    y_rot += start_point[1]
    z_rot += start_point[2]
    
    x_rot = x_rot.reshape(x.shape)
    y_rot = y_rot.reshape(y.shape)
    z_rot = z_rot.reshape(z.shape)
    
    ax.plot_surface(x_rot, y_rot, z_rot, color='b', alpha=0.6, label='Cylinder')

def main():
    start_point = [0, 0, 0]
    end_point = [0, 0, 10]
    radius = 2
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    plot_cylinder(ax, start_point, end_point, radius)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Cylinder')

    # Add a legend with variable names
    #ax.legend(["θ", "α", "β", "ψ", "ω", "γ"], loc='upper right')
    
    plt.show()

if __name__ == "__main__":
    main()
