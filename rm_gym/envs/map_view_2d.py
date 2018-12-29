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
    def __init__(self, map_name="RoboMaster Simulation"):
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
        # if __name__ == '__main__':     # weird
        #     while True:
        #         for event in pygame.event.get():
        #             if event.type == QUIT:
        #                 exit()
        #         self.update()

    def update(self, robot1Pos, robot2Pos, robot3Pos, robot4Pos):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        # 绘制背景
        self.screen.blit(self.background, (0, 0))
        # 绘制小车
        self.screen.blit(pygame.transform.rotate(self.robot1, 0), [robot1Pos[0]-IMAGE_OFFSET, robot1Pos[1]-IMAGE_OFFSET])
        self.screen.blit(pygame.transform.rotate(self.robot2, 0), [robot2Pos[0]-IMAGE_OFFSET, robot2Pos[1]-IMAGE_OFFSET])
        self.screen.blit(pygame.transform.rotate(self.robot3, 0), [robot3Pos[0]-IMAGE_OFFSET, robot3Pos[1]-IMAGE_OFFSET])
        self.screen.blit(pygame.transform.rotate(self.robot4, 0), [robot4Pos[0]-IMAGE_OFFSET, robot4Pos[1]-IMAGE_OFFSET])
        # 刷新画面
        pygame.display.update()

    def quit_game(self):
        pygame.display.quit()
        pygame.quit()


if __name__ == '__main__':
    MapView2D()
