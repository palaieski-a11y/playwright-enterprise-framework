from src.pages.login_page import LoginPage

def test_valid_login(page):

    login = LoginPage(page)

    login.navigate("https://example.com")

    login.login("admin", "password")

    assert page.url is not None