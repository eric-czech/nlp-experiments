import tensorflow as tf
import tensorflow_hub as hub
import json


#module_url = "https://tfhub.dev/google/universal-sentence-encoder/2"
module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/3"

print('Loading graph module ...')
g = tf.Graph()
with g.as_default():
    embed = hub.Module(module_url)
    tinput = tf.placeholder(dtype=tf.string, shape=[None])
    toutput = embed(tinput)
    init_op = tf.group([tf.global_variables_initializer(), tf.tables_initializer()])
g.finalize()
print('Graph module loaded')

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/use_embed', methods=['GET', 'POST'])
def use_embed():
    content = request.json
    with tf.Session(graph=g) as session:
        session.run(init_op)
        message_embeddings = session.run(toutput, feed_dict={tinput: content['sentences']})
        return jsonify(message_embeddings.tolist())
