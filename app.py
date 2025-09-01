import streamlit as st

# python -m streamlit run app.py

# ------------------------------------------------- Sidebar

st.sidebar.image("logo.png")
st.sidebar.title('Mateus Motors')


carros = ['BMW','Mustang', 'Porsche', 'Fusca', 'Toro']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)



# ----------------------------------------------- Principal 
st.title('Mateus motors - Aluguel de Carros')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

if opcao == 'BMW':
    diaria = 450

elif opcao == 'Mustang':
    diaria = 500

elif opcao == 'Porsche':
    diaria = 300

elif opcao == 'Fusca':
    diaria = 250

elif opcao == 'Toro':
    diaria = 550





if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')






