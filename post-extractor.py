from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os

linkedin_username = "***"
linkedin_password = "***"
profile_name = "***"
profile_url = f'https://www.linkedin.com/in/{profile_name}/recent-activity/all/'
number_of_scroll = 1000  # number of post to extract
number_of_page_to_scroll = int(number_of_scroll / 20)  # 20 post per page
scroll_pause_time = 2
output_folder = "output"
chrome_options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


def login():
    login_url = "https://www.linkedin.com/login"
    driver.get(login_url)
    time.sleep(2)
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username.send_keys(linkedin_username)
    password.send_keys(linkedin_password)
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print('LogedIn')


def get_image_type(response):
    content_type = response.headers.get('Content-Type')
    if content_type:
        if 'image' in content_type:
            return content_type.split('/')[-1]
    return 'png'


def save_image(image_url, folder_path, image_name):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(os.path.join(folder_path, f'{image_name}.{get_image_type(response)}'), 'wb') as file:
            file.write(response.content)


def save_description(description, folder_path, file_name):
    with open(os.path.join(folder_path, file_name), 'w') as file:
        file.write(description)


def extract_iframe_content(iframe):
    driver.switch_to.frame(iframe)
    iframe_html = driver.page_source
    driver.switch_to.default_content()
    return iframe_html


def smooth_scroll():
    driver.execute_script("return window.scrollTo(0, 0);")
    last_height = 0
    current_scroll = 0

    while True:
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.documentElement.scrollTop")
        if new_height == last_height or current_scroll > number_of_scroll:
            break
        last_height = new_height
        current_scroll += 1


def extract_post():
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    posts = soup.find_all('li', class_='profile-creator-shared-feed-update__container')
    iframe_count = 0
    for i, post in enumerate(posts):
        description = post.find('span', class_='break-words tvm-parent-container').text
        save_description(description, output_folder, f'{i}_description.txt')
        image_tag = post.find('img',
                              class_='ivm-view-attr__img--centered ivm-view-attr__img--aspect-fill update-components-image__image evi-image lazy-image ember-view')
        image_url = image_tag['src'] if image_tag else None
        if image_url:
            save_image(image_url, output_folder, f'{i}_img.png')
        else:
            iframe = post.find('iframe')
            if iframe:
                iframe_content = BeautifulSoup(extract_iframe_content(iframe_count), 'html.parser')
                iframe_count += 1
                lis = iframe_content.find_all('li', class_='carousel-slide')
                for i_2, li in enumerate(lis):
                    img = li.find('img')
                    if img:
                        if 'src' in img.attrs.keys():
                            img_url = img['src'] if img else None
                            save_image(img_url, output_folder, f'{i}_{i_2}_img')
                        elif 'data-src' in img.attrs.keys():
                            img_url = img['data-src'] if img else None
                            save_image(img_url, output_folder, f'{i}_{i_2}_img')


def show_more():
    try:
        show_more_button = driver.find_element(By.XPATH,
                                               "//button[contains(@class, 'scaffold-finite-scroll__load-button')]")
        show_more_button.click()
        time.sleep(3)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    try:
        os.makedirs(output_folder, exist_ok=True)
        login()
        driver.get(profile_url)
        for i in range(0, number_of_page_to_scroll):
            show_more()
            time.sleep(2)
        smooth_scroll()
        extract_post()
    except Exception as e:
        print(e)
