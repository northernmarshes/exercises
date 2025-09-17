#!/usr/bin/env python3
import pytest
from playwright.sync_api import Page, expect

def test_5_tasks(page: Page):
    page.goto("https://example.com")
