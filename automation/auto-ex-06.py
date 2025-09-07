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
        todo_input = page.get_by_placeholder("What needs to be done?")
        await todo_input.click()
        await todo_input.fill("Moje zadanko")
        await todo_input.press("Enter")
        checkbox = page.locator(".todo-list li").first.locator("input[type=checkbox]")
        await checkbox.click()
        task_item = page.locator(".todo-list li").first
        await expect(task_item).to_have_class("completed")
        await context.tracing.stop(path = 'ex06-logs.zip')
        await browser.close()
asyncio.run(main())
