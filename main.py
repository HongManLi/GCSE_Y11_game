import pygame
import math    # Watch that this doesn't cause problems
import asyncio

# Init - pre-setup
pygame.init()
clock = pygame.time.Clock()
running = True
X = 800
Y = 400
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption("Qian Long Huang Chao")

# Setup 
font = pygame.font.Font("Fonts/NotoSansTC-Regular.ttf", 12)
scene = 1
text_ = 1
buttondrawn = "Normal"
buttonstages = []
answer = ""
final_answer = ""
sequence = []
army = 3
first_change = True
ending = None


# Questions and answers
# Path marker : Answer
qa = {'1':'2',
      '1a':'y=2x',
      '2':'y=x+1',
      '3a':'1',
      '3b':'yellow',
      '3c':'red',
      '3d':'white',
      '3e':'green',
      '3f':'black',
      '3g':'6912',
      '3h':'x-4',
      '3i':'1.7',
      '4a':'40',
      '4aa':'75%',
      '4b':'12',
      '4c':'26.39',
      '4d':'11',
      '4e':'47.75',
      '5a':'-1',
      '5b':'(3,2)',
      '5c':'0.2',
      '5d':'22680.96',
      '5e':'a',
      '5f':'12',
      '5g':'y=-7'}


# Button coordinates
buttonxy = (200, 325)
buttonsize = (200,50)

# Three button scenarios
buttonxy3 = (90, 325)


# Textbox
def draw_tbox (x = X // 2, y = Y // 4 * 3.25):
    tbox = pygame.Rect(0, 0, buttonsize[0], buttonsize[1])
    tbox.center = ( X // 2, Y // 4 * 3.25)
    pygame.draw.rect(screen, "WHITE", tbox)


# Text wrapping
def drawText(text, color="BLACK", font=font, profilepic = None):


    # get the height of the font
    fontHeight = font.size(text)[1]
    fontwidth = font.size(text)[0]

    # Determine the height and make white box
    #height = math.ceil(fontwidth / 650) * fontHeight
    #rect = pygame.Rect(0, 0, fontwidth + 5 if fontwidth < 650 else 650, height + 3)
    rect = pygame.Rect(0, 0, 650, 4 * fontHeight + 5)
    rect.center = ( X // 2, 0)
    rect.bottom = Y - 10
    pygame.draw.rect(screen, "WHITE", rect)


    y = rect.top
    lineSpacing = 1

    # Draw character portrait
    if profilepic:
        position = bg[profilepic].get_rect()
        position.right = 3.25 / 4 * X
        position.bottom = rect.top - 5
        screen.blit(bg[profilepic], position)

    # Blit wrapped words

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        image = font.render(text[:i], True, color)

        screen.blit(image, (rect.left + 3, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text




# Text wrapping special - where position is variable
def drawText_variable(text, color="BLACK", font=font, yposition=200):

    '''Only new addition is the yposition argument - for positioning picture further up or down'''


    # get the height of the font
    fontHeight = font.size(text)[1]
    fontwidth = font.size(text)[0]

    # Determine the height and make white box
    rect = pygame.Rect(0, 0, 350, 5 * fontHeight + 10)
    rect.center = ( X // 2, 0)
    rect.bottom = yposition
    pygame.draw.rect(screen, "WHITE", rect)


    y = rect.top
    lineSpacing = 1

    # Blit wrapped words

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        image = font.render(text[:i], True, color)

        screen.blit(image, (rect.left + 3, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text



# Background function
bg = {
    "Hero" : pygame.transform.scale(pygame.image.load('Images/Hero.jpg').convert(), (100, 100)),
    "Heroine" : pygame.transform.scale(pygame.image.load('Images/Heroine.jpg').convert(), (100, 100)),
    "Princess" : pygame.transform.scale(pygame.image.load('Images/Princess.png').convert(), (100, 100)),
    "Prince" : pygame.transform.scale(pygame.image.load('Images/Prince.jpg').convert(), (100, 100)),
    "Amursana" : pygame.transform.scale(pygame.image.load('Images/Amursana.jpg').convert(), (100, 100)),
    "messenger" : pygame.transform.scale(pygame.image.load('Images/messenger.jpg').convert(), (100, 100)),
    "Home room" : pygame.image.load('Images/background home room.jpg').convert(),
    "Throne room" : pygame.transform.scale(pygame.image.load('Images/Throne room.jpg').convert(), (658, 439)),
    "Ceremony" : pygame.transform.scale(pygame.image.load('Images/ceremony.jpg').convert(), (658, 439)),
    "Battle_Dzungar" : pygame.transform.scale(pygame.image.load('Images/Battle_Dzungar.jpg').convert(), (658, 439)),
    "Soldier" : pygame.transform.scale(pygame.image.load('Images/Soldier.png').convert(), (100, 100)),
    "Dzungar_map" : pygame.transform.scale(pygame.image.load('Images/Dzungar_map.jpg').convert(), (300, 270)),
    "Dzungar_surrounded" : pygame.transform.scale(pygame.image.load('Images/Dzungar_surrounded.jpg').convert(), (658, 439)),
    "Winecup" : pygame.transform.scale(pygame.image.load('Images/Winecup.jpg').convert(), (250, 330)),
    "Jade" : pygame.transform.scale(pygame.image.load('Images/Jade.jpg').convert(), (300, 200)),
    "Gobi" : pygame.transform.scale(pygame.image.load('Images/Gobi.jpg').convert(), (658, 439)),
    "Altai" : pygame.transform.scale(pygame.image.load('Images/Altai.jpg').convert(), (658, 439)),
    "Learning" : pygame.transform.smoothscale(pygame.image.load('Images/Learning.jpg').convert(), (100, 100)),
    "Study" : pygame.transform.smoothscale(pygame.image.load('Images/Study.jpg').convert(), (658, 439)),
    "Poem1" : pygame.transform.scale(pygame.image.load('Images/Poem1.jpg').convert(), (200, 100)),
    "Poem2" : pygame.transform.scale(pygame.image.load('Images/Poem2.jpg').convert(), (200,100)),
    "Poem1English" : pygame.transform.scale(pygame.image.load('Images/Poem1English.jpg').convert(), (200, 120)),
    "Poem2English" : pygame.transform.scale(pygame.image.load('Images/Poem2English.jpg').convert(), (200,120)),
    "costume_scholar" : pygame.transform.scale(pygame.image.load('Images/costume_scholar.jpg').convert(), (200,300)),
    "costume_warrior" : pygame.transform.scale(pygame.image.load('Images/costume_warrior.jpg').convert(), (200,300)),
    "yellow_winecup" : pygame.transform.scale(pygame.image.load('Images/yellow_winecup.jpg').convert(), (200,150)),
    "white_winecup" : pygame.transform.scale(pygame.image.load('Images/white_winecup.jpg').convert(), (150,150)),
    "blue_winecup" : pygame.transform.scale(pygame.image.load('Images/blue_winecup.jpg').convert(), (150,150)),
    "bronze_winecup" : pygame.transform.scale(pygame.image.load('Images/bronze_winecup.jpg').convert(), (150,200)),
    "Study_outdoors" : pygame.transform.scale(pygame.image.load('Images/Study_outdoors.jpg').convert(), (658, 439)),
    "River_poem" : pygame.transform.scale(pygame.image.load('Images/River_poem.jpg').convert(), (350, 100)),
    "River_poem_English" : pygame.transform.scale(pygame.image.load('Images/River_poem_English.jpg').convert(), (350, 100)),
    "kunminghu" : pygame.transform.scale(pygame.image.load('Images/kunminghu.jpg').convert(), (658, 439)),
    "kunyuhe" : pygame.transform.scale(pygame.image.load('Images/kunyuhe.jpg').convert(), (658, 439)),
    "yuquanshan" : pygame.transform.scale(pygame.image.load('Images/yuquanshan.jpg').convert(), (658, 439)),
    "Q5g" : pygame.transform.scale(pygame.image.load('Images/Q5g.jpg').convert(), (350, 200)),
    "yongchang" : pygame.transform.scale(pygame.image.load('Images/yongchang.jpg').convert(), (200, 200)),
    #"River_poem" : pygame.transform.scale(pygame.image.load('Images/River_poem.jpg').convert(), (350, 100)),
}

def draw_bg (a):
    screen.blit(bg[a], bg[a].get_rect(center = screen.get_rect().center))

def draw_popup (pic, y):
    screen.blit(bg[pic], bg[pic].get_rect(center = (400,y)))

# Draw character module
# def draw_ch (a):
#     screen.blit(bg[a], bg[a].get_rect(center = (3 / 4 * X, 3 / 4 * Y)))


# Text function
# def draw_txt (a):
#     text = font.render(a, True, (0, 0, 0), (255, 255, 255))
#     textRect = text.get_rect()
#     textRect.center = (X // 2, Y - 30)
#     screen.blit(text, textRect)

def draw_button_text(text, option):
    ''' text is a list with maximum of 2 items allowed. Each item is one line. '''

    if len(text) > 1:
    # First line...
        text1 = text[1]
        text = font.render(text[0], True, "Black")
        textRect = text.get_rect()
        if option == 1:
            textRect.center = (buttonxy[0] + buttonsize[0] // 2, buttonxy[1] + buttonsize[1] // 2 - 7)
            screen.blit(text, textRect)
        else:
            textRect.center = ((buttonxy[0] + buttonsize[0] + 20) + buttonsize[0] // 2, buttonxy[1] + buttonsize[1] // 2 - 7)
            screen.blit(text, textRect)

    # Second line...
        text1 = font.render(text1, True, "Black")
        text1Rect = text1.get_rect()
        if option == 1:
            text1Rect.center = (buttonxy[0] + buttonsize[0] // 2, buttonxy[1] + buttonsize[1] // 2 + 7)
            screen.blit(text1, text1Rect)
        else:
            text1Rect.center = ((buttonxy[0] + buttonsize[0] + 20) + buttonsize[0] // 2, buttonxy[1] + buttonsize[1] // 2 + 7)
            screen.blit(text1, text1Rect)

    # Else if only one line is needed
    else:
        text = font.render(text[0], True, "Black")
        textRect = text.get_rect()
        if option == 1:
            textRect.center = (buttonxy[0] + buttonsize[0] // 2, buttonxy[1] + buttonsize[1] // 2)
            screen.blit(text, textRect)
        else:
            textRect.center = ((buttonxy[0] + buttonsize[0] + 20) + buttonsize[0] // 2, buttonxy[1] + buttonsize[1] // 2)
            screen.blit(text, textRect)


# Drawing text for 3 buttons
def draw_button_text_3(text):
    '''Single input of list containing 3 items, corresponding to option 1, 2 and 3.'''

    for n, i in enumerate(text):
        # Format text and create imaginary rectangle bearing for it
        t = font.render(i, True, "Black")
        textRect = t.get_rect()   
        # Parameters for blitting...
        textRect.center = (buttonxy3[0] + buttonsize[0] // 2 + n*(buttonsize[0] + 10), buttonxy3[1] + buttonsize[1] // 2 - 7)
        screen.blit(t, textRect)



# Check answer
def checkanswer(q_number):
    return(final_answer.replace(" ", "").lower() == qa[str(q_number)].lower())



# Buttons function
def draw_button ():
    pygame.draw.rect(screen, "WHITE", (buttonxy[0], buttonxy[1], buttonsize[0], buttonsize[1]))
    pygame.draw.rect(screen, "WHITE", (buttonxy[0] + buttonsize[0] + 20, buttonxy[1], buttonsize[0], buttonsize[1]))



# THREE Buttons function
def draw_button_3 ():
    pygame.draw.rect(screen, "WHITE", (buttonxy3[0], buttonxy[1], buttonsize[0], buttonsize[1]))
    pygame.draw.rect(screen, "WHITE", (buttonxy3[0] + buttonsize[0] + 10, buttonxy[1], buttonsize[0], buttonsize[1]))
    pygame.draw.rect(screen, "WHITE", (buttonxy3[0] + 2*(buttonsize[0] + 10), buttonxy[1], buttonsize[0], buttonsize[1]))

# Team icons
def team (a):

    if a:
        for num, portrait in enumerate(a):
            position = bg[portrait].get_rect()
            x_pos = num * 75 + 71
            position.topleft = (x_pos,0)
            to_show = pygame.transform.scale(bg[portrait], (75,75))
            screen.blit(to_show, position)




# Variables
app = {
    'brother_app' : 0,
    'sister_app' : 0,
    'teacher_app' : 0,
    'father_app' : 0
    }

# Gender specific lines
love_interest = {
    'Male' : ['晴晴'],
    'Female' : ['文長']
}



# Test only
# Remember to delete name and character globals
scene = 4
sequence.append('Home')
text_ = 8.92
character = 'Male'
bg['MC'] = bg['Hero']
name = 'Hi'

async def main():
    
    global running
    global X
    global Y
    global screen
    global font
    global scene
    global text_
    global buttonxy
    global buttonsize
    global bg
    global buttondrawn
    global answer
    global qa
    global final_answer
    global app
    global sequence
    global army
    global love_interest
    global first_change
    global ending
    global character
    global name

    while running:
        
        # Print tests here
        #print(text_)

        # Set clock for standardizing movement speeds
        clock.tick(20)

        # Need to paint screen black to blot out old dialogue text
        screen.fill('Black')

        # Scene determines text and background image


#region     ### FIRST SCENE
 

        # FIRST SCENE ######################################
        if scene == 1:

            # Background
            draw_bg('Home room')

            if text_ == 1:
                drawText('Please enter your name:')

            if text_ == 1.1:
                draw_tbox()
                buttondrawn = "Textinput"
                name = answer

            if text_ == 1.2:
                drawText('Please select your character:')

            if text_ == 1.3:
                draw_button()
                draw_button_text(['Scholarly Prince'], 1)
                draw_button_text(['Warrior Princess'], 2)
                screen.blit(bg['Hero'], bg['Hero'].get_rect(center = ((buttonxy[0] + buttonsize[0] // 2, Y // 2 + 60))))
                screen.blit(bg['Heroine'], bg['Heroine'].get_rect(center = ((buttonxy[0] + buttonsize[0] + 20) + buttonsize[0] // 2, Y // 2 + 60)))
                buttondrawn = "Button"                
                if first_change:
                    first_change = False
                    buttonstages.append(text_)


            if text_ == 1.31:
                character = "Male"
                bg['MC'] = bg['Hero']
                text_ = 1.4

            if text_ == 1.32:
                character = "Female"
                bg['MC'] = bg['Heroine']
                text_ = 1.4

            if text_ == 1.4:
                drawText('You are daydreaming in your room, when you hear a knock on the door')

            if text_ == 1.5:
                drawText('It is your teacher. "Would you like to revise a short while", he asks.')

            if text_ == 1.6:
                draw_button()
                draw_button_text(['I suppose'], 1)
                draw_button_text(['No way man!'], 2)
                buttondrawn = "Button"                
                if first_change:
                    first_change = False
                    buttonstages.append(text_)



            # Branch for first option
            if text_ == 1.61:
                drawText('Teacher approval + 1')
                if first_change:
                    first_change = False
                    app['teacher_app'] += 1

            if text_ == 1.71:
                drawText('"What is the gradient of the line connecting (0,1) and (2,2)?"')

            if text_ == 1.81:
                draw_tbox()
                buttondrawn = "Textinput"

            if text_ == 1.91:
                if checkanswer('1'):
                    drawText('Teacher approval + 1')
                    if first_change:
                        first_change = False                    
                        app['teacher_app'] += 1

                else:
                    drawText('"That\'s wrong. You have some way to go yet."')



            # Branch for second option
            if text_ == 1.62:
                drawText('Teacher approval - 3')
                if first_change:
                    first_change = False                       
                    app['teacher_app'] -= 3

            if text_ == 1.72:
                drawText('"I was hoping you would be more self directed. I won\'t let you get away, here is a much harder question."')

            if text_ == 1.82:
                drawText('"What is the equation of the line perpendicular to y = -0.5x - 3 and passing through (0,0)?"')

            if text_ == 1.92:
                draw_tbox()
                buttondrawn = "Textinput"

            if text_ == 2.02:
                if checkanswer('1a'):
                    drawText('Teacher: "You are very talented, but unfortunately slack."   Teacher approval + 1.')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] += 1

                else:
                    drawText('Teacher: "I am very disappointed. My approval for you has plummeted."')


            if text_ == 2.01 or text_ == 2.12 or text_ == 2.97:
                drawText('"Your father wants to see you urgently. Please get ready."')
                text_ = 2.97

            if text_ == 3.07:
                drawText('I will get ready at once.', profilepic='MC')

            if text_ == 3.17:
                text_ = 2
                scene = 2




# endregion



#region      ### SECOND SCENE

        # SECOND SCENE ###########################################################
        if scene == 2 or scene == 3:
            draw_bg('Throne room')

            if text_ == 2:
                drawText('Emperor: "Dear child, you have arrived. I have summoned all of you to help me with several problems."')

            if text_ == 2.1:
                drawText('"The time has come to hold the Spring ceremony, and pray for a year of good harvest."')

            if text_ == 2.2:
                drawText('"At the same time, we should take advantage of the internal conflict in the Dzungar nomads."')

            if text_ == 2.3:
                drawText('"And conquer them once and for all."')

            if text_ == 2.4:
                drawText('"Which one of you can share this burden of the Qing Empire?"')

            if text_ == 2.5:
                drawText('Brother prince: "I will lead against the Dzungars!"', profilepic='Prince')

            if text_ == 2.6:
                drawText('Sister princess: "I will hold the Spring ceremony"', profilepic='Princess')

            if text_ == 2.7:
                drawText(f'Teacher: "{name}, which option will you choose?"')

            if text_ == 2.8:
                draw_button()
                draw_button_text(['Lead army'], 1)
                draw_button_text(['Preside over ceremony'], 2)
                buttondrawn = "Button"                
                if first_change:
                    first_change = False
                    buttonstages.append(text_)



            # Branch for first option
            if text_ == 2.81:
                drawText('Brother prince: "You want to take my glory?! I won\'t let you!"', profilepic='Prince')

            if text_ == 2.91:
                drawText('What is the equation of the line passing through (0, 1) and (1,2)?', profilepic='Prince')

            if text_ == 3.01:
                draw_tbox()
                buttondrawn = "Textinput"

            if text_ == 3.11:
                if checkanswer('2'):
                    drawText('Teacher approval +1. Brother prince approval -1. Father emperor approval +1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] += 1
                        app['brother_app'] -= 1
                        app['father_app'] += 1

                else:
                    drawText('Brother prince: "You lost. Haha, you are not fit to do this at all."', profilepic='Prince')
                    if first_change:
                        first_change = False                            
                        app['brother_app'] += 1


            # Branch for second option
            if text_ == 2.82:
                drawText('Sister princess: "Since we were small we have fought. I won\'t let you win this time"', profilepic='Princess')

            if text_ == 2.92:
                drawText('What is the equation of the line passing through (0, 1) and (1,2)?', profilepic='Princess')

            if text_ == 3.02:
                draw_tbox()
                buttondrawn = "Textinput"

            if text_ == 3.12:
                if checkanswer('2'):
                    drawText('Teacher approval +1. Sister princess approval -1. Father emperor approval +1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] += 1
                        app['sister_app'] -= 1
                        app['father_app'] += 1

                else:
                    drawText('Sister princess: "You lost, finally I don\'t have to live under your shadow!"', profilepic='Princess')
                    if first_change:
                        first_change = False                            
                        app['sister_app'] += 1


            # Wrapping up the 3 outcomes

            if text_ == 3.22 or text_== 3.21:
                if checkanswer('2'):
                    drawText(f'Father Emperor: "{name}, you are indeed the best person for this job."')
                    if text_ == 3.22:
                        if first_change:
                            first_change = False                                
                            sequence.append('Ceremony')
                    else:
                        if first_change:
                            first_change = False                                
                            sequence.append('Battle')

                elif app['brother_app'] > 0:
                    drawText('Emperor: "Brother prince is the better person to lead the army."')
                    if first_change:
                        first_change = False        
                        sequence.append('Home')
                elif app['sister_app'] > 0:
                    drawText('Emperor: "Sister princess is the better choice for the Spring ceremony."')
                    if first_change:
                        first_change = False                            
                        sequence.append('Home')
            
            if text_ == 3.32 or text_== 3.31:
                if checkanswer('2'):
                    drawText('"Prepare to set off on the morrow."')
                else:
                    drawText('You remain in the palace and study.')

            if len(sequence) == 1 and text_ == 3.42 or text_ == 3.41:
                if sequence[0] == 'Home':
                    drawText('I will stay and focus on my studies, your Highness.', profilepic='MC')
                if sequence[0] == 'Battle':
                    drawText('I will not disappoint you, your Highness. My 16 years of training are just for this day.', profilepic='MC')
                if sequence[0] == 'Ceremony':
                    drawText('The ceremony will go smoothly, your Highness. I will return with blessings for our people and crops.', profilepic='MC')                    

            if text_ == 3.52 or text_ == 3.51:
                text_ = 4
                scene = 4


#endregion




#region      ### THIRD SCENE ceremony
        if scene == 4 and sequence[-1] == 'Ceremony':
            draw_bg('Ceremony')

            if text_ == 4:
                drawText('Teacher: "Let us run through some of the ceremony\'s details."')

            if text_ == 4.1:
                drawText('The Spring ritual belongs to the most distinctive order of ceremonies. We put our hopes for the empire in this tribute to the land.')

            if text_ == 4.2:
                drawText('Rituals are grouped based on their scale into "small", "medium" and "big". To put this into context, the ceremony for Confucious belongs to "medium", while the one for the Emperor\'s ancestors belongs to "big".')

            if text_ == 4.3:
                drawText('Traditionally, how many hours before sunrise do you to set off for the altar grounds? (Answer with an integer)')

            if text_ == 4.4: 
                draw_tbox()
                buttondrawn = "Textinput"
            
            if text_ == 4.5:
                if checkanswer('3a'):
                    drawText('Teacher approval + 1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] += 1
                else:
                    drawText('Teacher approval - 1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] -= 1

            if text_ == 4.6:
                drawText('These grounds, along with the Imperial Palace, were built in the late Ming Dynasty, in the reign of Yong Le.')

            if text_ == 4.7:
                drawText('Five different coloured soils make up the altar ground. Each comes from a distinctive region in the empire.')    

            if text_ == 4.8:
                drawText('What colored earth is taken from Henan?')

            if text_ == 4.9: 
                draw_tbox()
                buttondrawn = "Textinput"
            
            if text_ == 5:
                if checkanswer('3b'):
                    drawText('Teacher approval + 1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] += 1
                else:
                    drawText('Teacher approval - 1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] -= 1

            if text_ == 5.1:
                drawText('What colored earth is taken from Zhe Jiang and Fu Jian?')

            if text_ == 5.2: 
                draw_tbox()
                buttondrawn = "Textinput"
            
            if text_ == 5.3:
                if checkanswer('3c'):
                    drawText('Teacher approval + 1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] += 1
                else:
                    drawText('Teacher approval - 1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] -= 1

            if text_ == 5.4:
                drawText('What colored earth is taken from Jiang Xi and Hu Guang?')

            if text_ == 5.5: 
                draw_tbox()
                buttondrawn = "Textinput"
            
            if text_ == 5.6:
                if checkanswer('3d'):
                    drawText('Teacher approval + 1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] += 1
                else:
                    drawText('Teacher approval - 1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] -= 1

            if text_ == 5.7:
                drawText('What colored earth is taken from Shan Dong?')

            if text_ == 5.8: 
                draw_tbox()
                buttondrawn = "Textinput"
            
            if text_ == 5.9:
                if checkanswer('3e'):
                    drawText('Teacher approval + 1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] += 1
                else:
                    drawText('Teacher approval - 1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] -= 1

            if text_ == 6:
                drawText('What colored earth is taken from Beijing?')

            if text_ == 6.1: 
                draw_tbox()
                buttondrawn = "Textinput"
            
            if text_ == 6.2:
                if checkanswer('3f'):
                    drawText('Teacher approval + 1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] += 1
                else:
                    drawText('Teacher approval - 1')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] -= 1

            if text_ == 6.3:
                drawText(u'"The name of this ceremonial ground, 社稷壇, is derived from the name of two gods."')

            if text_ == 6.4:
                drawText(u'"社 is the God of Earth, while 稷 the God of Crops."')

            if text_ == 6.5:
                drawText('"Over time, the two words became synonymous with "Nation"')        

            if text_ == 6.6:
                drawText('"In the elaborate setup of the ritual lies gratitude and acknowledgement."') 

            if text_ == 6.7:  
                drawText('Teacher: "For the Spring ceremony, blessings are written on white paper with chartreuse ink, one day before the ceremony. Let\'s see you give it a go."')    

            if text_ == 6.8:
                drawText(f'What is the LCM of 2\N{SUPERSCRIPT FIVE} x 6\N{SUPERSCRIPT TWO} and 2 x 6\N{SUPERSCRIPT THREE}? Give answer as whole number.')

            if text_ == 6.9:
                draw_tbox()
                buttondrawn = "Textinput"

            if text_ == 7:
                if checkanswer('3g'):
                    drawText('Your blessings are thoughtful, respectful and lyrical, and beautiful handwriting too! Teacher approval + 1.')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] += 1

                else:
                    drawText('What you wrote makes no sense! All your studies have been in vain. Teacher approval - 1.')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] -= 1


            if text_ == 7.1:
                drawText('The ceremony is starting, pay attention now.')

            if text_ == 7.2:
                drawText('The first part is a procession to welcome the Deity. As the music plays, sacrificial items are buried. These are the hair and blood of cattle, sheep and pigs.              ')

            if text_ == 7.3:
                draw_popup('Jade', 175)
                drawText('In the second part we present offerings of jade ornaments and silk weavings.')

            if text_ == 7.4:
                draw_popup('Winecup', 150)
                drawText('Then comes the offering of wine (the first libation). There are three rounds of wine tribute; at each round you must perform "three kneels and nine kowtows".')

            if text_ == 7.5:
                draw_popup('costume_warrior', 160)
                drawText('"Dance of the Warrior" accompanies the first libation. This is the ceremonial dress of the dancers.')

            if text_ == 7.6:
                drawText('You are daydreaming! What is the inverse function of f(x) = x + 4?  For your answer no need to put in equal sign, just the expression in x.')

            if text_ == 7.7:
                draw_tbox()
                buttondrawn = "Textinput"

            if text_ == 7.8:
                if checkanswer('3h'):
                    drawText('You are following the procedures well. Teacher approval + 1.')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] += 1

                else:
                    drawText('You have no clue what you are doing. Those offerings are not for you to eat! And you spilled the wine everywhere! Teacher approval - 1.')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] -= 1          
      

            if text_ == 7.9:
                draw_popup('costume_scholar', 160)
                drawText('The second and third libation follows. They are accompanied by "Dance of the Scholar" this time. Their attire is slightly different.')                

            if text_ == 8:
                drawText('The ceremony closes, and the music changes, to farewell the Deity.')   

            if text_ == 8.1:
                drawText('Blessing placards, jade ornaments, woven silk and other offerings are buried under the earth.')   

            if text_ == 8.2:
                drawText('You fell asleep again, how dare you! In situations like this there are things bigger than just yourself.') 

            if text_ == 8.3:
                drawText('A rabbit travelled 1km/hr for 1 hour. Then it travelled 2km/hr for 2 hours. What is its overall average speed rounded to 1 decimal place?') 

            if text_ == 8.4:
                draw_tbox()
                buttondrawn = "Textinput"                

            if text_ == 8.5:
                if checkanswer('3i'):
                    drawText('Well it seems like you did a good job, the ceremony is a huge success. Teacher approval + 7. Father approval + 7.')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] += 7
                        app['father_app'] += 7     
                        sequence.insert(0, 'Ceremony:Success')                   

                else:
                    drawText('No, don\'t dig up the offerings, they are meant to remain buried! Your ignorance is boundless. Spring ceremony has failed. Teacher approval - 7. Father approval - 7.')
                    if first_change:
                        first_change = False                            
                        app['teacher_app'] -= 7     
                        app['father_app'] -= 7
                        sequence.insert(0, 'Ceremony:Failure')                          


            if text_ == 8.6:
                if first_change:
                    first_change = False
                    sequence.remove('Ceremony')
                    scene = 6


#endregion


#region      ### THIRD SCENE battle...
        if scene == 4 and sequence[-1] == 'Battle':
            draw_bg('Battle_Dzungar')
            

            if text_ == 4:
                drawText(f'It was in 1755, a period of internal strife for the Dzungar tribe, that {name} set off as commander.')

            if text_ == 4.1:
                screen.blit(bg['Dzungar_map'], bg['Dzungar_map'].get_rect(center = (400,175)))
                drawText('You picked two routes. Half your men travel through the Uliastai army camp in the North, and the other half through Barkol. The two will converge at the Bortala section of the Aibihu Lake.')

            if text_ == 4.2:
                draw_bg('Gobi')
                drawText('Along the Western route you come across the Gobi desert. The terrain is treacherous. Can you lead your men through?')

            if text_ == 4.3:
                draw_bg('Gobi')
                drawText('When x decreases by 16, 60% is left. What is x?')

            if text_ == 4.4:
                draw_bg('Gobi')
                draw_tbox()
                buttondrawn = "Textinput"

            if text_ == 4.5:
                draw_bg('Gobi')
                if checkanswer('4a'):
                    drawText('Teacher approval + 1. Crossing of the desert was successful. There were no casualties under your astute guidance.')
                    if first_change:                    
                        app['teacher_app'] += 1
                        first_change = False
                else:
                    drawText('Some of your men died in the desert because of your poor leadership. Teacher approval - 1. Qing army strength drops.')
                    if first_change:                  
                        app['teacher_app'] -= 1
                        army -= 1
                        first_change = False                  

            if text_ == 4.6:
                draw_bg('Altai')               
                drawText('On the Northern route you skirt the surrounding lands of the Altai mountains. One of your warriors tell you about its geography.')    

            if text_ == 4.7:
                draw_bg('Altai')               
                drawText('Amursana: "My people are the Drbeds, and this area is our home. We are of Mongolian descent but we are not nomads."', profilepic='Amursana')            

            if text_ == 4.8:
                draw_bg('Altai')               
                drawText('Amursana: "Being the source of the Irtysh River, the soil is rich and fertile here. It is the perfect spot for farms and crops."', profilepic='Amursana')            

            if text_ == 4.9:
                draw_bg('Altai')               
                drawText('"We should set up a supply depot here."', profilepic='Amursana') 

            if text_ == 5.0:
                draw_bg('Altai')               
                drawText('Can you set up a supply depot successfully? What is the percentage increase if 20 is increased to 35? Include % sign in answer.') 

            if text_ == 5.1:
                draw_bg('Altai')               
                draw_tbox()
                buttondrawn = "Textinput"

            if text_ == 5.2:
                draw_bg('Altai')               
                if checkanswer('4aa'):
                    drawText('Supply depot set up successfully. Teacher approval + 1.')
                else:
                    drawText('Even in the best of conditions you failed to set up a supply depot. Qing army strength drops.')
                    if first_change:
                        army -= 1
                        first_change = False
            
            if text_ == 5.3:
                drawText('At long last, the two armies on the North and West routes convene at Bortala river, gateway to Ili.')

            if text_ == 5.4:
                drawText('Dawachi, the enemy leader, sent two of his lieutenants into battle. Can you defeat them?')

            if text_ == 5.5:
                drawText('A number increased by 5% is 12.6. What is the number?')

            if text_ == 5.6:
                draw_tbox()
                buttondrawn = "Textinput"

            if text_ == 5.7:
                if checkanswer('4b'):
                    drawText('Teacher approval + 1. You annihilated their army and captured one of the lieutenants.')
                    if first_change:                    
                        app['teacher_app'] += 1
                        first_change = False
                else:
                    drawText('Teacher approval - 1. Qing army strength drops. You were defeated by a vastly inferior enemy.')
                    if first_change:                  
                        app['teacher_app'] -= 1
                        army -= 1
                        first_change = False  

            if text_ == 5.8:
                drawText('You press on towards Gedeng Mountain, where Dawachi is dug in. Gedeng is Mongolian for "bone at back of head", named for the mountain\'s shape.')

            if text_ == 5.9:                
                drawText('You decide to raid Dawachi\'s camp at night. Will it be successful?')

            if text_ == 6:
                drawText('What is the angle to 2 decimal places, if in a right angle triangle opposite is 4 and hypotenuse is 9?')

            if text_ == 6.1:
                draw_tbox()
                buttondrawn = "Textinput"

            if text_ == 6.2:
                if checkanswer('4c'):
                    drawText('Teacher approval + 1. With only 22 men you routed Dawachi\'s thousands strong. Dawachi fled South towards Hui Jiang (modern day Xin Jiang).')
                    if first_change:                    
                        app['teacher_app'] += 1
                        first_change = False
                else:
                    drawText('Teacher approval - 1. Qing army strength drops. The night raid failed and you lost a lot of soldiers. Dawachi led his troops South towards Hui Jiang (modern day Xin Jiang).')
                    if first_change:                  
                        app['teacher_app'] -= 1
                        army -= 1
                        first_change = False  


            if text_ in [6.3, 6.31, 6.32, 6.33]:
                if army == 3:
                    drawText('While escaping through Hui Jiang, Dawachi was captured by the Uyghur prefect Khojis and handed over to the Qing army. All Dzungar resistance ceases.')
                    if first_change:                  
                        text_ = 6.31
                        first_change = False  
                if 0 < army < 3:
                    drawText('Gathering the last of his troops, Dawachi summons a fight with you to the death.')
                    if first_change:                  
                        text_ = 6.32
                        first_change = False                      
                if army <= 0:
                    drawText('Suffering from terrible leadership and low morale, many of your troops deserted. The tables have turned against you. You must make a last-ditch attempt to come out alive.')
                    if first_change:                  
                        text_ = 6.33
                        first_change = False 

            if text_ == 6.41:
                drawText('My victory is total. My success knows no predecessor. Long livel the Qing Dynasty! Teacher approval + 7. Father Emperor approval + 7.', profilepic='MC')
                if first_change:                  
                    app['father_app'] += 7
                    app['teacher_app'] += 7
                    sequence.append('Battle: Success')
                    first_change = False       

            if text_ == 6.51:
                if first_change: 
                    first_change = False                 
                    sequence.remove('Battle')      
                    scene = 6                        

            if text_ == 6.42:
                draw_bg('Dzungar_surrounded')  
                drawText('"Watch this!", Dawachi called, as he struck at you with his sword.')

            if text_ == 6.52:
                draw_bg('Dzungar_surrounded')  
                drawText('There are 5 numbers. 4 of them are: 6, 12, 9, 18. The median of the 5 numbers is 11. What is the missing number?')
              
            if text_ == 6.62:
                draw_tbox()
                buttondrawn = "Textinput"

            if text_ == 6.72:
                if checkanswer('4d'):
                    drawText('"Phew, that was a close win. Some of the losses were unnecessary though. Long live the Qing Dynasty!"', profilepic='MC')
                    if first_change:                  
                        app['father_app'] += 4
                        app['teacher_app'] += 4
                        sequence.insert(0, 'Battle:Success')
                        first_change = False  

                else:
                    draw_bg('Dzungar_surrounded')  
                    drawText('"Arrgh, retreat, retreat! The cause is lost."', profilepic='MC')  
                    if first_change:                  
                        app['father_app'] -= 4
                        app['teacher_app'] -= 4
                        sequence.insert(0, 'Battle:Failure')
                        first_change = False                                           

            if text_ == 6.82:
                if first_change: 
                    first_change = False                 
                    sequence.remove('Battle')      
                    scene = 6                  


            if text_ == 6.43:
                draw_bg('Dzungar_surrounded')             
                drawText('As far as the eye can see are enemies. You and your men are on their last stand. This is life and death.')                              

            if text_ == 6.53:
                draw_bg('Dzungar_surrounded')  
                drawText(f'The radius of a cylinder is 2cm, the volume 600cm\N{SUPERSCRIPT THREE}. What is the height to 2 decimal places?')

            if text_ == 6.63:
                draw_bg('Dzungar_surrounded')  
                draw_tbox()
                buttondrawn = "Textinput"

            if text_ == 6.73:
                if checkanswer('4e'):
                    drawText('"Phew, I barely got out of that alive... The battle is lost, but at least I live."', profilepic='MC')
                    if first_change:                  
                        app['father_app'] -= 5
                        app['teacher_app'] -= 5
                        sequence.insert(0, 'Battle:Failure')
                        first_change = False  

                else:
                    draw_bg('Dzungar_surrounded')  
                    drawText('"There is no way out, and only one thing is left to do..."', profilepic='MC')  
                    if first_change:                  
                        ending = "Death on battlefield"
                        first_change = False    


            if text_ == 6.83 and not ending:
                if first_change: 
                    first_change = False                 
                    sequence.remove('Battle')      
                    scene = 6                      


            if text_ >= 4.3:
                team(['Soldier'] * army)            

#endregion 
 
 
 #region      ### THIRD SCENE home...
        if scene == 4 and sequence[-1] == 'Home':
            draw_bg('Study')

            if len(str(text_)) > 3 and str(text_)[3] == '2':
                draw_bg('Study_outdoors')

            if text_ == 4:
                drawText('Having lost the chance to prove yourself, you retired home to study.')
            
            if text_ == 4.1:
                drawText('Mindlessly, you flipped open a book at random. It opeoned to a Buddhist anecdote.')
 
            if text_ == 4.2:
                drawText('"The annals of Master Hui Neng", it reads.')

            if text_ == 4.3:
                drawText('"Master Hui Neng was the sixth generation successor of Zen Buddhism."')

            if text_ == 4.4:
                drawText('"Master Hui Neng\'s childhood was filled with hardships. He lost his father at an early age, and had to sell firewood to make a living for him and his mother."')                 
 
            if text_ == 4.5:
                drawText('"Through chance he became the pupil of Master Hong Ren (弘忍大師, 黃梅縣) -  the fifth generation successor of Zen Buddhism."')   

            if text_ == 4.6:
                drawText('Your mouth opened into a big yawn. Can you keep awake?')  
 
            if text_ == 4.7:
                drawText('What is the value of c in y = -3x + c, if it passes through point (8,-25)')  

            if text_ == 4.8:
                draw_tbox()
                buttondrawn = "Textinput"    

            if text_ == 4.9:
                if checkanswer('5a'):
                    drawText('You mastered your boredom and remained focused. Teacher approval + 1')
                    if first_change:                  
                        app['teacher_app'] += 1
                        first_change = False    

                else:
                    drawText('You fell asleep. Learning - 1. Teacher approval - 1.')     
                    if first_change:                  
                        app['teacher_app'] -= 1
                        army -= 1
                        first_change = False                                             

            if text_ == 5.0:
                drawText('"Master Hui Neng was unusually receptive towards Buddhist teachings. He was philosophical and intuitive."')

            if text_ == 5.1:
                drawText('"One day, Master Hong Ren asked all of his students to summarize their understanding of Zen in a few stanzas (like a poem)."')

            if text_ == 5.2:
                drawText('"A top student, Shen Xiu, wrote his thoughts on the corridor wall for everyone to see. Master Hui Neng added his reply underneath."')

            if text_ == 5.3:
                drawText('"Never did he imagine that his reply would become one of the most famous moments in Buddhist history, and eternalized in scriptures and art. It shifted Buddhism to a completely new level of accessibility."')

            if text_ == 5.4:
                drawText('Which of the following is Master Hui Neng\'s reply? (The other one is Shen Xiu\'s work)')

            if text_ == 5.5:
                draw_button()
                draw_button_text(['Poem 1'], 1)
                draw_button_text(['Poem 2'], 2)
                screen.blit(bg['Poem1'], bg['Poem1'].get_rect(center = ((buttonxy[0] + buttonsize[0] // 2, Y // 2 - 60))))
                screen.blit(bg['Poem1English'], bg['Poem1English'].get_rect(center = (buttonxy[0] + buttonsize[0] // 2, Y // 2 + 60)))
                screen.blit(bg['Poem2'], bg['Poem2'].get_rect(center = ((buttonxy[0] + buttonsize[0] + 20) + buttonsize[0] // 2, Y // 2 - 60)))
                screen.blit(bg['Poem2English'], bg['Poem2English'].get_rect(center = ((buttonxy[0] + buttonsize[0] + 20) + buttonsize[0] // 2, Y // 2 + 60)))                                
                buttondrawn = "Button"                
                if first_change:
                    first_change = False
                    buttonstages.append(text_)                

            if text_ == 5.51:
                drawText('Wrong, you have no idea what Zen is, and have no hope of ever grasping it. Learning - 1. Teacher approval - 1')
                if first_change:
                    first_change = False
                    app['teacher_app'] -= 1
                    army -= 1

            if text_ == 5.52:
                drawText('Excellent., you have grasped the concept of Zen. Teacher approval + 1')
                if first_change:
                    first_change = False
                    app['teacher_app'] += 1

            if text_ == 5.61 or text_ == 5.62 or text_ == 5.6:
                drawText('"With that breakthrough in understanding Master Hui Neng became the natural successor for the sixth generation."')
                text_ = 5.6

            if text_ == 5.7:
                drawText('"But he feared persecution from those who envied him, and was forced to move South towards Guang Dong."')

            if text_ == 5.8:
                drawText('You found your eyelids growing heavy again, and once more you fought with sleep for control.')

            if text_ == 5.9:
                drawText('What is the midpoint of (0,0) and (6,4)?')
            
            if text_ == 6:
                draw_tbox()
                buttondrawn = "Textinput"    

            if text_ == 6.1:
                if checkanswer('5b'):
                    drawText('You steadied yourself and continued your study. Teacher approval + 1.')
                    if first_change:
                        first_change = False
                        app['teacher_app'] += 1

                else:
                    drawText('Teacher: "Your snore is so loud the soldiers can hear it in the training ground!" Teacher approval - 1')
                    if first_change:
                        first_change = False
                        app['teacher_app'] -= 1
                        army -= 1                    

            if text_ == 6.2:
                drawText('"In Fa Xing temple in Guang Dong, Master Hui Neng became acquainted with Master Yin Zong. There he had his hair cut off by him and was finally initiated as a monk."')
            
            if text_ == 6.3:
                drawText('"It was also at Fa Xing temple that he first explained the concept of `Not two`, a distilled essence of Zen."')

            if text_ == 6.4: 
                drawText('"The centrepiece of the doctrine refers to an original and true nature that is wihin all men. Zen does not seek release, because with release there are two sides, release and no release."')
            
            if text_ == 6.5: 
                drawText('"Zen does not seek kindness. Because that again has two sides, kind and unkind."')

            if text_ == 6.6: 
                drawText('"`Not two` refers to a character of the world that transcends duality. It exacts an all-pervading consciousness unrestrained by worldliness."')
            
            if text_ == 6.7:
                drawText('Teacher: "What did you understand so far?"')

            if text_ == 6.8:
                draw_button()
                draw_button_text(['Nothing'], 1)
                draw_button_text(['Everything'], 2)                              
                buttondrawn = "Button"                
                if first_change:
                    first_change = False
                    buttonstages.append(text_)                   

            if text_ == 6.81:
                drawText('It is true wisdom to understand and acknowledge your own limits. You are progressing well. Teacher approval + 1.')
                if first_change:
                    first_change = False
                    app['teacher_app'] += 1

            if text_ == 6.82:
                drawText('The bewilderment on your face says otherwise. Being honest with yourself is the first step in self cultivation. Teacher approval - 1.')
                if first_change:
                    first_change = False
                    app['teacher_app'] -= 1
                    army -= 1                   

            if text_ == 6.91 or text_ == 6.92 or text_ == 6.9:
                drawText('The chapter closes. Read next chapter?')
                text_ = 6.9

            if text_ == 7:
                draw_button()
                draw_button_text(['Definitely.'], 1)
                draw_button_text(['Enough of this!', 'I\'m out of here!'], 2)
                buttondrawn = "Button"                
                if first_change:
                    first_change = False
                    buttonstages.append(text_)                  

            ####################### Study branch ########################
            if text_ == 7.01:
                drawText('"The origin of Zen", the next chapter opened.')

            if text_ == 7.11:
                drawText('Brahma, the divine figure in Brahmanism, invited Buddha to speak to a great mass of people on Vulture Peak, India.')                

            if text_ == 7.21:
                drawText('"Offering a golden lotus to Buddha, Brahma asked him to share his wisdom with those gathered."')                

            if text_ == 7.31:
                drawText('"All eyes were on Buddha as they waited silently for him to speak. Yet for a long time Buddha did not say a single word. He only contemplated the golden lotus he held in his hand."')

            if text_ == 7.41:
                drawText('"One of the monks in the audience, Mahākāśyapa, smiled."')

            if text_ == 7.51:
                drawText('"Buddha noticed this, and knew that Mahākāśyapa was capable of becoming his successor."')

            if text_ == 7.61:
                drawText('Teacher: "Wake up! Tell me the meaning of Mahākāśyapa\'s smile, and why Buddha saw it as defining."')

            if text_ == 7.71:
                drawText('Four boxes have an average weight of 1.2kg. After adding one box, the average weight becomes 1kg. What is the weight of the added box, in kgs?')

            if text_ == 7.81:
                draw_tbox()
                buttondrawn = "Textinput"    

            if text_ == 7.91:
                if checkanswer('5c'):
                    drawText('"You have intuition beyond your years." Teacher approval + 1.')
                    if first_change:
                        first_change = False
                        app['teacher_app'] += 1

                else:
                    drawText('Teacher: "You are telling me you don\'t know anything?!" Teacher approval - 1')
                    if first_change:
                        first_change = False
                        app['teacher_app'] -= 1
                        army -= 1                   
            
            if text_ == 8.01:
                drawText('"Buddha\'s message, according to followers of Zen, is that absolute knowledge is gained from a physical act, rather than through words."')

            if text_ == 8.11:
                drawText('"Different people will find revelation through different encounters, but all of them are of a material type, of things that can be touched, seen, heard."')

            if text_ == 8.21:
                drawText('"Inner understanding can be unlocked when the heart is ready and when suitably prompted by an event. Lengthy texts on the metaphysical cannot achieve this."')

            if text_ == 8.31:
                drawText('"Buddha\'s contemplation of the golden lotus was the prompt Mahākāśyapa needed. This has since been termed "以心印心" - impressing heart upon heart without speech."')

            if text_ == 8.41:
                drawText('Teacher: "Show me that you understand. What is the total amount after 3 years if a person deposited 21000 into a bank paying 2.6% interest? Give answer to 2 decimal places."')

            if text_ == 8.51:
                draw_tbox()
                buttondrawn = "Textinput"    

            if text_ == 8.61:
                if checkanswer('5d'):
                    drawText('"Wonderful! Your hard work will serve you well in life." Teacher approval + 1.')
                    if first_change:
                        first_change = False
                        app['teacher_app'] += 1

                else:
                    drawText('Teacher: "You have again proven yourself to be unworthy." Teacher approval - 1')
                    if first_change:
                        first_change = False
                        app['teacher_app'] -= 1
                        army -= 1                   

            if text_ == 8.71:
                drawText(f"Messenger: \"The messenger respectfully meets the {'prince' if character == 'Male' else 'princess'}.\"", profilepic="messenger")

            if text_ == 8.81:
                drawText(f'{name}: "Come in"', profilepic="MC")

            if text_ == 8.91:
                drawText('Messenger: "Sister princess asks you for help with the Spring ceremony. She has forgotten to bring some important accessories."', profilepic="messenger")

            if text_ == 9.01:
                drawText('"Special cups are needed for the wine offering acts. Would you be able to supply them to the princess?"', profilepic="messenger")

            if text_ == 9.11:
                # Black background
                screen.fill('BLACK')
                # Prompt
                words = font.render("Enter A, B, C or D.", True, "BLACK", "WHITE")
                position = words.get_rect()
                position.center = (X//2, Y//2 + 85)
                screen.blit(words, position)
                # Images
                screen.blit(bg['yellow_winecup'], bg['yellow_winecup'].get_rect(center = (180, Y//2 - 30)))
                screen.blit(bg['white_winecup'], bg['white_winecup'].get_rect(center = (350, Y//2 - 30)))
                screen.blit(bg['blue_winecup'], bg['blue_winecup'].get_rect(center = (500, Y//2 - 30)))
                screen.blit(bg['bronze_winecup'], bg['bronze_winecup'].get_rect(center = (650, Y//2 - 30)))
                
                draw_tbox()
                buttondrawn = "Textinput"    

            if text_ == 9.21:
                if checkanswer('5e'):
                    drawText('"The princess sends her thanks." Teacher approval + 1, sister princess approval + 1.', profilepic="messenger")
                    if first_change:
                        first_change = False
                        app['teacher_app'] += 1
                        app['sister_app'] += 1

                else:
                    drawText('"That is the wrong choice. The Spring ceremony was ruined and the princess is furious with you." Teacher approval - 1, sister princess approval - 1', profilepic='messenger')
                    if first_change:
                        first_change = False
                        app['teacher_app'] -= 1
                        app['sister_app'] -= 1
                        army -= 1

            if text_ == 9.31:
                drawText('Teacher: "Bronze wares are common during the earlier eras, such as the Zhou Dynasty, but not the Qing dynasty. These later periods favour the use of porcelain, which are easier to craft and are more exquisite."')

            if text_ == 9.41:
                drawText('"Ceremonies are "colour-coded". The Sky altar (天壇) uses blue wares to mimic the sky, the Sun altar (日壇) dons red for the sun, the Moon altar (月壇) white, and the Earth altar (地壇) yellow."')

            if text_ == 9.51:
                drawText('"Because the Spring ceremony tributes the God of Crops and the God of Earth, ritual accessories are colored yellow. The yellow porcelain cup is the right choice."')




            ####################### Outdoor branch ########################
            if text_ == 7.02:
                drawText('(You went for a walk next to a stream. It attracts you with its unfathomable, silk-like surface.)') 

            if text_ == 7.12:
                drawText('Teacher: "Do you know much about this stream?"') 

            if text_ == 7.22:
                drawText('"It runs the length of the entire imperial palace. Most people see it as they enter the main Southern Entrance, Wu Men. It signals the start of the inner palace grounds."')                                   

            if text_ == 7.32:
                draw_popup('River_poem', 148)
                draw_popup('River_poem_English', 253)
                drawText('"As the Yuan Dynasty poet puts it, the river describes the rift between imperial aristocracy and the commoner."')   

            if text_ == 7.42:
                drawText('"Because it wounds so carelessly and gracefully, and its dark surface reminds people of jade, it is known as the "Jade Ribbon Stream"."')

            if text_ == 7.52:
                draw_bg('yuquanshan')
                drawText('"This is Yu Quan Mountain, where the \"Jade Ribbon Stream\" originates. From here, water travels more than 20km eastwards into the Imperial City, taking different names along the way."')

            if text_ == 7.62:
                draw_bg('kunminghu')
                drawText('"When the water reaches here it is known as Kun Ming Hu"')

            if text_ == 7.72:
                draw_bg('kunyuhe')
                drawText('"When the water reaches here it is known as Kun Yu He"')

            if text_ == 7.82:
                drawText('"And finally here it becomes Jade Ribbon Stream!"')

            if text_ == 7.92:
                draw_popup('Q5g', 200)
                drawText('"You have not been listening! What was it that I was telling you?"')

            if text_ == 8.02:
                draw_tbox()
                buttondrawn = "Textinput"            

            if text_ == 8.12:
                if checkanswer('5g'):
                    drawText('Well done, you are a natural scholar in geography and the classics. Teacher approval + 1.')
                    if first_change:
                        first_change = False
                        app['teacher_app'] += 1

                else:
                    drawText('Teacher: "Absolutely wrong. I advise you to book an appointment with the royal physician for a checkup. You have been falling asleep too often." Teacher approval - 1')
                    if first_change:
                        first_change = False
                        app['teacher_app'] -= 1
                        army -= 1

            if text_ == 8.22:
                drawText(f"Messenger: \"The lowly messenger bows to the {'prince' if character == 'Male' else 'princess'}'\"", profilepic='messenger')

            if text_ == 8.32:
                drawText(f'{name}: "You may rise. What is it?"', profilepic="MC")                

            if text_ == 8.42:
                drawText(f"Messenger: \"I carry the latest report from brother prince, about his campaign against the Dzungars.\"", profilepic='messenger')

            if text_ == 8.52:
                drawText(f"Messenger: \"He has successfully captured their leader and occupied their capital.\"", profilepic='messenger')

            if text_ == 8.62:
                drawText(f"Messenger: \"However, one of the surrendered generals, Amursana, rebelled. Some of our top generals were killed in the uprising.\"", profilepic='messenger')

            if text_ == 8.72:
                drawText(f"Messenger: \"Brother Prince has sent back army officials who have failed in their duty or were accused of misconduct. He asks you to decide on their fate.\"", profilepic='messenger')

            if text_ == 8.82:
                drawText(f'{name}: \"Hm... this is very important. I\'ll see to it now\"', profilepic="MC")    

            if text_ == 8.92:
                draw_popup('yongchang', 145)
                drawText_variable('永常,  \"Conqueror of the South\", is an ethnic Manchurian. ' \
                        'While commanding elite troops, he retreated out of cowardice. Indirectly caused the death of an ally general who was surrounded.', yposition=320)

                draw_button_3()   
                draw_button_text_3(['Execute','Imprison','Promote'])
                buttondrawn = "Button_3"              
                if first_change:
                    first_change = False
                    buttonstages.append(text_)

            if text_ == 8.921:
                drawText('Teacher: \"Good judgement. Desertion and cowardice must not be seen as being tolerated. As cruel a choice as this may seem, it is necessary for maintaining a disciplined army.\" '
                'Teacher approval + 1. Father Emperor approval + 1. Brother Prince approval + 1.')
                if first_change:
                    first_change = False
                    app['brother_app'] += 1
                    app['father_app'] += 1
                    app['teacher_app'] += 1

            if text_ == 8.922:
                drawText('Teacher: \"Sigh... you are too kind-hearted. Desertion leading to death belongs to the most serious of offences. This is especially true when cowardice is the cause.\" '
                'Teacher approval + 2. Father Emperor approval - 1. Brother Prince approval - 1.')
                if first_change:
                    first_change = False
                    app['brother_app'] -= 1
                    app['father_app'] -= 1
                    app['teacher_app'] += 2

            if text_ == 8.923:
                drawText('Teacher: \"Cowardice on the front lines cannot be tolerated. As a leading general he has more obligation than anyone else to set the right example. You fool!\" '
                'Teacher approval - 1. Father Emperor approval - 2. Brother Prince approval - 2.')
                if first_change:
                    first_change = False
                    app['brother_app'] -= 2
                    app['father_app'] -= 2
                    app['teacher_app'] -= 2












            # Combine the acts

            if text_ == 9.52 or text_ == 9.5:
                drawText('Teacher: "Now, let\'s proceed with the final lesson for today."')
                text_ = 9.5

            if text_ == 9.6:
                drawText('"In the writings of Hui Neng, it is stated that we all carry an "Original self" within us, and it is this "Original self" that we must strive to find."')

            if text_ == 9.7:
                drawText('"It is the truest state of being, the highest level of consciousness. Everything in this world are of equal standing in the light of this most clear and expansive understanding.             ')

            if text_ == 9.8:
                drawText('"Recall Zen\'s refutal of dualism. It circles back to that. Night and day are not TWO separate things but one and the same. Night defines day, and gives it existence. Emptiness is the precursor to the infinite transformations of this world; without space there can be no matter. It is this interlinked view of wholeness that is "Original Self:."')

            if text_ == 9.9:
                drawText('"In the same way, there is no distinction between Buddha and Man in this unclouded vision of equality. Buddha is someone who has discovered his "Original Self", but before that he is a man, just like you and me.        ')

            if text_ == 10.0:
                drawText('"Because this truest state of mind is inherent in all of us, we should direct our efforts at enlightenment to within ourselves. It is futile to look externally when the answer lies inside us."')
            
            if text_ == 10.1:
                drawText('Teacher: "Wake up, wake up! Were you listening? What is the number of sides of a regular polygon if its internal angle is 150?"')

            if text_ == 10.2:
                draw_tbox()
                buttondrawn = "Textinput"                                    
            
            if text_ == 10.3:
                if checkanswer('5f'):
                    drawText(f"\"Ah, you are a wise young {'man' if character == 'Male' else 'lady'}!\" Teacher approval + 1", profilepic="messenger")
                    if first_change:
                        first_change = False
                        app['teacher_app'] += 1
                        app['sister_app'] += 1

                else:
                    drawText('"Sloth is your biggest barrier to enlightenment." Teacher approval - 1', profilepic='messenger')
                    if first_change:
                        first_change = False
                        app['teacher_app'] -= 1
                        app['sister_app'] -= 1
                        army -= 1

            if text_ == 10.4:
                if 3 > army > 0:
                    drawText('Teacher: "You have made progress in your studies. I will let the Emperor know of your hard work. Father emperor approval + 1. Teacher approval + 1."')
                    if first_change:   
                        first_change = False                                           
                        sequence.insert(0, 'Home:Success')      
                        sequence.remove('Home')            

                elif army == 3:
                    drawText('Teacher: "You have shown patience, reflectiveness and commitment, enriching yourself remarkably within a short space of time. Father emperor approval + 2. Teacher approval + 2."')
                    if first_change:   
                        first_change = False                                           
                        sequence.insert(0, 'Home:Success')      
                        sequence.remove('Home')                       
            
                else:
                    drawText('Teacher: "You are much too possessed by earthly passions to have learned anything. This has been a complete waste of time.". Father emperor approval - 1. Teacher approval - 1.')
                    if first_change:   
                        first_change = False                                           
                        sequence.insert(0, 'Home:Failure')      
                        sequence.remove('Home')                       

            # At the end, but because code is run in a loop, see it as being instated at the beginning.
            if text_ >= 4.7 and text_ not in [5.5, 9.02]:
                team(['Learning'] * army)   
 
            # if text_ == 4.9:
            #     drawText('"A number increased by 5% is 12.6. What is the number?"')

            # if text_ == 5:
            #     draw_tbox()
            #     buttondrawn = "Textinput"

            # if text_ == 5.1:
            #     if checkanswer('4a'):
            #         drawText('Teacher approval + 1')
            #         app['teacher_app'] += 1
            #         text_ = 5.11

            #     else:
            #         drawText('Envoy: "There you go, you have no words left to argue with."')
            #         text_ = 5.12
            
            # if text_ == 5.21:
            #     drawText('Having bested the envoy in a debate, you sent him packing in shame back to his own camp')

            # if text_ == 5.22:
            #     drawText('Having been bested by the envoy in debate, some of your men deserted. Army strength - 1')
            #     army -= 1

            # if 5.3 > text_ >= 5.2:
            #     text_ = round(text_, 1)

            # if text_ == 5.3:
            #     text_ = 5.3
#endregion




        # All user interactions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False




            ####################################################################
            # First_change so that approvals are only adjusted once
            if event.type == pygame.MOUSEBUTTONDOWN and buttondrawn == "Normal":
                text_ = round(text_ + 0.1, 2)
                first_change = True
            



            ####################################################################
            # Logic is slightly different when button is drawn, no longer simply add 0.1
            elif event.type == pygame.MOUSEBUTTONDOWN and buttondrawn == "Button":
                

                # First button appends 0.01 to path marker
                # Path marker gets added to buttonstages then gets ejected after collision
                # Buttondrawn boolean ensures that clicking outside of buttons does not progress story
                if pygame.Rect(buttonxy[0], buttonxy[1], buttonsize[0], buttonsize[1]).collidepoint(event.pos) and text_ in buttonstages:
                    text_ = round(text_ + 0.01, 2)
                    buttondrawn = "Normal"
                    buttonstages.pop()
                    first_change = True                    

                # Second button appends 0.02 to path marker
                elif pygame.Rect(buttonxy[0] + buttonsize[0] + 20, buttonxy[1], buttonsize[0], buttonsize[1]).collidepoint(event.pos) and text_ in buttonstages:
                    text_ = round(text_ + 0.02, 2)
                    buttondrawn = "Normal"
                    buttonstages.pop()
                    first_change = True                                        




            ####################################################################
            # THREE buttons !!!!!!!!!!!!!!!!!
            elif event.type == pygame.MOUSEBUTTONDOWN and buttondrawn == "Button_3":
                

                # First button appends 0.001 to path marker
                # Path marker gets added to buttonstages then gets ejected after collision
                # Buttondrawn boolean ensures that clicking outside of buttons does not progress story
                if pygame.Rect(buttonxy3[0], buttonxy3[1], buttonsize[0], buttonsize[1]).collidepoint(event.pos) and text_ in buttonstages:
                    text_ = round(text_ + 0.001, 3)
                    buttondrawn = "Normal"
                    buttonstages.pop()
                    first_change = True                    

                # Second button appends 0.002 to path marker
                elif pygame.Rect(buttonxy3[0] + buttonsize[0] + 10, buttonxy3[1], buttonsize[0], buttonsize[1]).collidepoint(event.pos) and text_ in buttonstages:
                    text_ = round(text_ + 0.002, 3)
                    buttondrawn = "Normal"
                    buttonstages.pop()
                    first_change = True   

                # Third button appends 0.003 to path marker
                elif pygame.Rect(buttonxy3[0] + 2*(buttonsize[0] + 10), buttonxy3[1], buttonsize[0], buttonsize[1]).collidepoint(event.pos) and text_ in buttonstages:
                    text_ = round(text_ + 0.003, 3)
                    buttondrawn = "Normal"
                    buttonstages.pop()
                    first_change = True   




            ####################################################################
            # Logic is slightly different when input box is drawn, need to handle user input
            elif event.type == pygame.KEYDOWN and buttondrawn == "Textinput":

                # Press enter to submit
                if event.key == pygame.K_RETURN:
                        text_ = round(text_ + 0.1, 2)
                        buttondrawn = "Normal"
                        final_answer = answer
                        answer = ""


                # Backspace deletes
                elif event.key == pygame.K_BACKSPACE:
                    answer = answer[:-1]


                # Else concatenate input to answer string
                else:
                    answer += event.unicode



            

        # Show user input!
        if buttondrawn == "Textinput":
            userinput = font.render(answer, True, "Black")
            show_centered = userinput.get_rect()
            show_centered.center = (X // 2 - 20, Y // 4 * 3.25 + 5)
            screen.blit(userinput, show_centered)

            # Limit input size
            if userinput.get_width() > buttonsize[1] + 20:
                answer = answer[:-1]






        
        pygame.display.update()

        await asyncio.sleep(0)



asyncio.run(main())

# Python runs top down so will only reach this point when game loop exits
pygame.quit()