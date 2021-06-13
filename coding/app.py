from flask import Flask, jsonify

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def helow_world():
    return 'Please use GET /api/v1/{INT}'

@app.route('/api/v1/<int:number>', methods=['GET'] )
def find_multiples(number):
    result = ''
    if (number % 7) == 0: 
        result += 'E'
    if (number % 9) == 0: 
        result += 'G'
    if (result == ''):
        result = number
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)