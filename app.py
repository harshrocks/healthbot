from flask import Flask, render_template, request, jsonify

from try2 import get_dataset_response, get_category_and_rating
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    return render_template('base.html')


@app.post('/predict')
def predict():
    text = request.get_json().get('message')
    respo = get_dataset_response(text)
    response = respo[0]
    closest_question = respo[1]
    message = {'answer': response}
    if text.lower() in ["end", "stop", "quit", "exit", "bye"]:
        category = get_category_and_rating(response, closest_question)
        message = {'answer': f"Thank you for chatting with me!. I hope I was able to help you with your {category}."}
        return jsonify(message)
    else:
        return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True)
