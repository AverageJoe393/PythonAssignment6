"""
Name: Karl Honse
Date created: 11-2-2017
Purpose: a data type that I built to be used in any other program to help calculate data 
"""

class PlayersYear:
    #defines year player and stats
    def __init__(self, year, player, stats):

        self.__year = year
        self.__player = player
        self.__stats = stats
    
    #returns ony the stats list 
    def get_stats(self):
        return self.__stats
        
        
    #returns an ordered list of information player name, year, AB, S, D, T, HR, BA, SLG
    def __str__(self):
        return "%-15s%10s%10s%10s%10s%10s%10s%10.3f%10.3f" %(self.__player, self.__year, self.__stats[4], self.singles(), self.__stats[1], self.__stats[2], self.__stats[3], self.batting_average(), self.slugging_percentage())
    
    #Calculates how many singles each player had that year   
    def singles(self):
        return self.__stats[0] - self.__stats[1] - self.__stats[2] - self.__stats[3]


    #Calculates batting average
    def batting_average(self):
        return float(self.__stats[0]) / float(self.__stats[4])


    #Calculates slugging percentage
    def slugging_percentage(self):
        return (float(self.singles()) + float(self.__stats[1] * 2) + float(self.__stats[2] * 3) + float(self.__stats[3] * 4)) / float(self.__stats[4])


    #function for solving the less than problem
    def __lt__(self, other):
        if self.slugging_percentage() < other.slugging_percentage():
            outcome = True
        else:
            outcome = False
        return outcome


    #prints all playes in a format for averages. name, slugging percentage, year
    def print_player(self):
        print("%-17s%10.3f%13s" %(self.__player, self.slugging_percentage(), self.__year))

    #Heading for list of information player name, year, AB, S, D, T, HR, BA, SLG
    def heading1():
        print("---------------------------------------------------------------------------------------------\nPlayer              Year        AB        S         D          T        HR       BA       SLG\n---------------------------------------------------------------------------------------------")
    
    #heading for name, slugging percentage, year
    def heading2():
        print("---------------------------------------------\n   Player           Slugging %      Year\n---------------------------------------------")