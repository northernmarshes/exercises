# #!/usr/bin/env python3
# ----task-source:-ai-generated-----
# Zadanie 12: Edycja zadania
# Napisz test, który sprawdza edycję zadania - dodaj zadanie, kliknij dwukrotnie na nie, zmień tekst i zatwierdź.

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("viewport",[
    {"width": 1920, "height": 1080}
                                   ])
def test_task_edition(page: Page, viewport):
    """sprawdza edycję zadania"""
    page.set_viewport_size(viewport)
    page.goto("https://demo.playwright.dev/todomvc/")

    # zadania
    input_field = page.get_by_placeholder("What needs to be done?")
    input_field.fill("zrób pranie")
    input_field.press("Enter")
    expect(page.get_by_test_id("todo-title")).to_contain_text("zrób pranie")
    page.get_by_test_id("todo-title").dblclick()
    page.get_by_role("textbox", name="Edit").fill("zrób czarne pranie")
    page.get_by_role("textbox", name="Edit").press("Enter")
    expect(page.get_by_test_id("todo-title")).to_contain_text("zrób czarne pranie")

# ----------- Future Tips: -----------
# Sprawdzanie stanu też przed edycją,
# oraz czy stary tekst zniknął.
# Poza tym okej :>
