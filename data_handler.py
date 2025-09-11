import pandas as pd
from io import BytesIO
from config import EXCEL_PATH, DEFAULT_DATA, EXCEL_PATH_PODCAST, DEFAULT_DATA_PODCAST,DEFAULT_DATA_ACOES,EXCEL_PATH_ACOES
import streamlit as st


@st.cache_data
def load_dataframe(path=EXCEL_PATH):
    if path.exists():
        df = pd.read_excel(path)
    else:
        df = pd.DataFrame(DEFAULT_DATA, columns=[
            "Data", "Turno", "Horário", "Atividade", "Palestrante"
        ])
    # Normalizar Data
    df["Data_dt"] = pd.to_datetime(df["Data"], dayfirst=True, errors="coerce")
    df = df.sort_values(["Data_dt", "Turno", "Horário"])
    return df


@st.cache_data
def load_dataframe_podcast(path=EXCEL_PATH_PODCAST):
    if path.exists():
        df_podcast = pd.read_excel(path)
    else:
        df_podcast = pd.DataFrame(DEFAULT_DATA_PODCAST, columns=[
            "Data", "Turno", "Horário", "Atividade", "Palestrante"
        ])
    # Normalizar Data
    df_podcast["Data_dt"] = pd.to_datetime(df_podcast["Data"], dayfirst=True, errors="coerce")
    df_podcast = df_podcast.sort_values(["Data_dt", "Turno", "Horário"])
    return df_podcast


@st.cache_data
def load_dataframe_acoes(path=EXCEL_PATH_ACOES):
    if path.exists():
        df_acoes = pd.read_excel(path)
    else:
        df_acoes = pd.DataFrame(DEFAULT_DATA_PODCAST, columns=[
            "Data", "Turno", "Horário", "Atividade", "Palestrante"
        ])
    # Normalizar Data
    df_acoes["Data_dt"] = pd.to_datetime(
        df_acoes["Data"], dayfirst=True, errors="coerce")
    df_acoes = df_acoes.sort_values(["Data_dt", "Turno", "Horário"])
    return df_acoes


def to_excel_bytes(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Cronograma")
    return output.getvalue()


def to_excel_bytes_podcast(df_podcast):
    output_pod = BytesIO()
    with pd.ExcelWriter(output_pod, engine="openpyxl") as writer:
        df_podcast.to_excel(writer, index=False, sheet_name="Cronograma")
    return output_pod.getvalue()


def to_excel_bytes_acoes(df_acoes):
    output_acoes = BytesIO()
    with pd.ExcelWriter(output_acoes, engine="openpyxl") as writer:
        df_acoes.to_excel(writer, index=False, sheet_name="Cronograma")
    return output_acoes.getvalue()

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: white;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)
