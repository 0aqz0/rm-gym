#!/usr/bin/env python
"""
RoboMaster AI Challenge Simulation Environment.
"""
import gym
from rm_gym.envs.map_view_2d import MapView2D
from rm_gym.envs.map import Map
import time


class RoboMasterEnv(gym.Env):
    """
    The RoboMaster Simulation Class.
    """
    action_space = ["W", "E", "N", "S"]
    observation_space = None

    def __init__(self):
        self.map_view = MapView2D()
        self.state = None
        self.map = Map()

    def step(self, action):
        """
        Accepts an action and returns a tuple (observation, reward, done, info).
        Args:
            action (object): an action provided by the environment
        Returns:
            observation (object): agent's observation of the current environment
            reward (float) : amount of reward returned after previous action
            done (boolean): whether the episode has ended, in which case further step() calls will return undefined results
            info (dict): contains auxiliary diagnostic information (helpful for debugging, and sometimes learning)
        """
        if action == 'W':
            self.map_view.move_robot([50, 50])
        elif action == 'E':
            self.map_view.move_robot([100, 50])
        elif action == 'N':
            self.map_view.move_robot([50, 100])
        else:
            self.map_view.move_robot([100, 100])

        done = False
        reward = 0
        info = {}
        return self.state, reward, done, info

    def reset(self):
        """
        Resets the state of the environment and returns an initial observation.
        Returns: observation (object): the initial observation of the
            space.
        """
        pass

    def render(self, mode='human'):
        """
        Renders the environment.
        """
        self.map_view.update()


if __name__ == '__main__':
    env = RoboMasterEnv()
    env.reset()
    while True:
        for i in range(4):
            env.render()
            env.step(env.action_space[i])
            time.sleep(1)
