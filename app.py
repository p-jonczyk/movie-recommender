from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import const
import random
import movie_recommend
import emotion_detector

PATH = const.driver_path
chrome_options = Options()
# runs driver in background
chrome_options.add_argument("--headless")
# hides consol info
chrome_options.add_argument("log-level=3")
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)


def main():

    # get emotion from webcam
    detected_mood = emotion_detector.emotion_detector()
    mood = detected_mood.upper()

    # print start info
    print(f'\nIt looks like you feel {mood}')
    print('[INFO] Analyzing recommendations...\n')
    # list of recommended genres as urls for top 100
    recommend_genres = const.recommendation_dict[mood]
    # select random genre of recommended genres
    recommend_url = random.choice(recommend_genres)
    # get list of movies (from index 1)
    # index 0 is genre name
    movie_list = movie_recommend.get_movie_list(driver, recommend_url)
    answer = 'another'

    # give user info
    while True:

        if answer == 'another':
            # get random movie from obtained list
            recommend_movie = random.choice(movie_list[1:])
            # movie details
            genre = movie_list[0]
            movie_name = recommend_movie[0]
            movie_url = recommend_movie[1]

            print(f'You should watch movie of genre: {genre}')
            print(f'You should watch:\n\n{movie_name}\n')
            print("[INFO] If you would like to get some details type 'details'...")
            print(
                "[INFO] For another recommendation type 'another' or 'exit' to leave the program...")

        elif answer == 'details':
            print('\n[INFO] Gathering movie details...\n')
            details_list = movie_recommend.get_movie_details(driver, movie_url)
            print(f"Rotten Tomatoes score: {details_list['rt_rating']}%")
            print(f"Audience score: {details_list['audience_rating']}%")
            print(f"Runtime: {details_list['length']}")
            print(f"\nDESCRIPTION\n{details_list['description']}")

        elif answer == 'exit':
            exit()

        else:
            print("[INFO] Unsupported command...\nType: 'details', 'exit' or 'another'")

        answer = input('\n> ').lower()


if __name__ == "__main__":
    main()
