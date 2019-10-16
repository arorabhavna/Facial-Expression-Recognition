import os
import shutil
try:
    folder = 'C:\\xampp\\htdocs\\prakalpa\\temp\\'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
                os.unlink(file_path)
except:
    print()
