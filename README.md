# Projeto_Aplicado_ET2
Projeto Aplicado Multiplataformas etapa 2
Mertodologias:
Projeto feito em python, com as bibliotecas:
- Pandas para o tratamento dos dados
- Fast API para consumo de API
- jwt para geração de Autenticação de Token
- OAuth2, para requisições via API das contas Google sheets
- Gspread para conexão das contas do google

# Aplicação principal:
A aplicação principal é para tratamentos de planilhas via google sheets com credencias geradas e consumidas pela a função principal, nela é preciso dar o nome dos arquivos dentro das contas credenciads e comparalos para que se tenha um novo relatorio com interesse final do usuario, noa qual é disposto em tela para visualização ou download.

# Serviços de conexão e autorização da API Google Sheets
As bibliotecas Gspread e Oath2 servem para se conectar e fazer requisições as contas Google por meio de API, a API da aplicação envia uma requisição do tipo GET para APi do google que por sua vez faz envia uma resposta para aplicação, para validar a autenticação de credenciais arquivos.

# Frontend
Frontend desenvolvido em streamlit um framework Python, que ja e nativamente responsivo, dentro da aplicação o front e responsavel pelas requisições dos backend atraves da biblioteca reponse, a imagem que aparce na pagina é do parceiro que colaborou no desenvolvimento do projeto.

# Instruções para o uso da aplicação.

1. instalar todos os frameworks que estão na pasta requirements;
2. Os codigos listados a baixo terão que ser executados em terminais diferentes;
- uvicorn auth_service.main:app --port 8000 (conectar com serviços de autenticação)
- uvicorn compare_service.main:app --port 8001 (Ativar a função de comparar)
- streamlit run frontend/app.py (Rodar o frontend)
3. Nos labels das planilhas tera que ser digitado os seguintes nomes:
label planilha sefaz: "nsefaz"
label planilha sistema: "nsistema"
Obs: Isso ocorre pois os arquivos na conta do Google já estão nomeados assim.
