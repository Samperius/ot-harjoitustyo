import pygame


class StaticSprite(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, x, y, cell_size, color):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([cell_size, cell_size])
       self.image.fill(color)
       #self.image = pygame.transform.scale(pygame.image.load("./src/visuals/track2.png"), DEFAULT_IMAGE_SIZE)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y