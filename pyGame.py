import pygame, sys, math
from pygame.locals import *

# import Box2D # The main library
from Box2D import *

# --- constants ---
TARGET_FPS = 60
TIME_STEP = 1.0 /TARGET_FPS
screenXY = SCREEN_WIDTH, SCREEN_HEIGHT = 1140, 480
GREEN = (116, 255, 51)
vel_iters, pos_iters = 6, 2

# --- pygame setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Simple pygame example')
world = b2World(gravity=(0.0, 5.0), doSleep=True)
clock = pygame.time.Clock()

groundBodyDef = b2BodyDef()
groundBodyDef.position = (0, 200)

groundBody = world.CreateBody(groundBodyDef)

groundBox = b2PolygonShape(box=(SCREEN_WIDTH, 10))

groundBoxFixture = b2FixtureDef(shape=groundBox)

groundBody.CreateFixture(groundBoxFixture)


body = world.CreateDynamicBody(position=(100,0))
body.mass = 10



box = body.CreatePolygonFixture(box=(10, 10), density=1,friction=0.09)



while True:
    keypressed = pygame.key.get_pressed()
    if keypressed[K_RIGHT]:
        body.ApplyForce(force=(600,0),point=(body.position[0],body.position[1]),wake=True)
    if keypressed[K_LEFT]:
        body.ApplyForce(force=(-600,0),point=(body.position[0],body.position[1]),wake=True)
    if keypressed[K_SPACE]:
        body.ApplyForce(force=(0,-9999),point=(body.position[0],body.position[1]),wake=True)
    screen.fill((0,0,0))
    pygame.draw.rect(screen, GREEN, (groundBody.position[0],groundBody.position[1],SCREEN_WIDTH,10*2))
    pygame.draw.rect(screen, GREEN, (math.ceil(body.position[0]),math.ceil(body.position[1]),10,10*2))
    #print(body.position, body.angle)
    for event in pygame.event.get():
        if event.type == QUIT:
            clock.tick(TARGET_FPS)
            print('Done!')
            pygame.quit()
            sys.exit()
    world.Step(TIME_STEP, vel_iters, pos_iters)
    world.ClearForces()
    pygame.display.flip()



