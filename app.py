import pandas as pd
import joblib
from formup import SignupForm, LoginForm
from flask import (
    Flask,
    url_for,
    render_template,
    flash,
    redirect
)
from forms import InputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

model = joblib.load("model.joblib")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            Airline=[form.airline.data],
          
            Source=[form.source.data],
            Destination=[form.destination.data],
           
            Duration_mins=[form.duration.data],
            Total_Stops_upd=[form.total_stops.data],
            Additional_Info_upd=[form.additional_info.data]
        ))
        prediction = model.predict(x_new)[0]
        message = f"The predicted price is {prediction:,.0f} INR!"
    else:
        message = "Please provide valid input details!"
    return render_template("predict.html", title="Predict", form=form, output=message)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    formI = SignupForm()
    if formI.validate_on_submit():
        flash(f"Successfully Registered {formI.username.data}!")
        return redirect(url_for("home"))
    return render_template("signup.html", title="Sign Up", form=formI)


@app.route("/login", methods=["GET", "POST"])
def login():
    formI = LoginForm()
    if formI.validate_on_submit():
        flash("Logged in Successfully!")
        return redirect(url_for("home"))
    return render_template("login.html", title="Login", form=formI)


if __name__ == "__main__":
    app.run(debug=True)