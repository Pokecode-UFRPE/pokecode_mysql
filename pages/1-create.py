import streamlit as st
import mysql.connector
conn = mysql.connector.connect(
    host="Localhost",
    user="root",
    password="123456",
    database="pokecode"
)

cursor = conn.cursor()

cursor.execute("USE pokecode")

st.title("CRUD - CREATE")
def obter_nomes_tabelas():
    cursor.execute("SHOW TABLES")
    tabelas = [tabela[0] for tabela in cursor.fetchall()]
    conn.commit()
    
    return tabelas


# Aplicativo Streamlit
st.title("Tabelas do Banco de Dados")

# Chame a função para obter os nomes das tabelas
nomes_tabelas = obter_nomes_tabelas()


nomes = []
# Exiba os nomes das tabelas no aplicativo
for nome_tabela in nomes_tabelas:
    nomes.append(nome_tabela)

# Feche a conexão com o banco de dados

# CONSULTA DE TABELAS SIMPLES
def consultar_pokemons(tabela):
    query = f"""
    SELECT *
    FROM {tabela}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    return data



if st.button("Exibir"):
    for i in nomes:
        st.text(i)
        st.dataframe(consultar_pokemons(i))



cursor.close()
conn.close()