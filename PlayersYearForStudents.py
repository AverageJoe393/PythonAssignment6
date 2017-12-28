class PlayersYear:
    def __init__(self, year, player, stats):
        '''
        self.__year = the year (an int) this player register these stats
        self.__player = the players name (a string)
        self.__stats = this player's statistics (a list of ints)
        '''
        self.__year = year
        self.__player = player
        self.__stats = stats
    

    def get_stats(self):
        '''
        Returns the value of self.__stats to the caller.
        Don't forget to return a list of integers!
        '''
        
        
        
        
    def __str__(self):
        '''
        Returns a player's stats for a given the year as specified in heading1().
        Note this corresponds to a line like:
        Babe Ruth             1920     457      73      36       9      54    0.376    0.849
        '''
              ### your code goes here, don't forget to return a string!
             
        
    def singles(self):
        '''
        Returns the number of singles this player has in self.__year.
        '''
              ### your code goes here, don't forget to return an int!


    
    def batting_average(self):
        '''
        Returns the batting average of the self.__player in self__year.
        '''
             ### your code goes here, don't forget to return a float!


    
    def slugging_percentage(self):
        '''
        Returns the slugging percentage of self.__player in self.__year.
        The slugging percentage is the total number of bases / at bats. For example, 
        a triple = 3 bases, a single = 1 base, ...
        '''
             ### your code goes here, don't forget to return a float!



    def __lt__(self, other):
        '''
        Returns True is self's slugging percentage is smaller than the other's slugging percentage,
        otherwise, return False. You are allowed to call the slugging_percentage() function here.
        '''
            ### your code goes here, don't forget to return True or False!



    def print_player(self):
        '''
        Displays a player's stats for a given the year as specified in heading2().
        This corresponds to a line like:
        Babe Ruth           0.849           1920
        '''
             ### your code goes here, just print, nothing is returned!


    def heading1():
        '''
        Displays the heading1 shown in the drive.py.
        The heading is:
        -------------------------------------------------------------------------------------
        Player                Year      AB      S        D       T      HR     BA      SLG     
        -------------------------------------------------------------------------------------
        '''
             ### your code goes here, print exactly as shown in driver.py!
    
    
    def heading2():
        '''
        Displays the heading2 shown in the drive.py.
        The heading is:
        ---------------------------------------------
        Player           Slugging %      Year
        ---------------------------------------------
        '''
             ### your code goes here, print exactly as shown in driver.py!     