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



# def popular():
#     try:
#         insert_pokemons = '''
#         INSERT INTO pokemons (pokedex_number, nome, color, attack, defense, hp, speed, tipo, height, weight, rarity, evolve, region_id)
#                 VALUES
#                 (4, 'Charmander', 'Red', 52, 43, 39, 65, 'Fire', 0.6, 8.5, 'Common', TRUE, 1),
#                 (7, 'Squirtle', 'Blue', 48, 65, 44, 43, 'Water', 0.5, 9.0, 'Common', TRUE, 1),
#                 (152, 'Chikorita', 'Green', 49, 65, 45, 45, 'Grass', 0.9, 6.4, 'Common', TRUE, 2),
#                 (155, 'Cyndaquil', 'Yellow', 52, 43, 39, 65, 'Fire', 0.5, 7.9, 'Common', TRUE, 2),
#                 (158, 'Totodile', 'Blue', 48, 65, 50, 43, 'Water', 0.6, 9.5, 'Common', TRUE, 2),
#                 (252, 'Treecko', 'Green', 45, 35, 40, 70, 'Grass', 0.5, 5.0, 'Common',TRUE, 3),
#                 (255, 'Torchic', 'Red', 60, 40, 45, 45, 'Fire', 0.4, 2.5, 'Common', TRUE, 3),
#                 (258, 'Mudkip', 'Blue', 70, 50, 50, 40, 'Water', 0.4, 7.6, 'Common', TRUE, 3),
#                 (387, 'Turtwig', 'Green', 68, 64, 55, 31, 'Grass', 0.4, 10.2, 'Common', TRUE, 4),
#                 (390, 'Chimchar', 'Brown', 58, 44, 44, 61, 'Fire', 0.5, 6.2, 'Common', TRUE, 4),
#                 (393, 'Piplup', 'Blue', 51, 53, 53, 40, 'Water', 0.4, 5.2, 'Common', TRUE, 4);
#         '''

#         insert_trainers = '''
#                 INSERT INTO trainers (nome, email)
#                 VALUES
#                 ('Ash Ketchum', 'ash@example.com'),
#                 ('Misty', 'misty@example.com'),
#                 ('Brock', 'brock@example.com'),
#                 ('May', 'may@example.com'),
#                 ('Gary Oak', 'gary@example.com');

                
#         '''

#         insert_pokemon_trainers = '''
#             INSERT INTO trainers_pokemons (trainer_id, pokedex_number)
#             VALUES
#             (1, 1),
#             (1, 4),
#             (2, 7),
#             (3, 155),
#             (4, 255),
#             (5, 387);
#         '''
#         insert_regions = '''
#             INSERT INTO regions (nome, descricao, location)
#             VALUES
#             ('Kanto', 'A primeira região introduzida na série Pokémon.', 'Japan'),
#             ('Johto', 'Uma região próxima a Kanto, com uma nova aventura.', 'Japan'),
#             ('Hoenn', 'Conhecida por suas rotas aquáticas e clima diversificado.', 'Japan'),
#             ('Sinnoh', 'Uma região rica em história e lendas de Pokémon.', 'Japan');
#         '''
        

#         cursor.execute(insert_pokemons)
#         conn.commit()
#         cursor.execute(insert_trainers)
#         conn.commit()
#         cursor.execute(insert_pokemon_trainers)
#         conn.commit()
#         cursor.execute(insert_regions)
#         conn.commit()
#     except ValueError:
#         st.text("Algo deu errado!")
        
# if st.button("Popular"):
#     popular()



def popularPokemons(pokedex_number, nome, color, attack, defense, hp, speed, tipo, height, weight, rarity, evolve, region_id):
    
    insert_pokemons = f'''
        INSERT INTO pokemons (pokedex_number, nome, color, attack, defense, hp, speed, tipo, height, weight, rarity, evolve, region_id)
                VALUES
                ({pokedex_number}, '{nome}', '{color}', {attack}, {defense}, {hp}, {speed}, '{tipo}', {height}, {weight}, '{rarity}', {evolve}, {region_id});
                
        '''
    
    cursor.execute(insert_pokemons)
    conn.commit()

def popularTrainers(nome_treinador,email):  
    insert_trainers = f'''
    INSERT INTO trainers(nome,email)
    VALUES('{nome_treinador}','{email}')
    '''
    cursor.execute(insert_trainers)
    conn.commit()
def popularRegiao(nome, descricao, location):
    insert_regiao = f'''
    INSERT INTO regions(nome, descricao, location)
    VALUES('{nome}', '{descricao}', '{location}')
    '''
    cursor.execute(insert_regiao)
    conn.commit()

    
opcoes = ["Pokemons", "trainers", "regions"]

escolha = st.selectbox("Selecione uma opção:", opcoes)
if escolha == "Pokemons":
    st.title("Formulário Streamlit")

    # Adicione um campo de entrada de texto para o nome
    nome = st.text_input("nome")
    pokedex_number = st.text_input("pokedex_number")
    color = st.text_input("color")
    attack = st.text_input("attack")
    defense = st.text_input("defense")
    hp = st.text_input("hp")
    speed = st.text_input("speed")
    tipo = st.text_input("tipo")
    height = st.text_input("height")
    weight = st.text_input("weight")
    rarity = st.text_input("rarity")
    evolve = st.text_input("evolve")
    region_id = st.text_input("region_id")
    if st.button("Enviar"):
        popularPokemons(pokedex_number, nome, color, attack, defense, hp, speed, tipo, height, weight, rarity, evolve, region_id)
  
if escolha == "trainers":
    nome_treinador = st.text_input("nome_treinador")
    email = st.text_input("email")
    # Adicione um botão de envio
    if st.button("Enviar"):
        popularTrainers(nome_treinador,email)

if escolha == "regions":
    nome_regiao = st.text_input("nome_regiao")
    descricao = st.text_input("descricao")
    location = st.text_input("location")
    if st.button("Enviar"):
        popularRegiao(nome_regiao, descricao, location)
