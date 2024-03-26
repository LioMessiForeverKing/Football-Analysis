import numpy
import pandas
from matplotlib import pyplot
from sklearn.linear_model import LinearRegression
import re

data = pandas.read_csv('main.csv')

class League():
    """
    An instance of this class represents a League
    Each league would have variables called
    Wins: The wins to teams in the league
    Loses: The loses of the teams in the league
    Draws:The draws from teams of teams in the league
    Goals scored: The goals scored by teams in the leagued
    Goals against: The goals conceded by teams in the leagued
    Points:The points earend by the team in the league based on the legue(determins a teams rank) 

    These variables would be lists that contain the mean, median and standard deviation for the teams in that league.
    """

    def __init__(self, league, wins,loses,draws, gs, ga, pts):
        self.league = league
        self.wins = wins
        self.loses = loses
        self.draws =draws
        self.goals_scored= gs
        self.goals_against= ga
        self.points=pts
    
    def __str__(self):
        print('League: '+self.league)
        print(self.wins)
        print(self.loses)
        print(self.draws)
        print(self.goals_scored)
        print(self.goals_against)
        print(self.points)
        return ''
    
EPLdata = data.loc[data['League'] == 'EPL']
EPL_wins= 'Wins -->  ' + 'Mean: '+ str(numpy.mean(EPLdata.Wins)) + ', Median: '+ str(numpy.median(EPLdata.Wins)) + ', Standard deviation: ' + str (numpy.std(EPLdata.Wins))
EPL_loses= 'Loses -->  ' + 'Mean: '+ str(numpy.mean(EPLdata.Loses)) + ', Median: '+ str(numpy.median(EPLdata.Loses)) + ', Standard deviation: ' + str (numpy.std(EPLdata.Loses))
EPL_draws= 'Draws -->  ' + 'Mean: '+ str(numpy.mean(EPLdata.Draws)) + ', Median: '+ str(numpy.median(EPLdata.Draws)) + ', Standard deviation: ' + str (numpy.std(EPLdata.Draws))
EPL_gs=  'Goals scored -->  ' + 'Mean: '+ str(numpy.mean(EPLdata.Goals_scored)) + ', Median: '+ str(numpy.median(EPLdata.Goals_scored)) + ', Standard deviation: ' + str (numpy.std(EPLdata.Goals_scored))
EPL_ga= 'Goals against -->  ' + 'Mean: '+ str(numpy.mean(EPLdata.Goals_against)) + ', Median: '+ str(numpy.median(EPLdata.Goals_against)) + ', Standard deviation: ' + str (numpy.std(EPLdata.Goals_against))
EPL_points= 'Points -->  ' + 'Mean: '+ str(numpy.mean(EPLdata.Points)) + ', Median: '+ str(numpy.median(EPLdata.Points)) + ', Standard deviation: ' + str (numpy.std(EPLdata.Points))

EPL= League('EPL', EPL_wins, EPL_loses, EPL_draws, EPL_gs, EPL_ga, EPL_points)

Laligadata = data.loc[data['League'] == 'La liga']
Laliga_wins= 'Wins -->  ' + 'Mean: '+ str(numpy.mean(Laligadata.Wins)) + ', Median: '+ str(numpy.median(Laligadata.Wins)) + ', Standard deviation: ' + str (numpy.std(Laligadata.Wins))
Laliga_loses= 'Loses -->  ' + 'Mean: '+ str(numpy.mean(Laligadata.Loses)) + ', Median: '+ str(numpy.median(Laligadata.Loses)) + ', Standard deviation: ' + str (numpy.std(Laligadata.Loses))
Laliga_draws= 'Draws -->  ' + 'Mean: '+ str(numpy.mean(Laligadata.Draws)) + ', Median: '+ str(numpy.median(Laligadata.Draws)) + ', Standard deviation: ' + str (numpy.std(Laligadata.Draws))
Laliga_gs=  'Goals scored -->  ' + 'Mean: '+ str(numpy.mean(Laligadata.Goals_scored)) + ', Median: '+ str(numpy.median(Laligadata.Goals_scored)) + ', Standard deviation: ' + str (numpy.std(Laligadata.Goals_scored))
Laliga_ga= 'Goals against -->  ' + 'Mean: '+ str(numpy.mean(Laligadata.Goals_against)) + ', Median: '+ str(numpy.median(Laligadata.Goals_against)) + ', Standard deviation: ' + str (numpy.std(Laligadata.Goals_against))
Laliga_points= 'Points -->  ' + 'Mean: '+ str(numpy.mean(Laligadata.Points)) + ', Median: '+ str(numpy.median(Laligadata.Points)) + ', Standard deviation: ' + str (numpy.std(Laligadata.Points))

La_liga= League('La liga', Laliga_wins, Laliga_loses, Laliga_draws, Laliga_gs, Laliga_ga, Laliga_points)

Bundesligadata = data.loc[data['League'] == 'Bundesliga']
Bundesliga_wins= 'Wins -->  ' + 'Mean: '+ str(numpy.mean(Bundesligadata.Wins)) + ', Median: '+ str(numpy.median(Bundesligadata.Wins)) + ', Standard deviation: ' + str (numpy.std(Bundesligadata.Wins))
Bundesliga_loses= 'Loses -->  ' + 'Mean: '+ str(numpy.mean(Bundesligadata.Loses)) + ', Median: '+ str(numpy.median(Bundesligadata.Loses)) + ', Standard deviation: ' + str (numpy.std(Bundesligadata.Loses))
Bundesliga_draws= 'Draws -->  ' + 'Mean: '+ str(numpy.mean(Bundesligadata.Draws)) + ', Median: '+ str(numpy.median(Bundesligadata.Draws)) + ', Standard deviation: ' + str (numpy.std(Bundesligadata.Draws))
Bundesliga_gs=  'Goals scored -->  ' + 'Mean: '+ str(numpy.mean(Bundesligadata.Goals_scored)) + ', Median: '+ str(numpy.median(Bundesligadata.Goals_scored)) + ', Standard deviation: ' + str (numpy.std(Bundesligadata.Goals_scored))
Bundesliga_ga= 'Goals against -->  ' + 'Mean: '+ str(numpy.mean(Bundesligadata.Goals_against)) + ', Median: '+ str(numpy.median(Bundesligadata.Goals_against)) + ', Standard deviation: ' + str (numpy.std(Bundesligadata.Goals_against))
Bundesliga_points= 'Points -->  ' + 'Mean: '+ str(numpy.mean(Bundesligadata.Points)) + ', Median: '+ str(numpy.median(Bundesligadata.Points)) + ', Standard deviation: ' + str (numpy.std(Bundesligadata.Points))

Bundesliga= League('Bundesliga', Bundesliga_wins, Bundesliga_loses, Bundesliga_draws, Bundesliga_gs, Bundesliga_ga, Bundesliga_points)

Seriedata = data.loc[data['League'] == 'Serie A']
Serie_wins= 'Wins -->  ' + 'Mean: '+ str(numpy.mean(Seriedata.Wins)) + ', Median: '+ str(numpy.median(Seriedata.Wins)) + ', Standard deviation: ' + str (numpy.std(Seriedata.Wins))
Serie_loses= 'Loses -->  ' + 'Mean: '+ str(numpy.mean(Seriedata.Loses)) + ', Median: '+ str(numpy.median(Seriedata.Loses)) + ', Standard deviation: ' + str (numpy.std(Seriedata.Loses))
Serie_draws= 'Draws -->  ' + 'Mean: '+ str(numpy.mean(Seriedata.Draws)) + ', Median: '+ str(numpy.median(Seriedata.Draws)) + ', Standard deviation: ' + str (numpy.std(Seriedata.Draws))
Serie_gs=  'Goals scored -->  ' + 'Mean: '+ str(numpy.mean(Seriedata.Goals_scored)) + ', Median: '+ str(numpy.median(Seriedata.Goals_scored)) + ', Standard deviation: ' + str (numpy.std(Seriedata.Goals_scored))
Serie_ga= 'Goals against -->  ' + 'Mean: '+ str(numpy.mean(Seriedata.Goals_against)) + ', Median: '+ str(numpy.median(Seriedata.Goals_against)) + ', Standard deviation: ' + str (numpy.std(Seriedata.Goals_against))
Serie_points= 'Points -->  ' + 'Mean: '+ str(numpy.mean(Seriedata.Points)) + ', Median: '+ str(numpy.median(Seriedata.Points)) + ', Standard deviation: ' + str (numpy.std(Seriedata.Points))

Serie_A= League('Serie A', Serie_wins, Serie_loses, Serie_draws, Serie_gs, Serie_ga, Serie_points)

Seriedata = data.loc[data['League'] == 'Serie A']
Serie_wins= 'Wins -->  ' + 'Mean: '+ str(numpy.mean(Seriedata.Wins)) + ', Median: '+ str(numpy.median(Seriedata.Wins)) + ', Standard deviation: ' + str (numpy.std(Seriedata.Wins))
Serie_loses= 'Loses -->  ' + 'Mean: '+ str(numpy.mean(Seriedata.Loses)) + ', Median: '+ str(numpy.median(Seriedata.Loses)) + ', Standard deviation: ' + str (numpy.std(Seriedata.Loses))
Serie_draws= 'Draws -->  ' + 'Mean: '+ str(numpy.mean(Seriedata.Draws)) + ', Median: '+ str(numpy.median(Seriedata.Draws)) + ', Standard deviation: ' + str (numpy.std(Seriedata.Draws))
Serie_gs= 'Goals scored -->  ' + 'Mean: '+ str(numpy.mean(Seriedata.Goals_scored)) + ', Median: '+ str(numpy.median(Seriedata.Goals_scored)) + ', Standard deviation: ' + str (numpy.std(Seriedata.Goals_scored))
Serie_ga='Goals against -->  ' + 'Mean: '+ str(numpy.mean(Seriedata.Goals_against)) + ', Median: '+ str(numpy.median(Seriedata.Goals_against)) + ', Standard deviation: ' + str (numpy.std(Seriedata.Goals_against))
Serie_points= 'Points -->  ' + 'Mean: '+ str(numpy.mean(Seriedata.Points)) + ', Median: '+ str(numpy.median(Seriedata.Points)) + ', Standard deviation: ' + str (numpy.std(Seriedata.Points))

Serie_A= League('Serie A', Serie_wins, Serie_loses, Serie_draws, Serie_gs, Serie_ga, Serie_points)

Ligue1data= data.loc[data['League'] == 'Ligue 1']
Ligue1_wins= 'Wins -->  ' + 'Mean: '+ str(numpy.mean(Ligue1data.Wins)) + ', Median: '+ str(numpy.median(Ligue1data.Wins)) + ', Standard deviation: ' + str (numpy.std(Ligue1data.Wins))
Ligue1_loses= 'Loses -->  ' + 'Mean: '+ str(numpy.mean(Ligue1data.Loses)) + ', Median: '+ str(numpy.median(Ligue1data.Loses)) + ', Standard deviation: ' + str (numpy.std(Ligue1data.Loses))
Ligue1_draws= 'Draws -->  ' + 'Mean: '+ str(numpy.mean(Ligue1data.Draws)) + ', Median: '+ str(numpy.median(Ligue1data.Draws)) + ', Standard deviation: ' + str (numpy.std(Ligue1data.Draws))
Ligue1_gs= 'Goals scored -->  ' + 'Mean: '+ str(numpy.mean(Ligue1data.Goals_scored)) + ', Median: '+ str(numpy.median(Ligue1data.Goals_scored)) + ', Standard deviation: ' + str (numpy.std(Ligue1data.Goals_scored))
Ligue1_ga='Goals against -->  ' + 'Mean: '+ str(numpy.mean(Ligue1data.Goals_against)) + ', Median: '+ str(numpy.median(Ligue1data.Goals_against)) + ', Standard deviation: ' + str (numpy.std(Ligue1data.Goals_against))
Ligue1_points= 'Points -->  ' + 'Mean: '+ str(numpy.mean(Ligue1data.Points)) + ', Median: '+ str(numpy.median(Ligue1data.Points)) + ', Standard deviation: ' + str (numpy.std(Ligue1data.Points))

Ligue1= League('Ligue 1', Ligue1_wins, Ligue1_loses, Ligue1_draws, Ligue1_gs, Ligue1_ga, Ligue1_points)

print(EPL)
print(La_liga)
print(Bundesliga)
print(Serie_A)
print(Ligue1)

pyplot.scatter(data.Goals_scored, data.Points)
pyplot.xlabel('Goals scored')
pyplot.ylabel('Points')
pyplot.show()
gs_pts=LinearRegression().fit(data [['Goals_scored']], data [['Points']])

print('Coefficient: ')
print(gs_pts.coef_)

predictors= ['Goals_scored', 'Goals_against']
multiple_reg= LinearRegression().fit(data[predictors],data['Points'])
print(multiple_reg.coef_)

pyplot.bar(data.Ranking, data.Goals_scored)
pyplot.xlabel('Ranking')
pyplot.ylabel('Goals Scored')
pyplot.show()

pyplot.bar(data.Ranking, data.Goals_against)
pyplot.xlabel('Ranking')
pyplot.ylabel('Goals Against')
pyplot.show()

data_home = pandas.read_csv('home.csv')

data_away = pandas.read_csv('away.csv')

home_win_probability = []
for i in range(98):
    probability = data_home['Wins'][i] / data_home['Games_played'][i]
    home_win_probability.append(probability)
    
numpy.mean(home_win_probability)

away_win_probability = []
for i in range(98):
    probability = data_away['Wins'][i] / data_away['Games_played'][i]
    away_win_probability.append(probability)

numpy.mean(away_win_probability)

expected_points=[]
for i in data.Expected_points:
    string = str(i)
    value=re.search("(\d+.\d+)", i)
    expected_points.append(float(value.group(0)))
    
    
expected_goals_scored=[]
for i in data.Expected_goals_scored:
    string = str(i)
    value=re.search("(\d+.\d+)", i)
    expected_goals_scored.append(float(value.group(0)))
    
    
expected_goals_against=[]
for i in data.Expected_goals_against:
    string = str(i)
    value=re.search("(\d+.\d+)", i)
    expected_goals_against.append(float(value.group(0)))
            
        
# to see the correlation between expected goals and actual goals scored

correlation1 = numpy.corrcoef(data.Goals_scored, expected_goals_scored)[0,1]
print("Actual goals scored vs. Expected goals scored correlation coefficient: ")
print(correlation1)
print("")
correlation2 = numpy.corrcoef(data.Goals_against, expected_goals_against)[0,1]
print("Actual goals scored against vs. Expected goals scored against correlation coefficient: ")
print(correlation2)
print("")
correlation3 = numpy.corrcoef(data.Points, expected_points)[0,1]
print("Actual points earned vs. Expected points earned correlation coefficient: ")
print(correlation3)
print("")

points = []
for i in data.Points:
    points.append(i)

expected_goals=[]
for i in data.Expected_goals_scored:
    string = str(i)
    value=re.search("(\d+.\d+)", i)
    expected_goals.append([float(value.group(0))])
    

pyplot.scatter(expected_goals_scored, data.Points)
pyplot.xlabel('Expected Goals Scored')
pyplot.ylabel('Actual Points')
pyplot.show()
exg_pts=LinearRegression().fit( expected_goals, data[["Points"]])
print('Coeffiecient: ')
print(*exg_pts.coef_)

    
expected_goals_against=[]
for i in data.Expected_goals_against:
    string = str(i)
    value=re.search("(\d+.\d+)", i)
    expected_goals_against.append([float(value.group(0))])
    

pyplot.scatter(expected_goals_against, data.Points)
pyplot.xlabel('Expected Goals Conceded')
pyplot.ylabel('Actual Points')
pyplot.show()
exg_pts=LinearRegression().fit( expected_goals_against, data[["Points"]])
print('Coeffiecient: ')
print(*exg_pts.coef_)

# first start by creating a method

def mse(y, y_pred):
    mse = 0
    for i in range(len(y)):
        mse += (y[i] - y_pred[i])**2
    mse = mse / len(y)
    return mse

pyplot.scatter(data.Goals_scored, expected_goals_scored)
pyplot.show()
print('Goals Scored Mean Squared Error:', mse(data.Goals_scored, expected_goals_scored)) 

pyplot.scatter(data.Goals_against, expected_goals_against)
pyplot.show()
print('Goals Against Mean Squared Error:', mse(data.Goals_against, expected_goals_against))

pyplot.scatter(data.Points, expected_points)
pyplot.show()
print('Points Mean Squared Error:', mse(data.Points, expected_points)) 

