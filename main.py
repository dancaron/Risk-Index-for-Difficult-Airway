
import streamlit as st


st.title("El-Ganzouri Risk Index (EGRI) for Difficult Airway")
st.write("This tool helps to predict difficult airway or intubation.")

st.header("Please answer the following questions:")

age = st.slider("Age over 40 years (0 if No, 5 if Yes)", 0, 5, 0)
weight = st.slider("Weight over 110 kg (0 if No, 5 if Yes)", 0, 5, 0)
history_of_difficult_intubation = st.slider("History of difficult intubation (0 if No, 10 if Yes)", 0, 10, 0)
history_of_snoring = st.slider("History of snoring (0 if No, 3 if Yes)", 0, 3, 0)
beard = st.slider("Beard (0 if No, 1 if Yes)", 0, 1, 0)
lack_of_teeth = st.slider("Lack of teeth (0 if No, 1 if Yes)", 0, 1, 0)
limited_jaw_protrusion = st.slider("Limited jaw protrusion (0 if No, 5 if Yes)", 0, 5, 0)
maa_grade_3_or_4 = st.slider("Mallampati airway assessment (MAA) grade 3 or 4 (0 if No, 5 if Yes)", 0, 5, 0)
limited_neck_movement = st.slider("Limited neck movement (0 if No, 5 if Yes)", 0, 5, 0)

total_score = age + weight + history_of_difficult_intubation + history_of_snoring + beard + lack_of_teeth + limited_jaw_protrusion + maa_grade_3_or_4 + limited_neck_movement

st.header("Your EGRI score is:")
st.write(total_score)

st.write("This is a rough assessment and does not replace professional medical advice. Please consult with your healthcare provider for a thorough assessment.")
