import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from matplotlib.widgets import Slider, TextBox
from arm import Arm




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


def updateTheta(val):
        arm.m_theta = val*np.pi/180
        arm.clear()
        arm.draw()

def updateA(val):
        arm.m_a = val*np.pi/180
        arm.clear()
        arm.draw()

def updateB(val):
        arm.m_b = val*np.pi/180
        arm.clear()
        arm.draw()

def updatePsi(val):
        arm.m_psi = val*np.pi/180
        arm.clear()
        arm.draw()

def updateOmega(val):
        arm.m_omega = val*np.pi/180
        arm.clear()
        arm.draw()

def updateGamma(val):
        arm.m_gamma = val*np.pi/180
        arm.clear()
        arm.draw()


def main():
    

     # Create sliders
    ax_theta    = plt.axes([0.1 , 0.01, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_a        = plt.axes([0.55, 0.01, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_b        = plt.axes([0.1 , 0.05, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_psi      = plt.axes([0.55, 0.05, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_omega    = plt.axes([0.1 , 0.09, 0.35, 0.03], facecolor='lightgoldenrodyellow')
    ax_gamma    = plt.axes([0.55, 0.09, 0.35, 0.03], facecolor='lightgoldenrodyellow')

    s_theta = Slider(ax_theta, 'theta'  , -180, 180, valinit=0)
    s_a     = Slider(ax_a, 'a'          , -180, 180, valinit=-60)
    s_b     = Slider(ax_b, 'b'          , -180, 180, valinit=60)
    s_psi   = Slider(ax_psi, 'psi'      , -180, 180, valinit=0)
    s_omega = Slider(ax_omega, 'omega'  , -180, 180, valinit=0)
    s_gamma = Slider(ax_gamma, 'gamma'  , -180, 180, valinit=0)

    s_theta.on_changed(updateTheta)
    s_a.on_changed(updateA)
    s_b.on_changed(updateB)
    s_psi.on_changed(updatePsi)
    s_omega.on_changed(updateOmega)
    s_gamma.on_changed(updateGamma)
 
   
    plt.show()



if __name__ == "__main__":
    main()













