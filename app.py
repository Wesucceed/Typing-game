import pygame, random

pygame.init()

background = (200, 200, 255)
blue = (30, 30, 255)
green = (30, 150, 30)

x = 600
y = 400

speed = 0
point = 0

def new_word():
    global chosenWord, pressedWord, word_x, word_y, text, pointCaption, speed
    word_x = random.randint(100,500)
    word_y = 0
    speed += 0.0003
    pressedWord = ""
    lines = open("word.txt").read().splitlines()
    nWord = random.choice(lines)
    if len(nWord)>5:
        pos1 = random.randint(0,len(nWord)-6)
        nWord = nWord[pos1:pos1+5]
        if ' ' in nWord:
            for x in nWord:
                if x == ' ':
                    p = nWord.split(' ')
                    nWord = ''.join(p)
    else:
        if ' ' in nWord:
            for x in nWord:
                if x == ' ':
                    p = nWord.split(' ')
                    nWord = ''.join(p)
    chosenWord = nWord.lower()
    text = font.render(chosenWord, True, blue)


win = pygame.display.set_mode((x, y))
pygame.display.set_caption("Fast Typing Game")

font = pygame.font.SysFont("Serif", 32)

def difficulty(ask, win, font):
    while ask:
        for event in pygame.event.get():
            diff = "Select difficulty:"
            beg = "Beginner: press 'a'"
            ama = "Amateur: press 'b'"
            prof = "Professional: press 'c'"
            diff = font.render(diff, True, (255,255,255))
            win.blit(diff,(5,5))
            beg = font.render(beg, True, (255,255,255))
            win.blit(beg,(5,45))
            ama = font.render(ama, True, (255,255,255))
            win.blit(ama,(5,90))
            prof = font.render(prof, True, (255,255,255))
            win.blit(prof,(5,135))
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key)== 'a':
                    speed = 0.003
                    ask = False
                elif pygame.key.name(event.key)== 'b':
                    speed = 0.006
                    ask = False
                elif pygame.key.name(event.key)== 'c':
                    speed = 0.09
                    ask = False
                else:
                    ask = True

new_word()
ask = True
while True:
    while ask:
        for event in pygame.event.get():
            diff = "Select difficulty:"
            beg = "Beginner: press 'a'"
            ama = "Amateur: press 'b'"
            prof = "Professional: press 'c'"
            diff = font.render(diff, True, (255,255,255))
            win.blit(diff,(5,5))
            beg = font.render(beg, True, (255,255,255))
            win.blit(beg,(5,45))
            ama = font.render(ama, True, (255,255,255))
            win.blit(ama,(5,90))
            prof = font.render(prof, True, (255,255,255))
            win.blit(prof,(5,135))
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key)== 'a':
                    speed = 0.003
                    ask = False
                elif pygame.key.name(event.key)== 'b':
                    speed = 0.006
                    ask = False
                elif pygame.key.name(event.key)== 'c':
                    speed = 0.03
                    ask = False
                else:
                    ask = True
        
    win.fill(background)
    word_y +=speed

    win.blit(text, (word_x,word_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            pressedWord += pygame.key.name(event.key)
            if chosenWord.startswith(pressedWord):
                if chosenWord == pressedWord:
                    pygame.mixer.music.load("beep.mp3")
                    pygame.mixer.music.play()
                    point += len(chosenWord)
                    new_word()
            else:
                pressedWord = ""

    pointCaption = font.render(str(point), True, green)
    win.blit(pointCaption,(10,5))
    if word_y < y-5:
        pygame.display.update()
    else:
        win.fill(background)
        pygame.display.update()
        end = "GAME OVER!"
        end = font.render(end, True, (255,0,0))
        win.blit(end,(50,80))
        score = font.render('YOU GOT: ' +str(point)+'pts', True, (0,0,0))
        win.blit(score,(50,120))
        restart = "PRESS SPACE-BAR TO RESTART"
        restart = font.render(restart, True, (255,255,0))
        win.blit(restart,(50,160))
        pygame.display.update()
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            win.fill((0,0,0))
            ask = True
            difficulty(ask, win, font)
            point = 0
            new_word()

