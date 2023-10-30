from flask import Flask ,render_template,request
import joblib

app = Flask(__name__)
@app.route('/')
def base():
    return render_template('home.html')

@app.route('/predict',methods=["post"])
def predict():
    FA = request.form.get("FA")
    VA= request.form.get("VA")
    CA = request.form.get("CA")
    RS = request.form.get("RS")
    Chlorides = request.form.get("Chlorides")
    FSD= request.form.get("FSD")
    TSD = request.form.get("TSD")
    Density = request.form.get("Density")
    Ph= request.form.get("Ph")
    Sulphates = request.form.get("sulphates")
    Alcohol = request.form.get("Alcohol")

    model = joblib.load('WineQulaity.pkl')

    print(FA)
    print(VA)
    print(CA)
    print(RS)
    print(Chlorides)
    print(FSD)
    print(TSD)
    print(Density)
    print(Ph)
    print(Sulphates)
    print(Alcohol)
  
    output = model.predict([[FA,VA,CA,RS,Chlorides,FSD,TSD,Density,Ph,Sulphates,Alcohol]])

    if output == 0:
        data = "low standard wine"
    else :
        data = "high standard wine"
    return render_template('predict.html',data = data)

if __name__ =="__main__":
    app.run(debug=True)

















