import pygame
from pygame.locals import *

background_image_filename = 'images/map.png'
robot_image_filename = 'images/robot.png'
MAP_SIZE = (800, 500)

class MapView2D:

    def __init__(self, map_name="RoboMaster Simulation"):
        pygame.init()
        pygame.display.set_caption(map_name)
        self.clock = pygame.time.Clock()
        self._game_over = False

        self.screen = pygame.display.set_mode(MAP_SIZE, 0, 32)
        self.background = pygame.image.load(background_image_filename).convert()
        self.robot1 = pygame.image.load(robot_image_filename).convert_alpha()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            self.update()

    def update(self, robot1Pos=[30,30]):
        # 绘制背景
        self.screen.blit(self.background, (0, 0))
        # 绘制小车
        self.screen.blit(pygame.transform.rotate(self.robot1, 0), robot1Pos)
        # 刷新画面
        pygame.display.update()

    def quit_game(self):
        pygame.display.quit()
        pygame.quit()

if __name__ == '__main__':
    MapView2D()