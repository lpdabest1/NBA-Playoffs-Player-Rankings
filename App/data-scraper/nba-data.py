'''
This python script will collecting data from the following website: https://basketball.realgm.com/
We will be focusing on the top 100 players for each season of the past 20 NBA seasons (Playoffs ONLY)
'''

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import matplotlib as mpl

years = list()

# Desired Years Function
def selected_years(years): 
    for i in range(2002, 2022):
        years.append(i)


selected_years(years)

print(years)



# Scraper Function
def scraping_nba_playoff_player_stats(years):
    players= []
    for i in years:
        current_year = i
        print(current_year)
        url = 'https://www.basketball-reference.com/playoffs/NBA_' + str(i) + '_totals.html'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'}
        page = requests.get(url,headers=headers, timeout=2, allow_redirects = True )
        soup = bs(page.content, 'html.parser')
        href_tbody = soup.find_all('tbody')
        #print(url)
        
        for i in href_tbody:
            href_tr_data = i.find_all('tr')
            for j in href_tr_data:
                while True:
                    try:
                        # Data (INFO) that we are interested in
                        player_name = j.find('td', {'data-stat':'player'}).text

                        position = j.find('td', {'data-stat':'pos'}).text
                        age = j.find('td', {'data-stat':'age'}).text
                        team = j.find('td', {'data-stat':'team_id'}).text
                        games_played = j.find('td', {'data-stat':'g'}).text
                        games_started = j.find('td',{'data-stat':'gs'}).text
                        minutes_played = j.find('td', {'data-stat':'mp'}).text
                        field_goals = j.find('td', {'data-stat':'fg'}).text
                        field_goals_attempted = j.find('td', {'data-stat':'fga'}).text
                        field_goals_percentage = j.find('td', {'data-stat':'fg_pct'}).text
                        three_point_field_goals = j.find('td', {'data-stat':'fg3'}).text
                        three_point_field_goals_attempted = j.find('td', {'data-stat':'fg3a'}).text
                        three_point_field_goals_percentage = j.find('td', {'data-stat':'fg3_pct'}).text
                        two_point_field_goals = j.find('td', {'data-stat':'fg2'}).text
                        two_point_field_goals_attempted = j.find('td', {'data-stat':'fg2a'}).text
                        two_point_field_goals_percentage = j.find('td', {'data-stat':'fg2_pct'}).text
                        effective_field_goal_percentage = j.find('td', {'data-stat':'efg_pct'}).text
                        free_throws = j.find('td', {'data-stat':'ft'}).text
                        free_throws_attempted = j.find('td', {'data-stat':'fta'}).text
                        free_throws_percentage = j.find('td', {'data-stat':'ft_pct'}).text
                        offensive_rebounds = j.find('td', {'data-stat':'orb'}).text
                        defensive_rebounds = j.find('td', {'data-stat':'drb'}).text
                        total_rebounds = j.find('td', {'data-stat':'trb'}).text
                        assists = j.find('td', {'data-stat':'ast'}).text
                        steals = j.find('td', {'data-stat':'stl'}).text
                        blocks = j.find('td', {'data-stat':'blk'}).text
                        turnovers = j.find('td', {'data-stat':'tov'}).text
                        personal_fouls = j.find('td', {'data-stat':'pf'}).text
                        points = j.find('td', {'data-stat':'pts'}).text

                        # Formatting the data point (per player) into a standard format
                        player = { "Player": player_name,
                                    "Season": current_year,
                                    "Position": position,
                                    "Age": age,
                                    "Team": team,
                                    "GP": games_played,
                                    "GS": games_started,
                                    "MP": minutes_played,
                                    "FG": field_goals,
                                    "FGA": field_goals_attempted,
                                    "FG%": field_goals_percentage,
                                    "3P": three_point_field_goals,
                                    "3PA": three_point_field_goals_attempted,
                                    "3P%": three_point_field_goals_percentage,
                                    "2P": two_point_field_goals,
                                    "2PA": two_point_field_goals_attempted,
                                    "2P%": two_point_field_goals_percentage,
                                    "EFG": effective_field_goal_percentage,
                                    "FT": free_throws,
                                    "FTA": free_throws_attempted,
                                    "FT%": free_throws_percentage,
                                    "ORB": offensive_rebounds,
                                    "DRB": defensive_rebounds,
                                    "TRB": total_rebounds,
                                    "AST": assists,
                                    "STL": steals,
                                    "BLK": blocks,
                                    "TO": turnovers,
                                    "PF": personal_fouls,
                                    "PTS": points

                                 }
                        
                        players.append(player)
                    
                        break
                    except:
                        break

    df = pd.DataFrame(players)
    return df 

players_dataframe = scraping_nba_playoff_player_stats(years)

print(players_dataframe)

# Convert DataFrame of players_dataframe to a csv
players_db = players_dataframe.to_csv('App/pages/nba_playoff_players.csv', index=False)
players_db
# Output the csv version of the dataframe
#print(players_db)


