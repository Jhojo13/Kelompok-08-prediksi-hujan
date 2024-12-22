import pickle
import streamlit as st

# membaca model
seattleWeather_model =  pickle.load(open('seattleWeather.sav', 'rb'))

col1, col2 = st.columns([1, 4])

with col1:
    st.image('img/rain.png', use_container_width=True)

with col2:
    st.title('Prediksi Hujan')



PRCP = 0.0

TMAX = st.text_input('Suhu tertinggi')

TMIN = st.text_input('Suhu minimum')

# code untuk diagnosis hujan
hujan_prediksi = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    try:
        # Konversi input menjadi float
        TMAX = float(TMAX) if TMAX.strip() else 0.0
        TMIN = float(TMIN) if TMIN.strip() else 0.0
        
        # Melakukan prediksi
        hujan_prediction = seattleWeather_model.predict([[PRCP, TMAX, TMIN]])
        
        # Menentukan hasil
        if hujan_prediction[0] == 1:
            hujan_prediksi = 'Hujan'
        else:
            hujan_prediksi = 'Tidak hujan'
        
        st.success(hujan_prediksi)
    except ValueError:
        st.error("Pastikan semua input adalah angka yang valid!")
