import pygame
import sys
import random

screen_width = 1000
screen_height = 1000
maxHeight=100
N=300
sorttype='Bubble'
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
myfont = pygame.font.SysFont("monospace",32)

def bubblesort(List):
    sorted=False
    while not sorted:
        sorted=True
        for i in range(1,len(List)):
            if List[i]<List[i-1]:
                save=List[i-1]
                List[i-1]= List[i]
                List[i] = save
                sorted=False
            draw(List,i,-1,-1)
            clock.tick(0)
 
def quicksort(List,start,end):
    if start<end:
        pivot=List[end]
        pivotId=start
        for i in range(start,end):
            if List[i]<pivot:
                save=List[i]
                List[i]=List[pivotId]
                List[pivotId]=save
                pivotId+=1
        #save=List[end]
        #List[end]=List[pivotId]
        #List[pivotId]=save
        List[end],List[pivotId]=List[pivotId],List[end]
        draw(List,pivotId,start,end)
        clock.tick(20)
        quicksort(List,start,pivotId-1)
        quicksort(List,pivotId+1,end)
        return List
    else:
        return List

def draw(heights,red,green,blue):
    global customising
    global N
    global new
    global sorttype
    screen.fill(0)
    color=(255,255,255)
    for i in range(len(heights)):
        if i==red:
            color=(255,0,0)
        elif i==green:
            color=(0,255,100)
        elif i==blue:
            color=(0,100,255)
        else:
            color=(255,255,255)
        r=pygame.Rect( (i*screen_width/len(heights) , 0) , (screen_width/len(heights) , heights[i]/maxHeight*(screen_height-50))     )
        pygame.draw.rect(screen, color, r)
        text = myfont.render("Number of Towers: {0}".format(N), 1, (250,0,0))
        screen.blit(text, (5,screen_height-35))
        text = myfont.render("Sorting Type: {0}".format(sorttype), 1, (250,0,0))
        screen.blit(text, (620,screen_height-35))
        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                customising=not customising
            elif event.key == pygame.K_1:
                sorttype='Bubble'
            elif event.key == pygame.K_2:
                sorttype='Quick'
        elif pygame.mouse.get_pressed()[0]:
            N=min(3+pygame.mouse.get_pos()[0]//4,250)
            new=True
         

                
def NewTowers():
    heights=[]
    for i in range(0,N):
        heights.append(random.randint(1,maxHeight))
    return heights

while True:
    customising=True
    towers=NewTowers()
    while customising:
        new=False
        draw(towers,-1,-1,-1)
        if new:
            towers=NewTowers()
    if sorttype=='Bubble':
        bubblesort(towers) 
    else:
        quicksort(towers,0,len(towers)-1)   
    customising=True
    while customising:
        draw(towers,-1,-1,-1)

