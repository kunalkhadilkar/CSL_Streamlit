import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
st.image('CSL Logo.png',width=500)
st.title('Giant Eagle Survey Analysis')
df = pd.read_csv('survey_data.csv')

df['Which university do you belong to?'] = df['Which university do you belong to?'].replace(['Carnegie Mellon','Carnegie Mellon University','carnegie mellon','School of Computer Science','Carnegie mellon university','Carnegie Mellon University, School of Computer Science','School of Computer Science','Cmu','Carnegie Mellon University - CIT','Carnegie Mellon Univsersity','Carnegie Mellon Unviersity','Carnegie Mellon University','CIT','Carnegie Mellon ','Carnegie Mellon University ','CMU'],'Carnegie Mellon University')
df['Which university do you belong to?'] = df['Which university do you belong to?'].replace(['University of Pittsburgh','University of Pittsburgh '],'University of Pittsburgh')
print(df.columns)
value_counts_series = df['Which university do you belong to?'].value_counts()
uni_counts = value_counts_series.tolist()
uni_names = value_counts_series.index.tolist()
if st.checkbox('Raw Data'):
    st.write(df[0:5])


st.echo('Survey Analysis')
st.title('Who is answering our Survey? :bar_chart:')

import altair as alt
import pandas as pd

source = pd.DataFrame({
    'Universities': uni_names,
    'Number of Respondents': uni_counts
})

a = alt.Chart(source,width=500).mark_bar(size=40).encode(
    x='Universities',
    y='Number of Respondents'
)

st.altair_chart(alt.layer(a))

# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

st.title('Year wise distribution :school_satchel:')
import plotly.express as px
# This dataframe has 244 lines, but 4 distinct values for `day` 
year_series = df['Which best describes you?'].value_counts()
year_values = year_series.tolist()
year_names = year_series.index.tolist()
print(df)
fig = px.pie(values=year_values, names=year_names)
st.plotly_chart(fig)