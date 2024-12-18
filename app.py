import pandas as pd
import numpy as np
import pickle
import streamlit as st

this_pipe = pickle.load(open('ready_pipe.pkl', 'rb'))
teams = ['Australia', 'New Zealand', 'South Africa', 'England', 'India',
       'West Indies', 'Pakistan', 'Bangladesh', 'Afghanistan',
       'Sri Lanka']

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']

st.title('Cricket Score Predictor')
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))

with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

city = st.selectbox('Select City', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')

with col4:
    overs = st.number_input('Overs done (Write Overs more than 5)')

with col5:
    wickets = st.number_input('Wickets lost (OUT)')

last_five = st.number_input('Runs Scored in Last 5 Overs')

if st.button('Predict Total Scores'):
    ball_left = 120 - (overs * 6)
    wicket_left = 10 - wickets
    current_run_rate = current_score / overs

    input_df = pd.DataFrame(
        {'batting_team' : [batting_team], 'bowling_team' : [bowling_team], 'city' : [city], 'current_score' : [current_score], 'ball_left' : [ball_left], 'wicket_left' : [wicket_left], 'current_run_rate' : [current_run_rate], 'last_five' : [last_five]}
    )

    # st.table(input_df)

    result = this_pipe.predict(input_df)

    st.header('Predicted Score is: ' + str(int(result[0])))