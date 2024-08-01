import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# @st.cache_data
# def load_data():
day_data = pd.read_csv('https://raw.githubusercontent.com/alfajarjaya/dicoding-for-school/main/data/day.csv')
hour_data = pd.read_csv('https://raw.githubusercontent.com/alfajarjaya/dicoding-for-school/main/data/hour.csv')
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])
    # return day_data, hour_data

# day_data, hour_data = load_data()

st.title('Dashboard Streamlit Data CSV Peminjaman Sepeda')

st.sidebar.header('Opsi')
option = st.sidebar.selectbox(
    'Pilih jenis visualisasi:',
    ['Musim vs Total Peminjaman', 'Pola Penggunaan Berdasarkan Jam']
)

st.write('### Preview Data')
st.dataframe(day_data.head())

if option == 'Musim vs Total Peminjaman':
    st.write('### Total Peminjaman Sepeda berdasarkan Musim')
    seasonal_data = day_data.groupby('season')['cnt'].sum().reset_index()
    seasonal_data['season'] = seasonal_data['season'].map({
        1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
    })

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='season', y='cnt', data=seasonal_data, palette='viridis', ax=ax)
    ax.set_title('Total Peminjaman Sepeda berdasarkan Musim')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Total Peminjaman')
    st.pyplot(fig)

elif option == 'Pola Penggunaan Berdasarkan Jam':
    st.write('### Pola Penggunaan Sepeda berdasarkan Jam')
    hourly_data = hour_data.groupby('hr')['cnt'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='hr', y='cnt', data=hourly_data, marker='o', ax=ax)
    ax.set_title('Pola Penggunaan Sepeda berdasarkan Jam')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Total Peminjaman')
    st.pyplot(fig)

# Footer with copyright information
st.write("---")
st.write("© 2024 alfajarjaya(hehe). All rights reserved.")
