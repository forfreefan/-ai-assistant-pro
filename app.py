from flask import Flask, render_template, request, jsonify
import g4f
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": user_input}],
        )
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"response": "حدث خطأ أثناء المعالجة: " + str(e)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)