from flask import Flask, render_template, request, jsonify
import os
from try2 import get_dataset_response, get_category_and_rating
app = Flask(__name__)

print("in flask app")
@app.route('/', methods=['GET', 'POST'])
def chatbot():
    return render_template('base.html')


@app.post('/predict')
def predict():
    try:
        text = request.get_json().get('message')
        print(text)
        respo = get_dataset_response(text)
        print(respo)
        response = respo[0]
        print(response)
        closest_question = respo[1]
        print(closest_question)
        message = {'answer': response}
        print(message)
        if text.lower() in ["end", "stop", "quit", "exit", "bye"]:
            print('in if')
            category = get_category_and_rating(response, closest_question)

            message = {'answer': f"Thank you for chatting with me!. I hope I was able to help you with your {category}."}
            return jsonify(message)
        else:
            return jsonify(message)
    except Exception as e:
        print(e)
        return jsonify({'answer': e})



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
