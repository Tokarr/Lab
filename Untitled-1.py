from pygame import*
window = display.set_mode((700, 500))
display.set_caption("ГРа")

class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect_x = x
        self.rect_y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

wall1 = GameSprite('wall.jpg',80,180,250,400)
pacman = Player('pac-3.png', 40, 40, 100, 100, 0, 0)




run = True
while run:
    window.fill((250,250,250))
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                pacman.y_speed = -5
            if e.key == K_DOWN:
                pacman.y_speed = 5
            if e.key == K_LEFT:
                pacman.x_speed = -5
            if e.key == K_RIGHT:
                pacman.x_speed = 5
        elif e.type == KEYUP:
            if e.key == K_UP:
                pacman.y_speed = 0
            if e.key == K_DOWN:
                pacman.y_speed = 0
            if e.key == K_LEFT:
                pacman.x_speed = 0
            if e.key == K_RIGHT:
                pacman.x_speed = 0
    wall1.reset()
    pacman.update()
    pacman.reset()
    display.update()

