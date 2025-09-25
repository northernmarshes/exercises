#!/usr/bin/env python3
# Zadanie 10: Filtry zadań
# Napisz test, który dodaje kilka zadań, oznacza niektóre jako wykonane i sprawdza filtry "All", "Active", "Completed".

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("viewport",[
    {"width": 1920, "height": 1080}
])
def test_filters(page:Page, viewport):
    """sprawdza filtry all, active i completed"""
    page.set_viewport_size(viewport)
    page.goto("https://demo.playwright.dev/todomvc/")

    # zadania
    input_field = page.get_by_placeholder("What needs to be done?")
    tasks = ["task 1", "task 2", "task 3", "task 4", "task 5"]

    for task in tasks:
        input_field.click()
        input_field.fill(task)
        input_field.press("Enter")

    page.get_by_role("checkbox", name="Toggle Todo").nth(1).check()
    page.get_by_role("checkbox", name="Toggle Todo").nth(3).check()

    # sprawdzanie filtrów

    task_list = page.locator(".todo-list li")

    page.get_by_role("link", name="All").click()
    expect(task_list).to_have_count(len(tasks))

    page.get_by_role("link", name="Completed").click()
    expect(task_list).to_have_count(len(tasks) - 3)

    page.get_by_role("link", name="Active").click()
    expect(task_list).to_have_count(len(tasks) - 2)

# ----------- Future Tips: -----------
# nazwa funkcji musi zaczynać się od "test_" !!!
# poza tym good job >;)
