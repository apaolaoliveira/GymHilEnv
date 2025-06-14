import time
import numpy as np
import gymnasium as gym
from mujoco import viewer

env = gym.make("gym_hil/PandaPickCubeBase-v0", image_obs=True)
obs, _ = env.reset()

def move(action, steps=10, delay=0.05):
    for _ in range(steps):
        env.step(action)
        v.sync()
        time.sleep(delay)

def open_gripper():
    move(np.array([0, 0, 0, 0, 0, 0, -1.0]))

def close_gripper():
    move(np.array([0, 0, 0, 0, 0, 0, 0.0]))

def move_z(direction=+1):
    move(np.array([0, 0, 0.02 * direction, 0, 0, 0, 1.0]))

def move_xy(x=0.0, y=0.0):
    move(np.array([x, y, 0, 0, 0, 0, 1.0]))

with viewer.launch_passive(env.unwrapped.model, env.unwrapped.data) as v:
    move_z(-1) #down       
    open_gripper()
    close_gripper()
    move_z(+1) #up 
    input("Press Enter to close...")

