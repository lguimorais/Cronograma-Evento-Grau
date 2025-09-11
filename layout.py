import streamlit as st


def set_layout():
    st.set_page_config(page_title="Cronograma Impacto Social", layout="wide")

    # CSS customizado
    st.markdown("""
        <style>
            html, body, [class*="css"] { font-family: 'Arial', sans-serif; }
            .main { background-color: #f9fafb; }
            h1, h2, h3 { color: #003366; }
            .streamlit-expanderHeader { font-weight: bold; color: #1f2937; }
            .stDataFrame { border-radius: 10px; overflow-x: auto; }
        </style>
    """, unsafe_allow_html=True)


def render_header():
    st.image("Logo.png", width=180)
    st.title("📋 Cronograma — Impacto Social (Grau Dirceu)")
    st.markdown(
        '<a href="https://forms.gle/7o9BC76m5C2U6xPG7" target="_blank" style="font-size:22px; font-weight:bold;">Clique aqui:Formulário de Inscrição.</a>',
        unsafe_allow_html=True
    )
    st.markdown(
        "📅 Período: **15/09/2025 a 20/09/2025**  \n"
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
