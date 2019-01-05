#!/usr/bin/env python
"""
RoboMaster AI Challenge Simulation Environment.
"""
import gym
from rm_gym.envs.map_view_2d import MapView2D
from rm_gym.envs.map import Map
from rm_gym.envs.robot import Robot
import time
import math

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
        self.map_view = MapView2D(robot1Pos=ROBOT1_INITIAL_POS, robot2Pos=ROBOT2_INITIAL_POS,
                                  robot3Pos=ROBOT3_INITIAL_POS, robot4Pos=ROBOT4_INITIAL_POS)
        self.state = None
        self.map = Map()
        self.robot = [Robot(pos=ROBOT1_INITIAL_POS), Robot(ROBOT2_INITIAL_POS),
                      Robot(ROBOT3_INITIAL_POS), Robot(ROBOT4_INITIAL_POS)]

    def step(self, action, robotNum):
        """
        Accepts an action and returns a tuple (observation, reward, done, info).
        """
        # define action as a four-dimension array [delta_x, delta_y, shoot, shoot_dir]
        # position
        robotx = self.robot[robotNum]
        delta_x = action[0]
        delta_y = action[1]
        shoot = action[2]
        shoot_dir = action[3]
        new_x = self.robot[robotNum].pos[0] + delta_x
        new_y = self.robot[robotNum].pos[1] + delta_y

        if self.map.has_collision(new_x, new_y):
            reward = 0
            done = False
            info = {}
        else:
            robotx.pos[0] = new_x
            robotx.pos[1] = new_y
            self.map_view.move_robot([new_x, new_y], robotNum)
            done = False
            reward = 0
            info = {}
            if shoot:
                for robot in self.robot:
                    if robot != robotx:
                        angle = math.atan2(robot.pos[1]-robotx.pos[1],
                                           robot.pos[0] - robotx.pos[0])
                        if abs(angle - shoot_dir) < 0.1 and not self.map.has_collision(robot.pos, robotx.pos):
                            robot.health -= 1
                            reward = 1

        return self.robot, reward, done, info

    def reset(self):
        """
        Resets the state of the environment and returns an initial observation.
        Returns: observation (object): the initial observation of the
            space.
        """
        self.map_view.reset_robot()
        for robot in self.robot:
            robot.reset()
        return self.robot

    def render(self, mode='human', close=False):
        """
        Renders the environment.
        """
        if close:
            self.map_view.quit_game()
        return self.map_view.update()
