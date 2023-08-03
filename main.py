# main.py

from datetime import datetime
import json
from api.api_utils import fetch_data_from_api
from output.save_to_csv import save_data_to_csv

def main():
    # Carrega os tokens a partir do arquivo tokens.json
    with open("api/tokens.json") as f:
        tokens = json.load(f)

    print(tokens)

    # Lista para armazenar todos os dados coletados
    all_data = []

    # Loop sobre as APIs e tokens para fazer backup dos dados
    for api_name, api_info in tokens.items():
        token = api_info["token"]
        print(f"Fazendo backup dos dados da API: {api_name}...")

        # Chama a função para puxar os dados da API usando o token específico
        api_data = fetch_data_from_api(api_name, token, start_date, end_date, all_data)

        # Salva os dados coletados em um arquivo CSV
        save_data_to_csv(all_data, f"./files/dados_coletados.csv", api_name)
        all_data = []

    print("Backup concluído com sucesso!")

if __name__ == "__main__":
    data_atual = datetime.now()

    # Hora inicial do dia (00:00:00)
    start_date = datetime(data_atual.year, data_atual.month, data_atual.day, 0, 0, 0)
    #start_date_str = "2023-07-29 00:00:00"
    #start_date = datetime.fromisoformat(start_date_str.replace("Z", "+00:00"))

    # Hora final do dia (23:59:59)
    end_date = datetime(data_atual.year, data_atual.month, data_atual.day, 23, 59, 59)

    print(start_date, end_date)

    main()
