import pygame
from sys import exit

def display_score():
    global current_time
    current_time=int((pygame.time.get_ticks()/1000) - start_time)
    score_surf=text_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect=score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Chase')
clock=pygame.time.Clock()
game_active=False
current_time=0

text_font=pygame.font.Font('C:\\Users\Maged\Downloads\pygame 1/Pixeltype.ttf',50)
sky_surface=pygame.image.load('C:\\Users\Maged\Downloads\pygame 1/Sky.png').convert_alpha()
ground_surface=pygame.image.load('C:\\Users\Maged\Downloads\pygame 1/ground.png').convert_alpha()

player_surf=pygame.image.load('C:\\Users\Maged\Downloads\pygame 1/player_walk_1.png').convert_alpha()
player_rect=player_surf.get_rect(midbottom=(80, 300))
pl_gravity=0

snail_surface=pygame.image.load('C:\\Users\Maged\Downloads\pygame 1/snail1.png').convert_alpha()
snail_rect=snail_surface.get_rect(midbottom=(600,300))

#outro
pl_stand=pygame.image.load('C:\\Users\Maged\Downloads\pygame 1/player_stand.png').convert_alpha()
pl_stand=pygame.transform.rotozoom(pl_stand,0,2)
pl_stand_rect=pl_stand.get_rect(center=(400,200))

name_surf=text_font.render('Digital Chaser',False,'#ae1b79')
name_rect=name_surf.get_rect(center=(400,80))
message_surf=text_font.render('Press TAB to play', False, '#ae1b79')
message_rect=message_surf.get_rect(center=(400,330))

while True:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.y==216:
                    pl_gravity=-20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                game_active = True
                snail_rect.x = 600
                start_time=int(pygame.time.get_ticks()/1000)

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))

        display_score()

        snail_rect.x -= 4
        if snail_rect.right < 0: snail_rect.left = 800
        screen.blit(snail_surface,snail_rect)

        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if player_rect.y==216:
                pl_gravity=-20
        pl_gravity+=1
        player_rect.y+=pl_gravity
        if player_rect.bottom>300 :
             player_rect.bottom=300
        screen.blit(player_surf, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active=False
    else:
        screen.fill((94,129,162))
        final_score_surf = text_font.render(f'Score: {current_time}', False, ('white'))
        final_score_rect = final_score_surf.get_rect(center=(400, 80))
        screen.blit(pl_stand,pl_stand_rect)
        screen.blit(message_surf, message_rect)
        if current_time==0: screen.blit(name_surf, name_rect)
        else: screen.blit(final_score_surf, final_score_rect)

    pygame.display.update()
    clock.tick(60)