import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

DEADLY_COST = 255
INFLATION_COST = 1
NEED_DRAW_GRID = False
NEED_DRAW_INFLATED_GRID = False
NEED_INFLATION = True


class Map(object):
    """
    The Map Class
    """
    def __init__(self, MAP_WIDTH=800, MAP_HEIGHT=500, STEP_SIZE=10, INFLATION_RADIUS=30):
        self.width = MAP_WIDTH
        self.height = MAP_HEIGHT
        self.step_size = STEP_SIZE
        self._inflation_radius = INFLATION_RADIUS
        self.gridwidth = round(self.width/self.step_size)
        self.gridheight = round(self.height/self.step_size)
        self.grid_inflation_radius = round(self._inflation_radius/self.step_size)
        self.grid = np.zeros((2,self.gridwidth+1, self.gridheight+1))    # dim 0:region type,  dim 1 : obstacle map
        '''region type:
        free space = 0;
        obstacle = 1;
        start_region = 20,21,22,23; two for team1 (20,21) two for team2
        buff_region = 30,31;
        supply_region = 40,41;   40 for team1. 41 for team 2
        zone_of_robots =50,51,52,53;  for avoiding collision?? how to update? ---copy a grid and add new robots to it return newgrid
        '''
        # self.obstacle_list = [[120,400,220,375],[140,240,165,140],[325,100,350,0],
        #                        [350,262.5,450,237.5],[450,500,475,400],[580,125,680,100],
        #                        [635,360,660,260]]  # 记录障碍物的左上角坐标和右下角坐标（左、上、右、下）
        self.obstacle_list = [[[120,375],100,25],[[140,140],25,100],[[325,0],25,100],
                        [[350,237.5],100,25],[[450,400],25,100],[[580,100],100,25],
                        [[635,260],25,100]]  # 记录障碍物的左下角坐标和宽，高 （（x，y）， dx， dy）
        self.start_region_list = [[[0,0],100,100], [[700,0],100,100], 
                                [[0,400],100,100], [[700,400],100,100]]     #0,1 team1; 2,3 team2
        self.supply_region_list = [[[350,400],100,100], [[350,0],100,100]]
        self.buff_region_list = [[[580,125],100,100], [[180,275],100,100]]  #0 for team1. 1 for team 2

        self.initgrid()
        print (self.grid[0])

    def initgrid(self):
        """
        initialize the grid
        :return: grid
        """
        if NEED_INFLATION:
            self.grid_inflation()
        for obs in self.obstacle_list:
            self.grid[1,round(obs[0][0]/self.step_size):round((obs[0][0] + obs[1])/self.step_size) +1,
            round(obs[0][1]/self.step_size):round((obs[0][1] + obs[2])/self.step_size)+1] = DEADLY_COST
            self.grid[0,round(obs[0][0]/self.step_size):round((obs[0][0] + obs[1])/self.step_size) +1,
            round(obs[0][1]/self.step_size):round((obs[0][1] + obs[2])/self.step_size)+1] = 1

        i = 0
        for zone in self.start_region_list:
            self.grid[0,round(zone[0][0]/self.step_size):round((zone[0][0] + zone[1])/self.step_size) +1,
            round(zone[0][1]/self.step_size):round((zone[0][1] + zone[2])/self.step_size)+1] = 20 + i
            i += 1
        
        i = 0
        for zone in self.buff_region_list:
            self.grid[0,round(zone[0][0]/self.step_size):round((zone[0][0] + zone[1])/self.step_size) +1,
            round(zone[0][1]/self.step_size):round((zone[0][1] + zone[2])/self.step_size)+1] = 30 + i
            i += 1

        i = 0

        for zone in self.supply_region_list:
            self.grid[0,round(zone[0][0]/self.step_size):round((zone[0][0] + zone[1])/self.step_size) +1,
            round(zone[0][1]/self.step_size):round((zone[0][1] + zone[2])/self.step_size)+1] = 40 + i
            i += 1     

        if NEED_DRAW_GRID:
            fig1 = plt.figure() 
            ax1 = fig1.add_subplot(111, aspect='equal')
            plt.plot(0,0, self.gridwidth,0, self.gridwidth,self.gridheight, 0,self.gridheight, 0,0)

            for i in self.obstacle_list:                
                ax1.add_patch( patches.Rectangle([i[0][0]/self.step_size- self._inflation_radius,i[0][1]/self.step_size - self._inflation_radius], 
                            i[1]/self.step_size + 2 * self._inflation_radius, i[2]/self.step_size + 2 * self._inflation_radius, facecolor = 'black'))
            #borders
            ax1.add_patch( patches.Rectangle([0,0], self.gridwidth, self._inflation_radius, facecolor = 'grey'))
            ax1.add_patch( patches.Rectangle([0,self.gridheight - self._inflation_radius], self.gridwidth, self._inflation_radius, facecolor = 'grey'))
            ax1.add_patch( patches.Rectangle([0,0], self._inflation_radius, self.gridheight, facecolor = 'grey'))
            ax1.add_patch( patches.Rectangle([self.gridwidth - self._inflation_radius,0], self._inflation_radius, self.gridheight, facecolor = 'grey'))
            #regions
            plt.show()
        return self.grid

    def grid_inflation(self):
        """
        inflation based on the robot radius
        :return: grid
        """
        for obs in self.obstacle_list:

            inflation_x1 = round((obs[0][0]-self._inflation_radius)/self.step_size)

            inflation_y2 = round((obs[0][1] + obs[2] +self._inflation_radius)/self.step_size)

            inflation_x2 = round((obs[0][0] + obs[1] +self._inflation_radius)/self.step_size)

            inflation_y1 = round((obs[0][1] -self._inflation_radius)/self.step_size)

            self.grid[1, inflation_x1:inflation_x2+1,
            inflation_y1:inflation_y2+1] = INFLATION_COST

        # border inflation
        self.grid[1, 0:self.gridwidth+1, 0:round(self._inflation_radius/self.step_size)+1] = INFLATION_COST
        self.grid[1, 0:self.gridwidth+1, self.gridheight-round(self._inflation_radius / self.step_size):self.gridheight+1] = INFLATION_COST
        self.grid[1, 0:round(self._inflation_radius/self.step_size)+1, 0:self.gridheight+1] = INFLATION_COST
        self.grid[1, self.gridwidth-round(self._inflation_radius/self.step_size):self.gridwidth+1, 0:self.gridheight+1] = INFLATION_COST

        # if NEED_DRAW_INFLATED_GRID:
        #     for i in range(self.gridwidth):
        #         plt.scatter(i,0)
        #         plt.scatter(i,self.gridheight)
        #         for j in range(self.gridheight):
        #             plt.scatter(0,j)
        #             plt.scatter(self.gridwidth,j)
        #             if self.grid[i, j] != 0:
        #                 plt.scatter(i,j)
        #     plt.show()

        return self.grid

    def inside_border(self, x, y, mode = 'default'):
        """
        in the border
        :return: bool
        """
        if mode == 'default':
            if x >= 0 and x <= self.width and y >= 0 and y <= self.height:
                return True
        elif mode == 'grid':
            if x >= 0 and x <= self.gridwidth and y >= 0 and y <= self.gridheight:
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
        if mode == 'default' and self.grid[1, round(x/self.step_size), round(y/self.step_size)] == 0:
            return False
        if mode == 'grid' and self.grid[1, x, y] == 0:
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

    def supply_region(self, x, y):
        """
        judge which supply region you are in
        :return: region number
        0---no region, 1---blue supply region, 2---red supply region
        """
        if x>350 and x<450 and y>0 and y<100:
            return 1
        elif x>350 and x<450 and y>400 and y<500:
            return 2
        return 0

    def line_collision(self, x1, y1, x2, y2, step=5):
        """
        detect if collision will happen between two point(used when STEP_SIZE=1!!!)
        :return: bool
        """
        theta = math.atan2(y2-y1, x2-x1)
        length = math.sqrt((x1-x2)**2+(y1-y2)**2)
        for i in range(int(length/step)):
            new_x = x1+step*i*math.cos(theta)
            new_y = y1+step*i*math.sin(theta)
            if self.has_collision(new_x, new_y):
                return True
        return False



if __name__ == '__main__':
    map = Map()
    print(map.grid)

    # while(1):
    #     x = int(input("Please input x: "))
    #     y = int(input("Please input y: "))
    #     if map.has_collision(x, y):
    #         print("Collision!!!")
    #     else:
    #         print("No Collision.")