# output/save_to_csv.py

import csv

def save_data_to_csv(data_list, file_path, api_name):
    # Lista de campos que serão escritos no arquivo CSV
    fieldnames = ['id', 'time', 'value', 'variable', 'device']

    # Abrir o arquivo CSV em modo de escrita
    with open(file_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Escrever os cabeçalhos do arquivo CSV
        writer.writeheader()

        # Escrever cada dicionário na lista como uma linha no arquivo CSV
        for item in data_list:
            writer.writerow({
                'id': item.get('id', ''),  # Use .get() para lidar com campos ausentes
                'time': item.get('time', ''),
                'value': item.get('value', ''),
                'variable': item.get('variable', ''),
                'device': f'{api_name}'
            })
