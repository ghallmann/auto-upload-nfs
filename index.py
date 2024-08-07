from datetime import datetime
from utils.format_txt import txt_to_csv
from utils.upload_csv import upload_file
from utils.logger import write_log
from utils.copy_file import copy_file

curr_month = datetime.now().month
curr_year = datetime.now().year
file_name = f"Notas de AT do mes {curr_month}"
file_name_txt = file_name + '.txt'
file_name_csv = file_name + '.csv'

source_path = './' + file_name_txt
output_path = './' + file_name_csv

# pasta de notas do portal no server
remote_path = f"/var/www/portal.madesa.com/storage/app/nfs/nfs_{str(curr_month).zfill(2)}_{curr_year}.csv"

copy_file(file_name_txt, 'F:\XML', './')
txt_to_csv(source_path, output_path)
upload_file(output_path, remote_path)
