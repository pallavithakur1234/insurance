import pickle
import json
import config1
import numpy as np
class MedicalInsurance():
    def __init__(self,age,gender,bmi,children,smoker,region):
        self.age=age
        self.gender=gender
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region=region
    def __load_model(self):
        with open(r"G:\Python\INSURANCE\artifact\model.pkl","rb") as f:
            self.model=pickle.load(f)
            print("model is:",self.model)
        with open(r"G:\Python\INSURANCE\artifact\pro_data.json","r") as f:
            self.j_file=json.load(f)
            print("json file is:",self.j_file)  
    def get_prediction(self):
        self.__load_model()
        test_array=np.zeros(self.model.n_features_in_)
        test_array[0] = self.age
        test_array[1] = self.j_file['gender'][self.gender]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.j_file['smoker'][self.smoker]
        region = 'region_' + self.region
        index = self.j_file['cols'].index(region)

        test_array[index] = 1

        print("Test Array is :",test_array)
        predicted_charges = np.around(self.model.predict([test_array])[0],3)
        print("Predicted Charges :", predicted_charges)
        return predicted_charges


           