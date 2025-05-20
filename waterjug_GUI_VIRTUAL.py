import pygame
import sys
import random
import time

def draw_jug(screen, x, y, width, height, water_level, color, text):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height), 3)  # Jug outline
    pygame.draw.rect(screen, color, (x, y + (height - water_level), width, water_level))  # Water level
    font = pygame.font.Font(None, 30)
    label = font.render(text, True, (0, 0, 0))
    screen.blit(label, (x + width // 4, y - 30))

def draw_fireworks(screen):
    for _ in range(10):
        x, y = random.randint(100, 800), random.randint(100, 500)
        color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)])
        pygame.draw.circle(screen, color, (x, y), random.randint(5, 15))

def animate_transfer(screen, jug_a, jug_b, new_a, new_b, color_a, color_b):
    steps = 10
    diff_a = (new_a - jug_a) / steps
    diff_b = (new_b - jug_b) / steps
    for i in range(steps):
        screen.fill((150, 200, 250))
        draw_jug(screen, 250, 100, 100, 200, int((jug_a + diff_a * i) * 50), color_a, f"A: {int(jug_a + diff_a * i)}")
        draw_jug(screen, 500, 100, 100, 200, int((jug_b + diff_b * i) * 50), color_b, f"B: {int(jug_b + diff_b * i)}")
        pygame.display.flip()
        time.sleep(0.05)

def water_jug_game():
    pygame.init()
    screen = pygame.display.set_mode((900, 600), pygame.FULLSCREEN)
    pygame.display.set_caption("Water Jug Game")
    clock = pygame.time.Clock()
    
    jug_a_capacity, jug_b_capacity = 4, 3
    jug_a, jug_b = 0, 0
    goal_a, goal_b = 2, 0
    
    font = pygame.font.Font(None, 36)
    color_a, color_b = (0, 0, 255), (0, 255, 255)
    
    buttons = [
        ("Fill Jug A", 50, 500),
        ("Fill Jug B", 200, 500),
        ("Empty Jug A", 350, 500),
        ("Empty Jug B", 500, 500),
        ("Pour A -> B", 50, 550),
        ("Pour B -> A", 200, 550)
    ]
    
    goal_reached = False
    
    while True:
        screen.fill((150, 200, 250))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not goal_reached:
                    x, y = event.pos
                    for i, (text, bx, by) in enumerate(buttons):
                        if bx <= x <= bx + 140 and by <= y <= by + 40:
                            new_a, new_b = jug_a, jug_b
                            if i == 0:
                                new_a = jug_a_capacity
                            elif i == 1:
                                new_b = jug_b_capacity
                            elif i == 2:
                                new_a = 0
                            elif i == 3:
                                new_b = 0
                            elif i == 4:
                                transfer = min(jug_a, jug_b_capacity - jug_b)
                                new_a = jug_a - transfer
                                new_b = jug_b + transfer
                            elif i == 5:
                                transfer = min(jug_b, jug_a_capacity - jug_a)
                                new_b = jug_b - transfer
                                new_a = jug_a + transfer
                            animate_transfer(screen, jug_a, jug_b, new_a, new_b, color_a, color_b)
                            jug_a, jug_b = new_a, new_b
        
        draw_jug(screen, 250, 100, 100, 200, jug_a * 50, color_a, f"A: {jug_a}")
        draw_jug(screen, 500, 100, 100, 200, jug_b * 50, color_b, f"B: {jug_b}")
        
        for text, bx, by in buttons:
            pygame.draw.rect(screen, (50, 150, 50), (bx, by, 140, 40))
            button_text = font.render(text, True, (255, 255, 255))
            screen.blit(button_text, (bx + 10, by + 10))
        
        if (jug_a, jug_b) == (goal_a, goal_b):
            goal_reached = True
            win_text = font.render("Goal Reached!", True, (0, 200, 0))
            screen.blit(win_text, (350, 400))
            draw_fireworks(screen)
            pygame.display.flip()
            time.sleep(1)
            return water_jug_game()
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    water_jug_game()
