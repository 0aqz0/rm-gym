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
        self.robot2 = pygame.image.load(robot_image_filename).convert_alpha()
        self.robot3 = pygame.image.load(robot_image_filename).convert_alpha()
        self.robot4 = pygame.image.load(robot_image_filename).convert_alpha()
        if __name__ == '__main__':     # weird
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                self.update()

    def update(self, robot1Pos=[30,30], robot2Pos=[700,30], robot3Pos=[30,400], robot4Pos=[700,400]):
        # 绘制背景
        self.screen.blit(self.background, (0, 0))
        # 绘制小车
        self.screen.blit(pygame.transform.rotate(self.robot1, 0), robot1Pos)
        self.screen.blit(pygame.transform.rotate(self.robot2, 0), robot2Pos)
        self.screen.blit(pygame.transform.rotate(self.robot3, 0), robot3Pos)
        self.screen.blit(pygame.transform.rotate(self.robot4, 0), robot4Pos)
        # 刷新画面
        pygame.display.update()

    def quit_game(self):
        pygame.display.quit()
        pygame.quit()

if __name__ == '__main__':
    MapView2D()