import pygame
from random import randint
from pygame.font import Font

pygame.init()
screen = pygame.display.set_mode((1024, 576))
pygame.display.set_caption('Santa Clause')
running = True
GREEN = (100,100,100)
WHITE=(255,255,255)
RED=(255,0,0)
BLACK=(0,0,0)
DIEM=(0,111,255)
clock = pygame.time.Clock()

background_image= pygame.image.load("f.png")
tuanloc_image=pygame.image.load("tuanloc.png")
xelua_image=pygame.image.load("xelua.png")
maybay1_image=pygame.image.load("14.png")
maybay2_image=pygame.image.load("tl.png")
maybay3_image=pygame.image.load("tl.png")
maybay4_image=pygame.image.load("mb1.png")
maybay5_image=pygame.image.load("mb2.png")
maybay6_image=pygame.image.load("mb3.png")
dem_image=pygame.image.load("dem.png")
may1_image=pygame.image.load("may1.png")
may2_image=pygame.image.load("may2.png")
may3_image=pygame.image.load("may3.png")
chim_image=pygame.image.load("chim.png")

tien_image=pygame.image.load("tien.png")

no1_image=pygame.image.load("no1.png")
no2_image=pygame.image.load("no2.png")
no3_image=pygame.image.load("no3.png")
no4_image=pygame.image.load("no4.png")
no5_image=pygame.image.load("no5.png")
gamevover_image=pygame.image.load("gameover.png")
nhaydu_image=pygame.image.load("nhaydu.png")
trang_image=pygame.image.load("trang.png")
win_image= pygame.image.load("win.png")
#mây
may1_x=800
may1_y=40
may2_x=1300
may2_y=43
may3_x=1800
may3_y=43
#plane
fly_x=400
fly_y=240

fly1_x=1500
fly1_y=randint(140,330)
fly2_x=2000
fly2_y=randint(140,330)
fly4_x=2500
fly4_y=randint(140,330)
fly5_x=3000
fly5_y=randint(140,330)
fly6_x=3500
fly6_y=randint(140,330)

tien1_x=1750
tien1_y=260
tien2_x=2250
tien2_y=260
tien3_x=2750
tien3_y=260
tien4_x=3250
tien4_y=260
tien5_x=3800
tien5_y=260
du1_y=fly1_y - 40
du2_y=fly2_y - 40
du4_y=fly4_y - 40
du5_y=fly5_y - 40
du6_y=fly6_y - 40

diem=0
font = pygame.font.SysFont('sans',25)
x1_pass=False
TOCDO=6.5
TOCDOMAY=2
fly=0
tangdan=0.2
pause = False
lx=40
while running:	
	clock.tick(60)
	screen.fill(GREEN)
	screen.blit(background_image,(0,0))
	
	dem=screen.blit(dem_image,(370,420))
	maybay1=screen.blit(maybay1_image,(fly1_x,fly1_y))
	maybay2=screen.blit(maybay2_image,(fly2_x,fly2_y))
	maybay4=screen.blit(maybay4_image,(fly4_x,fly4_y))
	maybay5=screen.blit(maybay5_image,(fly5_x,fly5_y))
	maybay6=screen.blit(maybay6_image,(fly6_x,fly6_y))

	chim=screen.blit(chim_image,(fly_x,fly_y))

	tien1=screen.blit(tien_image,(tien1_x,260))
	tien2=screen.blit(tien_image,(tien2_x,260))
	tien3=screen.blit(tien_image,(tien3_x,260))
	tien4=screen.blit(tien_image,(tien4_x,260))
	tien5=screen.blit(tien_image,(tien5_x,260))

	may1=screen.blit(may1_image,(may1_x,may1_y))
	may2=screen.blit(may2_image,(may2_x,may2_y))
	may3=screen.blit(may3_image,(may3_x,may3_y))

	trang=screen.blit(trang_image,(15,20))

	may1_x=may1_x - TOCDOMAY
	may2_x=may2_x - TOCDOMAY
	may3_x=may3_x - TOCDOMAY
	fly1_x=fly1_x - TOCDO
	fly2_x=fly2_x - TOCDO
	fly4_x=fly4_x - TOCDO
	fly5_x=fly5_x - TOCDO
	fly6_x=fly6_x - TOCDO
	tien1_x=tien1_x - TOCDO
	tien2_x=tien2_x - TOCDO
	tien3_x=tien3_x - TOCDO
	tien4_x=tien4_x - TOCDO
	tien5_x=tien5_x - TOCDO

	if may1_x < -250:
		may1_x=1500
	if may2_x < -250:
		may2_x=1500	
	if may3_x < -250:
		may3_x=1500
	if fly1_x < -150:
		fly1_x=2400
		fly1_y=randint(160,360)
	if fly2_x < -150:
		fly2_x=2400
		fly2_y=randint(160,360)
	if fly4_x < -150:
		fly4_x=2400
		fly4_y=randint(160,360)
	if fly5_x < -150:
		fly5_x=2400
		fly5_y=randint(160,360)
	if fly6_x < -150:
		fly6_x=2400
		fly6_y=randint(160,360)
	if tien1_x < -150:
		tien1_x=2400
	if tien2_x < -150:
		tien2_x=2400
	if tien3_x < -150:
		tien3_x=2400
	if tien4_x < -150:
		tien4_x=2400
	if tien5_x < -150:
		tien5_x=2400

	if chim.colliderect(maybay1):
		pause = True
		TOCDO=0
		TOCDOMAY=0
		no1=screen.blit(no1_image,(fly1_x -100 ,fly1_y -90))
		nhaydu=screen.blit(nhaydu_image,(fly1_x -70 ,du1_y))
		du1_y += fly
		fly += tangdan
		gameover=screen.blit(gamevover_image,(580,35))
		gameover_txt = font.render( str(diem),True,GREEN)
		screen.blit(score_txt,(900,120))
		lx=0
	if chim.colliderect(maybay2):
		pause = True
		TOCDO=0
		TOCDOMAY=0
		no2=screen.blit(no2_image,(fly2_x -60 ,fly2_y -60))
		nhaydu=screen.blit(nhaydu_image,(fly2_x -70 ,du2_y))
		du2_y += fly
		fly += tangdan
		gameover=screen.blit(gamevover_image,(580,35))
		gameover_txt = font.render( str(diem),True,GREEN)
		screen.blit(score_txt,(900,120))
		lx=0
	if chim.colliderect(maybay4):
		pause = True
		TOCDO=0
		TOCDOMAY=0
		no3=screen.blit(no3_image,(fly4_x -60 ,fly4_y -50))
		nhaydu=screen.blit(nhaydu_image,(fly4_x -70 ,du4_y))
		du4_y += fly
		fly += tangdan
		gameover=screen.blit(gamevover_image,(580,35))
		gameover_txt = font.render( str(diem),True,GREEN)
		screen.blit(score_txt,(900,120))
		lx=0
	if chim.colliderect(maybay5):
		pause = True
		TOCDO=0
		TOCDOMAY=0
		no4=screen.blit(no4_image,(fly5_x -60 ,fly5_y -50))
		nhaydu=screen.blit(nhaydu_image,(fly5_x -70 ,du5_y))
		du5_y += fly
		fly += tangdan
		gameover=screen.blit(gamevover_image,(580,35))
		gameover_txt = font.render( str(diem),True,GREEN)
		screen.blit(score_txt,(900,120))
		lx=0
	if chim.colliderect(maybay6):
		pause = True
		TOCDO=0
		TOCDOMAY=0
		no5=screen.blit(no5_image,(fly6_x -45 ,fly6_y -50))
		nhaydu=screen.blit(nhaydu_image,(fly6_x -70 ,du6_y))
		du6_y += fly
		fly += tangdan
		gameover=screen.blit(gamevover_image,(580,35))
		gameover_txt = font.render( str(diem),True,GREEN)
		screen.blit(score_txt,(900,120))
		lx=0
	if chim.colliderect(may1):
		pause = True
		TOCDO=0
		TOCDOMAY=0
		gameover=screen.blit(gamevover_image,(580,35))
		gameover_txt = font.render( str(diem),True,GREEN)
		screen.blit(score_txt,(900,120))
		lx=0
	if chim.colliderect(may2):
		pause = True
		TOCDO=0
		TOCDOMAY=0
		gameover=screen.blit(gamevover_image,(580,35))
		gameover_txt = font.render( str(diem),True,GREEN)
		screen.blit(score_txt,(900,120))
		lx=0
	if chim.colliderect(may3):
		pause = True
		TOCDO=0
		TOCDOMAY=0
		gameover=screen.blit(gamevover_image,(580,35))
		gameover_txt = font.render( str(diem),True,GREEN)
		screen.blit(score_txt,(900,120))
		lx=0
	if chim.colliderect(tien1):
		tien1_x=3050
		diem +=1
	if chim.colliderect(tien2):
		tien2_x=3050
		diem +=1
	if chim.colliderect(tien3):
		tien3_x=3050
		diem +=1
	if chim.colliderect(tien4):
		tien4_x=3050
		diem +=1
	if chim.colliderect(tien5):
		tien5_x=3050
		diem +=1
	if diem == 30:
		TOCDO=0
		TOCDOMAY=0
		win=screen.blit(win_image,(579,35))

	score_txt = font.render(str(diem),True,BLACK)
	screen.blit(score_txt,(425,444))

	for event in pygame.event.get():  
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if pause == True:
					fly1_x=1500
					fly2_x=2000
					fly4_x=2500
					fly5_x=3000
					fly6_x=3500
					tien1_x=1750
					tien2_x=2250
					tien3_x=2750
					tien4_x=3250
					tien5_x=3800
					may1_x=800
					may2_x=1300
					may3_x=1800
					lx=40
					TOCDO=6.5
					TOCDOMAY=2
					TOCDOTL=1
					diem=0
					fly=0
					tangdan=0.2
					pause=False
		if event.type==pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				fly_y -=lx
			if event.button == 3:
				fly_y +=lx
	pygame.display.flip()
pygame.quit()