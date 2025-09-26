-- Zadanie 8
-- Znajdź wszystkie przedmioty (items) kosztujące więcej niż 10000.
-- *Tabela*: items

select identifier, cost
from items
where cost > 10000;

----------- Future Tips: -----------
-- najdroższy przedmiot kosztuje
-- 10000 dlatego wynik to 0
