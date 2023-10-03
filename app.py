# Import necessary modules
import os
import openai  # You need to install the 'openai' module
from flask import Flask, request, render_template

# Initialize Flask app
app = Flask(__name__)

# Set your Metaphor API key
metaphor_api_key = '949decf5-9ad9-4064-a687-a98dab7a5e26'

# Initialize OpenAI API with your key
openai.api_key = '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'

# Define a function to analyze text with the Metaphor API
def analyze_metaphor(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the metaphor in the text: '{text}'",
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        user_text = request.form['user_text']
        result = analyze_metaphor(user_text)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
