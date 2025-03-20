Projeto
Este é um projeto console base para criação de chatbots com RAG usando LangChain e o modelo de linguagem da OpenAI. Nele você poderá salvar PDFs em uma pasta e fazer com que o chatbot responda com informações obtidades dele.

É um projeto base. Não espere muito dele 😊

1. Pré-requisitos
Certifique-se de ter o Python 3.12.5 instalado em seu sistema.
Instale o Git se ainda não tiver, para clonar repositórios e gerenciar o código (opcional).
2. Configuração do Ambiente
Clone o repositório ou extraia o projeto: Se você recebeu o projeto como um arquivo zip, extraia-o para um diretório de sua escolha.

Navegue até o diretório do projeto:

cd caminho/para/chatbot_rag_langchain
Crie e ative um ambiente virtual (opcional, mas recomendado):

python3 -m venv venv
source venv/bin/activate   # No Windows use: venv\Scripts\activate
3. Instalação das Dependências
Com o ambiente virtual ativado, instale as dependências listadas no arquivo requirements.txt:

pip install -r requirements.txt
4. Configuração do Projeto
Configure as variáveis de ambiente no arquivo .env conforme necessário. Esse arquivo deve conter variáveis que o projeto utiliza, como chaves de API, caminhos de diretórios, etc.

5. Execução do Projeto
Para executar o projeto, você pode rodar o script principal:

python src/main.py
6. Estrutura de Arquivos e Pastas
src/chatbot.py: Contém a lógica do chatbot.
src/main.py: Ponto de entrada do projeto.
src/rag_pipeline.py: Lida com a pipeline RAG (Retrieval-Augmented Generation).
config/config.py: Arquivo de configuração usado pelo projeto.
data/pdfs/: Diretório onde ficam armazenados os PDFs usados para análise ou busca.
