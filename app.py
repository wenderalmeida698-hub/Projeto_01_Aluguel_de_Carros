import streamlit as st
st.title("aluga rapido")
st.write("selecione o modelo que mais corresponde a sua expectativa para uma melhor expericencia.")
st.sidebar.image("aluga.png")
st.sidebar.title("selecione um carro")
nomes = ["fiat uno", "gol quadrado", "honda civic" , "corolla"]
opcao = st.sidebar.selectbox ("carros disponiveis:" , nomes)
st.image(f"{opcao}.png")
st.title (f"você alugou o modelo: {opcao}")
if  opcao == "fiat uno":
    diaria = 80
elif opcao == "gol quadrado":
    diaria = 90
elif opcao == "honda civic":
    diaria = 150
elif opcao == "corolla":
    diaria = 158
dias = st.number_input(f"Quantos dias {opcao} foi alugado?", min_value=1, step=1)
km = st.number_input(f"Quantos km você pretende rodar com o {opcao}?", min_value=1, step=1)
if st.button("calcular"):
    dias = int(dias)
    km = float(km)
    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km
    st.warning(f"você alugou o {opcao} por {dias} dias e rodou {km}km. o valor total a pagar é R${aluguel_total:.2f}")