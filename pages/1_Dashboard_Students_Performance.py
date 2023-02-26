import streamlit as st 
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import pandas as pd

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "student.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "student_data.csv")

st.title("Dashboard - Students Performance")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)

School = st.selectbox("Select School:", df['school'].unique())

fig_1 = px.histogram(df[df['school'] == School], x="sex")
st.plotly_chart(fig_1, use_container_width=True)

