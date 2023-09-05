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

def create():
    create = '''
            CREATE TABLE IF NOT EXISTS pokemons (
        pokedex_number INT PRIMARY KEY,
        nome VARCHAR(255),
        color VARCHAR(50),
        attack INT,
        defense INT,
        hp INT,
        speed INT,
        tipo VARCHAR(50),
        height FLOAT,
        weight FLOAT,
        rarity VARCHAR(50),
        evolve bool,
        region_id INT
        );

        CREATE TABLE IF NOT EXISTS trainers (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(255),
        email VARCHAR(255) unique
        );

        CREATE TABLE IF NOT EXISTS trainers_pokemons (
        id INT PRIMARY KEY AUTO_INCREMENT,
        trainer_id INT,
        pokedex_number INT
        );

        CREATE TABLE IF NOT EXISTS regions (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(255),
        descricao TEXT,
        location VARCHAR(255)
        );
            '''
    cursor.execute(create)
    # se editar o banco de dados
    conn.commit()
    
create()





