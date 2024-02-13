from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    selected_type = data['selected_type']
    x_value = float(data['x_value'])

    # Define your data
    values = {
        'Audio': 1869,
        'Audiovisual': 20629,
        'In_Person': 159351,
        'None1': 141149
    }

    # Calculate percentage
    result = round((x_value/values[selected_type])*100, 1)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
