from ImageGenerator import *
from random_words import *
import uuid

def change_colors(source_file_name, amount_pictures):
    image = Image.open(source_file_name)
    rgb_values = convert_image_to_list(image)
    unique_rgb_values = get_unique_values_from_image_list(rgb_values)

    # Delete the background transparent layer from this list,
    # assuming the first pixel is transparent

    # hsv_values = convert_list_to_hsv(convert_image_to_list(image))
    # unique_hsv_values = get_unique_values_from_image_list(hsv_values)
    # hsv_new = convert_list_to_rgb(change_color_skin(hsv_values, unique_hsv_values, -90, 0, +.1, 'HSV'))


    for i in range(0, amount_pictures):
        rand_r = random.randint(-100, 100)
        rand_g = random.randint(-100, 100)
        rand_b = random.randint(-100, 100)

        # rgb_new = change_color_skin(rgb_values, unique_rgb_values, -100, 50, 50, 'RGB')
        rgb_new = change_color_skin(rgb_values, unique_rgb_values, rand_r, rand_g, rand_b, 'RGB')

        print (rand_r, rand_g, rand_b)

        random_word = str(uuid.uuid1())

        make_image(rgb_new, random_word)


change_colors('FeetAnim1-sheet.png', 10)
