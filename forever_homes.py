import streamlit as st
import pickle
import joblib
import pandas as pd

#unpickle model
model = joblib.load('./logit_model.pkl')

@st.cache()

def prediction(name, animal_type, age, sex):
    neutered_male = 0
    spayed_female = 0
    intact_male = 0
    intact_female = 0

    if name == True:
        name = 1
    else:
        name = 0

    if animal_type == "Dog":
        animal_type = 1
    else:
        animal_type = 0

    if sex == "Neutered Male":
        neutered_male = 1
    elif sex == "Spayed Female":
        spayed_female = 1
    elif sex == "Intact Male":
        intact_male = 1
    elif sex == "Intact Female":
        intact_female = 1
    pred = model.predict([[name, animal_type, age, neutered_male, spayed_female, intact_male, intact_female]])

    if pred == 0:
        outcome = "adopted"
    elif pred == 1:
        outcome = "dead"
    elif pred == 2:
        outcome = "euthanised"
    elif pred == 3:
        outcome = "lost and Found"
    else:
        outcome = "transfered"

    return outcome

html = """
<div style ="background-color:#000000;padding:14px;border-radius:14px;">
<h1 style ="color:lightgrey;text-align:center;font-size:56px;">
FOREVER HOMES
</h1>
</div>
"""

st.markdown(html, unsafe_allow_html = True)
st.title("Tell us about your animal.")

page = st.selectbox("Select a page",("Animal Assesment", "Resources"))

if page == "Resources":
    st.write("*Sarah McLachlan*")

if page == "Animal Assesment":
    st.write("Tell us about your animal:")
    name = st.checkbox('My animal has a name.')
    animal_type = st.selectbox('Is your animal a cat or a dog?', ['Cat', 'Dog'])
    age = st.slider('How old is your animal?', 0.0, 20.0, step=0.1)
    sex = st.multiselect('Sex?', ['Neutered Male', "Spayed Female", 'Intact Male', 'Intact Female'])

    if st.button("?"):
        outcome = prediction(name, animal_type, age, sex)
        st.write(f"Your animal would be {outcome}.")
