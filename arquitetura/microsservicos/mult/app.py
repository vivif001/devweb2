import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mult', methods=['GET'])
def multiplicar():
    # Pega os parâmetros op1 e op2 da URL (?op1=X&op2=Y)
    op1 = float(request.args.get('op1', 0))
    op2 = float(request.args.get('op2', 0))
    
    resultado = op1 * op2
    
    # Pega o nome do contêiner definido na variável de ambiente do Docker
    container_nome = os.getenv('CONTAINER_NAME', 'desconhecido')
    
    return jsonify({
        "resultado": resultado,
        "respondido_por": container_nome
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)