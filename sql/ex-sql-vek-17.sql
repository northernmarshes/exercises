-- Zadanie 17
-- Wyświetl wszystkie ruchy wraz z ich typami.

SELECT m.identifier , t.identifier
from moves m
join types t on m.type_id = t.id;

----------- Future Tips: -----------
-- to byłoby actually przydatne w grze xd
-- trzeba pamiętać o dodawaniu etykiet
-- poprzez AS
