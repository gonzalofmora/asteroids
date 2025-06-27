# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
#   print("Starting Asteroids!")
#   print(f"Screen width: {SCREEN_WIDTH}")
#   print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        for object in updatable:
            object.update(dt)
        for asteroid in asteroids:
            if asteroid.has_collided(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                print("Ast: ", asteroid.position, asteroid.radius, "Shot: ", shot.position, shot.radius)
                if asteroid.has_collided(shot):
                    asteroid.kill()
                    shot.kill()
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick / 1000


if __name__ == "__main__":
    main()

