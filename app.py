from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        action = request.form.get("action")

        if action == "square":
            n = int(request.form.get("number", 0))
            result = f"Square of {n} = {n*n}"

        elif action == "sum":
            a = int(request.form.get("a", 0))
            b = int(request.form.get("b", 0))
            result = f"Sum = {a+b}"

    return render_template("index.html", result=result)


@app.route("/health")
def health():
    return jsonify(status="UP", service="flask-docker-demo")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)