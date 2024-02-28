import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# from babel.numbers import format_currency

sns.set(style="dark")
st.set_page_config(
    page_title="Dashboard Air Quality",
    page_icon="✨",
)
# Load data
df = pd.read_csv("cleaned_data.csv")
colors = [ "#0766AD","#C7C8CC", "#C7C8CC","#C7C8CC", "#C7C8CC", "#C7C8CC","#C7C8CC", "#C7C8CC", "#C7C8CC", "#C7C8CC", "#C7C8CC", "#C7C8CC"]


# function
def plot_pollutant_year(data, pollutant):
    data = (
        data[[pollutant, "year"]]
        .groupby(["year"])
        .mean()
        .reset_index()
        .sort_values(by="year", ascending=False)
    )
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.lineplot(x="year", y=pollutant, data=df)
    plt.title(f"{pollutant} Trend Over Years")
    plt.xlabel("Year")
    plt.ylabel(f"{pollutant} Concentration")
    st.pyplot(fig)  # Menampilkan plot di Streamlit


def plot_pollutant_month(data, pollutant):
    data = (
        data[[pollutant, "month"]]
        .groupby(["month"])
        .mean()
        .reset_index()
        .sort_values(by="month", ascending=False)
    )
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.lineplot(x="month", y=pollutant, data=df)
    plt.title(f"{pollutant} Trend Over Month")
    plt.xlabel("Month")
    plt.ylabel(f"{pollutant} Concentration")
    st.pyplot(fig)  # Menampilkan plot di Streamlit


def plot_pollutant_day(data, pollutant):
    data = (
        data[[pollutant, "day"]]
        .groupby(["day"])
        .mean()
        .reset_index()
        .sort_values(by="day", ascending=False)
    )
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.lineplot(x="day", y=pollutant, data=df)
    plt.title(f"{pollutant} Trend Over Day")
    plt.xlabel("Year")
    plt.ylabel(f"{pollutant} Concentration")
    st.pyplot(fig)  # Menampilkan plot di Streamlit


def plot_station_comparison(data, pollutant):
    data_grouped = (
        data[[pollutant, "station"]]
        .groupby(["station"])
        .mean()
        .reset_index()
        .sort_values(by=pollutant, ascending=False)
    )
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.barplot(x=pollutant, y="station", data=data_grouped, palette=colors)
    plt.title(f"Average {pollutant} Concentration by Station")
    plt.xlabel(f"{pollutant} Concentration")
    plt.ylabel("Station")
    st.pyplot(fig)


# Header
st.header("Dashboard Air Quality")


# Polusi Udara berdasarkan parameternya Secara waktu
st.subheader("Polusi Udara berdasarkan waktu ")
tab1, tab2, tab3 = st.tabs(["Tahun", "Bulan", "Harian"])
with tab1:
    st.subheader("Tahun")
    pollutants = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
    selected_pollutant = st.selectbox(
        "Select Pollutant", pollutants, key="year_pollutant"
    )
    # Menjalankan fungsi untuk menampilkan plot
    plot_pollutant_year(df, selected_pollutant)

with tab2:
    st.subheader("Bulan")
    pollutants = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
    selected_pollutant = st.selectbox(
        "Select Pollutant", pollutants, key="month_pollutant"
    )
    # Menjalankan fungsi untuk menampilkan plot
    plot_pollutant_month(df, selected_pollutant)

with tab3:
    st.subheader("Harian")
    pollutants = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
    selected_pollutant = st.selectbox(
        "Select Pollutant", pollutants, key="day_pollutant"
    )
    # Menjalankan fungsi untuk menampilkan plot
    plot_pollutant_day(df, selected_pollutant)


# Header
st.header("Perbandingan parameter kualitas udara tiap Station")

selected_pollutant = st.selectbox(
    "Select Pollutant", pollutants, key="station_comparison_pollutant"
)
plot_station_comparison(df, selected_pollutant)
