#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 3: Odejmij tydzień od podanej daty
# Napisz kod, który odejmie tydzień (7 dni) od podanej daty.

from datetime import datetime, timedelta
given_date = datetime(2020, 2, 25)
new_date = given_date - timedelta(weeks=1)
print(new_date)

# ----------- Future Tips: -----------
# Okresy tworzymy za pomocą timedelta()
# Można było sformatować wynik tak samo
# jak input za pomocą strftime()
