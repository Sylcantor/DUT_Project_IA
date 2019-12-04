from turtle import *
import types

s = 50
startpos = (0, 200)


def cntstrs(list):
    return len([item for item in list if isinstance(item, int)])


def drawing(tree, pos, head=0):
    c = cntstrs(tree)
    while len(tree):
        goto(pos)
        item = tree.pop(0)
        if head:
            write(item, 1)
            drawing(tree.pop(0), pos)
        else:
            if isinstance(item, int):
                newpos = (pos[0] + s*c/4 - s*cntstrs(tree), pos[1] - s)
                down()
                goto((newpos[0], newpos[1] + 15))
                up()
                goto(newpos)
                write(item, 1)
            elif isinstance(item, list):
                drawing(item, newpos)


def draw_tree(list):
    """
    Fonction à lancer pour dessinner une liste par exemple: [1, [2, [3, [4, 5], 6], 7, 8]]
    À donner en argument
    """
    up()
    drawing(list, startpos, 1)
    exitonclick()

# myTree = [1, [2, [3, [4, 5], 6], 7, 8]]
# start_drawing(myTree)
