import pygame

pygame.init()

# ---------- SCREEN ----------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Players")
clock = pygame.time.Clock()

# ---------- PLAYER CLASS ----------
class Player:
    def __init__(self, x, y, color):
        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)
        self.color = color
        self.radius = 20

        self.acceleration = 0.5
        self.max_speed = 6
        self.friction = 0.9

    def apply_input(self, dx, dy):
        accel_vec = pygame.Vector2(dx, dy)
        if accel_vec.length() > 0:
            accel_vec.normalize_ip()
            self.vel += accel_vec * self.acceleration

    def update(self):
        if self.vel.length() > self.max_speed:
            self.vel.scale_to_length(self.max_speed)

        self.pos += self.vel
        self.vel *= self.friction

        self.handle_wall_collision()

    def handle_wall_collision(self):
        if self.pos.x - self.radius <= 0 or self.pos.x + self.radius >= WIDTH:
            self.vel.x *= -1
        if self.pos.y - self.radius <= 0 or self.pos.y + self.radius >= HEIGHT:
            self.vel.y *= -1

        self.pos.x = max(self.radius, min(WIDTH - self.radius, self.pos.x))
        self.pos.y = max(self.radius, min(HEIGHT - self.radius, self.pos.y))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def collide(self, other):
        delta = self.pos - other.pos
        distance = delta.length()

        if distance < self.radius + other.radius and distance != 0:
            normal = delta.normalize()

            self_vel = self.vel.dot(normal)
            other_vel = other.vel.dot(normal)

            self.vel += (other_vel - self_vel) * normal
            other.vel += (self_vel - other_vel) * normal

            overlap = self.radius + other.radius - distance
            self.pos += normal * (overlap / 2)
            other.pos -= normal * (overlap / 2)


# ---------- CREATE 4 PLAYERS ----------
players = [
    Player(150, 300, (28, 231, 235)),   # Player R
    Player(300, 200, (101, 214, 111)),  # Player M
    Player(500, 300, (163, 88, 161)),   # Player N
    Player(650, 200, (199, 0, 0))       # Player K
]

# ---------- GAME LOOP ----------
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ----- INPUT (WASD controls Player 0) -----
    keys = pygame.key.get_pressed()
    dx = dy = 0
    if keys[pygame.K_w]:
        dy = -1
    if keys[pygame.K_s]:
        dy = 1
    if keys[pygame.K_a]:
        dx = -1
    if keys[pygame.K_d]:
        dx = 1

    players[0].apply_input(dx, dy)

    # ----- UPDATE -----
    for player in players:
        player.update()

    # ----- COLLISIONS -----
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            players[i].collide(players[j])

    # ----- DRAW -----
    screen.fill((30, 30, 30))
    for player in players:
        player.draw(screen)

    pygame.display.flip()

pygame.quit()
