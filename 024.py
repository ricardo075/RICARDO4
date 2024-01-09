import streamlit as st

# Defina a senha
senha_correta = "COMPARTILHEOSITE942"

# Solicita a senha ao usuário
senha_digitada = st.text_input("Digite a senha:", type="password")

# Verifica se a senha está correta e libera o acesso
if senha_digitada == senha_correta:
    st.write("Senha correta. Você pode acessar o site.")
    st.write('PARA CALCULAR AREA FALANDO DE RESISTIVIDADE '
             '[clique aqui](https://ricardo1-ubxt2zt2raxacpyzlpogvg.streamlit.app/)')
    st.write('PARA CALCULAR A LARGURA FALANDO DE RESISTIVIIDADE '
             '[clique aqui](https://ricardi6-kgkbs2enusjebetvaqqtsw.streamlit.app/)')
    # Restante do código do seu site
    def calcula_resistividade(resistencia, largura, area):
        DADOS = f'DADOS:---------------------------------------------------------'
        DADOS2 = f'R= ?;'
        DADOS3 = f'r= {resistencia} ohm mm²/m'
        DADOS4 = f'L= {largura} m'
        DADOS5 = f'A= {area} m²'
        FORMULA3 = f'FORMULA:-----------------------------------------------------'
        FORMULA = f'R=r * L / A (RESISTIVIDADE = RESISTENCIA(r) vezes(*) LARGURA a dividir por(/) AREA(A)'
        RESOLUÇÃO = f'RESOLUÇAO:--------------------------------------------------'
        passo1 = f'Passo 1: Multiplicar a resistência ({resistencia} ohm mm² pela largura ({largura} m)'
        passo2 = f'Passo 2: Dividir o resultado pelo valor da área ({area} m²)'
        resistividade = (resistencia * largura) / area
        return resistividade, [DADOS, DADOS2, DADOS3, DADOS4, DADOS5, FORMULA3, FORMULA, RESOLUÇÃO, passo1, passo2]


    st.title('Calculadora de Resistividade')

    resistencia = st.number_input('Insira o valor da resistência (ohm mm²/m)')
    largura = st.number_input('Insira o valor da largura (m)')
    area = st.number_input('Insira o valor da área (m²)')

    if st.button('Calcular Resistividade'):
        resistividade, passos = calcula_resistividade(resistencia, largura, area)
        st.write('Passos para calcular a resistividade:')
        for passo in passos:
            st.write(passo)
        st.write(f'A resistividade é: {resistividade} ohm')
        st.write('OBRIGADO POR USAR ESTE SITE, SE HOUVER ALGUM PROBLEMA OU CRITICA CONSTRUTIVA'
                 'CONTACTE 841038887/868787572')
else:
    st.write("Senha incorreta. Acesso negado.")
