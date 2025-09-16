import streamlit as st
from data_handler import load_dataframe , load_dataframe_podcast,load_dataframe_acoes
from layout import set_layout, render_header
from sidebar import render_sidebar
from views import render_metrics, render_download, render_agenda, render_table , render_podcast, render_acoes

# Layout inicial
set_layout()
render_header()

# Carregar dados
df = load_dataframe()
df_podcast = load_dataframe_podcast()
df_acoes = load_dataframe_acoes()

# Sidebar
sel_dates, sel_turnos, sel_ministrante, search_text = render_sidebar(df)

# Aplicar filtros
mask = df["Data_dt"].dt.strftime("%d/%m/%Y").isin(sel_dates)
mask &= df["Turno"].isin(sel_turnos)
mask &= df["Palestrante"].isin(sel_ministrante)
if search_text.strip():
    st_text = search_text.strip().lower()
    mask &= df.apply(
        lambda row: st_text in str(row["Atividade"]).lower()
        or st_text in str(row["Palestrante"]).lower()
        or st_text in str(row["Horário"]).lower(),
        axis=1,
    )


df_f = df.loc[mask].copy()
df_f_pod = df_podcast.loc[mask].copy()
df_f_acoes = df_acoes.loc[mask].copy()
# Visualizações
render_metrics(df_f)
render_download(df_f)



st.markdown("---")

unique_dates_sorted = sorted(df["Data_dt"].dropna().dt.date.unique())
render_agenda(df_f, unique_dates_sorted)
unique_dates_sorted = sorted(df_podcast["Data_dt"].dropna().dt.date.unique())
render_podcast(df_f_pod, unique_dates_sorted)
unique_dates_sorted = sorted(df_acoes["Data_dt"].dropna().dt.date.unique())
render_acoes(df_f_acoes, unique_dates_sorted)
st.markdown(
    """📌 Documentos necessários para Emissão de novas CIN (Carteira de Identidade Nacional):\n
    Certidão de nascimento\n
    Comprovante de endereço\n"""
)




st.markdown("---")
render_table(df_f)
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
