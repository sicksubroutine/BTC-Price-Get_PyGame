import pygame

def key_input(event):
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_1:
      return 1
    elif event.key == pygame.K_2:
      return 2
    elif event.key == pygame.K_3:
      return 3
    elif event.key == pygame.K_4:
      return 4
    elif event.key == pygame.K_5:
      return 5
    elif event.key == pygame.K_6:
      return 6
    elif event.key == pygame.K_7:
      return 7
    elif event.key == pygame.K_8:
      return 8
    elif event.key == pygame.K_9:
      return 9
    elif event.key == pygame.K_0:
      return 0
    elif event.key == pygame.K_MINUS:
      return "-"
    elif event.key == pygame.K_EQUALS:
      return "="
    elif event.key == pygame.K_BACKSPACE:
      return "BACK"
    elif event.key == pygame.K_TAB:
      return "TAB"
    elif event.key == pygame.K_s:
      return "S"
    elif event.key == pygame.K_w:
      return "W"