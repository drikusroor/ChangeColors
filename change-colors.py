from ImageGenerator import *
import uuid

def change_colors(source_file_name, amount_pictures, variety):
    image = Image.open(source_file_name)
    rgb_values = convert_image_to_list(image)
    unique_rgb_values = get_unique_values_from_image_list(rgb_values)

    # Delete the background transparent layer from this list,
    # assuming the first pixel is transparent

    for i in range(0, amount_pictures):
        rand_r = random.randint(-variety, variety)
        rand_g = random.randint(-variety, variety)
        rand_b = random.randint(-variety, variety)
        rgb_new = change_color_skin(rgb_values, unique_rgb_values, rand_r, rand_g, rand_b, 'RGB')
        random_word = str(uuid.uuid1())
        make_image(rgb_new, random_word)

# To use, simply use the following command
# First param is the filename as string
# Second param is the amount of random images that will be created
# Third param is the amount of variety in color
# that can occur in each of the channels
# change_colors('FeetAnim1-sheet.png', 10, 200)
