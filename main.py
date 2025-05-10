from flask import Flask, jsonify, request

app = Flask(__name__)

habitos = []
prox_id = 1
@app.route('/')
def home():
    return jsonify({'mensagem': 'API de hábitos'})

@app.route('/habitos', methods =['POST'])
def criar_habito():
    global prox_id
    info = request.get_json()

    if not info or "nome" not in info:
        return jsonify({'erro': 'Informe o habito que você deseja adicionar: '}), 400

    habito = {
        'id': prox_id,
        'nome': info['nome'],
        'freq': info.get('freq','diario')
    }
    habitos.append(habito)
    prox_id += 1
    print(f"[POST] habito criado: {habito}")

    return jsonify({'mensagem': 'Hábito criado com sucesso!', 'habito': habito}), 201

@app.route('/habitos', methods=['GET'])
def listar_habitos():
    print("[GET] Listando hábitos")
    return jsonify(habitos), 200

@app.route('/habitos/<int:id>', methods=['DELETE'])
def deletar_habito(id):
    global habitos
    if any(h['id'] == id for h in habitos):
        habitos = [h for h in habitos if h['id'] != id]
        print(f"[DELETE] Hábito removido, com o ID: {id}")
        return jsonify({'mensagem': f'Hábito {id} removido com sucesso.'}), 200

    print(f"[DELETE] Hábito com ID {id} não encontrado.")
    return jsonify({'erro': f'Hábito com ID {id} não encontrado.'}), 404
#O delete foi o mais dificil de fazer
if __name__ == '__main__':
    app.run(debug=True)