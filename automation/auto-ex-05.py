#!/usr/bin/env python3
# Zadanie 5: Licznik zadań
# Napisz test, który dodaje zadanie, a następnie sprawdza czy licznik zadań pokazuje "1 item left".

import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        """browser setup"""
        browser = await p.firefox.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.goto("https://demo.playwright.dev/todomvc/")
        """actions"""
        todo_input = page.locator("input.new-todo")
        await todo_input.click()
        await todo_input.fill("Moje pierwsze zadanie")
        await todo_input.press("Enter")
        print("Zadanie dodane!")
        count = page.locator("span.todo-count")
        await expect(count).to_contain_text("1 item left")
        await context.tracing.stop(path = 'ex05-logs.zip')
        await browser.close()
asyncio.run(main())

# ----------- Future Tips: -----------
