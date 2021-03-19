import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
st.image('CSL Logo.png',width=500)
dataset = pd.read_csv('survey_data.csv')

df = dataset
df['Which university do you belong to?'] = df['Which university do you belong to?'].replace(['Carnegie Mellon','Carnegie Mellon University','carnegie mellon','School of Computer Science','Carnegie mellon university','Carnegie Mellon University, School of Computer Science','School of Computer Science','Cmu','Carnegie Mellon University - CIT','Carnegie Mellon Univsersity','Carnegie Mellon Unviersity','Carnegie Mellon University','CIT','Carnegie Mellon ','Carnegie Mellon University ','CMU'],'Carnegie Mellon University')
df['Which university do you belong to?'] = df['Which university do you belong to?'].replace(['University of Pittsburgh','University of Pittsburgh '],'University of Pittsburgh')
df['How often do you eat out? (Including dine-in, take outs, and deliveries)'] = df['How often do you eat out? (Including dine-in, take outs, and deliveries)'].replace(["Last semester was 5x a week (which I hated because I prefer cooking for health, but I didn't have time). Now 1-2x a month"],'1-3 times a month')
df['Select the type of kitchen you have access to in your residence'] = df['Select the type of kitchen you have access to in your residence'].replace(["Well, it has a cooker. We have a fridge and air extractor. So, I don't know if that counts as full."],'It has a small kitchen or kitchenette (e.g. small stove, fridge, and etc.).')

print(df.columns)
value_counts_series = df['Which university do you belong to?'].value_counts()
uni_counts = value_counts_series.tolist()
uni_names = value_counts_series.index.tolist()

st.title("Corporate Startup Lab x Giant Eagle Customer Dashboard :office:")

st.sidebar.title("Select Analysis")
st.sidebar.markdown("Choose between survey or interview analysis:")
option = st.sidebar.selectbox("Choose:",   ('','Survey Analysis', 'Interview Analysis'),format_func=lambda x: 'Select an option' if x == '' else x)

if option=='Survey Analysis':
	st.title('Giant Eagle Survey Analysis')
	if st.checkbox('Raw Data'):
		st.write(df[0:5])

	st.write('Basic Demographics')

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

	st.write("----------------------------------------------------------------------------------------------------")
	st.write('Kitchen Amenities and Eating Habits')

	expander_4 = st.beta_expander("Select the type of kitchen you have access to in your residence")
	with expander_4:
		st.title('Select the type of kitchen you have access to in your residence')
		# This dataframe has 244 lines, but 4 distinct values for `day` 
		kitchen_series = df['Select the type of kitchen you have access to in your residence'].value_counts()
		kitchen_values = kitchen_series.tolist()
		kitchen_names = kitchen_series.index.tolist()
		kitchen_df = pd.DataFrame({
			'Type of Kitchen': kitchen_names,
			'Number of Respondents': kitchen_values
		})
		fig = px.bar(kitchen_df,y='Number of Respondents', x='Type of Kitchen',height=500)

		fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)


	expander_5 = st.beta_expander("How often do you eat out? (Including dine-in, take outs, and deliveries)")
	with expander_5:
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

	expander_6 = st.beta_expander("How much do you spend on an average per month for grocery shopping?")
	with expander_6:
		st.title('How much do you spend on an average per month for grocery shopping? :dollar:')
		# This dataframe has 244 lines, but 4 distinct values for `day` 
		money_series = df['How much do you spend on an average per month for grocery shopping?'].value_counts()
		money_values = money_series.tolist()
		money_names = money_series.index.tolist()
		money_names = sorted(money_names)
		money_names = ['< $99','$100 - $149', '$150 -  $199', '$200 - $249', '$250 - $300', '$300+']
		money_values = [2,14,13,11,6,6]
		money_df = pd.DataFrame({
			'Amount Spent per month on groceries': money_names,
			'Number of Respondents': money_values
		})
		print(money_df)
		fig = px.bar(money_df,y='Number of Respondents', x='Amount Spent per month on groceries',height=500)

		fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)

	expander_7 = st.beta_expander("The most important factors in determining a grocery store")
	with expander_7:
		st.title('Most important factors in deciding the grocery store')
		# This dataframe has 244 lines, but 4 distinct values for `day` 
		factor_series = df['Rank the most important factor in deciding your grocery store [One]'].value_counts()
		factor_values = factor_series.tolist()
		factor_names = factor_series.index.tolist()
		factor_df = pd.DataFrame({
			'Most Important Factor': factor_names,
			'Number of Respondents': factor_values
		})
		print(factor_df.head())
		fig = go.Figure(data=[go.Pie(labels=factor_names, values=factor_values, hole=.3)])

		#fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)


		factor_series = df['Rank the most important factor in deciding your grocery store [Two]'].value_counts()
		factor_values = factor_series.tolist()
		factor_names = factor_series.index.tolist()
		factor_df = pd.DataFrame({
			'Most Important Factor': factor_names,
			'Number of Respondents': factor_values
		})
		print(factor_df.head())
		fig = go.Figure(data=[go.Pie(labels=factor_names, values=factor_values, hole=.3)])

		#fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)

		factor_series = df['Rank the most important factor in deciding your grocery store [Three]'].value_counts()
		factor_values = factor_series.tolist()
		factor_names = factor_series.index.tolist()
		factor_df = pd.DataFrame({
			'Most Important Factor': factor_names,
			'Number of Respondents': factor_values
		})

		print(factor_names)
		factor_names = ['Quality','Proximity','Product variety','Promotions', 'Open Hours']
		factor_values = [10,16,19,2,5]
		fig = go.Figure(data=[go.Pie(labels=factor_names, values=factor_values, hole=.3,sort=False)])

		#fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)

	expander_8 = st.beta_expander("Grocery Store Preferences")
	with expander_8:
		st.title('Grocery Store Preferences')
		# This dataframe has 244 lines, but 4 distinct values for `day` 
		store_series = df['Select your favorite grocery shopping choices [First choice]'].value_counts()
		store_values = store_series.tolist()
		store_names = store_series.index.tolist()
		store_df = pd.DataFrame({
			'First Preferred Store': store_names,
			'Number of Respondents': store_values
		})
		fig = px.bar(store_df,y='Number of Respondents', x='First Preferred Store',height=500)

		fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)

		store_series = df['Select your favorite grocery shopping choices [Second choice]'].value_counts()
		store_values = store_series.tolist()
		store_names = store_series.index.tolist()
		store_df = pd.DataFrame({
			'Second Preferred Store': store_names,
			'Number of Respondents': store_values
		})
		fig = px.bar(store_df,y='Number of Respondents', x='Second Preferred Store',height=500)

		fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)

		store_series = df['Select your favorite grocery shopping choices [Third choice]'].value_counts()
		store_values = store_series.tolist()
		store_names = store_series.index.tolist()
		store_df = pd.DataFrame({
			'Third Preferred Store': store_names,
			'Number of Respondents': store_values
		})
		fig = px.bar(store_df,y='Number of Respondents', x='Third Preferred Store',height=500)

		fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)

	expander_8 = st.beta_expander("Ideas you would like the grocery stores to implement?")
	with expander_8:
		st.title('Suggested Ideas')
		# This dataframe has 244 lines, but 4 distinct values for `day` 
		preference_list = df['Is there any service from the following list you would like your grocery shop to implement? (check all that apply)'].tolist()
		counts = {}
		preference_list_splitted = []
		for i in preference_list:
			individual = i.split(",")
			for k in individual:
				preference_list_splitted.append(k.strip())
		for i in preference_list_splitted:
			counts[i] = counts.get(i, 0) + 1
		#print(counts)
		preference_names = ['Student Membership / Discounts','Curbside Delivery','Grocery delivered to your Campus via On-Campus Locker system','Meals on Wheels','A parking lot instead of on-street parking']
		preference_values = [47,14,7,5,1]
		store_values = store_series.tolist()
		store_names = store_series.index.tolist()
		store_df = pd.DataFrame({
			'Ideas to Implement': preference_names,
			'Number of Respondents': preference_values
		})
		fig = px.bar(store_df,y='Number of Respondents', x='Ideas to Implement',height=500)	
		fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)


if option=='Interview Analysis':
	st.title('Giant Eagle Interview Analysis')
	interview_dataset = pd.read_csv('interview_data.csv')
	print(interview_dataset.head())
	int_df = interview_dataset

	if st.checkbox('Raw Data'):
		st.write(interview_dataset[0:5])

	expander = st.beta_expander("Basic Demographics")
	with expander:
		st.title('Gender :boy: :girl:')
			# This dataframe has 244 lines, but 4 distinct values for `day` 
		demographic_series = int_df['Gender'].value_counts()
		demographic_values = demographic_series.tolist()
		demographic_names = demographic_series.index.tolist()
		demographic_df = pd.DataFrame({
				'Gender': demographic_names,
				'Number of Respondents': demographic_values
		})
		fig = px.pie(values=demographic_values, names=demographic_names)

		fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)

		st.title('University Year :school_satchel:')
			# This dataframe has 244 lines, but 4 distinct values for `day` 
		demographic_series = int_df['Class'].value_counts()
		demographic_values = demographic_series.tolist()
		demographic_names = demographic_series.index.tolist()
		demographic_df = pd.DataFrame({
				'Class': demographic_names,
				'Number of Respondents': demographic_values
		})
		fig = px.pie(values=demographic_values, names=demographic_names)

		fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)

	expander = st.beta_expander("Housing Details")
	with expander:
		st.title('Do the students live on campus? :house_with_garden:')
			# This dataframe has 244 lines, but 4 distinct values for `day` 
		demographic_series = int_df['Live on campus'].value_counts()
		demographic_values = demographic_series.tolist()
		demographic_names = demographic_series.index.tolist()
		demographic_df = pd.DataFrame({
				'Live on campus': demographic_names,
				'Number of Respondents': demographic_values
		})
		fig = px.pie(values=demographic_values, names=demographic_names)

		fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)

		st.title('Do the students live alone?')
			# This dataframe has 244 lines, but 4 distinct values for `day` 
		demographic_series = int_df['Live alone'].value_counts()
		demographic_values = demographic_series.tolist()
		demographic_names = demographic_series.index.tolist()
		demographic_df = pd.DataFrame({
				'Live on campus': demographic_names,
				'Number of Respondents': demographic_values
		})
		fig = px.pie(values=demographic_values, names=demographic_names)

		fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)

	expander = st.beta_expander("Money Spent on Groceries and Takeouts")
	with expander:
		st.title('How much do students spend on groceries each week? :dollar:')
			# This dataframe has 244 lines, but 4 distinct values for `day` 
		demographic_series = int_df['Spent on Groceries Range'].value_counts()
		demographic_values = demographic_series.tolist()
		demographic_names = demographic_series.index.tolist()
		demographic_names = ['0-50','50-100','100-150','>150']
		demographic_values = [4,7,2,1]
		demographic_df = pd.DataFrame({
				'Money Spent on Groceries': demographic_names,
				'Number of Respondents': demographic_values
		})
		fig = px.bar(demographic_df,y='Number of Respondents', x='Money Spent on Groceries',height=500)

		fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)

		st.title('How much do students spend on takeouts each week? :dollar:')
			# This dataframe has 244 lines, but 4 distinct values for `day` 
		demographic_series = int_df['Takeout Range'].value_counts()
		demographic_values = demographic_series.tolist()
		demographic_names = demographic_series.index.tolist()
		demographic_df = pd.DataFrame({
				'Money Spent on Takeouts': demographic_names,
				'Number of Respondents': demographic_values
		})
		fig = px.bar(demographic_df,y='Number of Respondents', x='Money Spent on Takeouts',height=500)

		fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)

	expander = st.beta_expander("Personas Distribution")
	with expander:
		st.title('Personas Distribution')
			# This dataframe has 244 lines, but 4 distinct values for `day` 
		demographic_series = int_df['Personas'].value_counts()
		demographic_values = demographic_series.tolist()
		demographic_names = demographic_series.index.tolist()
		demographic_df = pd.DataFrame({
				'Personas': demographic_names,
				'Number of Respondents': demographic_values
		})
		fig = px.bar(demographic_df,y='Number of Respondents', x='Personas',height=500)

		fig.update_yaxes(automargin=True)
		st.plotly_chart(fig)
