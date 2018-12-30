import pygame
from pygame.locals import *

background_image_filename = 'images/map.png'
robot_image_filename = 'images/robot.png'
MAP_SIZE = (800, 500)
IMAGE_OFFSET = 30

class MapView2D:
    """
    The Map View Class.
    """
    def __init__(self, map_name="RoboMaster Simulation", robot1Pos=[50,50], robot2Pos=[750,50], robot3Pos=[50,450], robot4Pos=[750,450]):
        pygame.init()
        pygame.display.set_caption(map_name)
        self.clock = pygame.time.Clock()
        self._game_over = False

        self.screen = pygame.display.set_mode(MAP_SIZE, 0, 32)
        self.background = pygame.image.load(background_image_filename).convert()
        self.robot1 = pygame.image.load(robot_image_filename).convert_alpha()
        self.robot2 = pygame.image.load(robot_image_filename).convert_alpha()
        self.robot3 = pygame.image.load(robot_image_filename).convert_alpha()
        self.robot4 = pygame.image.load(robot_image_filename).convert_alpha()
        # initialize the position of robots
        self.robotInitialPos = [robot1Pos, robot2Pos, robot3Pos, robot4Pos]  # used in reset
        self.robot1Pos = robot1Pos
        self.robot2Pos = robot2Pos
        self.robot3Pos = robot3Pos
        self.robot4Pos = robot4Pos

    def move_robot(self, robot1Pos=None, robot2Pos=None, robot3Pos=None, robot4Pos=None):
        """
        move robots in the GUI
        :return:
        """
        if robot1Pos is not None:
            self.robot1Pos = robot1Pos
        if robot2Pos is not None:
            self.robot2Pos = robot2Pos
        if robot3Pos is not None:
            self.robot3Pos = robot3Pos
        if robot4Pos is not None:
            self.robot4Pos = robot4Pos
        self.update()

    def quit_game(self):
        pygame.display.quit()
        pygame.quit()

    def reset_robot(self):
        """
        reset robots' position
        :return: None
        """
        self.robot1Pos = self.robotInitialPos[0]
        self.robot2Pos = self.robotInitialPos[1]
        self.robot3Pos = self.robotInitialPos[2]
        self.robot4Pos = self.robotInitialPos[3]

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        # 绘制背景
        self.screen.blit(self.background, (0, 0))
        # 绘制小车
        self.screen.blit(pygame.transform.rotate(self.robot1, 0), [self.robot1Pos[0]-IMAGE_OFFSET, self.robot1Pos[1]-IMAGE_OFFSET])
        self.screen.blit(pygame.transform.rotate(self.robot2, 0), [self.robot2Pos[0]-IMAGE_OFFSET, self.robot2Pos[1]-IMAGE_OFFSET])
        self.screen.blit(pygame.transform.rotate(self.robot3, 0), [self.robot3Pos[0]-IMAGE_OFFSET, self.robot3Pos[1]-IMAGE_OFFSET])
        self.screen.blit(pygame.transform.rotate(self.robot4, 0), [self.robot4Pos[0]-IMAGE_OFFSET, self.robot4Pos[1]-IMAGE_OFFSET])
        # 刷新画面
        pygame.display.update()



if __name__ == '__main__':
    MapView2D()
