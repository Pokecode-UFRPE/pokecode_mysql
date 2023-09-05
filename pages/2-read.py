import streamlit as st
import mysql.connector

conn = mysql.connector.connect(
    host="Localhost",
    user="root",
    password="123456",
    database="pokecode"
)
cursor = conn.cursor()

# CONSULTA DE TABELAS SIMPLES
def consultar_pokemons():
    query = """
    SELECT *
    FROM pokemons
    """
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def consultar_nomes_e_tipo_pokemons():
    query = """
    SELECT nome, tipo
    FROM pokemons
    """
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def consultar_pokemons_tipo_grass():
    query = """
    SELECT nome, tipo, color, region_id
    FROM pokemons
    WHERE tipo='grass'
    """
    cursor.execute(query)
    data = cursor.fetchall()
    return data

st.title("CRUD - READ")
with st.expander("Visualização de Tabelas Simples"):
    view_option = st.selectbox("Selecione a visualização:", ["pokemons", "pokemons nome e tipo", "pokemons tipo grass"])

    if view_option == "pokemons":
        data = consultar_pokemons()
    elif view_option == "pokemons nome e tipo":
        data = consultar_nomes_e_tipo_pokemons()
    else:
        data = consultar_pokemons_tipo_grass()

    if st.button("Visualizar"):
        if data:
            st.subheader("Resultado da Consulta:")
            st.dataframe(data)
        else:
            st.subheader("Nenhum resultado encontrado.")
            
cursor.close()
conn.close()            
            






# CONSULTA DE TABELAS RELACIONADAS

conn = mysql.connector.connect(
    host="Localhost",
    user="root",
    password="123456",
    database="pokecode"
)
cursor = conn.cursor()

def criar_pokemons_regions_view():
    query = """
    SELECT p.pokedex_number, p.nome as 'Pokemon', p.tipo as 'Tipo', r.nome as 'Regiao'
    FROM pokemons as p, regions as r
    WHERE p.region_id = r.id;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def criar_trainers_pokemons_view():
    query = """
    SELECT t.nome AS treinador_nome, p.nome AS pokemon_nome
    FROM trainers_pokemons AS tp
    INNER JOIN trainers AS t ON tp.trainer_id = t.id
    INNER JOIN pokemons AS p ON tp.pokedex_number = p.pokedex_number
    """
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def criar_trainers_pokemons_regions_view():
    query = """
    SELECT t.nome AS nome_treinador, p.nome AS nome_pokemon, r.nome AS regiao_pokemon
    FROM trainers_pokemons AS tp
    INNER JOIN trainers AS t ON tp.trainer_id = t.id
    INNER JOIN pokemons AS p ON tp.pokedex_number = p.pokedex_number
    INNER JOIN regions AS r ON p.region_id = r.id
    """
    cursor.execute(query)
    data = cursor.fetchall()
    return data

with st.expander("Visualização de Tabelas Relacionadas"):
    
    view_option = st.selectbox("Selecione a visualização:", ["pokemons x regions", "trainers x pokemons", "trainers x pokemons x regions"])

    if view_option == "pokemons x regions":
        data = criar_pokemons_regions_view()
    elif view_option == "trainers x pokemons":
        data = criar_trainers_pokemons_view()
    else:
        data = criar_trainers_pokemons_regions_view()

    if st.button("Criar View"):
        if data:
            st.subheader("Resultado da Consulta:")
            st.dataframe(data)
        else:
            st.subheader("Nenhum resultado encontrado.")

cursor.close()
conn.close()






# CONSULTA DE TABELAS AVANÇADA

conn = mysql.connector.connect(
    host="Localhost",
    user="root",
    password="123456",
    database="pokecode"
)
cursor = conn.cursor()

table_info = {
    "pokemons": {
        "columns": ["pokedex_number", "nome", "color", "attack", "defense", "hp", "speed", "tipo", "height", "weight", "rarity", "evolve", "region_id"],
    },
    "trainers": {
        "columns": ["id", "nome", "email"],
    },
    "regions": {
        "columns": ["id", "nome", "descricao", "location"],
    },
    "trainers_pokemons": {
        "columns": ["id", "trainer_id", "pokedex_number"],
    }
}

def construir_query(table, campos, search_term):    
    # Cláusula SELECT
    select_clause = ", ".join(campos)

    # Cláusula WHERE
    where_clause = " OR ".join([f"{col} LIKE '%{search_term}%'" for col in campos])

    # Consulta SQL
    if "all" in campos:
        query = f"SELECT * FROM {table}"
    else:
        query = f"SELECT {select_clause} FROM {table} WHERE {where_clause}"
    
    return query

with st.expander("Visualização de Tabelas Avançada"):

    table = st.selectbox("Selecione a tabela:", ["pokemons", "trainers", "trainers_pokemons", "regions"])
    data = None
    
    info = table_info[table]
    campos_selecionados = st.multiselect("Filtros:", info["columns"] + ["all"], default=["all"])
        
    search_term = st.text_input("Pesquisar por:")

    if st.button("Consultar"):
        # Construa a consulta com base nos campos selecionados
        query = construir_query(table, campos_selecionados, search_term)

        cursor.execute(query)
        data = cursor.fetchall()

        if data:
            st.subheader("Resultado da Consulta:")
            aux_dic = {'0': 'id'}
            for i, col in enumerate(campos_selecionados):
                aux_dic[i + 1] = col

            st.dataframe(data, column_config=aux_dic)
        else:
            st.subheader("Nenhum resultado encontrado.")

cursor.close()
conn.close()