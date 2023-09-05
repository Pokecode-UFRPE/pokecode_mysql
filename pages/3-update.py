import streamlit as st
import mysql.connector

conn = mysql.connector.connect(
    host="Localhost",
    user="root",
    password="123456",
    database="pokecode"
)
cursor = conn.cursor()

# funções
def update_email(email, trainer):
    if isinstance(trainer, int):
        sql_update = "UPDATE trainers SET email = %s WHERE id = %s"
    else:
        sql_update = "UPDATE trainers SET email = %s WHERE nome = %s"
    cursor.execute(sql_update, (email, trainer))
    conn.commit() 
    return "Email atualizado com sucesso"

def adicionar_coluna(nome_tabela, nome_coluna, tipo_dados):
    sql_column = f"ALTER TABLE {nome_tabela} ADD COLUMN {nome_coluna} {tipo_dados}"
    cursor.execute(sql_column) 
    conn.commit()   
    return "Coluna adicionada com sucesso"

def popular_coluna(nome_coluna):
    trainer_values = [(1,2), (2,1), (3,1), (4,1), (5,0)]
    if nome_coluna == "pokemon_count":
        for trainer_id, pokemon_count in trainer_values:
            sql_values = "UPDATE trainers SET pokemon_count = %s WHERE id = %s"
            cursor.execute(sql_values, (pokemon_count, trainer_id))
            conn.commit()
        return "Coluna populada com sucesso"
    else:
        return "Coluna não populada"

def adicionar_trigger():
    sql_trigger = """
    CREATE TRIGGER  update_count
    AFTER INSERT ON trainers_pokemons
    FOR EACH ROW
    BEGIN
        UPDATE trainers
        SET pokemon_count = pokemon_count + 1
        WHERE id = NEW.trainer_id;
    END;
    """
    cursor.execute(sql_trigger)
    conn.commit()
    return "Trigger adicionado com sucesso"

def adicionar_pokemon(trainer_id, pokedex_number):
    sql_insert = "INSERT INTO trainers_pokemons (trainer_id, pokedex_number) VALUES (%s, %s)"
    cursor.execute(sql_insert, (trainer_id, pokedex_number))
    conn.commit()
    return "Pokemon adicionado com sucesso"

# tela streamlit
st.title("Update e trigger")

with st.expander("atualizar email"):
    opcao = st.radio("Selecionar opção:", ("Nome", "ID"))
    if opcao == "Nome":
        trainer = st.text_input("Nome do treinador:")
    else:
        trainer = st.number_input("ID do treinador:", format = "%d", step = 1)
    email = st.text_input("Novo email:")

    if st.button("Atualizar email"):
        st.success(update_email(email, trainer))

with st.expander("Adicionar coluna"):
    nome_tabela = st.text_input("Nome da tabela a ser modificada:")
    nome_coluna = st.text_input("Nome da coluna:")
    tipo_dados = st.text_input("Tipo de dados:")

    if st.button("Adicionar coluna"):
        st.success(adicionar_coluna(nome_tabela, nome_coluna, tipo_dados))
        st.success(popular_coluna(nome_coluna))

with st.expander("Adicionar trigger"):
    if st.button("Adicionar trigger"):
        st.success(adicionar_trigger())

with st.expander("Adicionar pokémon a um treinador"):
    trainer_id = st.number_input("ID do Treinador:", format = "%d", step = 1)
    pokedex_number = st.number_input("Número da Pokedex do Pokémon:", format = "%d", step = 1)
    
    if st.button("Adicionar Pokémon"):
        st.success(adicionar_pokemon(trainer_id, pokedex_number))

cursor.close()
conn.close()
