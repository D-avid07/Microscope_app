from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/micro', methods=['POST'])
def funky_calc():
    mango = float(request.json['mag'])
    pineapple = float(request.json['img'])

    real = pineapple / mango

    return jsonify({"real_size": real})

if __name__ == '__main__':
    app.run(debug=True)