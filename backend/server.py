
import pickle

import numpy as np
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__) # Inicializa o Flask
CORS(app) 
loaded_model = pickle.load(open("backend\ML_modelo.pkl", "rb")) # Carrega o modelo treinado

@app.route('/')
def index():
    return 'Server on!'

def convert_int64_to_int(data):
    if isinstance(data, np.int64):
        return int(data)
    if isinstance(data, list):
        return [convert_int64_to_int(x) for x in data]
    if isinstance(data, dict):
        return {k: convert_int64_to_int(v) for k, v in data.items()}
    return data
@app.route('/call_predict', methods=['POST'])

def call_predict():
    content = request.get_json()  # Obtém o conteúdo JSON da requisição
    if 'data' not in content:  # vê se 'data' está presente no conteúdo
        return jsonify({"error": "Missing 'data' field in JSON request"}), 400  # Retorna um erro 400 se 'data' não estiver presente

    data = content['data']  # Obtém os dados do campo 'data'
    data = convert_int64_to_int(data)  # Converte os valores int64 para inteiros
    to_predict = np.array(data).reshape(1, -1)  # Converte os dados em um array numpy e redimensiona para o formato esperado pelo modelo
    result = loaded_model.predict(to_predict)  #Faz a predição usando o modelo carregado

# Retorna a mensagem se o usuário é propenso ou não a realizar o teste grátis
    if result[0] == 0:
        return jsonify({'prediction': 'Nao e propenso a realizar o teste gratis'})
    else:
        return jsonify({'prediction': 'e propenso a realizar o teste gratis'})


if __name__ == '__main__':
    app.run(debug=True)
