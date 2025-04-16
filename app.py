from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    user_data = {
        "Username": "",
        "Password": "",
        "Email_Address": "",
        "Comments": "",
    }

    if request.method == 'POST':
        for field in user_data:
            user_data[field] = request.form.get(field, "")

    return render_template("index.html", **user_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
