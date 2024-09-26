print("Server Opened")
print("Server Opened")
# i = 1
# while True :
#     i = i + 1    
#     print(i)
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# ติดตั้ง ChromeDriver อัตโนมัติ
chromedriver_autoinstaller.install()

# กำหนด Options สำหรับ Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # เปิดในโหมด headless
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# สร้าง Driver
driver = webdriver.Chrome(options=chrome_options)

# เปิด YouTube
driver.get("https://www.youtube.com")
print(driver.title)  # แสดงชื่อหน้าเว็บ

# รอ 5 วินาที
time.sleep(5)

# ปิด Driver
driver.quit()
