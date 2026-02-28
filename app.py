from flask import Flask, render_template, request

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def home():
    flights = []
    if request.method == "POST":
        source = request.form["source"]
        destination = request.form["destination"]

        # Dummy flight data
        flights = [
            {"airline": "Indigo", "flight": "6E101"},
            {"airline": "Air India", "flight": "AI202"},
        ]

    return render_template("index.html", flights=flights)

if _name_ == "_main_":
    app.run(debug=True)
