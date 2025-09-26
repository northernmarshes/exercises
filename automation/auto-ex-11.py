#!/usr/bin/env python3
# -----task-source:-ai-generated------
# Zadanie 11: Clear completed
# Napisz test, który sprawdza funkcję "Clear completed" - dodaj zadania, oznacz niektóre jako wykonane, kliknij "Clear completed".

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("viewport",[
    {"width": 1920, "height": 1080}
])
def test_clear_completed(page: Page, viewport):
    """sprawdza funkcję clear completed"""
    page.set_viewport_size(viewport)
    page.goto("https://demo.playwright.dev/todomvc/")

    # zadania
    input_field = page.get_by_placeholder("What needs to be done?")
    tasks = ["task 1", "task 2", "task 3", "task 4"]
    for task in tasks:
        input_field.fill(task)
        input_field.press("Enter")
        page.get_by_role("listitem").filter(has_text=task).get_by_label("Toggle Todo").check()
    page.get_by_role("button", name="Clear completed").click()
    task_list = page.locator(".todo-list li")
    expect(task_list).to_have_count(0)

# ----------- Future Tips: -----------
# Lepiej byłoby zostawić jakieś zadanie tak, by
# móc stwierdzić czy przycisk usuwa dokładnie to
# co chcemy.
# Można też sprawdzić czy przycisk poprawnie pojawia
# się dopiero po dodaniu pierwszego zadania.
