from Minimax.game_tree import Node
from turtle import *
import types

s = 70
startpos = (0, 250)


def drawing(node, pos):
    successors = getSuccessors(node)
    # print(successors)
    i = 0
    for elem in successors:
        goto(pos)
        if not isinstance(elem, list):
            newpos = (pos[0] + s * len(successors)/4 -
                      s * i, pos[1] - s)
            down()
            goto((newpos[0], newpos[1] + 15))
            up()
            goto(newpos)
            write(elem.move, 1)
        if (elem.move):
            drawing(elem, newpos)

        i += 1


# successor states in a game tree are the child nodes...
def getSuccessors(node):
    """
    avoir les successeurs
    """
    assert node is not None
    return node.children


def draw_tree(list):
    """
    Fonction à lancer pour dessinner une liste par exemple: [1, [2, [3, [4, 5], 6], 7, 8]]
    À donner en argument
    """
    up()
    drawing(list, startpos)
    exitonclick()

# myTree = [1, [2, [3, [4, 5], 6], 7, 8]]
# start_drawing(myTree)
