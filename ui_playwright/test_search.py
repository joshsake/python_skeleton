from pageobjects.search import SearchPage

# test file - you still want page objects so that your test(s) can easily call them
# also your page objects are responsible for the selectors while tests are for actual validation
page = await browser.new_page()
search_page = SearchPage(page)
await search_page.navigate()
await search_page.search("search query")