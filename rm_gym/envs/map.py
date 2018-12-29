"""
The Map Class
"""
import numpy as np

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
        self._obstacle_list = [[120,140,325,350,450,580,635],[700,240,100,262.5,800,125,660],[220,165,350,450,475,680,660],[675,140,0,237.5,700,100,560]]              #记录障碍物的左上角坐标和右下角坐标（左、上、右、下）
        self.init_grid()

    def init_grid(self):
        """
        initialize the grid
        :return: grid
        """
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

