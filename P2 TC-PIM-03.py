from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver (ensure you have chromedriver installed and in PATH)
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://opensource-demo.orangehrmlive.com/")
# Login as "Admin" (assuming username and password are known)
driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

# Wait for the Admin link to appear in the menu and click on it
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "menu_admin_viewAdminModule"))
).click()

# Validate the presence of menu options on the Admin page
admin_menu_options = [
    "Admin",
    "PIM",
    "Leave",
    "Time",
    "Recruitment",
    "My Info",
    "Performance",
    "Dashboard",
    "Directory",
    "Maintenance",
    "Buzz"
]

for option in admin_menu_options:
    assert driver.find_element_by_id(f"menu_{option}").is_displayed(), f"Menu option '{option}' not found on Admin page"

# Close the browser session
driver.quit()