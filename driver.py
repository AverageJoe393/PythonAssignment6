"""
Karl Honse 

driver file given to ensure that we created out data type correctly

"""

from PlayersYear import *

### tests __init() constructor
henry = PlayersYear('1971', 'Hank Aaron', [162, 22, 3, 47, 495])
barry = PlayersYear('2002', 'Barry Bonds',  [149, 31, 2, 46, 403])
babe = PlayersYear('1920', 'Babe Ruth', [172, 36, 9, 54, 457])
print()


### Retrieves private data (self.__stats) from a PlayersYear object
print("Hank Aaron's stats:", henry.get_stats())
print("Barry Bonds' stats:", barry.get_stats())
print("Babe Ruth's stats:", babe.get_stats())
print()

'''
__str__()  creates this string for stat1 in line #13 of this program:

Hank Aaron            1971     495      90      22       3      47    0.327    0.669
'''
print(henry)      ### tests __str__()
print(barry)
print(babe)
print()
print()

print('Hank Aaron has %d singles' % henry.singles())     ### tests singles() function
print('Barry Bonds has %d singles' % barry.singles())
print('Babe Ruth has %d singles' % babe.singles())
print()

### tests batting_average() function
print('Hank Aaron has %.5f average' % henry.batting_average())    
print('Barry Bonds has %.5f average' % barry.batting_average())
print('Babe Ruth has %.5f average' % babe.batting_average())
print()


### tests slugging_percentage() function
print('Hank Aaron has %.5f slugging percentage' % henry.slugging_percentage())   
print('Barry Bonds has %.5f slugging percentage' % barry.slugging_percentage())
print('Babe Ruth has %.5f slugging percentage' % babe.slugging_percentage())
print()


### tests __lt__() to compare slugging_percentages
print('Hank Aaron has a lower slugging percentage than Barry Bonds? ', henry < barry)          
print('Barry Bonds has a lower slugging percentage than Hank Aaron? ', barry < henry)
print('Babe Ruth has a lower slugging percentage than Hank Aaron? ', babe < henry)
print()

'''
print_player() displays:

Hank Aaron          0.669           1971
'''
henry.print_player()       ### tests print_player() function
barry.print_player()
babe.print_player()
print()
print()

'''
heading1() displays:

-------------------------------------------------------------------------------------
Player                Year      AB      S        D       T      HR     BA      SLG     
-------------------------------------------------------------------------------------
'''
PlayersYear.heading1()     ### tests static function heading1()
print()
print()
print()

'''
heading2() displays:

---------------------------------------------
   Player           Slugging %      Year
---------------------------------------------
'''
PlayersYear.heading2()      ### tests heading2()