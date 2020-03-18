

def chapter1module ():
    print ('''CHAPTER 1
You walk into a gas station store to get some late night snacks.
       Your broken heart makes it hard to sleep. When you enter,you sadly
       realize that there is a line. Not too long but not short enough.
       While in the back of the line, you see your ex girlfriend with a new guy buying some gas.
       They are having a conversation.''')
    makedecision = str(input('''Press 'a' if you want to listen to her conversation.
                                Press 'b' if you want to cry.'''))
    if makedecision == "a":
        print  ( '''You hunch over to go unnoticed. You overhear your ex say,
                    'I love you so much baby. Way more than my ex. Heck, I
                    never loved him! Bahahahaha!' TRY AGAIN!''')
        chapter1module()
    elif makedecision == "b":
        makedecision2 = str(input( '''You start crying. Not just a normal cry either. A LOUD cry. Your ex turns
                    around and starts laughing. In fact, she is laughing
                    so hard that she is now crying too! Do you stay or run out!? Press 'c' to stay
                    or 'd' to run out.'''))
        if makedecision2 == "d":
            print("Try Again!")
            chapter1module()
        elif makedecision2 == "c":
            print('''CHAPTER 2
                  Your ex interlocks her hand with her new guy. They leave. You wipe your
                  tears. You are now almost at the front of the line. One person stands in front of you.''')
        
chapter1module()

def chapter2module ():
    makedecision = str(input('''Press 'a' if you want to run after your ex or press 'b' if
                                you want to stay in line'''))
    if makedecision == "a":
        print("Try Again!")
        chapter2module()
    else:
        print('''CHAPTER 3
                 A sketchy man enters the store and goes to the front of the line. The woman in front yells, 'Hey get in line
                 bucko!' The man slowly turns to her with a gun poking out of his jacket. The woman screams and runs out. You are frozen in shock. The robber points
                 his gun at the cashier. The robber yells, 'Gimme all the money!' He looks at You. 'Don't try to be a hero. Unless you wanna' be a zero!' The robber
                 looks back at the cashier. 'Hurry up!' ''')
chapter2module()

def chapter3module ():
    makedecision = str(input('''Press 'a' if you want to yell at the robber to leave. Press 'b' if you do not want to intervene!'''))
    if makedecision == "a":
        print ("You just got pistol whipped! You fall to the ground, holding your bleeding mouth.")
        makedecision2 = str(input("Press 'a' if you want to stop fighting. Press 'b' if you want to keep fighting!")) 
        if makedecision2 == "b":
            print("You just got shot! Try Again!!")
            chapter3module()
        elif makedecision2 == "a":
            print("The robber leaves you alone, but he still robs the store! Try Again!!")
    else:
        print('''CHAPTER 4
                 The robber has the money.Now he turns to leave.''')
chapter3module()

def chapter4module ():
    makedecision = str(input('''Press 'a' if you still do not want to intervene. Press 'b' if you are
                                brave enough to trip him!'''))
    if makedecision == "a":
        print ("No, no, no. You are not about to ignore this anymore!")
        chapter4module ()
    else:
        print ('''CHAPTER 5
                  You just tripped him! The robber hits his head on the ground. The gun falls out of the robbers
                  pants! You grab the gun and point it at the robber! Your hand is shaking.''')
chapter4module()

def chapter5module ():
    makedecision = str(input('''Press 'a' if you want to 'accidentally' shoot the robber.
                                 Press 'b' if you want to tell the robber to leave the store.
                                 Press 'c' if you want to rob the store now.'''))
    if makedecision == "a":
        print("You shot the robber! You don't know what to do! Try Again!")
        chpater5module()
    elif makedecision == "b":
        print ("You WON Bucko!!!!!")
        chapter1module()
    else:
        print('''You have the gun; you have the power. Your evil side kicks in. You
                point the gun at the store attendant. 'I'm robbing the place now!' You grab as many
                snacks as you want. And because you chose an option as inhumane as this, you must
                start over!''')
        chapter1module()
chapter5module()
        
                            
            
                 

    
                
        
                
        
            
                
  


                           



