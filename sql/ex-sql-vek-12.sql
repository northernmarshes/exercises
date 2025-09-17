-- Zadanie 12
-- Znajdź wszystkie Pokemony typu "fire".

select p.identifier, t.identifier
from pokemon p
join pokemon_types pt on p.id = pt.pokemon_id
join types t on pt.type_id = t.id
WHERE t.identifier = "fire";
