import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        speech = request.form["speech"]
        response = openai.Completion.create(
            model="text-curie-001",
            prompt=generate_prompt(speech),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


@app.route('/form-example')
def form_example():
	return 'Form Data Example'


def generate_prompt(speech):
    return f"""Tell whether the speaker is native English or not. Speaker: {speech.capitalize()} Answer:"""
