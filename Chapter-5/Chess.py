def isValidChessBoard(x):
    n=[1,2,3,4,5,6,7,8]
    l=['a','b','c','d','e','f','g','h']
    col=['w','b']
    s=[]
    t=['king','queen','pawn','bishop','rook','knight']
    try:
        for a in chess.values():
            s.append(a)
        if s.count('bking')>1 or s.count('wking')>1 or s.count('bqueen')>1 or s.count('wqueen')>1:
            print("Check no. of kings and queens.")
        if s.count('bpawn')>8 or s.count('wpawn')>8:
            print("Check no. of pawns.")
        if s.count('brook')>2 or s.count('wrook')>2:
            print("Check no. of rooks.")
        if s.count('bknight')>2 or s.count('wknight')>2:
            print("Check no. of knights.")
        if s.count('bbishop')>2 or s.count('wbishop')>2:
            print("Check no. of bishops.")

        for i in chess.keys():
            if int(i[0]) not in n or i[1] not in l:
                print(f"{i} is in wrong place. ")
            else:
                print("All positions are correct.")

        for j in chess.values():
            if j[0] not in col:
                print("Wrong color.")
            if j[1:] not in t:
                print(f"Wrong chess piece{j[1:]}.")
    except:
        print("The chessboard is correct.")
x={'1h':'bking'}
isValidChessBoard(x)
