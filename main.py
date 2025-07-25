import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        
    def add_points(self, points):
        self.score += points
        
    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)    
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()



    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    score = Score()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for bullet in shots:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    points = int(100 - asteroid.radius) * 10  # Larger asteroids = fewer points
                    score.add_points(max(points, 10))
                    asteroid.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        score.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
