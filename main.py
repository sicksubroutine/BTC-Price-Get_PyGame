import pygame
import pygame.freetype
import time
from btc_price import *
from key_input import *

pygame.init()
screen = pygame.display.set_mode((550, 250))
pygame.display.set_caption("Convert Your Sats!")
clock = pygame.time.Clock()
GAME_FONT = pygame.freetype.SysFont("Arial", 20)
running =  True
SATS = 0.00000001
FULL_BTC = 100000000
state = "start"
font = pygame.font.Font(None, 32)
input_box = pygame.Rect(100, 100, 140, 32)
active = False
text = ''
btc_logo = pygame.image.load("images/btc_logo.png")
btc_logo = pygame.transform.scale(btc_logo, (100, 100))
icon = pygame.image.load("images/btc_logo.png")
icon = pygame.transform.scale(icon, (25, 25))
pygame.display.set_icon(icon)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive


def state_machine():
  if state == "start":
    start()
  elif state == "satsToUsd":
    sats_update()
  elif state == "sats_input":
    sats_input()  
  elif state == "usd_input":
    usd_input() 
  elif state == "usdToSats":
    usd_update()
    return
  else:
    print("Error: Invalid state")

def start():
  global number, state, btc_logo
  number = btc_price_get()
  btc_logo = pygame.image.load("images/btc_logo.png")
  btc_logo = pygame.transform.scale(btc_logo, (100, 100))
  screen.fill((0,0,0))
  GAME_FONT.render_to(screen, (10, 25), "Current Bitcoin Price: ", (255, 255, 255))
  GAME_FONT.render_to(screen, (225, 25), "$" + str(number), (124, 252, 0))
  GAME_FONT.render_to(screen, (10, 50), "Press 1 to Convert USD Amounts into Sats", (255, 255, 255))
  GAME_FONT.render_to(screen, (10, 75), "Press 2 to Convert Sats into USD Amounts", (255, 255, 255))
  GAME_FONT.render_to(screen, (10, 100), "Press 3 to Exit", (255, 255, 255))
  screen.blit(btc_logo, (450, 10))
  pygame.display.flip()


def sats_update():
  price = btc_price_get()
  answer = what_amount * SATS
  answer2 = round(answer * price, 2)
  screen.fill((0,0,0))
  GAME_FONT.render_to(screen, (10, 25), "Current Bitcoin Price: ", (255, 255, 255))
  GAME_FONT.render_to(screen, (225, 25), "$" + str(price), (124, 252, 0))
  GAME_FONT.render_to(screen, (10, 50), "You input " + str(what_amount) + " sats.", (255, 255, 255))
  GAME_FONT.render_to(screen, (10, 75), "That equals: " + "$" + str(answer2) + "!", (255, 255, 255))
  screen.blit(btc_logo, (450, 10))
  pygame.display.flip()

def sats_input():
  price = btc_price_get()
  if active:
    color = color_active
  else:
    color = color_passive
  screen.fill((0,0,0))
  GAME_FONT.render_to(screen, (10, 25), "Current Bitcoin Price: ", (255, 255, 255))
  GAME_FONT.render_to(screen, (225, 25), "$" + str(price), (124, 252, 0))
  GAME_FONT.render_to(screen, (10, 80), "Input the amount of Sats:", (255, 255, 255))
  GAME_FONT.render_to(screen, (40, 140), "Click here ^", (255, 255, 255))
  screen.blit(btc_logo, (450, 10))
  txt_surface = font.render(text, True, color)
  # Resize the box if the text is too long.
  width = max(200, txt_surface.get_width()+10)
  input_box.w = width
  # Blit the text.
  screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
  # Blit the input_box rect.
  pygame.draw.rect(screen, color, input_box, 2)
  # draw cursor when active
  pygame.display.flip()
  

def usd_input():
  price = btc_price_get()
  screen.fill((0,0,0))
  if active:
    color = color_active
  else:
    color = color_passive
  GAME_FONT.render_to(screen, (10, 25), "Current Bitcoin Price: ", (255, 255, 255))
  GAME_FONT.render_to(screen, (225, 25), "$" + str(price), (124, 252, 0))
  GAME_FONT.render_to(screen, (10, 80), "Input an amount of USD:", (255, 255, 255))
  GAME_FONT.render_to(screen, (40, 140), "Click here ^", (255, 255, 255))
  screen.blit(btc_logo, (450, 10))
  txt_surface = font.render(text, True, color)
  # Resize the box if the text is too long.
  width = max(200, txt_surface.get_width()+10)
  input_box.w = width
  # Blit the text.
  screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
  # Blit the input_box rect.
  pygame.draw.rect(screen, color, input_box, 2)
  pygame.display.flip()
  
def usd_update():
  price = btc_price_get()
  screen.fill((0,0,0))
  USD = round(what_amount, 2)
  btc_amount = (USD / price) / SATS
  btc_amount = round(btc_amount)
  a = float(round(btc_amount / FULL_BTC, 8))
  GAME_FONT.render_to(screen, (10, 25), "Current Bitcoin Price: ", (255, 255, 255))
  GAME_FONT.render_to(screen, (225, 25), "$" + str(price), (124, 252, 0))
  GAME_FONT.render_to(screen, (10, 80), "You input $" + str(USD) + ".", (255, 255, 255))
  GAME_FONT.render_to(screen, (10, 100), "That equates to " + str(btc_amount) + " sats!", (255, 255, 255))
  GAME_FONT.render_to(screen, (10, 125), "That equals: " + str('{:.8f}'.format(a)) + " BTC!", (255, 255, 255))
  screen.blit(btc_logo, (450, 10))
  pygame.display.flip()

def exit_screen():
  screen.fill((0,0,0))
  GAME_FONT.render_to(screen, (10, 25), "Goodbye!", (255, 255, 255))
  screen.blit(btc_logo, (450, 10))
  pygame.display.flip()
  
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      if input_box.collidepoint(event.pos):
        active = not active
      else:
        active = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_2 and state == "start":
        text = ""
        state = "sats_input"
      elif event.key == pygame.K_1 and state == "start":
        text = ""
        state = "usd_input"
      elif event.key == pygame.K_3 and state == "start":
        exit_screen()
        time.sleep(2)
        running = False
      if active:
        if event.key == pygame.K_RETURN:
          if text != "" and state == "sats_input":
            what_amount = int(text)
            state = "satsToUsd"
          elif text!= "" and state == "usd_input":
            what_amount = float(text)
            state = "usdToSats"
          else:
            print("not in an input state")
        
        elif event.key == pygame.K_BACKSPACE:
          text = text[:-1]
        else:
          text += event.unicode    
  state_machine()
  clock.tick(60)  
pygame.quit()