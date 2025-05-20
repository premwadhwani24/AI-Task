import pygame
import time
import os

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkey and Banana Animation")

# Image filenames
image_files = {
    "monkey.png":"C:\\Users\\Toshiba x360\\Downloads\\monkey.jpg" ,
    "box.png": "C:\\Users\\Toshiba x360\\Downloads\\box.jpg",
    "banana.png": "C:\\Users\\Toshiba x360\\Downloads\\banana.jpg"
}

# Check if images exist, otherwise prompt user
for filename in image_files.values():
    if not os.path.exists(filename):
        print(f"Please download and place {filename} in the same directory.")
        exit()

# Load images
monkey_img = pygame.image.load("C:\\Users\\Toshiba x360\\Downloads\\monkey.jpg")
box_img = pygame.image.load("C:\\Users\\Toshiba x360\\Downloads\\box.jpg")
banana_img = pygame.image.load("C:\\Users\\Toshiba x360\\Downloads\\banana.jpg")

# Resize images
monkey_img = pygame.transform.scale(monkey_img, (80, 80))
box_img = pygame.transform.scale(box_img, (100, 60))
banana_img = pygame.transform.scale(banana_img, (50, 50))

# Positions
monkey_x, monkey_y = 100, 400
box_x, box_y = 300, 450
banana_x, banana_y = 320, 250

def draw_scene():
    screen.fill((135, 206, 250))  # Light blue background
    screen.blit(box_img, (box_x, box_y))
    screen.blit(banana_img, (banana_x, banana_y))
    screen.blit(monkey_img, (monkey_x, monkey_y))
    pygame.display.update()

def move_monkey(target_x, target_y):
    global monkey_x, monkey_y
    step = 5
    while monkey_x != target_x or monkey_y != target_y:
        if monkey_x < target_x:
            monkey_x += step
        elif monkey_x > target_x:
            monkey_x -= step
        if monkey_y < target_y:
            monkey_y += step
        elif monkey_y > target_y:
            monkey_y -= step
        draw_scene()
        time.sleep(0.05)

def main():
    running = True
    draw_scene()
    time.sleep(1)

    # Step 1: Move monkey to the box
    move_monkey(box_x, 400)
    time.sleep(1)

    # Step 2: Climb the box
    move_monkey(box_x, box_y - 30)
    time.sleep(1)

    # Step 3: Reach for the banana
    move_monkey(banana_x, banana_y - 10)
    time.sleep(1)

    # Step 4: Grab the banana
    print("Monkey got the banana!")
    time.sleep(2)
    pygame.quit()

if __name__ == "__main__":
    main()
