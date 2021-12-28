import pygame

# initialize pygame
pygame.init()

WIDTH, HEIGHT = 1200, 900

# create the screen (width, height)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Color Pallet
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
VIOLET = (153, 0, 76)
PINK = (255, 102, 102)
TEAL = (153, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FONTS
FONT = pygame.font.Font('CutiveMono-Regular.ttf', 25)

# Title and Icon
pygame.display.set_caption("HANGMAN")
icon = pygame.image.load('hangman.png')
pygame.display.set_icon(icon)

# Stick Images & Resizing
HEAD_IMAGE = pygame.image.load('stickhead.png')
HEAD = pygame.transform.scale(HEAD_IMAGE, (50, 40))

BODY_IMAGE = pygame.image.load('stickbody.png')
BODY = pygame.transform.scale(BODY_IMAGE, (50, 40))

RIGHT_ARM_IMAGE = pygame.image.load('strickrightarm.png')
RIGHT_ARM = pygame.transform.scale(RIGHT_ARM_IMAGE, (50, 40))

LEFT_ARM_IMAGE = pygame.image.load('stickleftarm.png')
LEFT_ARM = pygame.transform.scale(LEFT_ARM_IMAGE, (50, 40))

RIGHT_LEG_IMAGE = pygame.image.load('stickrightleg.png')
RIGHT_LEG = pygame.transform.scale(RIGHT_LEG_IMAGE, (50, 40))

LEFT_LEG_IMAGE = pygame.image.load('stickleftleg.png')
LEFT_LEG = pygame.transform.scale(LEFT_LEG_IMAGE, (50, 40))

FRAME_IMAGE = pygame.image.load('StickFrame.png')
FRAME = pygame.transform.scale(FRAME_IMAGE, (350, 450))

FPS = 60

SELECT_TEXT = FONT.render('SELECT A LETTER!', True, BLACK)


def draw_lines(word):
    pass


def draw_window():
    WIN.fill(PINK)
    WIN.blit(SELECT_TEXT, (600, 100))
    WIN.blit(FRAME, (50, 50))
    pygame.display.update()


# Game Loop
def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # if event.type == pygame.MOUSEBUTTONDOWN:

        # RGB - Red, Green, Blue
        draw_window()


if __name__ == "__main__":
    main()
