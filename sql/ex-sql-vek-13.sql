-- Zadanie 13
-- Policz ile Pokemonów ma każdy typ.

SELECT
	t.identifier,
	count(*) as pokemon_count
from pokemon_types pt
join types t on pt.type_id = t.id
group by t.identifier;
