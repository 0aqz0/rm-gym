#!/usr/bin/env python
"""
RoboMaster AI Challenge Simulation Environment.
"""
import gym
from rm_gym.envs.map_view_2d import MapView2D
from rm_gym.envs.map import Map
from rm_gym.envs.robot import Robot
import time

ROBOT1_INITIAL_POS = [50,50]
ROBOT2_INITIAL_POS = [750,50]
ROBOT3_INITIAL_POS = [50,450]
ROBOT4_INITIAL_POS = [750,450]


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
        self.robot = [Robot(pos=ROBOT1_INITIAL_POS), Robot(ROBOT2_INITIAL_POS),
                      Robot(ROBOT3_INITIAL_POS), Robot(ROBOT4_INITIAL_POS)]
        print(self.robot[0].pos)

    def step(self, action, robotNum):
        """
        Accepts an action and returns a tuple (observation, reward, done, info).
        """
        # define action as a four-dimension array [delta_x, delta_y, shoot, shoot_dir]
        # position
        print(robotNum)
        new_x = self.robot[robotNum].pos[0] + action[0]
        new_y = self.robot[robotNum].pos[1] + action[1]
        print(self.robot[robotNum].pos[0])
        # print(action[0])
        # print(new_x)
        if self.map.has_collision(new_x, new_y):
            observation = 'collision'
            reward = 0
            done = False
            info = {}
            return observation, reward, done, info
        else:
            self.robot[robotNum].pos[0] = new_x
            self.robot[robotNum].pos[1] = new_y
            self.map_view.move_robot(robot1Pos=[new_x, new_y])
            done = False
            reward = 0
            info = {}
            return self.robot, reward, done, info

    def reset(self):
        """
        Resets the state of the environment and returns an initial observation.
        Returns: observation (object): the initial observation of the
            space.
        """
        self.map_view.reset_robot()
        # for robot in self.robot:
        #     robot.reset()           # NEED TEST!!!
        return self.robot

    def render(self, mode='human', close=False):
        """
        Renders the environment.
        """
        if close:
            self.map_view.quit_game()
        return self.map_view.update()


if __name__ == '__main__':
    env = RoboMasterEnv()
    env.reset()
    while True:
        for i in range(4):
            env.render()
            env.step([20,0,0,0], 0)
            time.sleep(1)
