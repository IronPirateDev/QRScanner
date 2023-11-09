from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/qr_data')
def qr_data():
  return 'QR Data TBD'


@app.route('/details')
def details():
  return 'The Data def goes here'


@app.route('/qr')
def qrscan():
  return render_template('qr.html')


@app.route('/scan_qr', methods=['POST'])
def scan_qr():
  code = request.form['code']
  return code


@app.route('/process_option', methods=['POST'])
def process_option():
  data = request.get_json()
  option = data['option']
  return jsonify({'message': 'Option processed successfully'})


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
