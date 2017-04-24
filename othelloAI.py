# Othello AI


def maxDisks(tiles, turn_color, possibleMoves, blackPieceList, whitePieceList):

    if turn_color == "white":
        bestMove = ""
        lenlist = 0 
        for move in possibleMoves:
            if len(whitePieceList) > lenlist:
                lenlist = len(whitePieceList)
                bestMove = move

    if turn_color == "black":
        bestMove = ""
        lenlist = 0 
        for move in possibleMoves:
            if len(blackPieceList) > lenlist:
                lenlist = len(blackPieceList)
                bestMove = move


    return bestMove


def weightDisks(tiles):
    # weight 1

    weightList = [7,2,5,4,4,5,2,7,
                  2,1,3,3,3,3,1,2,
                  5,3,6,5,5,6,3,5,
                  4,3,5,6,6,5,3,4,
                  4,3,5,6,6,5,3,4,
                  5,3,6,5,5,6,3,5,
                  2,1,3,3,3,3,1,2,
                  7,2,5,4,4,5,2,7]

    for i in range (0,7):
        tiles[0,i] = weightList[i]
        tiles[1,i] = weightList[(i+8)]
        tiles[2,i] = weightList[(i+15)]
        tiles[3,i] = weightList[(i+22)]
        tiles[4,i] = weightList[(i+29)]
        tiles[5,i] = weightList[(i+36)]
        tiles[6,i] = weightList[(i+43)]
        tiles[7,i] = weightList[(i+50)]
        


    worst = 0     
    for move in possibleMoves:
        if eval(move) > worst:
            worst = eval(move)
            bestmove = move



    return bestmove 

    

    



            
        
    

    # check the length of blackPieceList
    # white piece list
