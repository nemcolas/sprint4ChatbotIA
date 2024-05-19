# Sprint 4 ChatBotIA

## Descrição

Esta aplicação é um sistema de predição feito utilizando Machine Learning que determina se um usuário é propenso a realizar um teste grátis.

O arquivo `main.ipynb` é um Jupyter Notebook que contém a análise exploratória dos dados e o treinamento do modelo de machine learning. Ele inclui visualizações de dados, pré-processamento de dados, seleção de modelo, treinamento de modelo e avaliação de modelo.

O arquivo `server.py` é o servidor principal que recebe as solicitações HTTP, faz as previsões usando o modelo treinado e retorna as respostas.

## Instalação

Para instalar e executar a aplicação, siga os seguintes passos:

1. Clone o repositório: `git clone https://github.com/nemcolas/sprint4ChatbotIA`
2. Entre no diretório do projeto: `cd sprint4ChatbotIA`
3. Instale as dependências do projeto: `pip install -r requirements.txt`
4. Execute a aplicação: `python server.py`

## Uso

Para usar a aplicação, faça uma solicitação POST para a rota `/call_predict`. Você pode fazer isso utilizando uma ferramenta como o Postman ou sua biblioteca de solicitação HTTP preferida. No corpo da solicitação, inclua o JSON com os dados de entrada esperado.

exemplo de solicitação:

"data": [1,2,1,2,1]
![alt text](image.png)

---------

"data:[3,3,3,5,5]
![alt text](image-1.png)


## Avisos importantes

Estamos atualmente na fase de implementação desta aplicação como parte da Sprint 4 da materia de Web. Você pode conferir o progresso do front-end aqui: [https://salesforce-web.vercel.app/analiseia]

A aplicação funciona corretamente quando acessada via Postman, porem, a integração com o front-end resultou em alguns bugs que até o dia 19/05 não conseguimos resolver, por favor tenha piedade da gente e n desconte pontinhos fessor

## Esse projeto foi desenvolvido por:

Ander Kamada RM: 553449
Nicolas Martins RM: 553478
Yago Lucas Gonçalves RM: 553013






