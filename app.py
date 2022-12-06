import streamlit as st
import pandas as pd
import joblib

Model = joblib.load("loanFile.pkl")
Inputs = joblib.load("InputsFile.pkl")

def predict(GenderEnc, MarriedEnc, DependentsEnc, EducationEnc,
       Self_EmployedEnc, ApplicantIncome, CoapplicantIncome,
       LoanAmount, Loan_Amount_Term, Credit_History,Property_AreaEnc):
    test_data = pd.DataFrame(columns = Inputs)
    test_data.at[0,"GenderEnc"] = GenderEnc
    test_data.at[0,"MarriedEnc"] = MarriedEnc
    test_data.at[0,"DependentsEnc"] = DependentsEnc
    test_data.at[0,"EducationEnc"] = EducationEnc
    test_data.at[0,"Self_EmployedEnc"] = Self_EmployedEnc
    test_data.at[0,"ApplicantIncome"] = ApplicantIncome
    test_data.at[0,"CoapplicantIncome"] = CoapplicantIncome
    test_data.at[0,"LoanAmount"] = LoanAmount
    test_data.at[0,"Loan_Amount_Term"] = Loan_Amount_Term
    test_data.at[0,"Credit_History"] = Credit_History
    test_data.at[0,"Property_AreaEnc"] = Property_AreaEnc
    result = Model.predict(test_data)[0]
    
    
    
    
def main():
    st.title("Loan Prediction App")
    GenderEnc = st.selectbox("Gender" , ['male', 'female'])
    MarriedEnc= st.selectbox("Married" , ['yes', 'no'])
    DependentsEnc = st.selectbox("Dependents" , ['0', '1','2','3','4'])
    EducationEnc = st.selectbox("Education" , ['yse', 'no'])
    Self_EmployedEnc = st.selectbox("Self Empployed" , ['yes', 'no'])
    ApplicantIncome = st.slider("Applicant Income" , min_value=0, max_value=5849, value=0, step=1)
    CoapplicantIncome = st.slider("Coapplicant Income" , min_value=0, max_value=3000, value=0, step=1)
    LoanAmount = st.selectbox("Loan Amount" , min_value=0, max_value=147, value=0 )
    Loan_Amount_Term = st.selectbox("Loan Amount Term" , ['0', '180','360'])
    Credit_History = st.selectbox("Credit History " , ['yes', 'no'])
    Property_AreaEnc = st.selectbox("Dependents" , ['urban', 'rural','semiurban'])
    
    if st.button("Predict"):
        result = predict(GenderEnc, MarriedEnc, DependentsEnc, EducationEnc,
       Self_EmployedEnc, ApplicantIncome, CoapplicantIncome,
       LoanAmount, Loan_Amount_Term, Credit_History,Property_AreaEnc)
        label = ["Loan Not Given","Loan Given"]
        st.text("The output is {}".format(label[result]))
if __name__ == '__main__':
    main()