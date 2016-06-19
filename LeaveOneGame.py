def printAdjList(AdjList):
    out = ""
    for key in AdjList:
        out =  key + " -> "
        for route in adjList[key]:
            out += str(route[0]) + "(" + str(route[1]) + ") "
        print out

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

#Generate a list of possible nodes
nodes = []
for node in adjList:
    nodes.append(node)

printAdjList(adjList)
