import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from matplotlib.widgets import Slider, TextBox
from arm import Arm
import threading
import time
from scipy.optimize import root


def createPlot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-200, 200])
    ax.set_ylim([-100, 300])
    ax.set_zlim([-100, 300])
    ax.view_init(elev=0, azim=0)

    return ax


def update(val):
        print("update called")
        print(val)
        #new_theta = s_theta.val
        #new_a = s_a.val
        #new_b = s_b.val
        #ax.clear()
        #drawArm(theta,a,b,psi,omega,gamma)

ax = createPlot()
arm = Arm(ax)
arm.draw()


def updateA(val):
        arm.a = val*np.pi/180
        arm.clear()
        arm.draw()

def updateB(val):
        arm.b = val*np.pi/180
        arm.clear()
        arm.draw()

def updateC(val):
        arm.c = val*np.pi/180
        arm.clear()
        arm.draw()

def updateD(val):
        arm.d = val*np.pi/180
        arm.clear()
        arm.draw()

def updateE(val):
        arm.e = val*np.pi/180
        arm.clear()
        arm.draw()

def updateF(val):
        arm.f = val*np.pi/180
        arm.clear()
        arm.draw()

def setUpPlot():
     # Create sliders
    ax_a = plt.axes([0.1 , 0.01, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_b = plt.axes([0.55, 0.01, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_c = plt.axes([0.1 , 0.05, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_d = plt.axes([0.55, 0.05, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_e = plt.axes([0.1 , 0.09, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_f = plt.axes([0.55, 0.09, 0.35, 0.03], facecolor='lightgoldenrodyellow')

    s_a = Slider(ax_a, 'a', -180, 180, valinit=0)
    s_b = Slider(ax_b, 'b', -180, 180, valinit=-60)
    s_c = Slider(ax_c, 'c', -180, 180, valinit=60)
    s_d = Slider(ax_d, 'd', -180, 180, valinit=0)
    s_e = Slider(ax_e, 'e', -180, 180, valinit=0)
    s_f = Slider(ax_f, 'f', -180, 180, valinit=0)

    s_a.on_changed(updateA)
    s_b.on_changed(updateB)
    s_c.on_changed(updateC)
    s_d.on_changed(updateD)
    s_e.on_changed(updateE)
    s_f.on_changed(updateF)
 
    plt.show()




def system_of_equations(vars):
    a, b, c, d, e ,f = vars
    return  getEndEffectorCoordinates(a,b,c,d,e,f) - [arm.x, arm.y, arm.z, arm.alpha, arm.beta, arm.gamma]





def solveInverseKinematics():
    

    initial_guess = [-10.0, 222.2 , 175.33, np.pi/2, 0, 0]
    solution = root(system_of_equations, initial_guess, method='hybr')
    print(solution)


def main():
    
    #x = threading.Thread(target=solveInverseKinematics)
    #x.start()

    #The desired location is set in the arm class directly.
    arm.x = -10.0
    arm.y = 222.2 
    arm.z = 175.33
    arm.alpha = np.pi/2
    arm.beta = 0
    arm.gamma = 0


    start_time = time.time()  # Record the start time
    solveInverseKinematics()
    end_time = time.time()    # Record the end time

    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print(f"Function call took {elapsed_time:.6f} seconds")




    

    #setUpPlot()

    

    



if __name__ == "__main__":
    main()













