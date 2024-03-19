# Sistema de Gestão de Associados

Este projeto implementa um sistema automatizado para gerenciamento de associados de uma organização. Através dele, é possível gerenciar pagamentos, enviar lembretes automatizados via WhatsApp e monitorar a situação dos associados ativos e inativos.

## Funcionalidades

- **Leitura de Dados**: Lê informações dos associados de um arquivo Excel.
- **Filtragem de Dados**: Filtra associados ativos e verifica as datas de pagamento e vencimento.
- **Envio Automatizado de Mensagens**: Envia lembretes automáticos via WhatsApp para associados com pagamentos próximos ou vencidos.
- **Relatórios**: Gera relatórios de associados com pagamentos pendentes ou planos vencidos.

## Como Usar

1. **Preparação do Ambiente**:
   - Certifique-se de ter o Python instalado em sua máquina.
   - Instale as dependências necessárias: `pandas`, `numpy`, e outras bibliotecas relevantes.

2. **Configuração do Projeto**:
   - Clone o repositório para sua máquina local.
   - Coloque o arquivo Excel com os dados dos associados na pasta raiz do projeto.

3. **Execução**:
   - Execute o script principal para iniciar o processamento dos dados.
   - O sistema lerá os dados, filtrará conforme as regras definidas e enviará mensagens automáticas quando necessário.

## Estrutura do Projeto

- `main.py`: Script principal que contém a lógica de filtragem e envio de mensagens.
- `Controle_de_Associados.xlsx`: Arquivo Excel de exemplo com a estrutura de dados necessária.
- `requirements.txt`: Arquivo com as dependências necessárias para executar o projeto.

## Contribuições

Contribuições são sempre bem-vindas! Se você tem alguma sugestão para melhorar este projeto, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é distribuído sob a licença XYZ. Veja o arquivo `LICENSE` para mais detalhes.

## Contato

Se você tiver qualquer dúvida ou sugestão, pode entrar em contato através de [kauen1999@gmail.com](mailto:kauen1999@gmail.com).

---

Desenvolvido por [Jocean Ferreira](https://github.com/kauen1999).
