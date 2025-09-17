-- Zadanie 14
-- Znajdź wszystkie Pokemony wraz z ich zdolnościami (abilities).

select p.identifier, a.identifier
from pokemon p
join pokemon_abilities pa on p.id = pa.pokemon_id
join abilities a on pa.ability_id = a.id;
