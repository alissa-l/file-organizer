class Category:


    def __init__(self, name, download_dir, file_types):
        self.name = name
        self.path = f'{download_dir}/{name}'
        self.file_types = file_types

    def __str__(self):
        return f'Category: {self.name}, Path: {self.path}'
    
    def dir(self):
        return self.output_base(self.path)
    
    def mvs(self, download_dir):
        script_entry = f'\necho "Moving {self.name} files to {self.path}"\n'
        for file_type in self.file_types:
            script_entry += f'mv {download_dir}/*.{file_type} {self.path}/ 2>/dev/null\n'

        script_entry += '\n'
        return script_entry

    def output_base(self, directory):
        return f'# Moving {self.name} files\nif [ ! -d {directory} ];\n  then mkdir {directory} \nfi\n'
