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
        await expect(todo_input).to_have_attribute("placeholder", "What needs to be done?")
        await context.tracing.stop(path = 'ex02_logs.zip')
        await browser.close()

asyncio.run(main())
