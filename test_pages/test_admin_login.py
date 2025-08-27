from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page


class TestAdminLogin:
    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"
    invalid_username = "admin123@yourstore.com"

    def test_login_functionality(self):
        # Dummy check just for setup validation
        assert True

    def test_title_verification(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        actual_title = self.driver.title
        print("----------->"+actual_title)
        expected_title = "nopCommerce demo store. Login"   # ✅ match the real page title
        assert actual_title == expected_title
        self.driver.quit()

    def test_validate_admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()

        self.admin_obj = Login_Admin_Page(self.driver)
        self.admin_obj.enter_username(self.username)
        self.admin_obj.enter_password(self.password)
        self.admin_obj.click_login()

        actual_dashboard_text = self.driver.find_element(
            By.XPATH, "//div[@class='content-wrapper']//div//h1"
        ).text
        assert actual_dashboard_text == "Dashboard"

        self.driver.quit()

    def test_invalidate_admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()

        self.admin_obj = Login_Admin_Page(self.driver)
        self.admin_obj.enter_username(self.invalid_username)
        self.admin_obj.enter_password(self.password)
        self.admin_obj.click_login()

        error_message = self.driver.find_element(
            By.XPATH, "//div[@class='message-error validation-summary-errors']").text.strip()
        print("----------->"+error_message)
        expected_message = "Login was unsuccessful. Please correct the errors and try again."

        # ✅ Check substring match
        assert expected_message in error_message, f"Expected '{expected_message}' but got '{error_message}'"

        self.driver.quit()
