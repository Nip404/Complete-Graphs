import pygame
import math
import decimal
import sys

s = [500,500]
maxfps = 40

pygame.init()
screen = pygame.display.set_mode(s,0,32)
pygame.display.set_caption("Multiplication Table by Francois Ni")

clock = pygame.time.Clock()
decimal.getcontext().prec = 6
numfont = pygame.font.SysFont("Garamond MS",20)

print_instructions = lambda: print("");print("SPACE to pause animation");print("ENTER to restart animation");print("Q to add 1 point");print("W to remove 1 point");print("A to add 10 points");print("S to remove 10 points");print("Z to add 50 points");print("X to remove 50 points")
get_points = lambda amount,radius,centre: [[[radius*math.cos(i)+centre[0],radius*math.sin(i)+centre[1]],[(radius+20)*math.cos(i)+centre[0],(radius+20)*math.sin(i)+centre[1]],p] for p,i in enumerate([math.radians(e+180 if e+180 < 360 else e-180) for e in [360*(k/amount) for k in range(amount)]])]
get_lines = lambda points,factor: [[i,i*factor if i*factor < points else loop(i*factor,points)] for i in range(points)]

def draw(rad,points,connections):
    pygame.draw.circle(screen,(0,0,0),[int(i/2) for i in s],rad,2)

    for num,point in enumerate(points):
        pygame.draw.circle(screen,(255,0,0),[int(i) for i in point[0]],4,0)
        screen.blit(numfont.render(str(point[2]),True,(0,0,0)),numfont.render("",True,(0,0,0)).get_rect(center=[int(i) for i in point[1]]))

    for line in connections:
        pygame.draw.line(screen,(0,0,0),get_from_num(points,line[0]),get_from_num(points,line[1]),2)

def get_from_num(points,num):
    for i in points:
        if i[2] == int(num):
            return i[0]

def loop(num,top):
    while num >= top:
        num -= top
    return num

def main():
    radius = 200
    factor = decimal.Decimal(0)
    points = 240
    pause = True

    print_instructions()
    
    while True:
        clock.tick(maxfps)
        
        screen.fill((255,255,255))
        
        pointlist = get_points(points,radius,[i/2 for i in s])
        lines = get_lines(points,factor)
        draw(radius,pointlist,lines)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    factor += 1 
                elif event.key == pygame.K_LEFT:
                    factor -= 1 if factor >= 1 else factor

                elif event.key == pygame.K_q:
                    points += 1
                elif event.key == pygame.K_w:
                    points -= 1

                elif event.key == pygame.K_a:
                    points += 10
                elif event.key == pygame.K_s:
                    points -= 10

                elif event.key == pygame.K_z:
                    points += 50
                elif event.key == pygame.K_x:
                    points -= 50

                elif event.key == pygame.K_SPACE:
                    pause = not pause
                elif event.key == pygame.K_RETURN:
                    factor = 0
                    
        if points < 0:
            points = 0
        elif points > 2000:
            points = 2000

        screen.blit(numfont.render(f"FPS: {str(clock.get_fps())[:5]}/{maxfps if maxfps else math.inf}",True,(0,0,0)),numfont.render("",True,(0,0,0)).get_rect(topleft=[10,10]))
        screen.blit(numfont.render(f"Factor: {factor}",True,(0,0,0)),numfont.render("",True,(0,0,0)).get_rect(topleft=[10,30]))
        screen.blit(numfont.render(f"Density: {decimal.Decimal(points)/decimal.Decimal(2000)*decimal.Decimal(100)}%",True,(0,0,0)),numfont.render("",True,(0,0,0)).get_rect(topleft=[10,50]))
    
        factor += decimal.Decimal(0.025) if not pause else decimal.Decimal(0)
        pygame.display.flip()

if __name__ == "__main__":
    main()
