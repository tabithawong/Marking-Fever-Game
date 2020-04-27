from tkinter import *
from math import *
from time import *
from random import *
from sys import *

root = Tk()
screen = Canvas(root, width=1000, height=600, background="white")
screen.pack()

def startScreen():
    global marking, startscreen
    #marking is defined here because we can't call setInitialValues without defining a level
    marking = PhotoImage ( file="marking.gif" )
    #draws startscreen image and binds mouse with startscreenclick function
    startscreen = screen.create_image(500,300,image = marking,anchor=CENTER)
    screen.bind( "<Button-1>", startScreenClick )

def startScreenClick(event):
    global xMouse,yMouse,level
    #deletes anything previously drawn
    screen.delete(ALL)
    xMouse = event.x
    yMouse = event.y
    #defines level based on which difficulty level a user clicks and then runs the game
    if 40 < xMouse < 310 and 465 < yMouse < 543:
        level = 1
        rungame()
    elif 360 < xMouse < 630 and 465 < yMouse < 543:
        level = 2
        rungame()
    elif 785 < xMouse < 955 and 465 < yMouse < 543:
        level = 3
        rungame()
    #sets level as a placeholder value and shows the instructions screen
    elif 450 < xMouse < 600 and 550 < yMouse < 600:
        level = 0
        #setInitialValues must be called to import the instructions screen image
        setInitialValues()
        instructions()
    return level

def instructions():
    global instruct
    #drawns instruction screen and binds mouse to instruction screen
    screen.create_image(500,300,image = instruct,anchor=CENTER)
    screen.bind( "<Button-1>", instructionClick )
    
def instructionClick(event):
    global xMouse,yMouse
    xMouse = event.x
    yMouse = event.y
    #if user clicks anywhere on the screen, startscreen is called
    if 0 < xMouse < 1000:
        screen.delete(instructions)
        startScreen()
    
def rungame():
    #runs the game
    global starttime,timeallowed,timetxt,level,clockDisplay,salary,testnum
    screen.bind( "<Button-1>", mouseClickHandler )
    setInitialValues()
    setupBackground()
    drawname()
    testtypepicker()
    #keeps track of time
    while timeallowed > 0 and salary > 5000 and testnum != 25:
        elapsedtime = time() - starttime
        if elapsedtime >= 1:
            timeallowed -= 1
            updatetime()
            starttime = time()
        else:
            screen.update()
        sleep(0.03)
        
def setInitialValues():
    global level,salary,rightar,salarycut,clockDisplay,xstarClick,mistakear,testtype,perfectar,namear,types,fired,instruct,yay
    global wrong, goldstars,madchoice,starttime,curtime,timeallowed,starar,goldstar,marking,testdrawing,testnum,testsleft,yRight,yWrong
    #sets initial salary and defines how the salary will decrease with each mistake
    salary = 80000
    salarycut = 0.5
    #arrays of words to be displayed on tests (some spelled incorrectly, some spelled correctly)
    mistakear = ["rythm","widhth","oppurtunity","wierd","neccessary","apearrance","acommplish","apartement","bassicaly","beleif","bussiness","intteligent","generaly","interruppt","percieve","reccomend","hight","dosen't","cubboard","enviroment","resterant","beleive","beggining","reciept","Febuary","dissapoint","fourty","freind","defanately","goverment"]
    perfectar = ["can't","confused","sleep","really","blossom","time","person","year","way","day","thing","man","world","life","hand","part","child","eye","woman","place","work","week","case","point","government","company","number","group","problem","fact"]
    #the list of names of students who wrote the tests
    namear = ["Phyllis Vance","Jim Halpert","Dwight Schrute","Kevin Malone","Angela Martin","Andy Bernard","Stanley Hudson","Meredith Palmer","Creed Bratton","Kelly Kapoor","Ryan Howard","Toby Flenderson","Michael Scott","Pam Beesly","Darryl Philbin"]
    #defines number and position of stars. also creates an array of stars so they can be deleted
    goldstars = 4
    starar = []
    xstarClick = 4250
    #defines starting time of game
    starttime = time()
    #defines user selected level
    if level == 3:
        timeallowed = 31
    elif level == 2:
        timeallowed = 46
    elif level == 1:
        timeallowed = 61
    #defines number of tests marked and number of tests left to mark
    testnum = 0
    testsleft = 25 - testnum
    #imports images
    goldstar = PhotoImage( file="goldstar.gif" )
    marking = PhotoImage( file="marking.gif" )
    instruct = PhotoImage ( file="instructions.gif" )
    fired = PhotoImage( file ="fired.gif" )
    yay = PhotoImage( file="yay.gif" )
    testdrawing = 0
    #sets variable for timer to be drawn
    clockDisplay = 0
    #empty arrays to store the y-values of test words
    yRight = []
    yWrong = []
    rightar = []
    #an array that prevents the same words from being drawn over and over again
    madchoice = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    #sets variable that represents incorrect word
    wrong = 0
    #controls the probability of a perfect vs. imperfect test
    types = ["True","True","True","True","True","True","True","True","True","True","True","True","True","True","True","True","True","True","True","True","True","False","False","False","False"]
    
def setupBackground():
    global salary1txt,salary2txt,testtxt,timetxt,clockDisplay,startxt,testsleft,timeallowed,goldstar,star,goldstars
    #draw separations
    screen.create_line(450,0,450,600, width = 3)
    screen.create_line(0,200,450,200, width = 3)
    screen.create_line(0,300,450,300, width = 3)
    screen.create_line(0,400,450,400, width = 3)
    screen.create_line(0,0,1000,0, width = 3)
    screen.create_line(0,600,1000,600, width = 3)
    screen.create_line(0,0,0,600, width = 3)
    screen.create_line(1000,0,1000,600, width = 3)
    #labels for sections
    salary1txt = screen.create_text(225,45, text = "SALARY:", font = "Arial 25")
    salary2txt = screen.create_text(225,125, text = str(salary),font = "Arial 40",fill = "red")
    testtxt = screen.create_text(225,250, text = "TESTS LEFT: " + str(testsleft), font = "Arial 25")
    timetxt = screen.create_text(210,350, text = "TIME LEFT: ", font = "Arial 25")
    startxt = screen.create_text(225,430, text = "GOLD STARS:", font = "Arial 25")
    #draw test paper
    screen.create_rectangle(550,50,900,550, fill = "antique white", width = 3)
    #draw gold stars
    xStar = 75
    for stars in range(goldstars):
        star = screen.create_image(xStar,520,image = goldstar,anchor=CENTER)
        starar.append(star)
        xStar = xStar + 100
    screen.update()

#defines what a click in certain areas will do
def mouseClickHandler( event ):
    global xMouse, yMouse,rightar, xstarClick, goldstars, starar, wrong,salary,salary2txt, types, testtype,testnum, numclicks, yWrong, yRight,yMistake,wrongclick1,wrongclick2,wrongtxt,rightclick1,rightclick2
    xMouse = event.x
    yMouse = event.y
    numclicks = 0

    #if user clicks in the test area
    if 625 < xMouse < 825:
        #if user clicks on a word that is spelled correctly (always wrong)
        if yMouse in yRight:
            #shows the user which word was actually spelled incorrectly
            if testtype == "True":
                #draws an x over the misspelled word
                wrongclick1 = screen.create_line(625,(yMistake-15),825,(yMistake+15),fill = "red")
                wrongclick2 = screen.create_line(825,(yMistake-15),625,(yMistake+15),fill = "red")
                wrongtxt = screen.create_text(725,300,text = "That word was correct, this one was wrong!",font = "Arial 15", fill= "red")
                screen.update()
                sleep(.35)
                screen.delete(wrongclick1,wrongclick2,wrongtxt)
                #decreases salary
                updatesalary()
                numclicks = 1
                #checks that this isn't the last click in the game (if so, a new test does NOT need to be drawn)
                if salary < 5000 or testnum == 25:
                    return numclicks
                else:
                    drawnewtest()
            #tells the user that the test was perfect (they should've clicked on a gold star!) 
            else:
                perftesttxt = screen.create_text(725,300,text = "This test has no mistakes!",font = "Arial 15", fill= "red")
                screen.update()
                sleep(.35)
                screen.delete(perftesttxt)
                #decreases salary
                updatesalary()
                numclicks = 1
                #checks that this isn't the last click in the game (if so, a new test does NOT need to be drawn)
                if salary < 5000 or testnum == 25:
                    return numclicks
                else:
                    drawnewtest()

        #if user clicks on a word that is spelled incorrectly
        elif yMouse in yWrong:
            if testtype == "True":
                #draws an x over the misspelled word
                rightclick1 = screen.create_line(625,(yMistake-15),825,(yMistake+15),fill = "red")
                rightclick2 = screen.create_line(825,(yMistake-15),625,(yMistake+15),fill = "red")
                screen.update()
                sleep(.35)
                screen.delete(rightclick1,rightclick2)
                numclicks = 1
                #checks that this isn't the last click in the game (if so, a new test does NOT need to be drawn)
                if salary < 5000 or testnum == 25:
                    return numclicks
                else:
                    drawnewtest()
                
            else:
                #should not need an else since if testtype == "False" then there is no misspelled word
                return ""

    #if the user clicks in the gold star box
    elif  25 < xMouse < xstarClick and 475 < yMouse < 560:
        if testtype == "False":
            #deletes the star on the far right
            xstarClick = xstarClick - 100
            screen.delete(starar[-1])
            starar.remove(starar[-1])
            goldstars = goldstars - 1
            numclicks = 1
            #checks that this isn't the last click in the game (if so, a new test does NOT need to be drawn)
            if salary < 5000 or testnum == 25:
                return numclicks
            else:
                drawnewtest()
                
        else:
            #displays message saying test wasn't perfect (star should not have been clicked)
            wrongstar = screen.create_text(225, 525, text = "The test wasn't perfect!",font = "Arial 20",fill = "red")
            screen.update()
            sleep(.35)
            screen.delete(wrongstar)
            #decreases salary
            updatesalary()
            numclicks = 1
            #checks that this isn't the last click in the game (if so, a new test does NOT need to be drawn)
            if salary < 5000 or testnum == 25:
                return numclicks
            else:
                drawnewtest()
                
def drawname():
    global namear, name,nameline
    #randomly picks a name from the namear array
    i = randint(0,14)
    #draws name and underline on screen
    name = screen.create_text(725,75, text = "Name: " + namear[i],font = "Arial 15")
    nameline = screen.create_line(630,87,830,87, width = 2)

def testtypepicker():
    global testtype,types
    #selects "testtype" (AKA a test with a misspelled word in it vs. a perfect test) from the types array (array was created to ensure a maximum of 4 perfect tests)
    if len(types) != 0:
        testtype = choice(types)
        #removes chosen type from array
        types.remove(testtype)
        #calls word drawing function according to the type chosen. "True" == has a mistake
        if testtype == "True":
            mistest()
        else:
            perftest()
    else:
        return ""
    
def mistest():
    global mistakear,perfectar,bad,sad,mad,wrong,right,testtype,mistake,yRight,yWrong,yMistake,rightar,madchoice
    #randomly selects position for misspelled word
    bad = randint(0,4)
    #randomly selects words from perfect and misspelled word arrays
    sad = randint(0,29)
    sd = 150
    rightar = []
    yWrong = []
    yRight = []
    for i in range(5):
        #incorrect word is drawn if i is equal to the randomly chosen number above
        if i == bad:
            #draws words that are a fixed distance above/below each other
            yMistake = (sd+(80*i))
            #creates a range of y-values for the player to click in
            for yRange in range(15):
                yWrong.append(yMistake+yRange)
                yWrong.append(yMistake-yRange)
            mistake = "True"
            #draws misspelled word
            wrong = screen.create_text(725,yMistake,text = mistakear[sad],font = "Arial 14")
            
        else:
            #draws words that are a fixed distance above/below each other
            yPerfect = (sd+(80*i))
            #creates a range of y-values for the player to click in 
            for yRange in range(15):
                yRight.append(yPerfect+yRange)
                yRight.append(yPerfect-yRange)
            mistake = "False"
            #randomly chooses an index to prevent repetition
            mad = choice(madchoice)
            madchoice.remove(mad)
            #draws correct words
            right = screen.create_text(725,yPerfect,text = perfectar[mad],font = "Arial 14")
            rightar.append(right)
        

def perftest():
    #draws a perfect test (no mistakes, happens only 4 times per game)
    global perfectar,testtype,rightar,madchoice
    sd = 150
    rightar = []
    yRight = []
    #very similar to mistest function except drawing of a misspelled word is omitted
    for i in range(0,5):
        yPerfect = (sd+(80*i))
        for yRange in range(15):
            yRight.append(yPerfect+yRange)
            yRight.append(yPerfect-yRange)
        mistake = "False"
        mad = choice(madchoice)
        madchoice.remove(mad)
        right = screen.create_text(725,yPerfect,text = perfectar[mad],font = "Arial 14")
        rightar.append(right)
        
def drawnewtest():
    #draws a new test after each round
    global salary1txt,salary2txt,testtxt,wrong,testtype,wrongar,rightar,timetxt,madchoice
    global startxt,testsleft,timeallowed,testtype,types,goldstar,star,goldstars,salary,salarycut,salarytxt2,xstarClick,mistakear,testtype,perfectar,namear,goldstars,starttime,curtime,timeallowed,starar,goldstar,marking,instruct,testdrawing,testnum,testsleft,yRight,yWrong
    #redefines array of indexes
    madchoice = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    #increases test number
    testnum = testnum + 1
    if testnum != 25:
        #deletes all the words for the next round
        updatetestsleft()
        screen.delete(wrong)
        #deletes differently based on test type (4 vs. 5 perfect words)
        if testtype == "True":
            for lol in range(4):
                screen.delete(rightar[lol])
        else:
            for hi in range(5):
                screen.delete(rightar[hi])
        screen.delete(testtxt,name,salary2txt)
        salary2txt = screen.create_text(225,125, text = str(salary),font = "Arial 40",fill = "red")
        testtxt = screen.create_text(225,250, text = "TESTS LEFT: " + str(testsleft), font = "Arial 25")
        #selects new name for test and reroutes program to pick the "type" of the next test
        drawname()
        testtypepicker()
    else:
        endgameg()
        
def updatesalary():
    #updates the salary, is only called in certain scenarios
    global salary,salarycut,salary2txt,name,nameline,testtxt,clockDisplay,testtype,rightar,wrong
    salary = int(salary * salarycut)
    #updates salary as long as it is over $5000
    if salary < 5000:
        screen.delete(ALL)
        endgameb()
        
def updatetestsleft():
    global testnum, testsleft,salary2txt,name,nameline,testtxt,clockDisplay,testtype,rightar,wrong
    screen.delete(testtxt)
    #updates text to display in testsleft as long as there are still tests left to mark
    if testnum <= 24:
        testsleft = 25 - testnum
    else:
        screen.delete(ALL)
        endgameg()

def updatetime():
    #updates timer display on screen
    global clockDisplay,timeallowed,salary2txt,name,nameline,testtxt,clockDisplay,testtype,rightar,wrong,salary,testnum
    if timeallowed > 0 and (salary > 5000 or testnum < 25):
        clockText = str(timeallowed)

        screen.delete(clockDisplay)
        clockDisplay = screen.create_text(325,350,text = clockText, font = "Arial 25")

        screen.update()
    else:
        #ends game if time runs out
        screen.delete(ALL)       
        endgameb()
        
def endgameb():
    #end of game screen if user makes too many mistakes or runs out of time
    global endscreen,fired,name,nameline,salary2txt,testtxt,testtype
    screen.delete(ALL)
    endscreen = screen.create_image(500,300,image = fired)
    screen.update()
    screen.bind( "<Button-1>", endgamebclick )
    
def endgamebclick( event ):
    global xMouse,yMouse
    xMouse = event.x
    yMouse = event.y
    #takes user back to startscreen if they click "yes" to play again. ends program if user clicks "no".
    if 425 < yMouse < 550:
        if 600 < xMouse < 725:
            screen.bind( "<Button-1>", startScreenClick )
            startScreen()
        elif 810 < xMouse < 900:
            root.destroy()
    
def endgameg():
    #end of game screen if user successfully marks all tests
    global endscreen,yay,name,nameline,salary2txt,testtxt
    endscreen = screen.create_image(500,300,image = yay)
    screen.update()
    screen.bind( "<Button-1>", endgamegclick )
    
def endgamegclick( event ):
    global xMouse, yMouse
    xMouse = event.x
    yMouse = event.y
    #takes user back to startscreen if they click "yes" to play again. ends program if user clicks "no".
    if 515 < yMouse < 565:
        if 145 < xMouse < 230:
            screen.bind( "<Button-1>", startScreenClick )
            startScreen()
        elif 745 < xMouse < 815:
            root.destroy()

#starts program at startscreen
root.after( 0, startScreen() )
screen.bind( "<Button-1>", startScreenClick )


##spacing = 50
##
##for x in range(0, 1000, spacing): 
##    screen.create_line(x, 25, x, 1000, fill="blue")
##    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N)
##
##for y in range(0, 1000, spacing):
##    screen.create_line(25, y, 1000, y, fill="blue")
##    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W)

screen.focus_set()
root.mainloop()
