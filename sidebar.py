import streamlit as st


def render_sidebar(df):
    st.sidebar.header("🔎 Filtros")

    unique_dates = df["Data_dt"].dropna().dt.date.unique()
    unique_dates_sorted = sorted(unique_dates)
    date_options = [d.strftime("%d/%m/%Y") for d in unique_dates_sorted]
    sel_dates = st.sidebar.multiselect(
        "Data", options=date_options, default=date_options)

    turnos = sorted(df["Turno"].dropna().unique())
    sel_turnos = st.sidebar.multiselect(
        "Turno", options=turnos, default=turnos)

    ministrantes = sorted(df["Ministrante/Responsável"].dropna().unique())
    sel_ministrante = st.sidebar.multiselect(
        "Ministrante", options=ministrantes, default=ministrantes)

    search_text = st.sidebar.text_input(
        "Pesquisar (atividade, ministrante, horário)", "")

    return sel_dates, sel_turnos, sel_ministrante, search_text
