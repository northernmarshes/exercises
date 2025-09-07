#!/usr/bin/env python3
import asyncio
from playwright.async_api import async_playwright, Playwright, expect

async def main():
    async with async_playwright() as p:
        """browser setup"""
        browser = await p.firefox.launch(headless=False)
        iphone = p.devices['iPhone 12']
        context = await browser.new_context(**iphone)
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new.page()

        await page.goto("https://demo.playwright.dev/todomvc/")
        """actions"""
        await browser.close()
asyncio.run(main())
