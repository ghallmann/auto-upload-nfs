import os
import pysftp
from dotenv import load_dotenv
from utils.logger import write_log

load_dotenv()

FTP_HOST = os.getenv('FTP_HOST')
FTP_USER = os.getenv('FTP_USER')
FTP_PASS = os.getenv('FTP_PASS')

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

def upload_file(source_path, remote_path):
    try:
        with pysftp.Connection(host=FTP_HOST, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
            sftp.put(localpath=source_path, remotepath=remote_path)
            write_log(remote_path, "File uploaded successfully")
            sftp.close()
            
        os.remove(source_path)
        write_log(source_path, 'File deleted successfully')
    except Exception as e:
        write_log(source_path, f"Error: {e}")
