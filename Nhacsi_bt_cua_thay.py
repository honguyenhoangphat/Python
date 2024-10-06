from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re


######################################################
# I. Tạo nơi chứa links và tạo dataframe rỗng
all_links = []
d = pd.DataFrame({'Name of the band': [], 'Years active': []})
######################################################
# II. Lấy ra tất cả các đường dẫn để truy cập
# Khởi tạo Webdriver
url = "https://en.wikipedia.org/wiki/Lists_of_musicians"
driver = webdriver.Chrome()
# Mở trang
driver.get(url)
# Đợi  để trang tải
time.sleep(0.5)
try:

    # Lấy ra tất cả ul
    ul_tags = driver.find_elements(By.TAG_NAME, "ul")
    #print(len(ul_tags))

    # Chọn thẻ ul thứ 21
    ul_music = ul_tags[21]  # list start with index=0

    # Lấy tất cả các thẻ <li>
    li_tags = ul_music.find_elements(By.TAG_NAME, "li")

    # Tao danh sach cac url
    links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
    for x in links:
        print(x)
except:
    print("Error!")

######################################################
# III. Lay thong tin tung nhac si
urll = driver.get(links[0])
ull_tags = driver.find_elements(By.TAG_NAME, "ul")
print(len(ul_tags))

ul_band = ull_tags[26]
lii_tags = ul_band.find_elements(By.TAG_NAME, "li")
band_links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in lii_tags]
for s in band_links:
    print(s)
    driver.get(s)
    time.sleep(1)
    try:
        band_name = driver.find_element(By.TAG_NAME, "h1").text
    except:
        band_name = ""
    try:
        years_active = driver.find_element(By.XPATH, "//th[span[text()='Years active']]/following-sibling::td]")
        years_active = years_active.text
    except:
        years_active = ""
        # Tao dictionary thong tin cua hoa si
    musicians = ({'Name of the band': band_name, 'Years active': years_active})

        # CHuyen doi dictionary thanh DataFrame
    musicians_df = pd.DataFrame([musicians])

        # Them thong tin vao DF chinh
    d = pd.concat([d, musicians_df], ignore_index=True)



####################
# IV. In thong tin
print(d)
file_name = 'Musicians.xlsx'

# saving the Excel
d.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')

driver.quit()