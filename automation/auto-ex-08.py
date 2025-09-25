#!/usr/bin/env python3
# Zadanie 8: Test responsywności
# Napisz test, który sprawdza responsywność - otwiera stronę w różnych rozmiarach okna (desktop, tablet, mobile).

import asyncio
from playwright.async_api import async_playwright, Playwright, expect

async def main():
    async with async_playwright() as p:
        """browser setup"""
        browser = await p.firefox.launch(headless=False)
        context = await browser.new_context()
        context.set_default_navigation_timeout(10000)
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 360, "height": 800}) # mobile
        await page.goto("https://demo.playwright.dev/todomvc/")
        await page.set_viewport_size({"width": 1024, "height": 768}) # table
        await page.goto("https://demo.playwright.dev/todomvc/")
        await page.set_viewport_size({"width": 1920, "height": 1080}) # desktop
        await page.goto("https://demo.playwright.dev/todomvc/")
        """actions"""
        await context.tracing.stop(path = "ex08-logs.zip")
        await browser.close()
asyncio.run(main())

# ----------- Future Tips: -----------
# użyć fixtures, assetrions oraz parametryzacji
