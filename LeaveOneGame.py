from random import randint
import time

def printAdjList(AdjList):
    #Utility function to print adacency list
    out = ""
    for key in AdjList:
        out =  key + " -> "
        for route in adjList[key]:
            out += str(route[0]) + "(" + str(route[1]) + ") "
        print out

def generateRandomMove(AdjList, NodeState):
    moves = []
    #Establish list of open nodes
    openNodes = []
    for node in NodeState:
        if NodeState[node] == 1:
            openNodes.append(node)

    #Determine if which open nodes could be a move
    for node in openNodes:
        routes = AdjList[node]
        for route in routes:
            if NodeState[route[0]] == 0 and NodeState[route[1]] == 0:
                move = route[0] + node + route[1]
                moves.append(move)
    return generateRandomNode(moves)

def generateRandomNode(Nodes):
    if len(Nodes) == 0:
        return ""
    r = randint(0,len(Nodes)-1)
    return Nodes[r]

def playGame(AdjList):
    #Setup game
    moves = []
    nodeState = dict()
    nodes = []
    for node in adjList:
        nodes.append(node)
        nodeState[node] = 0

    # Randomly pick a node to open to start the game
    openNode = generateRandomNode(nodes)
    nodeState[openNode] = 1
    print "Starting with node \"" + str(openNode) + "\" open"

    # Randomly select an available move
    while(True):
        move = generateRandomMove(AdjList, nodeState)
        if not move:
            break
        moves.append(move)
        print str("MOVE(") + str(move) + "): " + str(move[0]) + " -> " + str(move[1]) + " remove " + str(move[2])
        nodeState[move[0]] = 1
        nodeState[move[1]] = 0
        nodeState[move[2]] = 1
    pegs = len(AdjList)
    for key in nodeState:
        pegs = pegs - nodeState[key]
    print "Number of moves: " + str(len(moves))
    print "Pegs remaining: " + str(pegs)
    print "--------------------------"
    return pegs



'''
Represents a directed graph depicting all legal moves:

    A
   B C
  D E F
 G H I J
K L M N O

Example: If A is open and D and B contain pegs, D can move to A removing B.
'''
adjList = {'A': [["D", "B"],["F", "C"]],
           'B': [["G", "D"],["I", "E"]],
           'C': [["J", "F"], ["H", "E"]],
           'D': [["A", "B"], ["K", "G"], ["M", "N"], ["F", "E"]],
           'E': [["L", "H"], ["N", "I"]],
           'F': [["A", "C"], ["O", "J"], ["M", "I"], ["D", "E"]],
           'G': [["B", "D"], ["I", "N"]],
           'H': [["C", "E"], ["J", "I"]],
           'I': [["B", "E"], ["G", "H"]],
           'J': [["C", "F"], ["H", "I"]],
           'K': [["D", "G"], ["M", "L"]],
           'L': [["E", "H"], ["N", "M"]],
           'M': [["K", "L"], ["O", "N"], ["D", "H"], ["F", "I"]],
           'N': [["L", "M"], ["E", "I"]],
           'O': [["M", "N"], ["F", "J"]]}

games = 0;
timeStart = int(round(time.time() * 1000))
#Play until a game results in a single peg remaining
while(True):
    games = games + 1
    pegs = playGame(adjList)
    if pegs == 1:
        break
print "Games played: " + str(games)
print "Elapse time: " + str((int(round(time.time() * 1000)) - timeStart)) + " ms"


