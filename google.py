import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Bicky007\\Downloads\\chromedriver.exe")

driver.get("https://google.com")


# for 10 different search queries
@pytest.mark.parametrize("search_query",
                         ["selenium", "python", "java", "c++", "c#", "javascript", "ruby", "php", "c", "go"])

def test_search_results(search_query, num_results=10):
    # open google.com
    driver = webdriver.Chrome()
    driver.get(url)
    # enter search query
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    # check if search results are greater than 10
    search_results = driver.find_elements_by_class_name("g")
    assertlen(search_results) >= 10, "Search results are less than 10"
    driver.close()


url2 = "https://www.youtube.com/"


# test youtube for 5 different search queries
@pytest.mark.parametrize("search_query", ["selenium", "python", "java", "c++", "c#"])
def test_youtube_search_results(search_query, num_results=5):
    # open google.com
    driver = webdriver.Chrome()
    driver.get(url)
    # enter search query
    search_box = driver.find_element_by_name("search_query")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    # check if search results are greater than 10
    search_results = driver.find_elements_by_class_name("yt-lockup-video")
    assertlen(search_results) >= 10, "Search results are less than 5"
    driver.close()
