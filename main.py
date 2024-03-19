import pandas as pd
from datetime import datetime
import numpy as np
import webbrowser

# Importa as bibliotecas necessárias: pandas para manipulação de dados, 
# datetime para trabalhar com datas, numpy para operações matemáticas e 
# webbrowser para interação com o navegador web.

# Lê o arquivo Excel 'Controle_de_Associados.xlsx' usando o pandas e armazena os dados no DataFrame 'df'.
df = pd.read_excel('Controle_de_Associados.xlsx')

# Filtra as linhas do DataFrame onde a coluna 'Situação' é igual a 'ATIVA' 
# e armazena o resultado em um novo DataFrame chamado 'df_ativos'.
df_ativos = df[df['Situação'] == 'ATIVA']

# Obtém a data atual do sistema, descartando a informação de tempo, 
# e armazena na variável 'data_atual'.
data_atual = datetime.now().date()

# Cria uma lista vazia chamada 'dados_filtrados' para armazenar dados 
# específicos que serão filtrados nas etapas seguintes.
dados_filtrados = []

# Itera sobre cada linha de 'df_ativos' para verificar as colunas 
# 'Prox. Pgmento' e 'Data Vencimento'. Se ambas as datas forem diferentes, 
# a linha é adicionada à lista 'dados_filtrados'.
for index, row in df_ativos.iterrows():
    prox_pgto = row['Prox. Pgmento']
    data_vencimento = row['Data Vencimento']

    # Confirma se 'Prox. Pgmento' e 'Data Vencimento' são do tipo datetime
    # antes de compará-las.
    if isinstance(prox_pgto, datetime) and isinstance(data_vencimento, datetime):
        if prox_pgto.date() != data_vencimento.date():
            dados_filtrados.append(row.to_dict())

# Converte a lista de dicionários 'dados_filtrados' em um DataFrame chamado 'df_pgmensal'.
df_pgmensal = pd.DataFrame(dados_filtrados)

# Exibe o DataFrame 'df_pgmensal' para verificar os dados filtrados.
print(df_pgmensal)

# Cria outra lista vazia chamada 'dados_vencimentos' para armazenar dados 
# sobre vencimentos que serão filtrados.
dados_vencimentos = []

# Itera sobre cada linha de 'df_ativos' para verificar a coluna 'Data Vencimento'.
# Se a data de vencimento for igual ou anterior à data atual, a linha é 
# adicionada à lista 'dados_vencimentos'.
for index, row in df_ativos.iterrows():
    data_vencimento = row['Data Vencimento']

    if isinstance(data_vencimento, datetime) and data_vencimento.date() <= data_atual:
        dados_vencimentos.append(row.to_dict())

# Converte a lista 'dados_vencimentos' em um DataFrame chamado 'df_vencimentos'.
df_vencimentos = pd.DataFrame(dados_vencimentos)

# Exibe o DataFrame 'df_vencimentos' para verificar os dados filtrados.
print(df_vencimentos)

# Define uma função 'formatar_data' que converte um objeto datetime 
# em uma string de data no formato 'dd/mm/yyyy'. Se o dado de entrada 
# não for uma data, retorna 'data não definida'.
def formatar_data(data):
    if isinstance(data, datetime):
        return data.strftime('%d/%m/%Y')
    return "data não definida"

# Define a função 'criar_link_whatsapp' para gerar um link do WhatsApp.
# A função recebe um número de telefone e uma mensagem, e retorna o link 
# de mensagem WhatsApp formatado.
def criar_link_whatsapp(numero, mensagem):
    ddi = "55"  # Código DDI do Brasil
    base_url = "https://api.whatsapp.com/send?"
    mensagem_formatada = mensagem.replace(" ", "%20")
    numero_com_ddi = f"{ddi}{numero}"
    return f"{base_url}phone={numero_com_ddi}&text={mensagem_formatada}"

# Define a função 'abrir_whatsapp' para abrir o navegador padrão com 
# o link do WhatsApp gerado. A função recebe um número de telefone e 
# uma mensagem, cria o link do WhatsApp usando 'criar_link_whatsapp' 
# e abre o link no navegador.
def abrir_whatsapp(numero, mensagem):
    link_whatsapp = criar_link_whatsapp(numero, mensagem)
    webbrowser.open(link_whatsapp)

# Inicializa uma variável 'mensagem_enviada' como False para rastrear se alguma mensagem foi enviada.
mensagem_enviada = False

# Itera sobre cada linha do DataFrame 'df_pgmensal' para enviar mensagens de lembrete de pagamento.
for index, row in df_pgmensal.iterrows():
    # Extrai a data do próximo pagamento e verifica se é um objeto datetime válido.
    prox_pgto = row['Prox. Pgmento']
    if isinstance(prox_pgto, datetime):
        # Coleta informações do associado como nome, último pagamento e número de contato.
        nome = row['Nome Completo']
        ultimo_pgto = formatar_data(row['Ultimo Pgmento'])
        numero = str(row['Contato'])

        # Inicializa uma variável 'mensagem' como uma string vazia.
        mensagem = ""

        # Monta uma mensagem personalizada se a data do próximo pagamento for igual à data atual.
        if prox_pgto.date() == data_atual:
            mensagem = (f"Olá {nome}. Estamos entrando em contato para informar que hoje, "
                        f"{formatar_data(prox_pgto)}, é seu último dia de acesso referente ao "
                        f"pagamento efetuado no dia {ultimo_pgto}. O pagamento do mês atual pode "
                        "ser efetuado presencialmente na secretaria da Base, se desejar efetuar "
                        "o pagamento via pix posso te passar os dados necessários.")

        # Monta uma mensagem personalizada se a data do próximo pagamento for anterior à data atual.
        elif prox_pgto.date() < data_atual:
            mensagem = (f"Olá {nome}. Estamos entrando em contato para informar que dia {formatar_data(prox_pgto)}, "
                        f"foi seu ultimo dia de acesso referente ao pagamento efetuado no dia {ultimo_pgto}. "
                        "O pagamento do mês atual pode ser efetuado presencialmente na secretaria da Base, se desejar efetuar o pagamento via pix posso te passar os dados necessários.")

        # Se uma mensagem válida foi criada, abre o WhatsApp e envia a mensagem, marcando 'mensagem_enviada' como True.
        if mensagem:
            abrir_whatsapp(numero, mensagem)
            mensagem_enviada = True

# Se nenhuma mensagem foi enviada (mensagem_enviada ainda é False), imprime uma mensagem informando que não há cobranças para hoje.
if not mensagem_enviada:
    print("Não temos nenhuma cobrança para realizar hoje.")

# Inicializa uma variável 'mensagem_enviada_ativos' como False para rastrear se alguma mensagem foi enviada para os associados ativos.
mensagem_enviada_ativos = False

# Itera sobre cada linha do DataFrame 'df_vencimentos' para enviar mensagens relacionadas ao vencimento do plano.
for index, row in df_vencimentos.iterrows():
    # Extrai a data de vencimento e verifica se é um objeto datetime válido.
    data_vencimento = row['Data Vencimento']
    if isinstance(data_vencimento, datetime):
        # Coleta informações do associado como nome, plano e número de contato.
        nome = row['Nome Completo']
        plano = row['Plano']
        numero = str(row['Contato'])

        # Inicializa uma variável 'mensagem' como uma string vazia.
        mensagem = ""

        # Monta uma mensagem personalizada se a data de vencimento for igual à data atual.
        if data_vencimento.date() == data_atual:
            mensagem = (f"Olá {nome}. Estamos entrando em contato para informar que hoje, "
                        f"{formatar_data(data_vencimento)}, é seu último dia de acesso referente ao "
                        f"seu plano {plano}. Caso tenha interesse em permanecer utilizando nosso espaço, "
                        "peço que se dirija à secretaria da Base para efetuar a assinatura de um novo plano. Aguardamos você!☺ ")

        # Monta uma mensagem personalizada se a data de vencimento for anterior à data atual.
        elif data_vencimento.date() < data_atual:
            mensagem = (f"Olá {nome}. Estamos entrando em contato para informar que a data de vencimento "
                        f"do seu plano {plano}, que era em {formatar_data(data_vencimento)}, já passou. "
                        "Caso tenha interesse em permanecer utilizando nosso espaço, "
                        "peço que se dirija à secretaria da Base para efetuar a assinatura de um novo plano. Aguardamos você!☺")

        # Se uma mensagem válida foi criada, abre o WhatsApp e envia a mensagem, marcando 'mensagem_enviada_ativos' como True.
        if mensagem:
            abrir_whatsapp(numero, mensagem)
            mensagem_enviada_ativos = True

# Se nenhuma mensagem foi enviada para 'df_vencimentos' (mensagem_enviada_ativos ainda é False), 
# imprime uma mensagem informando que não há vencimentos de plano para hoje.
if not mensagem_enviada_ativos:
    print("Não tivemos nenhum vencimento de plano hoje.")