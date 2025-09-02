#!/usr/bin/env python3
import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.goto("https://demo.playwright.dev/todomvc/")
        todo_input = page.locator("input.new-todo")
        await todo_input.click()
        await todo_input.fill("Moje pierwsze zadanie")
        await expect(todo_input).to_have_value("Moje pierwsze zadanie")
        await context.tracing.stop(path = 'ex03-logs.zip')
        await browser.close()

asyncio.run(main())
