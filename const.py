driver_path = './chromedriver.exe'

rt_action_url = "https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
rt_comedy_url = "https://www.rottentomatoes.com/top/bestofrt/top_100_comedy_movies/"
rt_horror_url = "https://www.rottentomatoes.com/top/bestofrt/top_100_horror_movies/"
rt_scifi_url = "https://www.rottentomatoes.com/top/bestofrt/top_100_science_fiction__fantasy_movies/"
rt_romance_url = "https://www.rottentomatoes.com/top/bestofrt/top_100_romance_movies/"
rt_drama_url = "https://www.rottentomatoes.com/top/bestofrt/top_100_drama_movies/"
rt_animation_url = "https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
rt_international_url = "https://www.rottentomatoes.com/top/bestofrt/top_100_art_house__international_movies/"
rt_classics_url = "https://www.rottentomatoes.com/top/bestofrt/top_100_classics_movies/"
rt_documentary_url = "https://www.rottentomatoes.com/top/bestofrt/top_100_documentary_movies/"
rt_mystery_url = "https://www.rottentomatoes.com/top/bestofrt/top_100_mystery__suspense_movies/"
rt_western_url = "https://www.rottentomatoes.com/top/bestofrt/top_100_western_movies/"

recommendation_dict = {'NEUTRAL': [rt_action_url, rt_comedy_url, rt_romance_url,
                                   rt_animation_url, rt_western_url, rt_classics_url,
                                   rt_documentary_url, rt_scifi_url, rt_horror_url, rt_drama_url,
                                   rt_international_url, rt_mystery_url],
                       'SAD': [rt_comedy_url, rt_romance_url, rt_animation_url,
                               rt_drama_url, rt_mystery_url],
                       'HAPPY': [rt_action_url, rt_comedy_url, rt_romance_url,
                                 rt_animation_url, rt_western_url, rt_classics_url,
                                 rt_documentary_url, rt_scifi_url],
                       'ANGRY': [rt_western_url, rt_action_url, rt_horror_url],
                       'DISGUST': [rt_drama_url, rt_romance_url, rt_horror_url, rt_drama_url,
                                   rt_documentary_url],
                       'FEAR': [rt_horror_url],
                       'SURPRISE': [rt_international_url, rt_animation_url]}
