import pygame
pygame.init()

#overall size
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Frog Mail Delivery")
running = True

# Frog
frog_x = 100
frog_y = 300
frog_size = 40

# Letter
letter_x = 400
letter_y = 250
letter_size = 20

# Pick up the letter 
has_letter = False

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Make the frog move
  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    frog_x -= 5
  if keys[pygame.K_RIGHT]:
    frog_x += 5
  if keys[pygame.K_UP]:
    frog_y -= 5
  if keys[pygame.K_DOWN]:
    frog_y += 5
  
  frog_x = max(0, min(frog_x, WIDTH - frog_size))
  frog_y = max(0, min(frog_y, HEIGHT - frog_size))

  # Letter pick
  frog_rect = pygame.Rect(
    frog_x,
    frog_y,
    frog_size,
    frog_size
  )
  
  letter_rect = pygame.Rect(
    letter_x,
    letter_y,
    letter_size,
    letter_size
  )

  if frog_rect.colliderect(letter_rect):
    has_letter = True

  screen.fill((100 , 180 , 255))
  pygame.draw.rect(screen , (0,255,0), (frog_x,frog_y,frog_size,frog_size))
  if not has_letter:
    pygame.draw.rect(screen , (255,255,0) , (letter_x,letter_y,letter_size,letter_size))

  pygame.display.update()

pygame.quit()