-- Zadanie 16
-- Znajdź 5 Pokemonów z najwyższym bazowym doświadczeniem.

SELECT identifier, base_experience
FROM pokemon
ORDER BY base_experience
LIMIT 5;

----------- Future Tips: -----------
-- powinno być DESC w sortowaniu, inaczej
-- wyświetla wyniki od najniższych
