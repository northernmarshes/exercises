#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 2: Przekonwertuj string na obiekt datetime
# Napisz kod, który przekonwertuje podany string z datą na obiekt datetime Python.
from datetime import datetime

date_string = "Feb 25 2020 4:20PM"
czas = datetime.strptime(date_string,"%b %d %Y %I:%M%p")
print(czas)
# datetime.strptime(date_string, "")

# ----------- Future Tips: -----------
# przy formatowaniu pamiętamy o każdym znaku
# również ":"
