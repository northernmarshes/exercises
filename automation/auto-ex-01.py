#!/usr/bin/env python3
# Zadanie 1: Instalacja i pierwszy test
# Zainstaluj Playwright i pytest, a następnie napisz najprostszy test, który otwiera stronę [[https://demo.playwright.dev/todomvc/]] i sprawdza czy tytuł zawiera słowo "TodoMVC".

import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto ("https://demo.playwright.dev/todomvc/")
        print(await page.title())
        await expect(page).to_have_title("TodoMVC")
        await browser.close()

asyncio.run(main())

# ----------- Future Tips: -----------
# Rozwiązanie synchroniczne
# import pytest
# from playwright.sync_api import Page, expect
#
# def test_page_title(page: Page):
#     page.goto("https://demo.playwright.dev/todomvc/")
#     expect(page).to_have_title("TodoMVC")
