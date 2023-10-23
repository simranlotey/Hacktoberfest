from pygame.locals import *
import pygame
import time
import random

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3
        self.image = pygame.image.load("./resources/apple.jpg").convert()

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 19) * SIZE
        self.y = random.randint(1, 14) * SIZE

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("./resources/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'

    def increase_len(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        self.draw()

    def draw(self):
        self.parent_screen.fill((145, 50, 168))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.crash_sound = pygame.mixer.Sound("./resources/crash.mp3")
        self.ding_sound = pygame.mixer.Sound("./resources/ding.mp3")
        self.apple.draw()
        self.running = True

    def display_score(self):
        font = pygame.font.SysFont("arial", 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (800, 100))

    def play(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                if event.key == K_LEFT:
                    self.snake.move_left()
                if event.key == K_RIGHT:
                    self.snake.move_right()
                if event.key == K_UP:
                    self.snake.move_up()
                if event.key == K_DOWN:
                    self.snake.move_down()
            elif event.type == QUIT:
                self.running = False
        if self.running:
            self.snake.walk()
            self.apple.draw()
            self.display_score()
            pygame.display.flip()
            for i in range(self.snake.length):
                if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
                    self.snake.increase_len()
                    self.apple.move()
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.surface.get_width(), self.surface.get_height()):
                print("Game over")
                self.running = False
            time.sleep(0.2)

    def is_collision(self, x1, y1, x2, y2):
     if x1 == 0 or x1 == self.surface.get_width() - SIZE or y1 == 0 or y1 == self.surface.get_height() - SIZE:
        self.crash_sound.play()
        return True
     if x1 == x2 and y1 == y2:
        self.ding_sound.play()
        return True
     return False




    def run(self):
        while self.running:
            self.play()

if __name__ == '__main__':
    game = Game()
    game.run()




