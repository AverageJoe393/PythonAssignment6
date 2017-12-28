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
           
            
        frame1 = Frame(self.window)
        
        PNLabel = Label(frame1, text="Player's Name", bg = "Light Blue")
        PNLabel.pack(side=LEFT)
        
        self.NameVar = StringVar()
        PNentrybox = Entry(frame1, width = 20, relief=SUNKEN, textvariable = self.NameVar)
        PNentrybox.pack(side=LEFT)
        
        
        YearLabel = Label(frame1, text="Year", bg = "Light Blue")
        YearLabel.pack(side=LEFT)
        
        self.YearVar = StringVar()
        Yearentrybox = Entry(frame1, width = 10, relief=SUNKEN, textvariable = self.YearVar)
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
        
       
        
        frame2 = Frame(self.window)
        
        self.FileLabel = Label(frame2, text="File Name", bg = "Light Blue")
        self.FileLabel.pack(side=LEFT)
        
        self.FileName = StringVar()
        Fileentrybox = Entry(frame2, width = 40, relief=SUNKEN, textvariable = self.FileName)
        Fileentrybox.pack(side=LEFT)        
        
        frame2.pack(side=TOP, expand = YES, fill=BOTH)
        
        
        
        frame3 = Frame(self.window)
        
        self.HeaderLabel = Label(frame3, text=("%-18s%40s%24s%25s%25s%26s%23s%23s%23s" %("Player","Year","AB","S","D","T","HR","BA","SLG")), fg = "Blue")
        self.HeaderLabel.pack(side=LEFT)        
        
        frame3.pack(side=TOP, expand = YES, fill=BOTH)
        
        
        
        frame4 = Frame(self.window)
        
        self.text = Text(frame4, height=10, width=175)
        scroll = Scrollbar(frame4, command=self.text.yview)
        self.text.configure(yscrollcommand=scroll.set)
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)
        
        frame4.pack()
        
        
        
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
        
        
        mainloop()
    def compute(self):
        year = self.YearVar.get()
        name = self.NameVar.get()
        
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


    
    def process(self):
        filename = self.FileName.get()
        playerInput = self.readFile(filename)
        for player in playerInput:
            self.text.insert(END,player)
            self.text.insert(END,'\n')
                
        self.text.insert(END,'\n')            
        
    
    def save(self):
        self.filename = "session_log.txt"
        f = open(self.filename, 'w')
        f.write(self.text.get('1.0', END))
        f.close()
        messagebox.showinfo("Success!", "All data in Text Widget saved as session_log.txt")
    
    
    def clear(self):
        self.NameVar.set('')
        self.YearVar.set('')
        self.HitsVar.set('0')
        self.DoublesVar.set('0')
        self.TriplesVar.set('0')
        self.HomeRunsVar.set('0')
        self.AtBatsVar.set('0')
        self.text.delete('1.0',END)        
    
    def quit(self):
        self.window.destroy()


    def getKeyOnHomeRuns(self,player):
        return player.get_stats() [3]

    def SortOnHR(self):
        filename = self.FileName.get()
        listOfObj = self.readFile(filename)
        listOfObj.sort(key = self.getKeyOnHomeRuns, reverse = True)
        for player in listOfObj:
            self.text.insert(END,player)
            self.text.insert(END,'\n')
                
        self.text.insert(END,'\n')            


    def getKeyOnAtBat(self,player):
        return player.get_stats() [4]           
    
    def SortOnAB(self):
        filename = self.FileName.get()
        listOfObj = self.readFile(filename)
        listOfObj.sort(key = self.getKeyOnAtBat, reverse = True)
        for player in listOfObj:
            self.text.insert(END,player)
            self.text.insert(END,'\n')
                
        self.text.insert(END,'\n')


    def getKeyOnSlugging(self,player):
        return player.slugging_percentage()
    
    def SortOnSP(self):
        filename = self.FileName.get()
        listOfObj = self.readFile(filename)
        listOfObj.sort(key = self.getKeyOnSlugging, reverse = True)
        for player in listOfObj:
            self.text.insert(END,player)
            self.text.insert(END,'\n')
                
        self.text.insert(END,'\n')


    def getKeyOnBattingAve(self,player):
        return player.batting_average()
    
    def SortOnBA(self):
        filename = self.FileName.get()
        listOfObj = self.readFile(filename)
        listOfObj.sort(key = self.getKeyOnBattingAve, reverse = True)
        for player in listOfObj:
            self.text.insert(END,player)
            self.text.insert(END,'\n')
                
        self.text.insert(END,'\n')
    
    def Help(self):
        messagebox.showinfo("Help", "1. Enter information for a player (namen year, ...) into the boxes, then click the Compute button. This will Display the player's Statistics in the Text box.\n\n2. Enter a file name in the box provided and click the Process button. This will display the stats of all of the players in the text file.\n\n3. Information in the Text box is saved to the same location as this file when Save button is pressed.\n\n4. Selecting the sort menu will give you multiple options on how you can sort the data once it is already in the Text box.\n\n5. Click the Clear button to erase all fields and the Text box.\n\n6. Click the Quit button to exit the analyzer.") 
          
def main():
    gui = MLBAnalyzer()
    
main()