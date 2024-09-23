import streamlit as st
from datetime import datetime, time
def main():

    st.title("Sistema de input de dados")
    email = st.text_input("Campo de texto para inserção")
    data = st.date_input("Campo seleção data da Ocorrência", datetime.now())
    hora = st.time_input("Campo seleção hora da Ocorrência", value=time(9, 0)) # Valor padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade da venda", min_value=1, step=1)
    produto = st.selectbox("Selecione o produto",options=["Mel especial 240g - Alerquina", "Mel especial 240g - Batman", "Mel especial 240g - Coringa"])

    if st.button("Salvar"):
        data_hora = datetime.combine(data,hora)
        st.write("**Dados da Venda:**")
        st.write(f"Email Vendedor: {email}")
        st.write(f"Data e Hora da venda: {data_hora}")
        st.write(f"Valor da Venda: R$ {valor: .2f}")
        st.write(f"Quantidade Produtos: {quantidade}")
        st.write(f"Produto: {produto}")

if __name__=="__main__":
    main()