import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from google.cloud import texttospeech
from wtforms import TextAreaField
from wtforms.validators import DataRequired, length


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


class TTSForm(FlaskForm):
    text = TextAreaField('Text to synthesize', validators=[
                         DataRequired(), length(max=5000)])


@app.route('/')
def form():
    form = TTSForm()
    return render_template('form.html',
                           form=form
                           )


@app.route('/submit', methods=['POST'])
def submit():
    # Validate the form
    if request.method == 'POST':
        text = request.form['text']
        if text == '':
            return render_template('form.html', error='''
            Please enter text to convert.
            ''')
        elif len(text) > 5000:
            return render_template('form.html', error='''
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
