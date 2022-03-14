from flask import Flask, render_template, request
from google.cloud import texttospeech

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('home.html', error='')


@app.route('/submit', methods=['POST'])
def submit():
    # Validate the form
    if request.method == 'POST':
        text = request.form['text']
        if text == '':
            return render_template('home.html', error='''
            Please enter text to convert.
            ''')
        elif len(text) > 5000:
            return render_template('home.html', error='''
            Text must be less than 5000 characters.
            ''')
        else:
            # Create a client
            client = texttospeech.TextToSpeechClient()

            # Set the text input to be synthesized
            synthesis_input = texttospeech.types.SynthesisInput(text=text)

            # Build the voice request, select the language code ("en-US") and
            # the ssml voice


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
