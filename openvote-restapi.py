from flask import Flask, request, jsonify
import pika

app = Flask(__name__)

@app.route("/api/v1.0/vote", methods = ['POST'])
def vote():
  votedata = request.form['votedata']
  credentials = pika.PlainCredentials('guest', 'guest')
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
  channel = connection.channel()
  channel.queue_declare(queue='openvote')
  channel.basic_publish(exchange='', routing_key='openvote', body=votedata)
  return jsonify( { 'result': 'ok' } ), 201

if __name__ == "__main__":
  app.run()
