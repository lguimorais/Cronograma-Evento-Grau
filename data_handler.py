import pandas as pd
from io import BytesIO
from config import EXCEL_PATH, DEFAULT_DATA
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


def to_excel_bytes(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Cronograma")
    return output.getvalue()


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
