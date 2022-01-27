import streamlit as st
import datetime, time
'''
# TaxiFareModel Prediction
'''
page_load_start_time = time.time()
page_load_time_placeholder = st.sidebar.empty()
'''
## Enter taxi ride information:
'''
d = st.date_input("Enter your date of travel",
                  datetime.datetime(2022, 1, 1, 1))
st.write(d)
t = st.time_input('Choose a time', datetime.time(8, 45))
date_time = datetime.datetime.combine(d, t).strftime("%Y-%m-%d %H:%M:%S")
st.write(date_time)
pickup_longitude = st.number_input('pickup longitude')
pickup_latitude = st.number_input('pickup latitude')
dropoff_longitude = st.number_input('dropoff longitude')
dropoff_latitude = st.number_input('dropoff latitude')
passenger_count = st.slider('Select a modulus', 1, 10, 2)
url = 'https://taxifare.lewagon.ai/predict'
data = {
    "pickup_latitude": pickup_latitude,
    "pickup_longitude": pickup_longitude,
    "dropoff_latitude": dropoff_latitude,
    "dropoff_longitude": dropoff_longitude,
    "passenger_count": int(passenger_count),
    "pickup_datetime": date_time,
}
import requests
if st.button('Predict'):
    # print is visible in the server output, not in the page
    response = requests.get(url, params=data)
    pred = response.json()['prediction']
    """
    Result is:
    """
    st.write("It will cost $" + str(pred))
else:
    st.write('Enter the params first')
page_load_duration = time.time() - page_load_start_time
page_load_time_placeholder.markdown(f'{round(page_load_duration, 3)} seconds')
