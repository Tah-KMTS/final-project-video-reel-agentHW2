"""Screenshots each HTML slide to a PNG, for stitching into video."""

import os

from playwright.sync_api import sync_playwright


def screenshot_all(html_paths: list[str], width: int = 1280, height: int = 720) -> list[str]:
    png_paths = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height})
        for html_path in html_paths:
            png_path = html_path.rsplit(".", 1)[0] + ".png"
            page.goto("file://" + os.path.abspath(html_path))
            page.screenshot(path=png_path)
            png_paths.append(png_path)
        browser.close()
    return png_paths
