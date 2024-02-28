from PIL import Image, ImageFilter
import random
import os
import shutil

NOMBRE_IMAGE = 1000                         # Nombre d'image à générer
NOMBRE_DE_CLASSE = 4                        # Le nombre de pokemon max par image - 1
NOMBRE_POKEMON_TOTAL = 649                  # Nombre de pokemon possible
NOMBRE_BACKGROUND_TOTAL = 30                # Nombre de fond possible
L = 240                                     # Largueur background
H = 112                                     # Hauteur background
l = 96                                      # largueur image pokemon
h = 96                                      # hauteur image pokemon
DEBORDEMENT = 40                            # Debordement sur les bords de l'image en pixel
DISTANCE_MIN = 20                           # Distance min entre 2 pokemons
SCALE_MARGE = 15                            # Valriation max de la taille
FLOU = 0.2                                  # La valeur du flou appaorté à l'image
any = (-2*DISTANCE_MIN, -2*DISTANCE_MIN)    # Position eloigné de tout 


def generate_images():

    # Supprimer tous les dossiers existants
    base_de_donnee = 'base_de_donnee'
    if os.path.exists(base_de_donnee):
        shutil.rmtree(base_de_donnee)
    else:
        os.makedirs(base_de_donnee)

    # Créer les nouveaux dossiers
    for classe in range(NOMBRE_DE_CLASSE):
        dossier = os.path.join(base_de_donnee, str(classe))
        os.makedirs(dossier)

    # Générer les images
    for i in range(NOMBRE_IMAGE):

        # Ouvrir le background
        num_background = random.randint(1, NOMBRE_BACKGROUND_TOTAL)
        background = Image.open('backgrounds\\' + str(num_background) + '.png')

        # Ajouter les pokemons
        nombre_pokemon = random.randint(0, NOMBRE_DE_CLASSE - 1)
        mem = [any, any, any, any]

        for j in range(nombre_pokemon):

            # Ouvrir le pokemon
            pokemon = new_pokemon()
            # Superposer le pokemon sur le background
            pos = new_position()
            while distance(pos, mem[0]) < DISTANCE_MIN or distance(pos, mem[1]) < DISTANCE_MIN:
                pos = new_position()
            mem[j] = pos
            background.paste(pokemon, pos, pokemon)

        # Enregistrer l'image avec du flou
        background = background.filter(ImageFilter.GaussianBlur(FLOU)) 
        background.save('base_de_donnee\\' + str(nombre_pokemon) + '\\' + str(i) + '.png')


# Retourne une image de pokémon au hasard
def new_pokemon():
    # Tirer le numéro et le coté du pokémon
    num_pokemon = random.randint(1, NOMBRE_POKEMON_TOTAL)
    cote_pokemon = 'front' if random.randint(0, 1) else 'back'
    pokemon = Image.open(os.path.join('pokemons', cote_pokemon, f'{num_pokemon}.png'))
    pokemon = pokemon.convert("RGBA")
    # Changer la taille du pokémon
    nouvelle_taille = random.randint(h - SCALE_MARGE, h + SCALE_MARGE)
    pokemon = pokemon.resize((nouvelle_taille, nouvelle_taille))
    return pokemon


# Retourne une nouvelle possition au hasard
def new_position():
    x = random.randint(-DEBORDEMENT, L-l + DEBORDEMENT)
    y = random.randint(-DEBORDEMENT, H-h + DEBORDEMENT)
    return (x, y)


# Retourne la distance entre 2 points a et b
def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


generate_images()