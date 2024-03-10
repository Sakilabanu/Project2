from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver (ensure you have chromedriver installed and in PATH)
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Click on the "Forgot Password" link
forgot_password_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Forgot your password?"))
)
forgot_password_link.click()

# Wait for the Forgot Password page to load
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "securityAuthentication_userName"))
)

# Enter the username
username_input = driver.find_element_by_id("securityAuthentication_userName")
username_input.send_keys("your_username")

# Click on the "Reset Password" button
reset_password_button = driver.find_element_by_id("btnSearchValues")
reset_password_button.click()

# Wait for the success message
success_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='message success fadable']"))
)

# Verify the success message
assert "Reset Password link sent successfully" in success_message.text

# Close the browser session
driver.quit()