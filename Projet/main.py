# coding: utf-8

from example.operation import ajoute_deux

age = input("Quel est votre age? : ")
age = int(age)
print("Vous avez %d ans" % age)

# age_plus_un = ajoute_un(age)

# print("Dans un an vous aurez %d ans" % age_plus_un)

age_plus_deux = ajoute_deux(age)

print("Dans un an vous aurez %d ans" % age_plus_deux)