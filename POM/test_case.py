import Login_page,Home_page

def test_script(setup):
    drivers=setup
    L=Login_page.LOGIN(drivers)
    L.enter_username('student')
    L.enter_password('Password123')
    L.click_submit()

    H=Home_page.HOME(drivers)
    H.click_logout_button()