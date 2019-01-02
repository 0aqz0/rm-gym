# author: 0aqz0
# date: 2018/11/20
"""
A* path planning implementation with python
"""
import math
from collections import deque
import matplotlib.pyplot as plt
import time
from map import Map


NEED_DRAW = False
map = Map()
grid_size = 10      # grid resolution
robot_size = 1     # robot size
obstacle_x = []      # coordinate x of obstacles
obstacle_y = []      # coordinate y of obstacles
motions = [
    [1,0,1],                # right          cost: 1
    [0,1,1],                # up             cost: 1
    [-1,0,1],               # left           cost: 1
    [0,-1,1],               # down           cost: 1
    # [-1,-1,math.sqrt(2)],   # left and down  cost: 2^0.5
    # [-1,1,math.sqrt(2)],    # left and up    cost: 2^0.5
    # [1,-1,math.sqrt(2)],    # right and down cost: 2^0.5
    # [1,1,math.sqrt(2)],     # right and up   cost: 2^0.5
]

class Point:
    """
    smallest unit of the grid map
    """
    def __init__(self, x, y, gcost, parent, motion):
        self.parent = parent
        self.parent_motion = motion
        self.x = x
        self.y = y
        self.g = gcost

def not_legal(node, robot_id):
    if node.x < 0 or node.x >= map.gridwidth or node.y < 0 or node.y >= map.gridheight:
        return True
    if map.grid[1,node.x,node.y] > 0:
        return True

    if map.grid[0,node.x,node.y] >= 40 and (map.grid[0,node.x,node.y]%40 != math.floor(robot_id/2)):
        return True

def calculate_heuristic(node1, node2):
    """
    calculate the heuristic evaluation from node1 to node2
    :param node1: start node
    :param node2: goal node
    :return: the heuristic evaluation
    """
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)

def a_star_planning(start_x, start_y, goal_x, goal_y, id):
    """
    A* path planning implementation
    """
    # extract the index of start node, goal node and obstacles
    start = Point(round(start_x/grid_size), round(start_y/grid_size), 0.0, -1, [0,0,0])
    goal = Point(round(goal_x/grid_size), round(goal_y/grid_size), 0.0, -1, [0,0,0])
    if not_legal(goal, id):
        print ('not a legal goal')
        return False
  
    # time.sleep(10)

    # create the open list and close list to store nodes
    openset, closeset = deque(), deque()
    openset.append(start)

    while True:
        # find out the min f node to explore

        current_node = min(openset,
                         key=lambda node: node.g + calculate_heuristic(node,goal))

        # pltplt.plot(current_node.x, current_node.y, "b*")
        if len(closeset) % 10 == 0:
            plt.pause(0.001)

        if current_node.x == goal.x and current_node.y == goal.y:
            print("Congratulations! You have found the goal!")
            goal.parent = current_node
            break

        # Remove it from the open list
        openset.remove(current_node)
        # Add it to the close list
        closeset.append(current_node)

        # Explore the neighbour
        for motion in motions:
            if motion == current_node.parent_motion:
                turn_cost = 0
            elif (motion[0] == -1 * current_node.parent_motion[0]) and (motion[1] == -1 * current_node.parent_motion[1]):
                turn_cost = 1.5
            else:
                turn_cost = 1

            node = Point(current_node.x + motion[0],
                        current_node.y + motion[1],
                        current_node.g + motion[2] + turn_cost,
                        current_node,
                        motion,
                        )

            # ignore it if it is in the close list
            flag = False
            for item in closeset:
                if item.x == node.x and item.y == node.y:
                    flag = True
                    break
            if flag:
                continue
            # ignore it if it is obstacle

            if not_legal(node, id):
                continue
            # update its parent if it is the open list
            flag = True
            for item in openset:
                if item.x == node.x and item.y == node.y:
                    flag = False
                    # if closer, update the parent
                    if node.g <= item.g:
                        item.g = node.g
                        item.parent = node.parent
                        item.parent_motion = node.parent_motion
                    break
            # add to the open list if it is not in the open list
            if flag:
                openset.append(node)

    # generate the final path
    while True:
        route = deque()
        route.append(goal)
        plt.plot(goal.x, goal.y, "rx")
        if goal.parent == -1:
            break
        else:
            goal = goal.parent
            route.appendleft(goal)
    #     return route
    # return False
    if NEED_DRAW:
        # draw map
        for i in range(map.gridwidth):
            for j in range(map.gridheight):
                if map.grid[1,i,j] >0:
                    plt.plot(i, j, "xc")

        plt.plot(start.x, start.y, "ro")
        plt.plot(goal.x, goal.y, "go")

        for goal in route:
            plt.plot(goal.x, goal.y, "rx")
        plt.show()



if __name__ == '__main__':
    start_x = 50.0
    start_y = 50.0
    goal_x = 750.0
    goal_y = 50.0

    a_star_planning(start_x, start_y, goal_x, goal_y, 1)
