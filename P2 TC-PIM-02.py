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

# Validate the title of the Admin page
assert "OrangeHRM" == driver.title, "Title validation failed for Admin page"

# Validate the presence of options on the Admin page
admin_options = [
    "User Management",
    "Job",
    "Organization",
    "Qualifications",
    "Nationalities",
    "Corporate Banking",
    "Configuration"
]

for option in admin_options:
    assert driver.find_element_by_link_text(option).is_displayed(), f"Option '{option}' not found on Admin page"

# Close the browser session
driver.quit()