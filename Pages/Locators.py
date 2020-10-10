class login_page():
    txt_username = "session[username_or_email]"  #name
    txt_password = "session[password]"
    btn_submit = "[data-testid='LoginForm_Login_Button']"     #css


class dashboard():
    txt_search = "[data-testid='SearchBox_Search_Input']"
    first_element = "//div[@role='option']"
    name = "//span[contains(.,'@reliancegroup')]"     #classname
    link_following = "//body/div[@id='react-root']/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/a[1]"
    following_list = "//div[@class='css-1dbjc4n']//div[@data-testid='UserCell']//a[1]"


class log_out():
    user = "//span[contains(.,'@Shankar88463029')]"
    logout = "[data-testid='AccountSwitcher_Logout_Button']"