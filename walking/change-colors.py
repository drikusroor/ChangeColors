from PIL import Image
from ImageGenerator import *


image = Image.open('FeetAnim1-sheet.png')
rgb_values = convert_image_to_list(image)

light_blue = (99, 155, 255)
med_blue = (91, 110, 225)
dark_blue = (48, 96, 130)
light_brown = (143, 86, 59)
med_brown = (102, 57, 49)
dark_brown = (69, 40, 60)

palette = (dark_blue, med_blue, light_blue, dark_brown, med_brown, light_brown)

hsv_values = convert_list_to_hsv(convert_image_to_list(image))
palette_hsv = convert_palette_to_hsv(palette)

rgb_new = change_color_skin(rgb_values, palette, -100, 50, 50, 'RGB')
hsv_new = convert_list_to_rgb(change_color_skin(hsv_values, palette_hsv, -90, 0, +.1, 'HSV'))
make_image(hsv_new, 'megaman_hsv')
make_image(rgb_new, 'OtherFeet')
