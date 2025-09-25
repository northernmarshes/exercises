-- Zadanie 19
-- Policz średnią cenę przedmiotów w każdej kategorii.

SELECT i.identifier, ic.identifier
from items i
join item_categories ic, on i.id = ic.id;

----------- Future Tips: -----------
