drop database if exists pokecode;
CREATE DATABASE pokecode;
USE pokecode;

CREATE TABLE pokemons (
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

CREATE TABLE trainers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    email VARCHAR(255) unique
);

CREATE TABLE trainers_pokemons (
    id INT PRIMARY KEY AUTO_INCREMENT,
    trainer_id INT,
    pokedex_number INT
);

CREATE TABLE regions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    descricao TEXT,
    location VARCHAR(255)
);

INSERT INTO regions (nome, descricao, location)
VALUES
    ('Kanto', 'A primeira região introduzida na série Pokémon.', 'Japan'),
    ('Johto', 'Uma região próxima a Kanto, com uma nova aventura.', 'Japan'),
    ('Hoenn', 'Conhecida por suas rotas aquáticas e clima diversificado.', 'Japan'),
    ('Sinnoh', 'Uma região rica em história e lendas de Pokémon.', 'Japan');

INSERT INTO pokemons (pokedex_number, nome, color, attack, defense, hp, speed, tipo, height, weight, rarity, evolve, region_id)
VALUES
    (1, 'Bulbasaur', 'Green', 49, 49, 45, 45, 'Grass', 0.7, 6.9, 'Common', TRUE, 1),
    (4, 'Charmander', 'Red', 52, 43, 39, 65, 'Fire', 0.6, 8.5, 'Common', TRUE, 1),
    (7, 'Squirtle', 'Blue', 48, 65, 44, 43, 'Water', 0.5, 9.0, 'Common', TRUE, 1),
    (152, 'Chikorita', 'Green', 49, 65, 45, 45, 'Grass', 0.9, 6.4, 'Common', TRUE, 2),
    (155, 'Cyndaquil', 'Yellow', 52, 43, 39, 65, 'Fire', 0.5, 7.9, 'Common', TRUE, 2),
    (158, 'Totodile', 'Blue', 48, 65, 50, 43, 'Water', 0.6, 9.5, 'Common', TRUE, 2),
    (252, 'Treecko', 'Green', 45, 35, 40, 70, 'Grass', 0.5, 5.0, 'Common',TRUE, 3),
    (255, 'Torchic', 'Red', 60, 40, 45, 45, 'Fire', 0.4, 2.5, 'Common', TRUE, 3),
    (258, 'Mudkip', 'Blue', 70, 50, 50, 40, 'Water', 0.4, 7.6, 'Common', TRUE, 3),
    (387, 'Turtwig', 'Green', 68, 64, 55, 31, 'Grass', 0.4, 10.2, 'Common', TRUE, 4),
    (390, 'Chimchar', 'Brown', 58, 44, 44, 61, 'Fire', 0.5, 6.2, 'Common', TRUE, 4),
    (393, 'Piplup', 'Blue', 51, 53, 53, 40, 'Water', 0.4, 5.2, 'Common', TRUE, 4);

INSERT INTO trainers (nome, email)
VALUES
    ('Ash Ketchum', 'ash@example.com'),
    ('Misty', 'misty@example.com'),
    ('Brock', 'brock@example.com'),
    ('May', 'may@example.com'),
    ('Gary Oak', 'gary@example.com');

INSERT INTO trainers_pokemons (trainer_id, pokedex_number)
VALUES
    (1, 1),
    (1, 4),
    (2, 7),
    (3, 155),
    (4, 255),
    (5, 387);

ALTER TABLE pokemons ADD FOREIGN KEY (region_id) REFERENCES regions(id) ON delete cascade;
ALTER TABLE trainers_pokemons ADD FOREIGN KEY (trainer_id) REFERENCES trainers(id) ON delete cascade;
ALTER TABLE trainers_pokemons ADD FOREIGN KEY (pokedex_number) REFERENCES pokemons(pokedex_number) ON delete cascade;

