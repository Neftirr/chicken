from pygame import *
from random import randint, choice
class GameSprite(sprite.Sprite):
    def __init__(self, img, x,y,w,h, speed):
        super().__init__()
        self. image = transform.scale(image.load(img), (w,h))
        self.rect= self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.rect.h = h
        self.rect.w = w
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Food(GameSprite):
    def __init__(self, img, x,y,w,h, speed):
        super().__init__(img, x,y,w,h, speed)
        self.images = list()
        self.images.append(self.image)
        
    def add_image(self, img):
        w = self.rect.width
        h = self.rect.height
        new_image = transform.scale(image.load(img), (w,h))
        self.images.append(new_image)

    def new_position(self):
        self.rect.x = randint(5,700-5-self.rect.width)
        self.rect.y = randint(5,500-5-self.rect.height)
        self.image = choice(self.images)
    
class Snake(GameSprite):
    def __init__(self, img, x,y,w,h, speed):
        super().__init__(img, x,y,w,h, speed)
        self.images = list()
        self.images.append(self.image)
        for i in range(3):
            self.image = transform.rotate(self.image, 90)
            self.images.append(self.image)
    def update(self,direction):
        if direction == 'left':
            self.rect.x -= self.speed
            self.image = self.images[1]
        elif direction == 'right':
            self.rect.x += self.speed
            self.image = self.images[3]
        elif direction == 'down':
            self.rect.y += self.speed
            self.image = self.images[2]
        elif direction == 'up':
            self.rect.y -= self.speed
            self.image = self.images[0]
            
            

         



        


back = (4, 0, 0)

window = display.set_mode((700,500))
display.set_caption('Курица')
clock = time.Clock()
FPS = 60

my_food = Food('ny_blin2.png', 100, 100, 100, 50, 0)
my_food.add_image('ny_blin3.png')
head = Snake('ny_blin.png', 350, 250, 60, 55, 3)
tale = Snake('ny_blin1.png', -100, -100, 60, 55, 0)






game = True
direction = 'stop'
finish = False
eat = 0
snake = [head]

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_q:
            my_food.new_position()
        if e.type == KEYDOWN:
            if e.key == K_w:
                direction = 'up'
        if e.type == KEYDOWN:
            if e.key == K_s:
                direction = 'down'
        if e.type == KEYDOWN:
            if e.key == K_a:
                direction = 'left'
        if e.type == KEYDOWN:
            if e.key == K_d:
                direction = 'right'

    if finish != True:
        window.fill(back)
        my_food.reset()
        for i in range(len(snake)-1, 0, -1):
            snake[1].rect.x = snake[i-1].rect.x
            snake[1].rect.y = snake[i-1].rect.y
            snake[i].reset()
        head.update(direction)
        head.reset()

        if head.rect.x<5 or head.rect.x>700-50:
            finish = True
        if head.rect.y<5 or head.rect.y>700-50:
            finish = True
        if head.rect.colliderect(my_food.rect):
            my_food.new_position()
            eat += 1
            tale.rect.x = head.rect.x
            tale.rect.y = head.rect.y
            snake.append(tale)


    display.update()
    clock.tick(FPS)