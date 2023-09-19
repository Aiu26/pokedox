import sys
import os
from PIL import Image

# grab first and second argument
image_path= sys.argv[1]
output_path= sys.argv[2]

#check if new\ exists if not create it

if not os.path.exists(output_path):
    os.makedirs(output_path)
print(image_path, output_path)

for filename in os.listdir(image_path):
    img= Image.open(f'{image_path}{filename}')
    #splitting the extension
    clean_name= os.path.splitext(filename)[0]
    # print(clean_name)
    img.save(f'{output_path}{clean_name}.png','png')
    print('all done')
