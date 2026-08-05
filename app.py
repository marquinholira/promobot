from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def inicio():

    with open(
        "dados/cupons.json",
        "r",
        encoding="utf-8"
    ) as f:

        cupons = json.load(f)

    return render_template(
        "index.html",
        cupons=cupons
    )

if __name__ == "__main__":
    app.run(debug=True)
