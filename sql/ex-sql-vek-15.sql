-- Zadanie 15
-- Wyświetl wszystkie Pokemony z ich podstawowymi statystykami HP.

SELECT p.identifier, s.identifier, ps.base_stat
from pokemon p
join pokemon_stats ps on p.id = ps.pokemon_id
join stats s on ps.stat_id = s.id
where s.identifier = 'hp';
