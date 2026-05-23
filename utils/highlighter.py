def highlight(page, locator):
    element = page.locator(locator)

    element.evaluate("""
    element => {
        element.style.border = '3px solid red';
        element.style.backgroundColor = 'yellow';
    }
    """)