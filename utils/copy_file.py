import os
import shutil
from utils.logger import write_log

def copy_file(file_name, source_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(source_dir):
        if filename == file_name:
            source_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(output_dir, filename)
            shutil.copy(source_file, dest_file)
            write_log(file_name, f"File {filename} copied to {output_dir} successfully")