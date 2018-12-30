import numpy as np
import math

INITIAL_POSITION = [30, 30]       # initial x, y coordinates of the robot
INITIAL_DIR = 0                   # initial dir of the robot, range in [0, 2*pi]
INITIAL_STATE = None              # initial state of the robot
INITIAL_BULLET = 40               # initial bullets of the robot
INITIAL_HEALTH = 2000             # initial health of the robot
ROBOT_SIZE = (60.0, 60.0)         # size of the robot

MAX_SPEED = 0.1                   # max speed(m/s) of the robot
MAX_ROTATE_SPEED = 0.1            # max rotation(rad/s) speed of the robot
MAX_BULLET = 50                   # max bullets of the robot

DAMAGE = 5                        # damage per shot , if defencing: /2
SLEEP_TIME = 0.1


class Robot:
    def __init__(self, pos=INITIAL_POSITION, dir=INITIAL_DIR, state=INITIAL_STATE, health=INITIAL_HEALTH,
                 bullet=INITIAL_BULLET):
        self._pos = pos
        self._dir = dir
        self._state = state
        self._health = health
        self._bullet = bullet
        self._has_buff = False
        self._is_survive = True

    def reset(self):
        """
        reset the robot
        """
        self._pos = INITIAL_POSITION
        self._dir = INITIAL_DIR
        self._state = INITIAL_STATE
        self._health = INITIAL_HEALTH
        self._bullet = INITIAL_BULLET
        self._has_buff = False
        self._is_survive = True

    def move_by_step(self, dx, dy, dtheta=0):
        """
        move by small steps
        """
        self._pos[0] += dx
        self._pos[1] += dy
        self._dir = (self._dir + dtheta) % (2 * math.pi)

    def move_to_point(self, x, y, dir=0):
        """
        move directly to a point
        """
        self._pos[0] = x
        self._pos[1] = y
        self._dir = dir

    # def shot(self, target):
    #     if self.turn_gun(target):
    #         print('turnning, heading to:', self.state.pose.theta)
    #     else :
    #         self.state.bullet -= 1
    #         if rd.random() >= 0.5:   #this could be a function
    #             target.shoted()
    #
    # def turn_gun(self, target):
    #     direction = np.arctan((target.state.pose.y - self.state.pose.y)/(target.state.pose.x - self.state.pose.x))
    #     direction = np.degrees(direction)    #this could be a function
    #     dtheta = direction - self.state.pose.theta
    #     if dtheta == 0:
    #         return False
    #
    #     if abs(dtheta) >= 6:
    #         self.state.pose.theta += 6 * dtheta/ abs(dtheta)
    #     else:
    #         self.state.pose.theta = direction
    #
    #     return True

    def add_bullet(self, bullets):
        if self._bullet + bullets > MAX_BULLET:
            self._bullet = MAX_BULLET
        else:
            self._bullet += bullets

    def get_shot(self, damage=5):
        """
        get shot counted by damage
        """
        if self._has_buff:
            self._health -= damage / 2
        else:
            self._health -= damage
        if self._health <= 0:
            self._is_survive = False

    def get_buff(self):
        """
        get the buff
        """
        self._has_buff = True

    def lose_buff(self):
        """
        lose the buff
        """
        self._has_buff = False

    @property
    def pos(self):
        return self._pos

    @property
    def state(self):
        return self._state

    @property
    def health(self):
        return self._health

    @property
    def bullet(self):
        return self._bullet

    @property
    def is_survive(self):
        return self._is_survive

    @property
    def has_buff(self):
        return self._has_buff
