
import time
import pygame 
import numpy as np 
import random

color_bg = (0, 0, 0)
color_grid = (60, 60, 60)
color_cell = (255, 255, 0)


def update(screen, box, size, with_progress=False):

    updated_cells = np.zeros((box.shape[0], box.shape[1]))

    for row, col in np.ndindex(box.shape):
        alive = np.sum(box[row - 1:row + 2, col - 1:col + 2]) - box[row, col]
        color = color_bg if box[row, col] == 0 else color_cell

        if box[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = color_cell
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = tuple(random.randint(0, 255) for _ in range(3))  
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = tuple(random.randint(0, 255) for _ in range(3))  

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    box = np.zeros((60, 80))
    screen.fill(color_grid)
    update(screen, box, 10)
    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, box, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                box[pos[1] // 10, pos[0] // 10] = 1
                update(screen, box, 10)
                pygame.display.update()

        screen.fill(color_grid)

        if running:
            box = update(screen, box, 10, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)


if __name__ == '__main__':
    main()
