from selenium import webdriver
from selenium.webdriver.common.by import By
import const


def get_movie_list(driver, url: str) -> list:
    """Scrap from Rotten Tomatoes top 100 movies of choosen genre

    Parameter: 

    driver: webdriver
    url: url of the top 100 movies from Rotten Tomatoes

    Retruns: list of top 100 movies of choosen genre and genre name at index 0"""

    driver.get(url)
    movie_list = []
    genre = driver.find_element(
        By.XPATH, '//*[@id="top_movies_main"]/div/div[2]/button').text
    movie_list.append(genre)
    # make sure that list len is 100
    top_hundred_list = driver.find_elements(
        By.CSS_SELECTOR, "#top_movies_main > div > table > tbody > tr")
    count = len(top_hundred_list)
    # gets all top 100 movies info and save it to list of tuples
    for i in range(1, count+1):

        name = driver.find_element(
            By.CSS_SELECTOR, f"#top_movies_main > div > table > tbody > tr:nth-child({i}) > td:nth-child(3) > a")
        url = name.get_attribute("href")

        movie_list.append((name.text, url))

    return movie_list


def get_movie_details(driver, movie_url: str) -> dict:
    """Get the details of movie from Rotten Tomatoes

    Parameter:
    driver: webdriver     
    movie_name: movie name of which details will be returned

    Returns: dict with movie details"""

    driver.get(movie_url)
    # need to take whole short info board of movie
    score_selector = driver.find_element(
        By.XPATH, '//*[@id="topSection"]/div[1]/score-board')
    rt_rating = score_selector.get_attribute('tomatometerscore')
    audience_rating = score_selector.get_attribute('audiencescore')
    movie_description = driver.find_element(
        By.XPATH, f'//*[@id="movieSynopsis"]').text
    # using try because older movie info from RT doesn't have that selector
    try:
        movie_length = driver.find_element(
            By.XPATH, f'//*[@id="mainColumn"]/section[3]/div/div/ul/li[10]/div[2]/time').text
    except:
        movie_length = " "

    movie_details = {"rt_rating": rt_rating,
                     "audience_rating": audience_rating,
                     "description": movie_description,
                     "length": movie_length}

    return movie_details


def main():
    """testing"""
    PATH = const.driver_path
    driver = webdriver.Chrome(PATH)
    movie_list = get_movie_list(driver, const.rt_scifi_url)
    print(movie_list)

    movie_details = get_movie_details(driver, movie_list[1][1])

    print(movie_details['length'], '\n', movie_details['description'], '\n',
          movie_details['rt_rating'], '\n', movie_details['audience_rating'])


if __name__ == "__main__":
    main()
