from PIL import Image
import os
def resize(im, input_width, input_height):
    resized_im = im.resize((input_width, input_height))
    return resized_im
file_list = os.listdir('resized/Damage Belt image')
print(file_list)
if not os.path.exists('resizzed'):
    os.makedirs('resizzed')
for file_name in file_list:
    file_path = os.path.join('resized/Damage Belt image', file_name)
    im = Image.open(file_path)
    image = resize(im, 299, 299)
    base_name = os.path.splitext(file_name)
    resized_file_path = f'resizzed/{base_name}.jpg'
    image.save(resized_file_path)