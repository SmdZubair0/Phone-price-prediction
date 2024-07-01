from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange
import pandas as pd

data = pd.read_csv("files/final_data.csv")
brands = [(i, i.capitalize()) for i in data['brand'].unique()]
rams = []
for i in data.ram.unique():
    if i < 1:
        rams.append((f"{int(i*1000)} MB", f"{int(i*1000)} MB"))
    else:
        rams.append((f"{int(i)} GB", f"{int(i)} GB"))
touch = [(str(i), str(i)) for i in data.touch.unique()]
quick_charge = [(str(i), str(i)) for i in data.quick_charge.unique()]
processor_brand = [(i, i) for i in data.processor_brand.unique()]
core = [(i, i) for i in data.core.unique()]
gpu = [(i, i) for i in data.gpu.unique()]
network = [(i, i) for i in data.network.unique()]
hd = [(i, i) for i in data.hd.unique()]
battery_type = [(i, i) for i in data.battery_type.unique()]
charger = [(i, i) for i in data.charger.unique()]

class Inputform(FlaskForm):
    brand = SelectField(
        "Company/Brand",
        validators=[DataRequired()],
        choices=brands
    )
    ram = SelectField(
        "RAM",
        validators=[DataRequired()],
        choices=rams
    )
    touchscreen = SelectField(
        "Touch Screen",
        validators=[DataRequired()],
        choices=touch
    )
    storage = IntegerField(
        "Storage",
        validators=[DataRequired(), NumberRange(min=0, max=512, message="Maximum storage is 512")]
    )
    expandable = IntegerField(
        "Expandable upto",
        validators=[DataRequired(), NumberRange(min=0, max=32000, message="Maximum expandable upto 32 gb")]
    )
    quick_charging = SelectField(
        "Quick Charging Available",
        validators=[DataRequired()],
        choices=quick_charge
    )
    processor = SelectField(
        "Processor Brand",
        validators=[DataRequired()],
        choices=processor_brand
    )
    core = SelectField(
        "Processor Core",
        validators=[DataRequired()],
        choices=core
    )
    gpu = SelectField(
        "GPU Available",
        validators=[DataRequired()],
        choices=gpu
    )
    network = SelectField(
        "Network Type",
        validators=[DataRequired()],
        choices=network
    )
    hd = SelectField(
        "HD available",
        validators=[DataRequired()],
        choices=hd
    )
    battery = IntegerField(
        "Battery Capacity",
        validators=[DataRequired(), NumberRange(min=400, max=7000, message="Battery between 400 to 7000")]
    )
    battery_type = SelectField(
        "Battery type",
        validators=[DataRequired()],
        choices=battery_type
    )
    charger = SelectField(
        "Charger Available",
        choices=charger
    )
    height = DecimalField(
        "Resolution Height (Pixels)",
        validators=[DataRequired(), NumberRange(min=120, max=3200, message="Value should be between 120 to 3200")]
    )
    display = DecimalField(
        "Display size (cm)",
        validators=[DataRequired(), NumberRange(min=6, max=17, message="Value should be between 6 to 17")]
    )
    rating = DecimalField(
        "Rating",
        validators=[DataRequired(), NumberRange(min=0, max=5, message="Value should be between 0 to 5")]
    )
    submit = SubmitField("Predict")
