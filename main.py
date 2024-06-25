import json
import classes.category as category
from classes.category import Category
from os import listdir
from os.path import isfile, join
import subprocess

home_dir = "$HOME"

config_dir = 'config'
config_files = [f for f in listdir(config_dir) if isfile(join(config_dir, f)) and f.endswith('.json')]

cats = {}

for config_file in config_files:

    print(f'Found config file: {config_file}\n')
    cats[config_file] = []

    with open(f'{config_dir}/{config_file}', 'r') as f:
        cat_dict = json.load(f)
        

    keys = cat_dict.keys()

    dir = home_dir + "/" + config_file.replace(".json", "")

    for key in keys:
        cat = Category(key, dir, cat_dict[key])
        cats[config_file].append(cat)


file = open('organize.sh', 'w')

print(f'Writing to organize.sh')

for key in cats.keys():
    cats_list = cats[key]
    for cat in cats_list:
        dir_script = cat.dir()
        mvs_script = cat.mvs(dir)

        if dir_script != None and mvs_script != None:
            file.write(dir_script)
            file.write(mvs_script)
        else:
            print(f'Error in {cat.name} category.')

file.close()

subprocess.run(['chmod', 'u+x', 'organize.sh'])