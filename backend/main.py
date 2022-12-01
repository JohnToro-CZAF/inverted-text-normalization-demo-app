from flask import Flask, request, jsonify, render_template, url_for, abort
from flask_cors import CORS, cross_origin
from app.model import Model, get_model

app = Flask('demo-nemo')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/predict", methods=['POST'])
@cross_origin()
def predict() -> dict:
  data = request.get_json()
  if 'text' not in data or len(data['text']) == 0 or 'model' not in data:
    abort(400)
  print(data)
  model = get_model(data['model'])
  inverted_text = model.infer(data['text'])
  return jsonify({"inverted_text": inverted_text})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)