from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/api/v1.0/vote", methods = ['POST'])
def vote():
  m = request.form['msg']
  #return m
  return jsonify( { 'result': 'ok' } ), 201

if __name__ == "__main__":
  app.run()
