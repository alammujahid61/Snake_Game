import pygame
import random
import os

pygame.mixer.init()
pygame.init()

# Resolution
height=500
width=700

# window and title
window=pygame.display.set_mode((width,height)) # open output window
pygame.display.set_caption('Snake!!') # give title to the output window

#image
image=pygame.image.load('image/ground.jpg')
image=pygame.transform.scale(image,(width,height)).convert_alpha()
image_1 = pygame.image.load('image/snk.jpg')
image_1 = pygame.transform.scale(image_1, (width, height)).convert_alpha()
image_2 = pygame.image.load('image/game_over.jpg')
image_2 = pygame.transform.scale(image_2, (width, height)).convert_alpha()

def sound(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(2)

# Colour
white=(255,255,255) # rgb
red=(25,64,32) # rgb
pink=(154,32,121) # rgb
black=(0,0,0) # rgb
wao=(233,210,229)
green=(0,255,0)

clock=pygame.time.Clock() # it will frame rate move
font = pygame.font.SysFont('Harrington', 35)# set font None means default font and 55 is the font size

# Function
def display(text,colour,x,y):
    screen_text=font.render(text,True,colour)   # font.render give option to set text and is colour
    window.blit(screen_text,[x,y])  # window.blit is a function to show on the screen

def length(window,color,snake_list,snake_size):
    for i,j in snake_list:
        pygame.draw.ellipse(window,color,[i,j,snake_size,snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        window.blit(image_1,(0,0))
        display('Press 1 to play level 1',(90,19,19),195,200)
        display('Press 2 to play level 2',(90,19,19),195,250)
        display('Press q to play level Quit',(90,19,19),170,300)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    free()
                if event.key==pygame.K_2:
                    border()
                if event.key==pygame.K_q:
                    quit()

def free():
    # Variable
    x_axis = random.randint(20, width)  # position on x axis on the surface or graph
    y_axis = random.randint(20, height)  # position on y axis on the surface or graph
    snake_size = 10
    intial_velocity = 1
    velocity_x = 0  # move in the Right direction  with the speed of vilocity_x
    velocity_y = 0  # move in the Down direction  with the speed of vilocity_x
    game_over = False
    exit_game=False
    score = 0
    fbs = 45  # frame per second
    snake_length = 1
    snake_list = []

    # Food
    food_size = 10
    food_x_axis = random.randint(20, width - 10)  # position on x axis on the surface or graph
    food_y_axis = random.randint(20, height - 10)  # position on y axis on the surface or graph

    # file
    if not os.path.exists('High_Score.txt'):
        with open('High_Score.txt','w') as f:
            f.write(str(0))
    with open('High_Score.txt') as f:
        high_score=f.read()

    while not exit_game:
        if game_over:
            with open('High_Score.txt', 'w') as f:
                f.write(str(high_score))
            window.blit(image_2,(0,0))
            display('Press Enter to play', red, 210, 240)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                       welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:   # move UP
                        velocity_y=-intial_velocity
                        velocity_x=0
                    elif event.key==pygame.K_DOWN:  # move DOWN
                        velocity_y = intial_velocity
                        velocity_x = 0
                    elif event.key==pygame.K_RIGHT:  # move RIGHT
                        velocity_x = intial_velocity
                        velocity_y = 0
                    elif event.key==pygame.K_LEFT:   # move LEFT
                        velocity_x=-intial_velocity
                        velocity_y = 0
                    elif event.key==pygame.K_q:  # using as a cheat code to increase 10 points
                        score+=10
            x_axis=x_axis+velocity_x  # give the speed continues because of while loop
            y_axis=y_axis+velocity_y  # give the speed continues because of while loop
            if abs(x_axis-food_x_axis)<6 and abs(y_axis-food_y_axis)<6:
                pygame.mixer.music.load('sound/beep.mp3')
                pygame.mixer.music.play()
                food_x_axis = random.randint(20, width - 10)
                food_y_axis = random.randint(20, height - 10)
                intial_velocity+=0.3
                score+=10
                snake_length+=5
                if score>int(high_score):
                    high_score=score
            window.blit(image,(0,0))  # image
            display(f'score={str(score)}   High Score={high_score}', red, 5, 5)
            pygame.draw.rect(window, white, [food_x_axis, food_y_axis, food_size, food_size])
            head=[]
            head.append(x_axis)
            head.append(y_axis)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                sound('sound/boom.mp3')
                game_over=True
            if x_axis > width:
                x_axis = 0
            elif x_axis < 0:
                x_axis = width
            elif y_axis > height:
                y_axis = 0
            elif y_axis < 0:
                y_axis = height
            length(window,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fbs) # it will frame rate move
    pygame.quit()
    quit()

def border():
    # Variable
    x_axis = random.randint(20, width)  # position on x axis on the surface or graph
    y_axis = random.randint(20, height)  # position on y axis on the surface or graph
    snake_size = 10
    intial_velocity = 1
    velocity_x = 0  # move in the Right direction  with the speed of vilocity_x
    velocity_y = 0  # move in the Down direction  with the speed of vilocity_x
    game_over = False
    exit_game = False
    score = 0
    fbs = 45  # frame per second
    snake_length = 1
    snake_list = []

    # Food
    food_size = 10
    food_x_axis = random.randint(20, width - 10)  # position on x axis on the surface or graph
    food_y_axis = random.randint(20, height - 10)  # position on y axis on the surface or graph

    # file
    if not os.path.exists('High_Score.txt'):
        with open('High_Score.txt', 'w') as f:
            f.write(str(0))
    with open('High_Score.txt') as f:
        high_score = f.read()

    while not exit_game:
        if game_over:
            with open('High_Score.txt', 'w') as f:
                f.write(str(high_score))
            window.blit(image_2, (0, 0))
            display('Press Enter to play', red, 210, 240)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:  # move UP
                        velocity_y = -intial_velocity
                        velocity_x = 0
                    elif event.key == pygame.K_DOWN:  # move DOWN
                        velocity_y = intial_velocity
                        velocity_x = 0
                    elif event.key == pygame.K_RIGHT:  # move RIGHT
                        velocity_x = intial_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:  # move LEFT
                        velocity_x = -intial_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_q:  # using as a cheat code to increase 10 points
                        score += 10
            x_axis = x_axis + velocity_x  # give the speed continues because of while loop
            y_axis = y_axis + velocity_y  # give the speed continues because of while loop
            if abs(x_axis - food_x_axis) < 6 and abs(y_axis - food_y_axis) < 6:
                pygame.mixer.music.load('sound/beep.mp3')
                pygame.mixer.music.play()
                food_x_axis = random.randint(20, width - 10)
                food_y_axis = random.randint(20, height - 10)
                intial_velocity += 0.3
                score += 10
                snake_length += 5
                if score > int(high_score):
                    high_score = score
            window.blit(image, (0, 0))  # image
            display(f'score={str(score)}   High Score={high_score}', red, 5, 5)
            pygame.draw.rect(window, white, [food_x_axis, food_y_axis, food_size, food_size])
            head = []
            head.append(x_axis)
            head.append(y_axis)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                sound('sound/boom.mp3')
                game_over = True
            if head in snake_list[:-1]:
                sound('sound/boom.mp3')
                game_over = True
            if x_axis > width or x_axis < 0 or y_axis > height or y_axis < 0:
                sound('sound/boom.mp3')
                game_over = True
            length(window, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fbs)  # it will frame rate move
    pygame.quit()
    quit()
welcome()