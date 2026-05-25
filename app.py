import joblib
import streamlit as st

model = joblib.load('best_model.pkl')

st.title('Spam Detector')
st.caption('Check if your email/message is safe or not')
text = st.text_area('Paste the email/message here')

if st.button('Detect'):
    prediction = model.predict([text])
    if prediction == 1:
        st.error('This is spam')
    else:
        st.success('This is not spam')




