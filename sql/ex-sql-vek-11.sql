-- Zadanie 11
-- Wyświetl wszystkie Pokemony wraz z ich typami.
-- *Tabele*: pokemon, pokemon_types, types

select p.identifier, t.identifier
from pokemon p
join pokemon_types pt on p.id = pt.pokemon_id
join types t on pt.type_id = t.id;

----------- Future Tips: -----------
