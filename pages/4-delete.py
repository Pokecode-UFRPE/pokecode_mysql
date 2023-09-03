import streamlit as st
import mysql.connector

def consultar_tables(table):
    conn = mysql.connector.connect(
        host = "Localhost", 
        user = "root", 
        password = "123456", 
        database = "pokecode")
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table}")
    columns = [column[0] for column in cursor.description]

    data = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return data, columns


def consultar_atributo(table, column):
    conn = mysql.connector.connect(
        host = "Localhost", 
        user = "root", 
        password = "123456", 
        database = "pokecode")
    cursor = conn.cursor()

    cursor.execute(f"SELECT DISTINCT {column} FROM {table}")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return data


def delete(table, atributo, valor):
    conn = mysql.connector.connect(
        host = "Localhost", 
        user = "root", 
        password = "123456", 
        database = "pokecode")
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM {table} WHERE {atributo} = '{valor}'")
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return "Deletado com sucesso!"


#st.image('assets\logo-down.png', width=200)
st.title("CRUD - DELETE")
with st.expander("Escolher table do DF"):
    table = st.selectbox("Selecione a tabela:", ["pokemons", "trainers", "trainers_pokemons", "regions"])
    data, columns = consultar_tables(table)
    # BLOCO DE CODIGO PARA RECUPERAR COLUNAS DO DF E PASSAR PARA DENTRO DA EXIBIÇÃO, SEM ISSO SÓ APARECEM OS INDICES
    aux_dic = {}
    aux_dic = {'0': 'id'}
    for i in range(len(columns)):
        aux_dic[i+1] = columns[i]

    st.dataframe(data, column_config=aux_dic)

with st.expander("Deletar dados:"):
    # CONVERTER O DIC EM LISTA P USAR AQUI NAS OPÇÕES DO SELECT E RETIRAR 1º POSICAO REPETIDA
    aux_list = list(aux_dic.values())
    aux_list = aux_list[1:]
    option = st.selectbox("Selecione por qual atributo você quer realizar a exclusão", aux_list)

    if option != None:
        # OBTENDO E CONVERTENDO OS DADOS DA COLUNA SELECIONADA
        valores_atributo = consultar_atributo(table, option)
        lista_valores = []
        for i in range(len(valores_atributo)):
            lista_valores.append(valores_atributo[i][0])

        dado_exclusao = st.radio(
            "Selecione qual deseja excluir", lista_valores)

        if st.button("Deletar", type="primary"):
            st.success(delete(table, option, dado_exclusao))
            st.balloons()


st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
col1, col2, col3 = st.columns([4,1,3])
with col2:
    st.image('https://i.gifer.com/origin/76/76dfca2a58c4dff5c9827b527132bda8.gif', width=50)