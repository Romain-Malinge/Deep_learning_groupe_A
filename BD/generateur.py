"""
Nom du Script : generateur.py
Auteur :        Romain Malinge
Description :   Produit une base de donnée d'image de pokemon selon diver paramettres
"""

from PIL import Image, ImageFilter
import random
import os
import shutil
import math

DIR_NAME = 'validation'                     # Nom du dossier pour les images
NOMBRE_IMAGE = 1000                         # Nombre d'image à générer
NOMBRE_DE_CLASSE = 4                        # Nombre de pokemon max par image
NOMBRE_POKEMON_TOTAL = 649                  # Nombre de pokemon possible 
NOMBRE_BACKGROUND_TOTAL = 30                # Nombre de fond possible
L = 256                                     # Largueur background
H = 192                                     # Hauteur background
l = 96                                      # largueur image pokemon
h = 96                                      # hauteur image pokemon
DEBORDEMENT = math.floor(h/3)               # Debordement sur les bords de l'image en pixel
DISTANCE_MIN = math.floor(h/1.5)            # Distance min entre 2 pokemons
SCALE_COEF = 1.5                            # Valriation max de la taille
PERCENT_DARK = 20                           # Pourcentage de fond sombre
PERCENT_ELEM = 50                           # Pourcentage d'image avec des éléments
NOMBRE_ELEM = 5                             # Nombre d'éléments différents

any = (-2*DISTANCE_MIN, -2*DISTANCE_MIN)    # Position eloigné de tout

def generate_images():

    # Supprimer tous les dossiers existants
    path = DIR_NAME
    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        os.makedirs(path)

    # Créer les nouveaux dossiers
    for classe in range(NOMBRE_DE_CLASSE):
        dossier = os.path.join(path, str(classe + 1))
        os.makedirs(dossier)

    # Générer les images
    for i in range(NOMBRE_IMAGE):

        # Ouvrir le background
        num_background = random.randint(1, NOMBRE_BACKGROUND_TOTAL)
        image = Image.open('data\\backgrounds\\' + str(num_background) + '.png')
        if random.randint(1, 100) <= PERCENT_DARK:
            image = image.point(adjust_brightness)

        # Ajouter les pokemons
        nombre_pokemon = random.randint(1, NOMBRE_DE_CLASSE)
        mem = []
        for j in range(nombre_pokemon):

            # Ajouter un pokemon
            pokemon = new_pokemon()
            (pos, centre) = new_position(pokemon)
            while pos_not_ok(centre, mem):
                (pos, centre) = new_position(pokemon)
            mem.append(centre)
            image.paste(pokemon, pos, pokemon)

        # Ajouter un élément
        if random.randint(1, 100) <= PERCENT_ELEM:
            for _ in range(2):
                num_image = random.randint(1, NOMBRE_ELEM)
                elem = Image.open(os.path.join('data\\elements', f'{num_image}.png'))
                image.paste(elem, (0,0), elem)

        # Enregistrer l'image
        image.save(path + '\\' + str(nombre_pokemon) + '\\' + str(i) + '.png')


# Retourne une image de pokémon au hasard
def new_pokemon():
    # Tirer le numéro et le coté du pokémon
    num_pokemon = random.randint(1, NOMBRE_POKEMON_TOTAL)
    cote_pokemon = 'front' if random.randint(0, 1) else 'back'
    pokemon = Image.open(os.path.join('data\\pokemons', cote_pokemon, f'{num_pokemon}.png'))
    pokemon = pokemon.convert("RGBA")
    # Changer la taille du pokémon
    nouvelle_taille = random.randint(h, math.floor(h*SCALE_COEF))
    pokemon = pokemon.resize((nouvelle_taille, nouvelle_taille))
    return pokemon


# Retourne une nouvelle possition au hasard
def new_position(pokemon):
    largeur, hauteur = pokemon.size
    x = random.randint(-DEBORDEMENT, L-largeur + DEBORDEMENT)
    y = random.randint(-DEBORDEMENT, H-hauteur + DEBORDEMENT)
    centre = (x + largeur * 0.5, y + hauteur * 0.5)
    return ((x, y), centre)


# Retourne la distance entre 2 points a et b
def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


# Vérifie si une position est correcte
def pos_not_ok(centre, mem):
    for i in range(len(mem)):
        if distance(centre, mem[i]) < DISTANCE_MIN:
            return True
    return False

# Réduit la luminosité à 50%
def adjust_brightness(pixel_value):
    return int(pixel_value * 0.5)


generate_images()