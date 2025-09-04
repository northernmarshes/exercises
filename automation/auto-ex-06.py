#!/usr/bin/env python3
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
        await todo_input.fill("Moje zadanko")
        await todo_input.press("Enter")
        checkbox = page.get_by_role("checkbox")
        await checkbox.click()
        await expect(checkbox).to_have_class("completed")
        await context.tracing.stop(path = 'ex06-logs.zip')
        await browser.close()
asyncio.run(main())
