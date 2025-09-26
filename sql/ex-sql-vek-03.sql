-- Zadanie 3
-- Wyświetl 10 najcięższych Pokemonów.
-- *Tabela*: pokemon

SELECT identifier, weight
FROM pokemon
ORDER BY weight DESC
LIMIT 10;

----------- Future Tips: -----------
