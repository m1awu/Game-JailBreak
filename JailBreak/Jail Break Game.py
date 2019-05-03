#Kryptix Incorporation
#Roy, Nick, Kennen, Mia
#Jail Break
#Jail Break is about a famed escapist, named Jack Wellington, who is caught in Essex and has to escape to regain his lost freedom.
#He does this by passing through 3 levels, each filled with different bosses.

from gamelib import*

#objects
game=Game(800,600,"Jail Break",60)

hero = Animation("prisoner.gif",8,game,864/8,280/2,3)
hero.resizeBy(-28)
hero.moveTo(50,104)
hero.setSpeed(0,90)

bk = Image("maxresdefault.jpg",game)
bk.resizeTo(game.width, game.height)

bk1 = Image("bk1.jpg",game)
bk1.resizeTo(game.width,game.height)
game.setBackground(bk1)

endscreen=Image("KennenBusted.PNG",game)
endscreen.resizeTo(game.width,game.height)
endscreen.visible=False

logo = Image("logo.png",game)
logo.y=100
logo.resizeBy(30)
logo.visible = True

story = Image("story.png", game)
story.y=282
story.resizeBy(30)
story.visible = True

hop = Image("howtoplay.png",game)
hop.y=365
hop.resizeBy(30)
hop.visible = True

play =Image("play.png",game)
play.y=445
play.resizeBy(40)
play.visible = True

arrow = Image("arrow.png",game)
arrow.moveTo(48,49)
arrow.visible = False
arrow.resizeBy(-80)

ins1= Image("ins1.png",game)
ins1.resizeTo(800,600)
ins1.visible= False

sImage = Image ("sImage.png",game)
sImage.resizeTo(800,600)
sImage.visible = False

lv1= Image("Level 1.png",game)
lv1.visible= False
lv1.moveTo(63,23)
lv1.resizeBy(-72)

lv2= Image("Level 2.png",game)
lv2.visible=False
lv2.moveTo(63,23)
lv2.resizeBy(-72)

lv3=Image("Level 3.png",game)
lv3.visible=False
lv3.moveTo(63,23)
lv3.resizeBy(-72)

f = Font(white,16,black,"Georgia")
time=60
onPlatform = False #platform

platform=Image("wood.png",game)
platform.resizeBy(-82)
platform.setSpeed(2,90)

spike=[]
x=383

for index in range(1):
    spike.append(Image("spike.png",game))

for index in range(1):
    spike[index].moveTo(500-25,585)
    spike[index].resizeBy(-85)
    spike[index].setSpeed(3,90)
    x+=800
    
bomb=[]
for index in range(100):
    bomb.append(Image("bomb.png",game))

for index in range(100):
    x+=389
    y=randint(280,400)
    bomb[index].moveTo(x,y)
    bomb[index].resizeBy(-65)
    bomb[index].setSpeed(3,90)
    
hero.health = 100
items = 0 
#variables for jumping actions

jumping = False #used to see if you are jumping
landed = False #used to see if you gaved landed on the ground
factor = 1 #used for a slow effect of the jumping

#boss 1 setup
b1=[]
x = 500
y = 490

for index in range(12):
    b1.append(Image("boss1.png",game))

for index in range(len( b1)):
    b1[index].moveTo(x,530)  
    b1[index].resizeBy(-85)
    b1[index].setSpeed(6,90)
    x+= 510

b2=[]
for index in range(5):
    b2.append(Animation("Zombie.png",16,game,861/4,899/4))

for index in range(5):
    x=randint(1000,1250)
    b2[index].moveTo(x,randint(100,1000))
    b2[index].resizeBy(-35)
    b2[index].setSpeed(6,90)


#platform list variable
#wood=[]
#for index in range(1):
    #wood.append(Image("wood.png", game))

#for index in range(1):
    #wood[index].moveTo(b1[index].x, y)
    #wood[index].resizeBy(-82)
    #wood[index].setSpeed(3,90)
    

#Title Screen
while not game.over:
    game.processInput()
    bk.draw()
    logo.draw()
    story.draw()
    ins1.draw()
    sImage.draw()
    hop.draw()
    play.draw()
    arrow.draw()
    


    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over= True
        lv1.visible = True

    if hop.collidedWith(mouse) and mouse.x>hop.left and mouse.x<hop.right and mouse.y>hop.top and mouse.y<hop.bottom and mouse.LeftClick:
        ins1.visible = True
        logo.visible = False
        play.visible = False
        story.visible = False
        hop.visible = False
        arrow.visible = True


    if arrow.collidedWith(mouse) and mouse.x>arrow.left and mouse.x<arrow.right and mouse.y>arrow.top and mouse.y<arrow.bottom and mouse.LeftClick:
        bk.visible = True
        bk.draw()
        sImage.visible = False
        arrow.visible = False
        logo.visible = True
        play.visible = True
        story.visible = True
        hop.visible = True
        ins1.visible = False
        game.setBackground(bk)

    if story.collidedWith(mouse) and mouse.x>story.left and mouse.x<story.right and mouse.y>story.top and mouse.y<story.bottom and mouse.LeftClick:
        sImage.visible = True
        logo.visible = False
        play.visible = False
        story.visible = False
        hop.visible = False
        arrow.visible = True

    if mouse.x>hop.left and mouse.x<hop.right and mouse.y>hop.top and mouse.y>hop.bottom and mouse.LeftClick:
        ins1.visible= True
        logo.visible=True
        play.visible=True
        hop.visible=True
        story.visible = True


    game.update(30)
game.over= False

#Level 1
while not game.over: #essential game loop
    game.processInput()
    game.scrollBackground("left",0)
    bk1.draw()
    hero.draw()
    hero.stop()
    platform.draw()
    lv1.draw()
    endscreen.draw()
    for index in range(100):
        bomb[index].move()
    for index in range(5):
        b2[index].move()
    for index in range(len(b1)):
        b1[index].move()

#Right Arrow key
    if keys.Pressed[K_RIGHT]:
        game.scrollBackground("left",3)
        hero.draw()
        bk1.draw()
        lv1.draw()
        hero.nextFrame()
        #for index in range(1):
            #wood[index].move()
        for index in range(len(b1)):
            b1[index].move()
        for index in range(3):
            platform.move()
        for index in range(100):
            bomb[index].move()
        for index in range(5):
            b2[index].move()
                    
            
#Left Arrow key
    if keys.Pressed[K_LEFT]:
        game.scrollBackground("right",0)
        game.displayTime(0,65,f)
        hero.draw()
        bk1.draw()
        hero.nextFrame()
        #for index in range(1):
            #wood[index].move()
        for index in range(len(b1)):
            b1[index].move()
        for index in range(3):
            platform.move()
        for index in range(100):
            bomb[index].move()
        for index in range(5):
            b2[index].move()

#Code for Jack to jump and landed needs altercations
    if hero.y <540 and not onPlatform:
        landed = False

    else:
        landed = True

    if keys.Pressed[K_SPACE] and landed and not jumping:
        jumping = True
        
    if jumping:
        hero.y -= 34*factor  
        factor*=.95
        landed= False
        onPlatform= False

        if factor < .18:
            jumping = False
            factor = 1

    if not landed:
        hero.y +=5

    if hero.collidedWith(platform,"rectangle") and hero.x>platform.left and hero.x<platform.right and hero.y<platform.top+10:
        onPlatform = True

    if hero.collidedWith(platform,"rectangle") and hero.x>platform.left and hero.x<platform.right and hero.y<platform.top and hero.y<platform.y+50:
        onPlatform = True
        
    if onPlatform and hero.x>platform.right and not jumping:
        onPlatform = False
        hero.y+=8
        
    if onPlatform and hero.x<platform.left and not jumping:
        onPlatform = False
        hero.y+=8

    for index in range(len(b1)):
        if b1[index].isOffScreen("left"):
            b1[index].moveTo(x,530)
            x+=237
        if hero.collidedWith(b1[index]):
            hero.health-=0.5
    for index in range(4):
        if hero.collidedWith(b2[index]):
            hero.health-=0.25
    for index in range(3):
        if platform.isOffScreen("left"):
            y=randint(225,400)
            platform.moveTo(950,y)

    #for index  in range(1):
        #wood[index].move()
        #if wood[index].isOffScreen("left"):
            #y=randint(225,400)
            #wood[index].moveTo(950,y)
     
    for index in range(100):
        if bomb[index].isOffScreen("left"):
            bomb[index].moveTo(x,y)
        if hero.collidedWith(bomb[index]):
            items+=1
            bomb[index].visible = False
    if hero.health<0:
        game.over = True
        endscreen.visible= True
        endscreen.draw()

    if hero.health>0 and items>=12:
        game.over=False


    for index in range(5):
        if b2[index].isOffScreen("left"):
            b2[index].moveTo(x,y)
            

    game.drawText("Jack's Health : " + str(hero.health),651,0,f)
    game.drawText("Jack's Bombs : " + str(items),651,25,f)
    game.drawText("Time Left : " +str(time),0,55,f)

    

    

    game.update(30)

#temporary way for the player to transition to the next level
health=50
items=10

game.over= False


#Level 2
while not game.over and hero.health>0 and items>3:
      game.processInput()
      bk1.draw()
      lv2.draw()
    



      game.update(30)

game.over=False



#End Screen
while not game.over:
    game.processInput()



    game.update(30)


game.over=False

    
  

        

    
    
