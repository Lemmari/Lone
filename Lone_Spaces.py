#Lone Spaces
#Lucas Brumatti

import random

Pasta = True #Random variable, used for primary testing
x = 1 #Since this operates in a grid, the values of x and y are needed
y = 1
Coordinates = ("(%d, %d)" %(x, y)) #This displays the coordinates in an understandable manner

Map_Size = int(input("> ")) #This allows the player to input the map size

Player_Pos = (Map_Size*(Map_Size+1))-Map_Size #This sets the player postion to be the bottom left of the map

Map = """""" #The starting string value for the displayed map
Places = []
Quadrants = Map.split(' ') #This is the values of each quadrant of the map, each quadrant is a light year

Spaces = ":" #This is the filler spaces of the map

On_Spot = False #Checks if there is another spaceship present

Ship = "" #Name of the ship

Ships_L = ["plasmoids", "drobiners", "frankengruller's", "cem-tills", "ellecents"] #Different types of ships that can be present, from most common to rarest
Ships_Symbols = ["C", "/", "@", "}", "§"] #The ships as they will be displayed on the map
Ships_Quadrants = [] #The placement of the ships on the map, starting from top left

Commands = """To move aroun the map, type:
up,
down,
left,
right
To access the map, just type 'map'
To access any of these commands again, type 'commands'""" #Commands to display

Foward = ['f', 'foward']
Backward = ['b', 'backwards']
Left = ['l', 'left']
Right = ['r', 'right']

def Ships():
    global Ships_L
    global Ship
    global Map_Size
    global Ships_Quadrants
    global Ships_Symbols
    
    Counter = 0

    for Counter in range(0, Map_Size): #Repeats ship generation
        
        x = 0
        
        Ship_P = random.randint(1, 100) #Chooses the random ship
        
        if Ship_P >= 1 and Ship_P <= 50: #Probabilities of most likely ships
            Ship = Ships_L[0] #Fetches the ship, in order of probability
            x=0 #Saves the correct ship
        elif Ship_P > 50 and Ship_P <= 75:
            Ship = Ships_L[1]
            x=1
        elif Ship_P > 75 and Ship_P <= 85:
            Ship = Ships_L[2]
            x=2
        elif Ship_P > 85 and Ship_P <= 90:
            Ship = Ships_L[3]
            x=3
        elif Ship_P > 90 and Ship_P <= 100:
            Ship = Ships_L[4]
            x=4

        Ship == Ships_L[x] #Saves ship name from list
        Ships_Quadrants += Ships_Symbols[x] #Appends the ship symbol from the Ship symbol list
        print(Ship) #Displays the type of ship
        print(Ships_Quadrants)
    print(len(Ships_Quadrants))

    Mapping();
    

def Movement():
    global x
    global y
    global Places
    global Player_Pos
    global Quadrants
    global On_Spot
    global Map_Size
    global Ship
    global Ships_Quadrants
    global Ships_Symbols
    global Ships_L

    On_Spot = False
    
    # x == 1, y == 1, Places[9] == 2
    # x == 1, y == 2, Places[8] == 1
    if Places[Map_Size-y] == x: #This allows the code to know if there is a ship in the quadrant of the player
        print("There's", Ship, "here")
        On_Spot = True
        
    if y != Map_Size: #Does not let player go beyond the map limits
        if Places[(Map_Size-1)-y] == x:
            Shippen = Quadrants[Player_Pos-(Map_Size+1)]
            n = Ships_Symbols.index(Shippen)
            Ship = Ships_L[n]
            Ship = Ship.title()
            print("There's", Ship, "in front of you")

    if x != Map_Size:           
        if Places[Map_Size-y] == x+1: #A slight variation on the previous code
            Shippen = Quadrants[Player_Pos+1] #Checks what type of ship to the right of the player 
            n = Ships_Symbols.index(Shippen)
            Ship = Ships_L[n]
            Ship = Ship.title()
            print("There's", Ship, "to your right")
        
    if x != 1:
        if Places[Map_Size-y] == x-1:
            Shippen = Quadrants[Player_Pos-1]
            n = Ships_Symbols.index(Shippen)
            Ship = Ships_L[n]
            Ship = Ship.title()
            print("There's", Ship, "to your left")
        
    if y != 1:
        if Places[(Map_Size+1)-y] == x:
            Shippen = Quadrants[Player_Pos+(Map_Size+1)]
            n = Ships_Symbols.index(Shippen)
            Ship = Ships_L[n]
            Ship = Ship.title()
            print("There's", Ship, "behind you")
            
    elif Places[Map_Size-y] != x:
        print("There's nothing here cowboy")
    else:
        print("There's nothing here cowboy")
    
    Input();

def Input():
    global Map
    global x
    global y
    global Player_Pos
    global Quadrants
    global Commands
    global On_Spot
    global Map_Size
    global Coordinates
    global Ships_L
    global Ships_Symbols
    global Spaces
    global Foward
    global Backward
    global Left
    global Right

    User_Input = input("> ").lower()

    Words = User_Input.split()

    if On_Spot == False:
        Quadrants[Player_Pos] = Spaces
    elif On_Spot == True:
        Quadrants[Player_Pos] = 'x'
        
    #Multijump
    if len(Words) == 3: #Checks to see if the word is a right length for the multijump
        if 'by' in Words: #It will only be accounted as a multijump if there is a 'by' present
            n = int(Words[2]) #The third value will always be the number of spaces to be jumped

            Spaces_Remaining_Up = Map_Size - y
            Spaces_Remaining_Right = Map_Size - x

            print(Player_Pos)
            
            for n in range(0, n):
                
                if Words[0] in Foward:
                    if Spaces_Remaining_Up <= n:
                        print("There's no way you can move there")
                        Input();
                        
                    if Spaces_Remaining_Up >= n and Player_Pos-n >= 0:
                        print(Player_Pos)
                        y = y + 1            
                        Player_Pos = Player_Pos - (Map_Size+1)

                        print(format(Coordinates, '>78'))

                        if Places[(Map_Size-1)-y] == x:
                            Shippen = Quadrants[Player_Pos-(Map_Size+1)]
                            n = Ships_Symbols.index(Shippen)
                            Ship = Ships_L[n]
                            Ship = Ship.title()
                            print("There's", Ship, "in front of you")
                            
                            print("Do you wish to continue?")
                            User_Input = input("> ").lower()
                            if User_Input == 'yes':
                                print("okay")
                            elif User_Input == 'no':
                                print("Stopping ship, sir")
                                Quadrants[Player_Pos+(Map_Size+1)] = Spaces
                                Quadrants[Player_Pos] = '^'
                                Map = ' '.join(Quadrants)
                                Input();

                    else:
                        print("There's no way you can move there")
                        Input();
                    
                if Words[0] in Right:
                    Quadrants[Player_Pos] = Spaces
                    x = x + 1
                    Player_Pos = Player_Pos + 1

                    print(format(Coordinates, '>78'))

                    if Places[Map_Size-y] == x+1: #A slight variation on the previous code
                        Shippen = Quadrants[Player_Pos+1] #Checks what type of ship to the right of the player 
                        n = Ships_Symbols.index(Shippen)
                        Ship = Ships_L[n]
                        Ship = Ship.title()
                        print("There's", Ship, "to your right")

                        print("Do you wish to continue?")
                        User_Input = input("> ").lower()
                        if User_Input == 'yes':
                            print("okay")
                        elif User_Input == 'no':
                            print("Stopping ship")
                            Quadrants[Player_Pos-1] = Spaces
                            Quadrants[Player_Pos] = '^'
                            Map = ' '.join(Quadrants)
                            Input();

                if Words[0] in Left:
                    Quadrants[Player_Pos] = Spaces
                    x = x - 1
                    Player_Pos = Player_Pos - 1

                    print(format(Coordinates, '>78'))

                    if Places[Map_Size-y] == x-1:
                        Shippen = Quadrants[Player_Pos-1]
                        n = Ships_Symbols.index(Shippen)
                        Ship = Ships_L[n]
                        Ship = Ship.title()
                        print("There's", Ship, "to your left")

                        print("Do you wish to continue?")
                        User_Input = input("> ").lower()
                        if User_Input == 'yes':
                            print("okay")
                        elif User_Input == 'no':
                            print("Stopping ship")
                            Quadrants[Player_Pos+1] = Spaces
                            Quadrants[Player_Pos] = '^'
                            Map = ' '.join(Quadrants)
                            Input();
                            
                if Words[0] in Backward:
                    Quadrants[Player_Pos] = Spaces
                    y = y - 1
                    Player_Pos = Player_Pos + (Map_Size+1)

                    print(format(Coordinates, '>78'))

                    if Places[(Map_Size+1)-y] == x:
                        Shippen = Quadrants[Player_Pos+(Map_Size+1)]
                        n = Ships_Symbols.index(Shippen)
                        Ship = Ships_L[n]
                        Ship = Ship.title()
                        print("There's", Ship, "behind you")

                        print("Do you wish to continue?")
                        User_Input = input("> ").lower()
                        if User_Input == 'yes':
                            print("okay")
                        elif User_Input == 'no':
                            print("Stopping ship")
                            Quadrants[Player_Pos-(Map_Size+1)] = Spaces
                            Quadrants[Player_Pos] = '^'
                            Map = ' '.join(Quadrants)
                            Input();

        else:
            print("What??")
            
    elif len(Words) == 1:

        if y < 10:
            if User_Input in Foward:
                y = y + 1            
                Player_Pos = Player_Pos - (Map_Size+1)
        if x < 10:
            if User_Input in Right:
                Quadrants[Player_Pos] = Spaces
                x = x + 1
                Player_Pos = Player_Pos + 1
        if y > 1:
            if User_Input in Backward:
                Quadrants[Player_Pos] = Spaces
                y = y - 1
                Player_Pos = Player_Pos + (Map_Size+1)
        if x > 1:
            if User_Input in Left:
                Quadrants[Player_Pos] = Spaces
                x = x - 1
                Player_Pos = Player_Pos - 1
            
    if User_Input == 'map':
        print(Map)

    if User_Input == 'commands':
        print(Commands)

    if User_Input == 'kill':
        quit

    Coordinates = ("(%d, %d)" %(x, y))
        
    Quadrants[Player_Pos] = '^'
    Map = ' '.join(Quadrants)
        
    print(format(Coordinates, '>78'))
    Movement();

    if y == 1 or y == Map_Size or x == 1 or x == Map_Size:
        print("You can't move there")
        print(format(Coordinates, '>78'))
        Movement();

    
#while Pasta == True:

def Mapping():
    global Map
    global Places
    global Quadrants
    global Map_Size
    global Ships_Quadrants

    print('-'.center(78, "-"))
    print(Ships_Quadrants)
    print(Ships_Quadrants[0])

    Map += ' '
    
    Lines = 0

    n = 0
    
    for Lines in range(0, Map_Size):
        
        Place = random.randint(1, Map_Size)
        Places += [Place]
        print(Place)
        Counter = 1
            
        for Counter in range(1, Place):
            Map += Spaces
            Map += ' '
            
        Map += Ships_Quadrants[n]
        Map += ' '

        n = n + 1
        
        Rest_Spaces = Map_Size - Place

        Counter = 0

        for Counter in range(0, Rest_Spaces):
            Map += Spaces
            Map += ' '

        Map += '\n'
        Map += ' '

    #print(Map)

    Quadrants = Map.split(' ')
    #print(Quadrants)
    #print(len(Quadrants))

    if Places[0] == Map_Size:
        Quadrants[Map_Size-1] = Spaces
        print("Tanken action!")
        Place = random.randint(1, Map_Size)
        Quadrants[Place] = 'x'
        Map = ' '.join(Quadrants)

    if Places[Map_Size-1] == 1:
        Quadrants[Player_Pos] = '^'
        print("Tanken action!")
        Place = random.randint(Map_Size*Map_Size-(Map_Size), Map_Size*Map_Size+1)
        Quadrants[Place] = 'x'
        Map = ' '.join(Quadrants)
        Pasta = False

    
    Quadrants[Player_Pos] =  "^"
    
    Map = ' '.join(Quadrants)
    #print(Quadrants)

    Map = ' '.join(Quadrants)
    print(Map)

    print("-".center(78, "-"))

    Input();

print("Lone Spaces".center(78, "|"))
print(Commands)
print("Type start to begin")
User_Input = input("> ").lower()
if User_Input == 'start':
    print("Beggining".center(78, " "))
    Ships();
else:
    print("Please input an actual command")
    quit
