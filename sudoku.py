import pygame
import sys
import constants
#from sudoku_generator import SudokuGenerator

background_color = (255, 255, 255)
def start_screen(win, start_title_font, button_font):

    win.fill(background_color)
    title_surface = start_title_font.render("Welcome to Sudoku", 0, constants.LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center = (constants.WIDTH // 2, constants.HEIGHT // 2 - 150))
    win.blit(title_surface, title_rectangle)


    selection_text = button_font.render("Select Game Mode:", 0, (255, 255, 255))
    easy_text = button_font.render("EASY", 0, (255, 255, 255))
    medium_text = button_font.render("MEDIUM", 0, (255, 255, 255))
    hard_text = button_font.render("HARD", 0, (255, 255, 255))


    selection_text_surface = pygame.Surface((selection_text.get_size()[0] + 20, selection_text.get_size()[1] + 20))

    selection_text_surface.fill(constants.LINE_COLOR)

    selection_text_surface.blit(selection_text, (10, 10))

    selection_rect = selection_text_surface.get_rect(center = (constants.WIDTH // 2, constants.HEIGHT // 2 + 100))

    win.blit(selection_text_surface, selection_rect)

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))

    easy_surface.fill(constants.LINE_COLOR)

    easy_surface.blit(easy_text, (10, 10)) # area of text (inside orange rectangle)

    easy_rect = easy_surface.get_rect(center = (145, 600))

    win.blit(easy_surface, easy_rect)

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))

    medium_surface.fill(constants.LINE_COLOR)

    medium_surface.blit(medium_text, (10, 10))

    medium_rect = medium_surface.get_rect(center = (constants.WIDTH // 2, constants.HEIGHT // 2 + 250))

    win.blit(medium_surface, medium_rect)

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))

    hard_surface.fill(constants.LINE_COLOR)

    hard_surface.blit(hard_text, (10, 10))

    hard_rect = hard_surface.get_rect(center = (560, 600))

    win.blit(hard_surface, hard_rect)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            return

        if event.type == pygame.MOUSEBUTTONDOWN:

            if easy_rect.collidepoint(event.pos):
                return game_screen(win, button_font)

            elif medium_rect.collidepoint(event.pos):
                return game_screen(win, button_font)

            elif hard_rect.collidepoint(event.pos):
                return game_screen(win, button_font)

    return easy_rect, medium_rect, hard_rect


def game_screen(win, button_font):

    win.fill(background_color)
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:

                if reset_rect.collidepoint(event.pos):
                    return game_screen(win, button_font)

                elif restart_rect.collidepoint(event.pos):
                    return

                elif exit_rect.collidepoint(event.pos):
                    sys.exit()


        for i in range(0, 10):
            # for every 3rd line draw a bold line

            if i % 3 == 0:
                pygame.draw.line(win, (0, 0, 0), [50 + 50 * i, 50], [50 + 50 * i, 500], 4)
                pygame.draw.line(win, (0, 0, 0), [50, 50 + 50 * i], [500, 50 + 50 * i], 4)

            pygame.draw.line(win, (0, 0, 0), [50 + 50 * i, 50], [50 + 50 * i, 500], 2) #50 + 50 * i, 50
            pygame.draw.line(win, (0, 0, 0), [50, 50 + 50 * i], [500, 50 + 50 * i], 2)

            reset_text = button_font.render("RESET", 0, (255, 255, 255))
            restart_text = button_font.render("RESTART", 0, (255, 255, 255))
            exit_text = button_font.render("EXIT", 0, (255, 255, 255))

            reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))

            reset_surface.fill(constants.LINE_COLOR)

            reset_surface.blit(reset_text, (10, 10))  # area of text (inside orange rectangle)

            reset_rect = reset_surface.get_rect(center=(120, 600))

            win.blit(reset_surface, reset_rect)

            restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))

            restart_surface.fill(constants.LINE_COLOR)

            restart_surface.blit(restart_text, (10, 10))  # area of text (inside orange rectangle)

            restart_rect = restart_surface.get_rect(center=(constants.WIDTH // 2, constants.HEIGHT // 2 + 250))

            win.blit(restart_surface, restart_rect)

            exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))

            exit_surface.fill(constants.LINE_COLOR)

            exit_surface.blit(exit_text, (10, 10))  # area of text (inside orange rectangle)

            exit_rect = exit_surface.get_rect(center=(560, 600))

            win.blit(exit_surface, exit_rect)

            pygame.display.update()


GameState = "START"
def main():

    pygame.init()
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)
    win = pygame.display.set_mode([constants.WIDTH, constants.HEIGHT])
    pygame.display.set_caption("Sudoku")
    font = pygame.font.SysFont('Comic Sans MS', 35)

    while True:

        if GameState == "START":

            start_screen(win, start_title_font, button_font)
            #easy_rect, medium_rect, hard_rect = shut down the program



            # keys = pygame.key.get_pressed()
                #
                # if keys[pygame.K_1]:
                #     pass
                #
                # if key[pygame.K_2]:
                #     pass
                #
                # if key[pygame.K_3]:
                #     pass
                #
                # if key[pygame.K_4]:
                #     pass
                #
                # if key[pygame.K_5]:
                #     pass
                #
                # if key[pygame.K_6]:
                #     pass
                #
                # if key[pygame.K_7]:
                #     pass
                #
                # if key[pygame.K_8]:
                #     pass
                #
                # if key[pygame.K_9]:
                #     pass
                #
                # if key[K_RETURN]:
                #     pass
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             sys.exit()


        pygame.display.update()

        # for event in pygame.event.get():

            # if event.type == pygame.QUIT:
            #     pygame.quit()
            #     return



main()