from random import randint

def printAdjList(AdjList):
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
    print openNodes

    #Determine if which open nodes could be a move
    for node in openNodes:
        routes = AdjList[node]
        print str(node) + " : " + str(routes)
        for route in routes:
            print route
            if NodeState[route[0]] == 0 and NodeState[route[1]] == 0:
                move = route[0] + node + route[1]
                print str("MOVE(") + str(move) + "): " + str(route[0]) + " -> " + str(node) + " remove " + str(route[1])
                moves.append(move)
    return generateRandomNode(moves)
    return 0

def generateRandomNode(Nodes):
    r = randint(0,len(Nodes)-1)
    return Nodes[r]

def playGame(AdjList):
    #Setup game
    nodeState = dict()
    nodes = []
    for node in adjList:
        nodes.append(node)
        nodeState[node] = 0

    #Randomly pick a node to open to start the game
    nodeState[generateRandomNode(nodes)] = 1
    print nodeState

    #Randomly select an available move
    move = generateRandomMove(AdjList, nodeState)
    print "MOVE: " + str(move)


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

playGame(adjList)


