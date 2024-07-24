import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired


# getting the data
train = pd.read_csv("selected_features_train_data.csv")
# val = pd.read_csv("data/val.csv")
X_data = train.drop(columns="Price")

class InputForm(FlaskForm):
    airline = SelectField(
        label="Airline",
        choices=X_data.Airline.unique().tolist(),
        validators=[DataRequired()]
    )
  
    source = SelectField(
        label="Source",
        choices=X_data.Source.unique().tolist(),
        validators=[DataRequired()]
    )
    destination = SelectField(
        label="Destination",
        choices=X_data.Destination.unique().tolist(),
        validators=[DataRequired()]
    )
   
    duration = IntegerField(
        label="Duration",
        validators=[DataRequired()]
    )
    total_stops = IntegerField(
        label="Total Stops",
        validators=[DataRequired()]
    )
    additional_info = SelectField(
        label="Additional Info -- '1' for Food_Included  '0' for Food_Excluded",
        choices=X_data.Additional_Info_upd.unique().tolist(),
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")