# Projet d'apprentissage profond - Groupe A

## <span style="color:darkorange">Sujet</span>
Entraîner un réseau de neurones à reconnaître le **nombre de Pokémon** sur une image. Les classes possibles sont 0, 1, 2 et 3, correspondant au nombre de Pokémon sur l'image.

## <span style="color:darkorange">Membres</span>
- Samy Afker
- Thomas Bocande
- Lilian Guihur
- Romain Malinge
- Laura Bauriaud

## <span style="color:darkorange">Base de données</span>

### <span style="color:orange">Génération</span>

La base de données est constituée d'images générées avec un script ayant les réglages suivants :
- La taille de l'image finale est de **256 x 192**.
- Il y a 30 arrière-plans possibles.
- Il y a 0, 1, 2 et 3 Pokémon sur l'image.
- Il y a 649 Pokémon possibles, chacun avec un côté avant et arrière (Pokémons de la 5ème génération).
- La taille originale des images de Pokémon est de **96 x 96**.
- Une modification de taille est appliquée aux Pokémon.
- Les Pokémon peuvent déborder de l'image.
- Les Pokémon ont une proximité maximale.
- Un flou gaussien est appliqué à l'image.

Les parramètres précis sont disponible dans le fichier **generateur.py**.

### <span style="color:orange">Constitution</span>
La base de données suit la répartition suivante :
- Ensemble d'entraînement : 4000 images générées
- Ensemble de validation : 1000 images générées
- Ensemble de test : ??? images tirées du jeu
