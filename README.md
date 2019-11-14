#### Castel Aurélien, Léa Dacosta, Kevin Seri, Nicolas Guiblin

# Cahier des charges PT
## Délais (Octobre 2019 à Mars 2020)

## Sommaire

### I) Spécifications fonctionnelles
### 
### II) Spécifications techniques
### 
### III) Diagrammes



## I) Spécifications fonctionnelles

Le but de ce projet est de créer une API d’Intelligence Artificielle permettant
de jouer à n’importe quel jeu à deux joueurs en tour par tour et à information
complète tels que le jeu de Nim, le Korridor, etc.

Afin de déterminer les fonctionnalités que nous devrons au minimum
produire, nous utilisons la méthode MoSCoW :

```
 M : Must (fonctionnalités vitales)
 S : Should (fonctionnalités importantes)
 C : Could (fonctionnalités optionnelles)
 W : Would (fonctionnalités pour parfaire le projet)
```

#### Diagramme de MoSCoW
![alt text](https://dwarves.iut-fbleau.fr/git/castel/PT-API-IA-python/raw/master/images/MoSCoW.png)


## II) Spécifications techniques

```
Objectif
```
Notre projet sera codé en Python. En effet, ce langage est le plus utilisé
dans le domaine de l’intelligence artificielle et possède de nombreuses
librairies. De plus, c’est l’occasion de se former sur un langage qui nous est
inconnu.

Nous utiliserons dans un premier temps l’algorithme minimax, qui est
le plus adapté au type de jeux utilisés dans le cadre de ce projet. De ce fait,
l’IA prendra la meilleure décision parmi celles qui lui sont offertes, au vu de
l’état actuel du jeu.
Contraintes

L’API devra être la plus générique possible afin d’en faciliter son
intégration dans le développement du programmeur. Elle devra également
être mise à jour sans corruption des fonctionnalités des différents jeux.
Ainsi le projet utilisera le data-driven developpement : le projet est
piloté par les données qui lui sont fournies et l’application marchera peu
importe ces données.

#### Diagramme de Gantt
![alt text](https://dwarves.iut-fbleau.fr/git/castel/PT-API-IA-python/raw/master/images/Gantt.png)

## III) Diagrammes

#### Diagramme de cas d’usage
![alt text](https://dwarves.iut-fbleau.fr/git/castel/PT-API-IA-python/raw/master/images/Cas%20d%27usage.png)



