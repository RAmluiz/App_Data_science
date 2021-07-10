# Stremlit_test

# Para rodar o App basta entrar na pasta do arquivo e deigitar :
# Para cada alteracao somente salvar, se precisar rode o codigo
# stremlit run [arquivo.py]

import streamlit as st
import pandas as pd
import numpy as np

# Crinado paginas no app

paginas = ["Home", "Graficos"]
pagina = st.sidebar.selectbox("Selecione a página de interesse", paginas)
st.image("E:\DADOS DE CURSOS\WEB_APP_Streamlit\Imagem2.jpg", use_column_width = "always")

st.header("meu primeiro App")
dados = pd.read_csv("automobile.csv")

if pagina == "home":

    st.markdown("# Título do meu App")

    

    st.write(dados)
#Selecionando dados "seletor" 
# ao criar a variável var posso fazer operações com ela

    variaveis = dados.columns.tolist()
    var = st.sidebar.selectbox("Selecione uma categoria", ["symboling","make"]) # O selectbox gera o menu dropdown e o sidebar joga para a barra lateral


    ms = dados["symboling"].groupby(dados[var]).mean()# Agrupando poer média 
    st.write(ms)
# Escrevendo e printando a variável anterior

    var1 = st.sidebar.selectbox("Selecione uma variável", variaveis) 



# Exemplo em Latex
'''
# Utilizando latex no App
'''
st.latex('\int_a^b f(x) dx - \mu')

'''
# Também funciona para códigos
'''
st.code('''
lista = [1,2,3]

for i in lista:
    print(f"numero{i}")
''')

'''# Se eu quiser uma tabela estática'''
apresentacao = dados.describe()
st.table(apresentacao)



# Fazendo gráficos

grafico1 = dados[var1].value_counts().plot(kind = "barh") # o count_values é do pandas mesmo
st.pyplot(grafico1.figure) 



# Exemplos do stremlit
# https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py



#---------#
#Botões

#Guardam valores True ou False

st.button(label = '-> Clique aqui! <-', help = 'É só clicar ali')



st.checkbox('Clique para me selecionar', help = 'Clique e desclique quando quiser')

#Botões de Rádio

# Guarda o item do botão selecionado

st.radio('Botões de Rádio', options = [100, 'Python', print, [1, 2, 3]], index = 1, help = 'Ajuda')

# Guarda o item da caixa selecionado

st.selectbox('Clique no item que deseja', options = ['azul', 'roxo', 'verde'], index = 2)

st.multiselect('Selecione quantas opções desejar', options = ['A', 'B', 'C', 'D', 'E'])


#Guarda o número selecionado

st.slider('Entrada numérica', min_value = 1, max_value = 25, value = 7, step = 2)	

#Entrada numérica

