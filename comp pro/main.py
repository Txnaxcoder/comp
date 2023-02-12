from flask import Flask, render_template,request


import smtplib


app = Flask(__name__)



@app.route('/')
def hero():
    return render_template('hero.html')

@app.route('/images/<path:path>')
def send_image(path):
    return app.send_static_file('images/' + path)


@app.route("/send_email", methods=["POST"])
def send_email():
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("tanmaychandra10@gmail.com", "prgvppdtqgjrupxh")

    msg = f"Subject: {subject}\n\n{message}"

    server.sendmail(email,"tanmaychandra10@gmail.com", msg)

    server.quit()

    return "Email sent successfully"


if __name__ == '__main__':
    app.run()
