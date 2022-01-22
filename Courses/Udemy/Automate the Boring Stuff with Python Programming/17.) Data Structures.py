cat = {'name': 'Zophie', 'age': 7, 'color':'gray'}

allCats = []
allCats.append({'name': 'Oaie', 'age': 2, 'color':'white'})
allCats.append({'name': 'Cibrix', 'age': 1, 'color':'orange'})
allCats.append({'name': 'Gipsy', 'age': 3, 'color':'orange'})
allCats.append({'name': 'Simba', 'age': 3, 'color':'orange'})
#ect.

print(allCats)

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ','mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ','low-L': ' ', 'low-M': ' ','low-R': ' ',}
print(theBoard)

import pprint
pprint.pprint(theBoard)

theBoard['mid-M'] = 'X'
pprint.pprint(theBoard)

theBoard['top-L'] = 'O'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'O'
theBoard['mid-L'] = 'X'
theBoard['low-R'] = 'X'
pprint.pprint(theBoard)

def printBoard(board):

    print(board['top-L'] + '    |   ' + board['top-M'] + '   |    ' + board['top-R'])
    print('---------------------   ')
    print(board['mid-L'] + '    |   ' + board['mid-M'] + '   |    ' + board['mid-R'])
    print('----------------------   ')
    print(board['low-L'] + '    |   ' + board['low-M'] + '   |    ' + board['low-R'])

printBoard(theBoard)









 









