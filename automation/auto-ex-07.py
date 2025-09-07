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
        input_window = page.get_by_role("textbox", name="What needs to be done?")
        await input_window.click()
        await input_window.fill("zadanie do usunięcia")
        await input_window.press("Enter")
        delete_button = page.get_by_role("button", name="Delete")
        task =  page.get_by_test_id("todo-title")
        await task.hover()
        await delete_button.click()
        """check for success"""
        task_list = page.locator(".todo-list li")
        await expect(task_list).to_have_count(0)
        await context.tracing.stop(path = "ex07-logs.zip")
        await browser.close()
asyncio.run(main())
