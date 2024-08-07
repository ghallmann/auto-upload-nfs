import os
import csv
from utils.logger import write_log

def remove_lines(file_path):
    try:
        with open(file_path, 'r', encoding='latin1') as file:
            lines = file.readlines()
        
        modified_lines = lines[6:-1]
        
        with open(file_path, 'w', encoding='latin1') as file:
            file.writelines(modified_lines)
        
        write_log(file_path, 'File formatted successfully')
    except Exception as e:
        write_log(file_path, f'Error: {e}')

def format_file(file_path):
    formatted_data = []
    
    try:
        with open(file_path, 'r', encoding='latin1') as file:
            for line in file:
                order_code = line[0:12].strip()
                nf = line[13:21].strip()
                serie = line[22:27].strip()
                stablishment = line[28:33].strip()
                cancel = line[34:39].strip()
                emission = line[40:50].strip()
                provider = line[51:65].strip()
                marktplace = line[66:79].strip()
                client = line[80:94].strip()
                shipping_company = line[95:107].strip()
                shipping_company_redispatch = line[108:123].strip()
                items = line[127:].strip()
                
                formatted_data.append([
                    order_code, nf, serie, stablishment, cancel, emission,
                    provider, marktplace, client, shipping_company,
                    shipping_company_redispatch, items
                ])
        write_log(file_path, 'File formatted successfully')
        return formatted_data
    except Exception as e:
        write_log(file_path, f'Error: {e}')

def write_csv(data, output_path):
    headers = [
        'Código Pedido', 
        'Nota Fiscal', 
        'Série', 
        'Estabelecimento', 
        'Cancelado?', 
        'Data emissão', 
        'Fornecedor/Cliente', 
        'Marktplace', 
        'CPF/CNPJ', 
        'Transportadora', 
        'Transportadora Redespacho', 
        'Itens'
    ]
    
    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(data)
        
        write_log(output_path, 'CSV file created successfully')
    except Exception as e:
        write_log(output_path, f'Error: {e}')

def txt_to_csv(file_path, output_path):
    remove_lines(file_path)
    data = format_file(file_path)
    if data:
        write_csv(data, output_path)
        try:
            os.remove(file_path)
            write_log(file_path, 'File deleted successfully')
        except Exception as e:
            write_log(file_path, f'Error deleting file: {e}')

