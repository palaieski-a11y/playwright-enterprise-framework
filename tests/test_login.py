from src.pages.login_page import LoginPage

def test_valid_login(page):

    login_html = """
    <html>
    <body>
        <input id="username" />
        <input id="password" type="password" />
        <button id="login">Login</button>
    </body>
    </html>
    """

    page.set_content(login_html)

    login = LoginPage(page)

    login.login("admin", "password")