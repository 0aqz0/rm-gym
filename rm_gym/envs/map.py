"""
The Map Class
"""
import numpy as np
import matplotlib.pyplot as plt

DEADLY_COST = 255
NEED_DRAW = False

class Map(object):
    def __init__(self, MAP_WIDTH=800, MAP_HEIGHT=500, STEP_SIZE=10, INFLATION_RADIUS=42):
        self._width = MAP_WIDTH
        self._height = MAP_HEIGHT
        self._step_size = STEP_SIZE
        self._inflation_radius = INFLATION_RADIUS
        self._grid_width = int(self._width/self._step_size)
        self._grid_height = int(self._height/self._step_size)
        self._grid_inflation_radius = int(self._inflation_radius/self._step_size)
        self._grid = np.zeros((self._grid_width, self._grid_height))
        self._obstacle_list = [[120,400,220,375],[140,240,165,140],[325,100,350,0],
                               [350,262.5,450,237.5],[450,500,475,400],[580,125,680,100],
                               [635,360,660,260]]  # 记录障碍物的左上角坐标和右下角坐标（左、上、右、下）
        self.init_grid()

    def init_grid(self):
        """
        initialize the grid
        :return: grid
        """
        for obs in self._obstacle_list:
            self._grid[int(obs[0]/self._step_size):int(obs[2]/self._step_size)+1,
            int(obs[3]/self._step_size):int(obs[1]/self._step_size)+1] = DEADLY_COST

        if NEED_DRAW:
            for i in range(self._grid_width):
                plt.scatter(i,0)
                plt.scatter(i,self._grid_height)
                for j in range(self._grid_height):
                    plt.scatter(0,j)
                    plt.scatter(self._grid_width,j)
                    if self._grid[i, j] != 0:
                        plt.scatter(i,j)
            plt.show()
        return self._grid

    def inside_border(self, pos):
        """
        in the border
        :return: bool
        """
        if pos[0]>=0 and pos[0]<=self._width and pos[1]>=0 and pos[1]<=self._height:
            return True
        else:
            return False

    def has_collision(self):
        pass


if __name__ == '__main__':
    Map()

