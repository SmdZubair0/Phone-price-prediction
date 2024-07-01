from flask import Flask, render_template, request
from form import Inputform
import pandas as pd
import pickle as pkl

model = pkl.load(open("files/pipe.pkl", "rb"))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefghijklmnopqrstuvwxyz'

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    form = Inputform()
    
    if request.method == 'POST':
        print("Form submitted!")
        print(f"Form data: {request.form}")
    
        print("Form validated!")
        # Process form data and make predictions
        df = pd.DataFrame({
            "brand" : [form.brand.data.lower()],
            "ram" : [int(form.ram.data[:-3])],
            "touch" : [form.touchscreen.data],
            "storage" : [form.storage.data],
            "expandable" : [form.expandable.data],
            "quick_charge" : [form.quick_charging.data],
            "processor_brand" : [form.processor.data],
            "core" : [form.core.data],
            "gpu" : [form.gpu.data],
            "network" : [form.network.data],
            "hd" : [form.hd.data],
            "battery" : [form.battery.data],
            "battery_type" : [form.battery_type.data],
            "charger" : [True if form.charger.data=="True" else False],
            "height" : [form.height.data],
            "display" : [1 if form.display.data >= 14 else 0],
            "rating" : [form.rating.data]
        })

        pred = model.predict(df)[0]

        return render_template("index.html", form=form, pred=int(pred))
    # if form.validate_on_submit():
    
    return render_template("index.html", form=form, pred=None)

if __name__ == "__main__":
    app.run(debug=True)
