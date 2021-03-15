import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
st.image('CSL Logo.png',width=500)
st.title('Giant Eagle Survey Analysis')
df = pd.read_csv('survey_data.csv')

df['Which university do you belong to?'] = df['Which university do you belong to?'].replace(['Carnegie Mellon','Carnegie Mellon University','carnegie mellon','School of Computer Science','Carnegie mellon university','Carnegie Mellon University, School of Computer Science','School of Computer Science','Cmu','Carnegie Mellon University - CIT','Carnegie Mellon Univsersity','Carnegie Mellon Unviersity','Carnegie Mellon University','CIT','Carnegie Mellon ','Carnegie Mellon University ','CMU'],'Carnegie Mellon University')
df['Which university do you belong to?'] = df['Which university do you belong to?'].replace(['University of Pittsburgh','University of Pittsburgh '],'University of Pittsburgh')
df['How often do you eat out? (Including dine-in, take outs, and deliveries)'] = df['How often do you eat out? (Including dine-in, take outs, and deliveries)'].replace(["Last semester was 5x a week (which I hated because I prefer cooking for health, but I didn't have time). Now 1-2x a month"],'1-3 times a month')
print(df.columns)
value_counts_series = df['Which university do you belong to?'].value_counts()
uni_counts = value_counts_series.tolist()
uni_names = value_counts_series.index.tolist()
if st.checkbox('Raw Data'):
    st.write(df[0:5])


st.echo('Survey Analysis')

expander_1 = st.beta_expander("Who is answering our survey?")
with expander_1:
	st.title('Who is answering our Survey? :bar_chart:')

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
expander_2 = st.beta_expander("Year wise distribution")
with expander_2:
	st.title('Year wise distribution :school_satchel:')
	# This dataframe has 244 lines, but 4 distinct values for `day` 
	year_series = df['Which best describes you?'].value_counts()
	year_values = year_series.tolist()
	year_names = year_series.index.tolist()
	fig = px.pie(values=year_values, names=year_names)
	st.plotly_chart(fig)

expander_3 = st.beta_expander("Are you an international student?")
with expander_3:
	st.title('Are you an international student? :school:')
	# This dataframe has 244 lines, but 4 distinct values for `day` 
	international_series = df['Are you an international student?'].value_counts()
	international_values = international_series.tolist()
	international_names = international_series.index.tolist()
	fig = px.pie(values=international_values, names=international_names)
	st.plotly_chart(fig)

expander_4 = st.beta_expander("How often do you eat out? (Including dine-in, take outs, and deliveries)")
with expander_4:
	st.title('How often do you eat out? (Including dine-in, take outs, and deliveries) :fries:')
	# This dataframe has 244 lines, but 4 distinct values for `day` 
	eating_series = df['How often do you eat out? (Including dine-in, take outs, and deliveries)'].value_counts()
	eating_values = eating_series.tolist()
	eating_names = eating_series.index.tolist()
	eating_df = pd.DataFrame({
	    'Eating Habits': eating_names,
	    'Number of Respondents': eating_values
	})
	fig = px.bar(eating_df,y='Number of Respondents', x='Eating Habits',height=500)

	fig.update_yaxes(automargin=True)
	st.plotly_chart(fig)

# left_column, right_column = st.beta_columns(2)
# pressed = left_column.button('Press me?')
# if pressed:
#     right_column.write("Woohoo!")
