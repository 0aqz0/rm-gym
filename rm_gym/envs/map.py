import numpy as np
import matplotlib.pyplot as plt

DEADLY_COST = 255
INFLATION_COST = 1
NEED_DRAW_GRID = False
NEED_DRAW_INFLATED_GRID = False
NEED_INFLATION = True


class Map(object):
    """
    The Map Class
    """
    def __init__(self, MAP_WIDTH=800, MAP_HEIGHT=500, STEP_SIZE=1, INFLATION_RADIUS=30):
        self._width = MAP_WIDTH
        self._height = MAP_HEIGHT
        self._step_size = STEP_SIZE
        self._inflation_radius = INFLATION_RADIUS
        self._grid_width = round(self._width/self._step_size)
        self._grid_height = round(self._height/self._step_size)
        self._grid_inflation_radius = round(self._inflation_radius/self._step_size)
        self._grid = np.zeros((self._grid_width+1, self._grid_height+1))
        self._obstacle_list = [[120,400,220,375],[140,240,165,140],[325,100,350,0],
                               [350,262.5,450,237.5],[450,500,475,400],[580,125,680,100],
                               [635,360,660,260]]  # 记录障碍物的左上角坐标和右下角坐标（左、上、右、下）
        self.init_grid()

    def init_grid(self):
        """
        initialize the grid
        :return: grid
        """
        if NEED_INFLATION:
            self.grid_inflation()
        for obs in self._obstacle_list:
            self._grid[round(obs[0]/self._step_size):round(obs[2]/self._step_size)+1,
            round(obs[3]/self._step_size):round(obs[1]/self._step_size)+1] = DEADLY_COST

        if NEED_DRAW_GRID:
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

    def grid_inflation(self):
        """
        inflation based on the robot radius
        :return: grid
        """
        for obs in self._obstacle_list:
            if obs[0]!=0:
                inflation_x1 = round((obs[0]-self._inflation_radius)/self._step_size)
            else:
                inflation_x1 = obs[0]
            if obs[1]!=self._height:
                inflation_y2 = round((obs[1]+self._inflation_radius)/self._step_size)
            else:
                inflation_y2 = obs[1]
            if obs[2]!=self._width:
                inflation_x2 = round((obs[2]+self._inflation_radius)/self._step_size)
            else:
                inflation_x2 = obs[2]
            if obs[3]!=0:
                inflation_y1 = round((obs[3]-self._inflation_radius)/self._step_size)
            else:
                inflation_y1 = obs[3]
            self._grid[inflation_x1:inflation_x2+1,
            inflation_y1:inflation_y2+1] = INFLATION_COST

        # border inflation
        self._grid[0:self._grid_width+1, 0:round(self._inflation_radius/self._step_size)+1] = INFLATION_COST
        self._grid[0:self._grid_width+1, self._grid_height-round(self._inflation_radius / self._step_size):self._grid_height+1] = INFLATION_COST
        self._grid[0:round(self._inflation_radius/self._step_size)+1, 0:self._grid_height+1] = INFLATION_COST
        self._grid[self._grid_width-round(self._inflation_radius/self._step_size):self._grid_width+1, 0:self._grid_height+1] = INFLATION_COST

        if NEED_DRAW_INFLATED_GRID:
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

    def inside_border(self, x, y, mode = 'default'):
        """
        in the border
        :return: bool
        """
        if mode == 'default':
            if x >= 0 and x <= self._width and y >= 0 and y <= self._height:
                return True
        elif mode == 'grid':
            if x >= 0 and x <= self._grid_width and y >= 0 and y <= self._grid_height:
                return True
        return False

    def has_collision(self, x, y, mode='default'):
        """
        detect collision
        :return: bool
        """
        if not self.inside_border(x, y, mode=mode):
            print("Outside the border!!!")
            return True
        if mode == 'default' and self._grid[round(x/self._step_size), round(y/self._step_size)] == 0:
            return False
        if mode == 'grid' and self._grid[x, y] == 0:
            return False
        return True

    def start_region(self, x, y):
        """
        judge if you are in a start region
        :return: region number
        0---no region, 1---red1, 2---red2, 3---blue1, 4---blue2
        """
        if x>0 and x<100 and y>0 and y<100:
            return 1
        elif x>700 and x<800 and y>0 and y<100:
            return 2
        elif x>0 and x<100 and y>400 and y<500:
            return 3
        elif x>700 and x<800 and y>400 and y<500:
            return 4
        return 0

    def buff_region(self, x, y):
        """
        judge which buff region you are in
        :return: region number
        0---no region, 1---defence buff, 2---attack buff
        """
        if x>120 and x<220 and y>275 and y<375:
            return 1
        elif x>580 and x<680 and y>125 and y<225:
            return 2
        return 0


if __name__ == '__main__':
    map = Map()
    while(1):
        x = int(input("Please input x: "))
        y = int(input("Please input y: "))
        if map.has_collision(x, y):
            print("Collision!!!")
        else:
            print("No Collision.")
