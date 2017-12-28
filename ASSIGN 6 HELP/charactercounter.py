'''
Let's build a GUI that looks like

 ___________________________
|     Character Counter     |  Window
/---------------------------\
|              _________    |
|   file name |         |   |     Label, Entry
|             |_________|   |
|                           |
|   ______________________  |
|  | space      17        | |     Text
|  | a           4        | |
|  |     ...              | |
|  |______________________| |
|                           |
|  ___________  _________   |
|  || Clear ||  || Exit ||  |     Button, Button
|  ||_______||  ||______||  |
|___________________________|

'''

from tkinter import *

class GUI:
    def __init__(self):
        # Create the main window
        self.window = Tk()
        
        # Assign a title for this window
        self.window.title('Character Counter')
        
        frame1 = Frame(self.window, bg = 'white')
        frame1.pack(side=TOP, expand=YES, fill=Y)
       
        frame2 = Frame(self.window, bg = 'yellow')
        frame2.pack(side=TOP, expand=YES, fill=BOTH) 
        
        frame3 = Frame(self.window, bg = 'white')
        frame3.pack(side=TOP, expand=YES, fill=BOTH) 
        
        label = Label(frame1, text = "File's Name")
        label.pack(side=LEFT)
        
        self.display = StringVar() 
        filename_entry = Entry(frame1, width = 10, textvariable = self.display)       
        filename_entry.pack(side=LEFT)
        
        self.text = Text(frame2, height=20, width=50)
        scroll = Scrollbar(frame2, command=self.text.yview)
        self.text.configure(yscrollcommand=scroll.set)  
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)   
        
        clearbutton = Button(frame3, text = 'Clear', command = self.clear)
        exitbutton = Button(frame3, text = 'Exit', command = quit)
        processbutton = Button(frame3, text = 'Read File', command = self.process)
        clearbutton.pack(side=TOP)
        processbutton.pack(side=TOP)
        exitbutton.pack(side=TOP)        
        
        # Enter tkinter main loop
        mainloop()



    def quit(self):
        self.window.destroy()
        

    def clear(self):
        self.display.set('')      
        self.text.delete('1.0',END)
        
    
    def process(self):
        filename = self.display.get()
        dictionary = GUI.read_text(filename) 
        output = GUI.print_dictionary(dictionary)
        self.text.insert(END,output)
        
        
    def read_text(filename):
        filein = open(filename, 'r')
        dictionary = {}
            
        line = filein.readline()
        
        while line != '':
            line = line.rstrip('\n')
            line = line.lower()
                
            for ch in line:
                val = dictionary.get(ch)
                if val == None:
                    dictionary[ch] = 1
                else:
                    dictionary[ch] += 1
                        
            line = filein.readline()
                           
        return dictionary
        

    def print_dictionary(dict):
        list_of_pairs = list(dict.items())
        list_of_pairs.sort()
            
        output = ''
        for key,val in list_of_pairs: 
            if key == ' ':
                output += '%-10s%3d\n' % ('space', val)
            else:
                output += '%-10s%3d\n' % (key, val)
                
        return output              
        
        
        
def main():        
    gui = GUI()
    
    
main()