# Projeto de Backup de Dados de API

Este é um projeto Python desenvolvido para fazer backup de dados de várias APIs diferentes e salvar os dados coletados em arquivos CSV, com o objetivo de utilizar esses arquivos para enviar os dados a um banco de dados para armazenamento permanente.

## Configuração do Ambiente

Antes de executar o projeto, verifique se você possui o Python instalado em sua máquina. Recomenda-se o uso do Python 3.6 ou superior.

1. Clone este repositório para o seu computador:

```bash
git clone https://github.com/seu_usuario/meu_projeto_backup.git
cd meu_projeto_backup
```

2. Crie um ambiente virtual (opcional, mas recomendado) para isolar as dependências do projeto:

```bash
python -m venv venv
```

3. Ative o ambiente virtual:

- No Windows:

```bash
venv\Scripts\activate
```

- No macOS e Linux:

```bash
source venv/bin/activate
```

4. Instale as dependências usando o `pip`:

```bash
pip install -r requirements.txt
```

---

## Configuração das APIs

Para configurar as APIs que você deseja fazer backup, adicione as informações de autenticação (por exemplo, tokens de acesso) no arquivo `api/tokens.json`. O formato do arquivo deve ser semelhante ao seguinte:

```json
{
  "api_1": {
    "token": "SEU_TOKEN_API_1"
  },
  "api_2": {
    "token": "SEU_TOKEN_API_2"
  },
  "api_3": {
    "token": "SEU_TOKEN_API_3"
  }
}
```

Certifique-se de substituir `"SEU_TOKEN_API_1"`, `"SEU_TOKEN_API_2"` e `"SEU_TOKEN_API_3"` pelos tokens de autenticação reais para cada API específica que você deseja fazer backup.

---

## Executando o Projeto

Para fazer o backup dos dados da API e salvar em arquivos CSV, execute o arquivo `main.py`:

```bash
python main.py
```

Os dados coletados de cada API serão salvos em arquivos CSV separados no diretório `output/`.

---

## Enviando os Dados para o Banco de Dados

Após coletar os dados e salvá-los em arquivos CSV, você pode utilizar os arquivos para enviar os dados a um banco de dados para armazenamento permanente. Para isso, você pode criar um script que leia os arquivos CSV e insira os dados no banco de dados. O arquivo `output/save_to_csv.py` já contém a lógica para salvar os dados em CSV, e você pode adaptá-lo para enviar os dados para o banco de dados.

---

## Estrutura de Arquivos

```plaintext
meu_projeto_backup/
│
├── api/
│   ├── __init__.py
│   ├── api_utils.py
│   └── tokens.json
│
├── output/
│   ├── __init__.py
│   └── save_to_csv.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para criar um fork e enviar um pull request com suas melhorias!

