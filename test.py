import json
import classes.category as category
from classes.category import Category

home_dir = "$HOME"

with open('./cat.json', 'r') as f:
    cat_dict = json.load(f)
    

keys = cat_dict.keys()
cats = []

downloads_dir = f'{home_dir}/Downloads'

for key in keys:
    cat = Category(key, downloads_dir, cat_dict[key])
    cats.append(cat)


file = open('test.sh', 'w')

print(f'Writing to test.sh')

for cat in cats:
    dir_script = cat.dir()
    mvs_script = cat.mvs(downloads_dir)

    if dir_script != None and mvs_script != None:
        file.write(dir_script)
        file.write(mvs_script)
    else:
        print(f'Error in {cat.name} category.')

file.close()

