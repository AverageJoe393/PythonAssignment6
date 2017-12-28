"""
Name: Karl Honse
Date created: 11-2-2017
Purpose: Use a data type that I've created in order to read and organize data from text files. 




Sample run:
Enter a File Name: baseball.txt
All Players in file Order: 
---------------------------------------------------------------------------------------------
Player              Year        AB        S         D          T        HR       BA       SLG
---------------------------------------------------------------------------------------------
Hank Aaron         1971       495        90        22         3        47     0.327     0.669
Barry Bonds        2002       403        70        31         2        46     0.370     0.799
Rod Carew          1974       599       180        30         5         3     0.364     0.446
Ty Cobb            1912       553       166        30        23         7     0.409     0.584
Joe DiMaggio       1937       621       119        35        15        46     0.346     0.673
Mickey Mantle      1956       533       109        22         5        52     0.353     0.705
Roger Maris        1961       590        78        16         4        61     0.269     0.620
Willie Mays        1963       596       110        32         7        38     0.314     0.582
Wilbur Stargell      1978       390        67        18         2        28     0.295     0.567
Ted Williams       1957       420        96        28         1        38     0.388     0.731
Babe Ruth          1920       457        73        36         9        54     0.376     0.849
Bill Mazeroski      1960       538       110        21         5        11     0.273     0.392
Frank Gustine      1941       463        93        24         7         1     0.270     0.359
Thurman Munson      1975       597       151        24         3        12     0.318     0.429
Orlando Cepada      1967       563       121        37         0        25     0.325     0.524

All Averages is File Order: 
---------------------------------------------
   Player           Slugging %      Year
---------------------------------------------
Hank Aaron            0.669         1971
Barry Bonds           0.799         2002
Rod Carew             0.446         1974
Ty Cobb               0.584         1912
Joe DiMaggio          0.673         1937
Mickey Mantle         0.705         1956
Roger Maris           0.620         1961
Willie Mays           0.582         1963
Wilbur Stargell       0.567         1978
Ted Williams          0.731         1957
Babe Ruth             0.849         1920
Bill Mazeroski        0.392         1960
Frank Gustine         0.359         1941
Thurman Munson        0.429         1975
Orlando Cepada        0.524         1967

Sorted by Home Runs: 
---------------------------------------------------------------------------------------------
Player              Year        AB        S         D          T        HR       BA       SLG
---------------------------------------------------------------------------------------------
Frank Gustine      1941       463        93        24         7         1     0.270     0.359
Rod Carew          1974       599       180        30         5         3     0.364     0.446
Ty Cobb            1912       553       166        30        23         7     0.409     0.584
Bill Mazeroski      1960       538       110        21         5        11     0.273     0.392
Thurman Munson      1975       597       151        24         3        12     0.318     0.429
Orlando Cepada      1967       563       121        37         0        25     0.325     0.524
Wilbur Stargell      1978       390        67        18         2        28     0.295     0.567
Willie Mays        1963       596       110        32         7        38     0.314     0.582
Ted Williams       1957       420        96        28         1        38     0.388     0.731
Barry Bonds        2002       403        70        31         2        46     0.370     0.799
Joe DiMaggio       1937       621       119        35        15        46     0.346     0.673
Hank Aaron         1971       495        90        22         3        47     0.327     0.669
Mickey Mantle      1956       533       109        22         5        52     0.353     0.705
Babe Ruth          1920       457        73        36         9        54     0.376     0.849
Roger Maris        1961       590        78        16         4        61     0.269     0.620

Sorted by at bats: 
---------------------------------------------------------------------------------------------
Player              Year        AB        S         D          T        HR       BA       SLG
---------------------------------------------------------------------------------------------
Wilbur Stargell      1978       390        67        18         2        28     0.295     0.567
Barry Bonds        2002       403        70        31         2        46     0.370     0.799
Ted Williams       1957       420        96        28         1        38     0.388     0.731
Babe Ruth          1920       457        73        36         9        54     0.376     0.849
Frank Gustine      1941       463        93        24         7         1     0.270     0.359
Hank Aaron         1971       495        90        22         3        47     0.327     0.669
Mickey Mantle      1956       533       109        22         5        52     0.353     0.705
Bill Mazeroski      1960       538       110        21         5        11     0.273     0.392
Ty Cobb            1912       553       166        30        23         7     0.409     0.584
Orlando Cepada      1967       563       121        37         0        25     0.325     0.524
Roger Maris        1961       590        78        16         4        61     0.269     0.620
Willie Mays        1963       596       110        32         7        38     0.314     0.582
Thurman Munson      1975       597       151        24         3        12     0.318     0.429
Rod Carew          1974       599       180        30         5         3     0.364     0.446
Joe DiMaggio       1937       621       119        35        15        46     0.346     0.673

Sorted by slugging percentages (Hi to Low): 
---------------------------------------------
   Player           Slugging %      Year
---------------------------------------------
Wilbur Stargell       0.567         1978    <----- Fixed this sorting issue by moving listOfObj.sort above the for loop
Barry Bonds           0.799         2002
Ted Williams          0.731         1957
Mickey Mantle         0.705         1956
Joe DiMaggio          0.673         1937
Hank Aaron            0.669         1971
Roger Maris           0.620         1961
Ty Cobb               0.584         1912
Willie Mays           0.582         1963
Wilbur Stargell       0.567         1978
Orlando Cepada        0.524         1967
Rod Carew             0.446         1974
Thurman Munson        0.429         1975
Bill Mazeroski        0.392         1960
Frank Gustine         0.359         1941

"""

from PlayersYear import *

#reads the information from the text file and break it up into the pieces that the data type recognizes. 
def read_player_file(filename):
    
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

#read_player_file('dimaggio.txt')

#Displays each player within the specified file
def display_players(listOfObj):
    PlayersYear.heading1()
    for player in listOfObj:
        print(player)
    print()
    
#display_players(read_player_file('dimaggio.txt'))

#Displays the Averages for each player with help from the PlayersYear dta type
def display_averages(listOfObj):
    PlayersYear.heading2()
    for player in listOfObj:
        player.print_player()
    print()


#display_averages(read_player_file('dimaggio.txt'))

#Sets the key for sorting as the 3rd index of the get_stats data type aka the number of home runs
def getKeyOnHomeruns(player):
    return player.get_stats() [3]


#Sorts the players based on the number of home runs in ascending order
def sortByHomeRuns(listOfObj):
    PlayersYear.heading1()
    listOfObj.sort(key = getKeyOnHomeruns)
    for player in listOfObj:
        print(player)
    print()
    
#sortByHomeRuns(read_player_file('dimaggio.txt'))    

#Sets the key for sorting as the 4th index of get_stats aka number of times at bat that year
def getKeyOnAtBat(player):
    return player.get_stats() [4]

#Sorts the players based on the number of times they were at bat
def sortByAtBat(listOfObj):
    PlayersYear.heading1()
    listOfObj.sort(key = getKeyOnAtBat)
    for player in listOfObj:
        print(player)
    print()
        
    
#sortByAtBat(read_player_file('dimaggio.txt'))    


#additional function needed to set key as slugging percentage
def getKeyOnSlugging(player):
    return player.slugging_percentage() 

#sorting by slugging by descending order with use of reverse = True
def sortBySlugging(listOfObj):
    PlayersYear.heading2()
    listOfObj.sort(key = getKeyOnSlugging, reverse = True)
    for player in listOfObj:
        #listOfObj.sort(key = getKeyOnSlugging, reverse = True)
        player.print_player()
    print()        
    

#main function used to enter name of file as well as call the other functions in the order desired
def main():
    entry = input("Enter a File Name: ")
    listOfObj = read_player_file(entry)
    
    print("All Players in file Order: ")
    display_players(listOfObj)
    
    print("All Averages is File Order: ")
    display_averages(listOfObj)
    
    print("Sorted by Home Runs: ")
    sortByHomeRuns(listOfObj)
    
    print("Sorted by at bats: ")
    sortByAtBat(listOfObj)
    
    print("Sorted by slugging percentages (Hi to Low): ")
    sortBySlugging(listOfObj) 
    
    
    
main()



##1. Your first task is to create a function with one parameter (a file name) that reads each line of data and creates a PlayersYear object from that line, then places it in a list. After all lines are read, this list of PlayersYear objects is returned to the main function.

##2. Next, create a function with one parameter (the list of PlayersYear objects) to display all the players in a table proceeded by heading1.

##3. Next, create a function with one parameter (the list of PlayersYear objects) to display the averages of each player in a table proceeded by heading2.

##4. Next, create a function to get the key that permits sorting on the number of homeruns a player hits. This function has one parameter, (a Player object). This function returns the number of home runs hit by this PlayersYear object.

##5. Next, create a function with one parameter (the list of PlayersYear objects) that sorts this list with respect to home runs.

##6. Next, create a function to get the key that permits sorting on the number of at bats. This function has one parameter, (a Player object). This function returns the number of at bats of this PlayersYear object.

##7. Next, create a function with one parameter (the list of PlayersYear objects) that sorts this list with respect to at bats.

##8. Finally, the main() function (is where the functions are called) is described by the comments below:
#### Ask user to enter file's name
#### Read the data from the file, return a list of PlayersYear objects
#### Display all stats of the players (heading1)
#### Display all averages (heading2)
#### Display all stats of the players sorted by homer (heading1)
#### Display all stats of the players sorted by at bats (heading1)
#### Display all averages sorted from highest to lowest slugging percentage (heading2)