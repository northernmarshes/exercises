-- Zadanie 18
-- Znajdź wszystkie Pokemony, które mogą ewoluować (mają evolves_from_species_id).

SELECT *
FROM pokemon_species ps
WHERE evolves_from_species_id > 0;

----------- Future Tips: -----------
-- lepiej napisać IS NOT NULL
