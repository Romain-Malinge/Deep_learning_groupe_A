"""
Nom du Script : rognage.py
Auteur :        Romain Malinge
Description :   Rogne un l'ensemble des images png d'un dossier
"""

from PIL import Image
import os


def crop_images(input_folder, output_folder, target_width, target_height, top_left_x, top_left_y):

    # Vérifier si le dossier de sortie existe, sinon le créer
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]
    for image_file in image_files:

        # Ouvrir l'image
        input_path = os.path.join(input_folder, image_file)
        image = Image.open(input_path)

        # Effectuer le rognage
        cropped_image = image.crop((top_left_x, top_left_y, top_left_x + target_width, top_left_y + target_height))

        # Enregistrer l'image
        output_path = os.path.join(output_folder, image_file)
        cropped_image.save(output_path)

        print(f"Image rognée et enregistrée : {output_path}")


input_folder = "./"
output_folder = "./"
target_width = 640
target_height = 480
top_left_x = 694
top_left_y = 94

crop_images(input_folder, output_folder, target_width, target_height, top_left_x, top_left_y)
