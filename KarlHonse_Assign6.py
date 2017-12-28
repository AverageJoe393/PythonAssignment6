'''
Name: Karl Honse
Date created: 12-5-2017
Purpose: Learn how to creat a GUI that can utilize a data type
'''

from tkinter import *
from tkinter import messagebox
from PlayersYear import *

class MLBAnalyzer:
    def __init__(self):
      
        self.window = Tk()
            
        self.window.title('Major League Baseball Analyzer')
            
        
    # Create a menu
        menu = Menu(self.window)
        self.window.config(menu=menu)
        
    # Create submenu
        submenu = Menu(menu)
        about = Menu(menu)
        menu.add_cascade(label='Sort', menu=submenu)
        menu.add_cascade(label='About Analyzer', menu=about)

    # Add menu choices and group accordingly
        submenu.add_command(label='Sort on Home Runs', command=self.SortOnHR)
        submenu.add_command(label='Sort on At Bats', command=self.SortOnAB)
        submenu.add_command(label='Sort on Slugging Percentage', command=self.SortOnSP)
        submenu.add_command(label='Sort on Batting Average', command=self.SortOnBA)
        
        about.add_command(label='Help', command=self.Help)
           
    # First Frame Including 7 labels and 7 Entry boxes
        frame1 = Frame(self.window)
        
        PNLabel = Label(frame1, text="Player's Name", bg = "Light Blue")
        PNLabel.pack(side=LEFT)
        
        self.NameVar = StringVar()
        PNentrybox = Entry(frame1, width = 20, relief=SUNKEN, textvariable = self.NameVar)
        PNentrybox.pack(side=LEFT)
        
        
        YearLabel = Label(frame1, text="Year", bg = "Light Blue")
        YearLabel.pack(side=LEFT)
        
        self.YearVar = StringVar()
        Yearentrybox = Entry(frame1, width = 10, relief=SUNKEN, textvariable = self.YearVar) # had to specify the widths so that they would all fit inside the window
        Yearentrybox.pack(side=LEFT)
        
        
        HitsLabel = Label(frame1, text="Hits", bg = "Light Blue")
        HitsLabel.pack(side=LEFT)
        
        self.HitsVar = StringVar()
        Hitsentrybox = Entry(frame1, width = 10, relief=SUNKEN, textvariable = self.HitsVar)
        Hitsentrybox.pack(side=LEFT)
        
        
        DoublesLabel = Label(frame1, text="Doubles", bg = "Light Blue")
        DoublesLabel.pack(side=LEFT)
        
        self.DoublesVar = StringVar()
        Doublesentrybox = Entry(frame1, width = 10, relief=SUNKEN, textvariable = self.DoublesVar)
        Doublesentrybox.pack(side=LEFT)
        
        
        TriplesLabel = Label(frame1, text="Triples", bg = "Light Blue")
        TriplesLabel.pack(side=LEFT)
        
        self.TriplesVar = StringVar()
        Triplesentrybox = Entry(frame1, width = 10, relief=SUNKEN, textvariable = self.TriplesVar)
        Triplesentrybox.pack(side=LEFT)
        
        
        HRLabel = Label(frame1, text="Home Runs", bg = "Light Blue")
        HRLabel.pack(side=LEFT)
        
        self.HomeRunsVar = StringVar()
        HRentrybox = Entry(frame1, width = 10, relief=SUNKEN, textvariable = self.HomeRunsVar)
        HRentrybox.pack(side=LEFT)
        
        
        ABLabel = Label(frame1, text="At Bats", bg = "Light Blue")
        ABLabel.pack(side=LEFT)
        
        self.AtBatsVar = StringVar()
        ABentrybox = Entry(frame1, width = 10, relief=SUNKEN, textvariable = self.AtBatsVar)
        ABentrybox.pack(side=LEFT)           
        
        frame1.pack(side=TOP, expand = YES, fill=BOTH)
    # End of First frame 
       
    # Second Frame used to hold the File Name label and Entry box
        frame2 = Frame(self.window)
        
        self.FileLabel = Label(frame2, text="File Name", bg = "Light Blue")
        self.FileLabel.pack(side=LEFT)
        
        self.FileName = StringVar()
        Fileentrybox = Entry(frame2, width = 40, relief=SUNKEN, textvariable = self.FileName)
        Fileentrybox.pack(side=LEFT)        
        
        frame2.pack(side=TOP, expand = YES, fill=BOTH)
    # End of Second Frame
        
    # Third Frame Used to display the Header for the text box
        frame3 = Frame(self.window)
        
        self.HeaderLabel = Label(frame3, text=("%-18s%40s%24s%25s%25s%26s%23s%23s%23s" %("Player","Year","AB","S","D","T","HR","BA","SLG")), fg = "Blue")
        self.HeaderLabel.pack(side=LEFT)        
        
        frame3.pack(side=TOP, expand = YES, fill=BOTH)
    # End of Third Frame
        
    # Frame 4 used to display text box with verticle scroll bar
        frame4 = Frame(self.window)
        
        self.text = Text(frame4, height=10, width=175)  #95 to fit exact and skip to new line
        scroll = Scrollbar(frame4, command=self.text.yview)
        self.text.configure(yscrollcommand=scroll.set)
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)
        
        frame4.pack()
    # End of Frame 4
        
    # Frame 5 used to place 5 Buttons at the Bottom of the GUI
        frame5 = Frame(self.window)
        
        self.Compute = Button(frame5, text="Compute a Player's Statistics", command=self.compute)   # command tells which method is executed
        self.Compute.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.Process = Button(frame5, text="Process a Player File", command=self.process) 
        self.Process.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.Save = Button(frame5, text="Save Log", command=self.save)   
        self.Save.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.Clear = Button(frame5, text="Clear Player's Statistics", command=self.clear)  
        self.Clear.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.Quit = Button(frame5, text="Quit Baseball Analyzer", command=self.quit)  
        self.Quit.pack(side=LEFT, expand=YES, fill=BOTH)        
        
        frame5.pack(side=BOTTOM, expand=YES, fill=BOTH)
    # End of Frame 5 
        
        
    # main loop of the GUI holding all functions
        mainloop()
        
    # function used to take the information that the User has entered and turn in into the same format as the txt files would appear in the Text box
    def compute(self):
        year = self.YearVar.get()
        name = self.NameVar.get()
    # Set each entry box from above to a corrisponding variable to be able to make a PlayersYear object
        H = int(self.HitsVar.get())
        D = int(self.DoublesVar.get())
        T = int(self.TriplesVar.get())
        HR = int(self.HomeRunsVar.get())
        AB = int(self.AtBatsVar.get())
        
        stats = [H, D, T, HR, AB]
        
        playerInput = PlayersYear(year, name, stats)
        
        output = playerInput
        self.text.insert(END,output)
        self.text.insert(END,'\n')
        
        #print(playerInput)
        
        #print(player)
        #print(year)
        #print(stats)
        
    # read file function similar to how Assignment 4 worked
    def readFile(self, filename):
        
        fileIn = open(filename, 'r')
        YearPlayerStats = []
        for line in fileIn:
            line = line.rstrip('\n')
            year = line[:4]
            temp = line[4:].split(":")
            player = temp[0]
            temp2 = line.split(":")
            stats = temp2[1:6]
            
            for i in range(len(stats)):
                stats[i] = int(stats[i])
                
            YearPlayerStats.append(PlayersYear(year, player, stats))
            
        return YearPlayerStats


    # process function is used to take the name that the user had entered in the file name entry box and read it with the help of the readFile function above
    def process(self):
        filename = self.FileName.get()
        playerInput = self.readFile(filename)
        for player in playerInput:
            self.text.insert(END,player)
            self.text.insert(END,'\n')
                
        self.text.insert(END,'\n')            
        
    # saves everything that was in the Texk box as a txt file 
    def save(self):
        self.filename = "session_log.txt"
        f = open(self.filename, 'w')
        f.write(self.text.get('1.0', END))
        f.close()
    # displays a message box to ensure that the save was successful
        messagebox.showinfo("Success!", "All data in Text Widget saved as session_log.txt")
    
    # sets all the entry fields to blank or zero and removes any data that was in the text box
    def clear(self):
        self.NameVar.set('')
        self.YearVar.set('')
        self.HitsVar.set('0')
        self.DoublesVar.set('0')
        self.TriplesVar.set('0')
        self.HomeRunsVar.set('0')
        self.AtBatsVar.set('0')
        self.text.delete('1.0',END)        
    
    # destroys the GUI window stopping the program
    def quit(self):
        self.window.destroy()

    # Setting home runs as the key for use in the sort on home runs function
    def getKeyOnHomeRuns(self,player):
        return player.get_stats() [3] # using get stats from PlayersYear data type to specify which stat is home runs

    # re-enters the data that is already in the text box now sorted by highest home runs to lowest
    def SortOnHR(self):
        filename = self.FileName.get()
        listOfObj = self.readFile(filename)
        listOfObj.sort(key = self.getKeyOnHomeRuns, reverse = True)
        for player in listOfObj:
            self.text.insert(END,player)
            self.text.insert(END,'\n')
                
        self.text.insert(END,'\n')            

    # Setting at bat as the key
    def getKeyOnAtBat(self,player):
        return player.get_stats() [4]           
    
    # sorts on at bat
    def SortOnAB(self):
        filename = self.FileName.get()
        listOfObj = self.readFile(filename)
        listOfObj.sort(key = self.getKeyOnAtBat, reverse = True)
        for player in listOfObj:
            self.text.insert(END,player)
            self.text.insert(END,'\n')
                
        self.text.insert(END,'\n')

    # sorts on slugging percent
    def getKeyOnSlugging(self,player):
        return player.slugging_percentage() #using PlayerYear data type to calculate slugging percent
    
    # sorts on SP
    def SortOnSP(self):
        filename = self.FileName.get()
        listOfObj = self.readFile(filename)
        listOfObj.sort(key = self.getKeyOnSlugging, reverse = True)
        for player in listOfObj:
            self.text.insert(END,player)
            self.text.insert(END,'\n')
                
        self.text.insert(END,'\n')

    # sets key to batting average
    def getKeyOnBattingAve(self,player):
        return player.batting_average()
    
    # sorts on BA
    def SortOnBA(self):
        filename = self.FileName.get()
        listOfObj = self.readFile(filename)
        listOfObj.sort(key = self.getKeyOnBattingAve, reverse = True)
        for player in listOfObj:
            self.text.insert(END,player)
            self.text.insert(END,'\n')
                
        self.text.insert(END,'\n')
    
    # help function to display what the program does, can be found in the about sub menu
    def Help(self):
        messagebox.showinfo("Help", "1. Enter information for a player (namen year, ...) into the boxes, then click the Compute button. This will Display the player's Statistics in the Text box.\n\n2. Enter a file name in the box provided and click the Process button. This will display the stats of all of the players in the text file.\n\n3. Information in the Text box is saved to the same location as this file when Save button is pressed.\n\n4. Selecting the sort menu will give you multiple options on how you can sort the data once it is already in the Text box.\n\n5. Click the Clear button to erase all fields and the Text box.\n\n6. Click the Quit button to exit the analyzer.") 
          
def main():
    gui = MLBAnalyzer()
    
main()