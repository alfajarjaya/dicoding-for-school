# Proyek Analisis Data dan Dashboard Streamlit ✨

## Deskripsi
Proyek ini melibatkan analisis data dari dua dataset: `day.csv` dan `hour.csv`. Analisis ini mencakup eksplorasi data, visualisasi, dan pembuatan dashboard interaktif menggunakan Streamlit.

## Setup Environment - Anaconda
1. **Buat Environment Baru**
    ```bash
    conda create --name main-ds python=3.9
    ```
2. **Aktifkan Environment**
    ```bash
    conda activate main-ds
    ```
3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Setup Environment - Shell/Terminal
1. **Buat Direktori Proyek**
    ```bash
    mkdir proyek_analisis_data
    cd proyek_analisis_data
    ```
2. **Install Dependencies Menggunakan Pipenv**
    ```bash
    pipenv install
    pipenv shell
    pip install -r requirements.txt
    ```

## Menjalankan Aplikasi Streamlit
Jalankan aplikasi Streamlit dengan perintah berikut:
```bash
python -m streamlit run app.py
