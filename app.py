import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configurações da Página
st.set_page_config(page_title="SAD - Logística", layout="wide")
st.title("👕 Painel de Logística: Campanha de Agasalhos 2026")

# 2. Métricas de Resumo
col1, col2, col3 = st.columns(3)
col1.metric("Peças Arrecadadas", "1.432", "+120")
col2.metric("Itens Processados", "92%", "Estável")
col3.metric("Famílias Atendidas", "156", "+15")

st.divider()

# 3. Estruturação dos Dados (Tratamento e Integridade)
# Criando os dados para os gráficos (Reflete o que você colocou no currículo)
df_estoque = pd.DataFrame({
    "Categoria": ["Agasalhos", "Cobertores", "Calçados", "Roupas Infantis"],
    "Quantidade": [450, 320, 180, 250]
})

df_tamanhos = pd.DataFrame({
    "Tamanho": ["P", "M", "G", "GG"],
    "Estoque": [85, 140, 95, 50]
})

# 4. Exibição dos Gráficos
col_esq, col_dir = st.columns(2)

with col_esq:
    st.write("### Distribuição por Categoria")
    fig_pizza = px.pie(df_estoque, names='Categoria', values='Quantidade', hole=0.4)
    st.plotly_chart(fig_pizza, use_container_width=True)

with col_dir:
    st.write("### Inventário por Tamanho")
    fig_barra = px.bar(df_tamanhos, x="Tamanho", y="Estoque", color="Tamanho", 
                       color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_barra, use_container_width=True)