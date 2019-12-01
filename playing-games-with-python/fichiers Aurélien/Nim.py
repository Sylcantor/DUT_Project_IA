class Nim:
    def __init__(self, my_id):
        self.name = 'Bot'
        self.my_id = my_id
        self.parent = 0
        self.children = []

    def __repr__(self):
        if self.children:
            return str((object.__repr__(self), self.name, self.my_id, self.parent, self.children))[1:-1]
        return str((object.__repr__(self), self.name, self.my_id, self.parent))[1:-1]


def generate_some_objects():
    objects = [Nim(i) for i in range(7)]
    objects[0].name = 'Human'
    objects[6].name = 'Human'
    objects[6].parent = objects[5].my_id
    return objects


objects = generate_some_objects()
print('ALL:', objects)

parent = None
for nim in objects:
    if nim.my_id == nim.parent:
        parent = nim
        break
print('Parent:', parent)

indexed_objects = {nim.my_id: nim for nim in objects}
for nim in objects:
    if nim.my_id != nim.parent:
        my_parent = indexed_objects[nim.parent]
        my_parent.children.append(nim)

print('Parent:', [parent])

"""
ALL: ['<__main__.Nim object at 0x0171BD30>', 'Human', 0, 0, '<__main__.Nim object at 0x0171BD10>', 'Bot', 1, 0, '<__main__.Nim object at 0x0171BD50>',
'Bot', 2, 0, '<__main__.Nim object at 0x0171BD70>', 'Bot', 3, 0, '<__main__.Nim object at 0x0171BDB0>', 'Bot', 4, 0, '<__main__.Nim object at 0x0171BE10>', 'Bot', 5, 0, '<__main__.Nim object at 0x0171BE30>', 'Human', 6, 5]
Parent: '<__main__.Nim object at 0x0171BD30>', 'Human', 0, 0
Parent: ['<__main__.Nim object at 0x0171BD30>', 'Human', 0, 0, ['<__main__.Nim object at 0x0171BD10>', 'Bot', 1, 0, '<__main__.Nim object at 0x0171BD50>', 'Bot', 2, 0, '<__main__.Nim object at 0x0171BD70>', 'Bot', 3, 0, '<__main__.Nim object at 0x0171BDB0>', 'Bot', 4, 0, '<__main__.Nim object at 0x0171BE10>', 'Bot', 5, 0, ['<__main__.Nim object at 0x0171BE30>', 'Human', 6, 5]]]
"""
