import streamlit as st
import pandas as pd
from data_handler import to_excel_bytes


def render_metrics(df_f):
    st.markdown("### 📊 Resumo dos Filtros")
    col1, col2, col3 = st.columns(3)
    col1.metric("quantidade de palestras", len(df_f))
    col2.metric("Palestrantes",
                df_f["palestrante"].nunique())
    col3.metric("Datas do evento", df_f["Data_dt"].dt.date.nunique())


def render_download(df_f):
    excel_bytes = to_excel_bytes(df_f.drop(columns=["Data_dt"]))
    st.download_button(
        "⬇️ Baixar cronograma filtrado (.xlsx)",
        data=excel_bytes,
        file_name="Cronograma_filtrado.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


def render_agenda(df_f, unique_dates_sorted):
    st.header("📅 Agenda por Data")
    for d in unique_dates_sorted:
        d_str = d.strftime("%d/%m/%Y")
        df_day = df_f[df_f["Data_dt"].dt.date == d]
        if df_day.empty:
            continue
        with st.expander(f"{d_str} — {len(df_day)} atividades", expanded=False):
            df_day_sorted = df_day.sort_values(["Turno", "Horário"])
            for _, row in df_day_sorted.iterrows():
                st.markdown(f"""
                    <div style="
                        background-color:#ffffff;
                        border:1px solid #ddd;
                        border-radius:12px;
                        padding:12px;
                        margin-bottom:10px;
                        box-shadow:0 2px 4px rgba(0,0,0,0.05);
                    ">
                        <p><b>🕒 Horário:</b> {row['Horário']}</p>
                        <p><b>📌 Turno:</b> {row['Turno']}</p>
                        <p><b>🎯 Atividade:</b> {row['Atividade']}</p>
                        <p><b>👤 Ministrante:</b> {row['Palestrante']}</p>
                    </div>
                """, unsafe_allow_html=True)


def render_table(df_f):
    st.header("📑 Tabela Completa (Filtrada)")
    st.dataframe(
        df_f[["Data", "Turno", "Horário", "Atividade", "Palestrante"]]
        .reset_index(drop=True),
        use_container_width=True,
    )


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
