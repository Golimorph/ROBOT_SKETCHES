import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from matplotlib.widgets import Slider, TextBox
from arm import Arm
import threading
import time
from scipy.optimize import least_squares
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

ax = createPlot()
arm = Arm(ax)
arm.draw()

def system_of_equations(vars):
    a, b, c, d, e ,f = vars
    X = arm.getEndEffectorCoordinates(a,b,c,d,e,f)
    return  [X[0]- arm.x, X[1] - arm.y, X[2]- arm.z, X[3] - arm.alpha, X[4] - arm.beta, X[5] - arm.gamma]

def solveInverseKinematics():
    
    initial_guess = [arm.a, arm.b , arm.c, arm.d, arm.e, arm.f]
    solution = root(system_of_equations, initial_guess, method='hybr')

    arm.a = solution.x[0]
    arm.b = solution.x[1]
    arm.c = solution.x[2]
    arm.d = solution.x[3]
    arm.e = solution.x[4]
    arm.f = solution.x[5]


#def solveInverseKinematics():
#
#    initial_guess = [arm.a, arm.b , arm.c, arm.d, arm.e, arm.f]
#    lower_bounds = [-np.pi/2,-np.pi/2, -np.pi/2, -np.pi/2, -np.pi/2, -np.pi/2]
#    upper_bounds = [np.pi/2 , np.pi/2,  np.pi/2,  np.pi/2,  np.pi/2,  np.pi/2]
#    solution = least_squares(system_of_equations, initial_guess, bounds=(lower_bounds, upper_bounds))    
#    arm.a = solution.x[0]
#    arm.b = solution.x[1]
#    arm.c = solution.x[2]
#    arm.d = solution.x[3]
#    arm.e = solution.x[4]
#    arm.f = solution.x[5]






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

def updateX(val):
    arm.x = val
    solveInverseKinematics()
    arm.clear()
    arm.draw()

def updateY(val):
    arm.y = val
    solveInverseKinematics()
    arm.clear()
    arm.draw()

def updateZ(val):
    arm.z = val
    solveInverseKinematics()
    arm.clear()
    arm.draw()

def updateAlpha(val):
    arm.alpha = val*np.pi/180
    solveInverseKinematics()
    arm.clear()
    arm.draw()

def updateBeta(val):
    arm.beta = val*np.pi/180
    solveInverseKinematics()
    arm.clear()
    arm.draw()

def updateGamma(val):
    arm.gamma = val*np.pi/180
    solveInverseKinematics()
    arm.clear()
    arm.draw()     




def setUpPlot():
     # Create sliders
    ax_x        = plt.axes([0.1 , 0.01, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_y        = plt.axes([0.55, 0.01, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_z        = plt.axes([0.1 , 0.05, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_alpha    = plt.axes([0.55, 0.05, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_beta     = plt.axes([0.1 , 0.09, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_gamma    = plt.axes([0.55, 0.09, 0.35, 0.03], facecolor='lightgoldenrodyellow')

    s_x     = Slider(ax_x       , 'x'       , -200, 200, valinit=0)
    s_y     = Slider(ax_y       , 'y'       , -200, 400, valinit=190)
    s_z     = Slider(ax_z       , 'z'       , -200, 400, valinit=150)
    s_alpha = Slider(ax_alpha   , 'alpha'   , -180, 180, valinit=90)
    s_beta  = Slider(ax_beta    , 'beta'    , -180, 180, valinit=0)
    s_gamma = Slider(ax_gamma   , 'gamma'   , -180, 180, valinit=0)

    s_x.on_changed(updateX)
    s_y.on_changed(updateY)
    s_z.on_changed(updateZ)
    s_alpha.on_changed(updateAlpha)
    s_beta.on_changed(updateBeta)
    s_gamma.on_changed(updateGamma)
 
    plt.show()






def main():
    
    #x = threading.Thread(target=solveInverseKinematics)
    #x.start()

    #start_time = time.time()  # Record the start time
    #solveInverseKinematics()
    #end_time = time.time()    # Record the end time
#
    #elapsed_time = end_time - start_time  # Calculate the elapsed time
    #print(f"Function call took {elapsed_time:.6f} seconds")

    setUpPlot()

    

    



if __name__ == "__main__":
    main()




































#def setUpPlot():
#     # Create sliders
#    ax_a = plt.axes([0.1 , 0.01, 0.35, 0.03], facecolor='lightgoldenrodyellow')
#    ax_b = plt.axes([0.55, 0.01, 0.35, 0.03], facecolor='lightgoldenrodyellow')
#    ax_c = plt.axes([0.1 , 0.05, 0.35, 0.03], facecolor='lightgoldenrodyellow')
#    ax_d = plt.axes([0.55, 0.05, 0.35, 0.03], facecolor='lightgoldenrodyellow')
#    ax_e = plt.axes([0.1 , 0.09, 0.35, 0.03], facecolor='lightgoldenrodyellow')
#    ax_f = plt.axes([0.55, 0.09, 0.35, 0.03], facecolor='lightgoldenrodyellow')
#
#    s_a = Slider(ax_a, 'a', -180, 180, valinit=0)
#    s_b = Slider(ax_b, 'b', -180, 180, valinit=-60)
#    s_c = Slider(ax_c, 'c', -180, 180, valinit=60)
#    s_d = Slider(ax_d, 'd', -180, 180, valinit=0)
#    s_e = Slider(ax_e, 'e', -180, 180, valinit=0)
#    s_f = Slider(ax_f, 'f', -180, 180, valinit=0)
#
#    s_a.on_changed(updateA)
#    s_b.on_changed(updateB)
#    s_c.on_changed(updateC)
#    s_d.on_changed(updateD)
#    s_e.on_changed(updateE)
#    s_f.on_changed(updateF)
# 
#    plt.show()





