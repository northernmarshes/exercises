#!/usr/bin/env python3
# Zadanie 9: Dodawanie wielu zadań
# Napisz test, który dodaje 5 różnych zadań i sprawdza czy wszystkie są widoczne na liście.

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("viewport",[
    {"width": 1920, "height": 1080}
])
def test_5_tasks(page: Page, viewport):
    """dodaje 5 zadań i sprawdza czy są na liście"""
    page.set_viewport_size(viewport)
    page.goto("https://demo.playwright.dev/todomvc/")

    # interakcja
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("Posprzątać taras")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("Pozmywać naczynia")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("Pojechać po zakupy")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("Poczytać książkę")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("Dobrze się bawić")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")

    # asercje
    expect(page.get_by_test_id("todo-title")).to_contain_text([
        "taras",
        "naczynia",
        "zakupy",
        "książkę",
        "bawić"
    ])
    expect(page.locator(".todo-list li")).to_have_count(5)


# ----------- Future Tips: -----------
# jeśli jest wiele etykiet pod jednym placeholderem sprawdzamy je zbiorczo
# inaczej pytest przerwie test na wszelki wypadek by zapobiec niejednoznaczności
#
# asercje również generujemy w playwright codegen
#
# zadania możemu dodawać za pomocą pętli for dla zachowania DRY:
#
#+BEGIN_SRC python
# def test_add_multiple_tasks(page: Page):
#     page.goto("https://demo.playwright.dev/todomvc/")

#     tasks = ["Zadanie 1", "Zadanie 2", "Zadanie 3", "Zadanie 4", "Zadanie 5"]
#     input_field = page.get_by_placeholder("What needs to be done?")

#     # Dodaj wszystkie zadania
#     for task in tasks:
#         input_field.fill(task)
#         input_field.press("Enter")

#     # Sprawdź czy wszystkie są widoczne
#     task_list = page.locator(".todo-list li")
#     expect(task_list).to_have_count(len(tasks))

#     # Sprawdź czy każde zadanie istnieje
#     for task in tasks:
#         expect(page.locator(".todo-list")).to_contain_text(task)
#+END_SRC
#
# albo
#
#+BEGIN_SRC python
# import pytest
# from playwright.sync_api import Page, expect

# @pytest.mark.parametrize("viewport", [
#     {"width": 1920, "height": 1080}
# ])
# def test_add_multiple_tasks(page: Page, viewport):
#     """Dodaje 5 zadań i sprawdza czy są na liście"""
#     page.set_viewport_size(viewport)
#     page.goto("https://demo.playwright.dev/todomvc/")

#     # lista zadań do dodania
#     tasks = [
#         "Posprzątać taras",
#         "Pozmywać naczynia",
#         "Pojechać po zakupy",
#         "Poczytać książkę",
#         "Dobrze się bawić"
#     ]

#     # pole tekstowe
#     input_box = page.get_by_role("textbox", name="What needs to be done?")

#     # dodawanie w pętli
#     for task in tasks:
#         input_box.fill(task)
#         input_box.press("Enter")

#     # asercje
#     task_list = page.locator(".todo-list li")
#     expect(task_list).to_have_count(len(tasks))  # sprawdzamy ilość

#     for task in tasks:  # sprawdzamy każdy tekst
#         expect(page.locator(".todo-list")).to_contain_text(task)
#+END_SRC
