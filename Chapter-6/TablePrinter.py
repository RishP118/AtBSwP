
def printTable(n):

    l=[]
    for i in range(len(n)):
        p=[]
        for j in range(len(n[i])):
            a=len(n[i][j])
            p.append(a)
            p.sort(reverse=True)
        l.append(strlen[0])
    print(l)

    for x in range(len(n[1])):
        for y in range(len(n)):
            print(n[y][x].rjust(l[y]), end=" ")
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
