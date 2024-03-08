# Projet d'apprentissage profond - Groupe A

## <span style="color:darkorange">Sujet</span>
Entraîner un réseau de neurones à reconnaître le **nombre de Pokémon** sur une image. Les classes possibles sont **1, 2, 3 ou 4**, correspondant au nombre de Pokémon sur l'image.

## <span style="color:darkorange">Membres</span>
- Samy Afker
- Thomas Bocande
- Lilian Guihur
- Romain Malinge
- Laura Bauriaud

## <span style="color:darkorange">Base de données</span>

### <span style="color:orange">Génération</span>

>Pour les ensembles d'entrainement et de validation les images sont générées avec un script ayant les réglages suivants :
- La taille de l'image finale est de **256 x 192**.
- Il y a 30 arrière-plans possibles.
- Il y a 1, 2, 3 ou 4 Pokémon sur l'image.
- Il y a 649 Pokémon possibles, chacun avec un côté avant et arrière (Pokémons de la 5ème génération).
- La taille originale des images de Pokémon est de **96 x 96**.
- Une modification sur la taille des Pokémons est appliqué avec un coefitient aléatoirement choisie  entre 1 et 1,5.
- Les Pokémon peuvent déborder de l'image d'1/3 de leur taille.
- Les Pokémon ont une proximité maximale d'1/2 de leur taille.
- Un flou gaussien est appliqué à l'image.

Les parramètres précis sont disponible dans le fichier **generateur.py**.

>Pour l'ensemble de test, les images ont été obtenue directement dans le jeu Pokémon version Noir. Les captures d'écran on été réaliser avec le scripte **auto-screenshot.py** et on été recadrées avec le scripte **rognage.py**.

### <span style="color:orange">Constitution</span>
La base de données suit la répartition suivante :
- Ensemble d'entraînement : 4000 images générées (1000 par classe)
- Ensemble de validation : 1000 images générées
- Ensemble de test : 100 images tirées du jeu
