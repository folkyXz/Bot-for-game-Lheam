import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import geckodriver_autoinstaller

# ติดตั้ง Geckodriver อัตโนมัติ
geckodriver_autoinstaller.install()

# สร้าง Driver สำหรับ Firefox
driver = webdriver.Firefox()

# เปิด YouTube
driver.get("https://www.youtube.com")
print(driver.title)  # แสดงชื่อหน้าเว็บ

# รอ 5 วินาที
time.sleep(5)

# ปิด Driver
driver.quit()
