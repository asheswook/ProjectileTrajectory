import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from typing import List, Union, Tuple

# Make 3D projectile trajectory plot
def plot3D(x, y, z, title, xlabel, ylabel, zlabel):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, zs=0, zdir='z', label='zs=0, zdir=z')

    ax.plot(x, y, z)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    plt.show()

# class Force:
#     def __init__(self, Fx: np.float16, Fy: np.float16, Fz: np.float16):
#         self.Fx = Fx
#         self.Fy = Fy
#         self.Fz = Fz

# class TemporalForce(Force):
#     def __init__(self, Fx: np.float16, Fy: np.float16, Fz: np.float16, start_time: np.float16, end_time: np.float16):
#         super().__init__(Fx, Fy, Fz)
#         self.start_time = start_time
#         self.end_time = end_time



class Projectile:
    def __init__(self, x0: np.float16, y0: np.float16, z0: np.float16):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.set_inital_velocity(0, 0, 0)
        self.set_gravity(9.81)
        self.set_mass(10)
        # self.set_nonconservative_force(Force(0, 0, 0), 0, 0)
        self.set_move_time(10)
        self.set_time_step(0.5)

    def set_inital_velocity(self, v0: np.float16, theta: np.float16, phi: np.float16):
        self.v0 = v0
        self.theta = theta
        self.phi = phi
        # phi가 0이면 x, z축 운동

    # m/s^2
    def set_gravity(self, g: np.float16):
        self.g = g
    
    # kg
    def set_mass(self, m: np.float16):
        self.m = m

    # def add_nonconservative_force(self, F: Force, influence_time: np.float16, influence_start_time: np.float16):
    #     self.F = F
    #     self.force_influence_time = influence_time
    #     self.force_influence_start_time = influence_start_time

    def set_move_time(self, t: np.float16):
        self.t = t

    def set_time_step(self, dt: np.float16):
        self.dt = dt

    def calc_trajectory(self) -> Tuple[List[np.float16], List[np.float16], List[np.float16]]:
        # Calculate trajectory
        x = [self.x0]
        y = [self.y0]
        z = [self.z0]
        vx = [self.v0 * np.sin(self.theta) * np.cos(self.phi)]
        vy = [self.v0 * np.sin(self.theta) * np.sin(self.phi)]
        vz = [self.v0 * np.cos(self.theta)]
        t = [0]
        while t[-1] < self.t:
            # Calculate velocity
            vx.append(vx[-1])
            vy.append(vy[-1])
            vz.append(vz[-1] - self.g * self.dt)
            # Calculate position
            x.append(x[-1] + vx[-1] * self.dt)
            y.append(y[-1] + vy[-1] * self.dt)
            z.append(z[-1] + vz[-1] * self.dt)
            # Calculate time
            t.append(t[-1] + self.dt)
        return x, y, z
    
발사체 = Projectile(0, 0, 0)
발사체.set_inital_velocity(10, np.pi/4, np.pi/4)
발사체.set_move_time(1.5)
발사체.set_time_step(0.1)
x, y, z = 발사체.calc_trajectory()
plot3D(x, y, z, 'Projectile Trajectory', 'x', 'y', 'Vertical Height')




