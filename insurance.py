from flask import Flask,render_template,request,jsonify
import config1
from util import MedicalInsurance
import traceback
app=Flask(__name__,template_folder='templates')
@app.route("/")
def home():
    return render_template('index.html')
    # return "prediction class"
@app.route("/predict",methods = ['GET','POST'])   
def predict():
    try:
        if request.method=="GET":
            data=request.args.get
            print("data is:",data) 
            age = eval(data('age'))
            gender = data('gender')
            bmi= eval(data('bmi'))
            children = eval(data('children'))
            smoker = data('smoker')
            region = data('region')
            medical_ins = MedicalInsurance(age, gender, bmi, children, smoker, region)
            charges = medical_ins.get_prediction()
            return  render_template('index.html',prediction = charges)
            # return jsonify({"charges"})
        else:
            data = request.form.get

            print("User Data is ::::",data)
            age = eval(data('age'))
            gender = data('gender')
            bmi = eval(data('bmi'))
            children = eval(data('children'))
            smoker = data('smoker')
            region = data('region')
            medical_ins = MedicalInsurance(age, gender, bmi, children, smoker, region)
            charges = medical_ins.get_prediction()

            # return  jsonify({"Result" : f"Medical Insurence Charges will be : {charges}"})
            return  render_template('index.html',prediction = charges)
            
    except:
        print(traceback.print_exc())
        return  jsonify({"Message" : "Unsuccessful"})
        # return  jsonify({"Result" : f"Medical Insurence Charges will be : {charges}"})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5004,debug=True) 
