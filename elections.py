from requests import Session
import csv
import numpy

# Get the polling data
session = Session()
#response = session.get("https://www.270towin.com/polls/php/get-early-polls.php?election_year=2020&candidate_name_rep=Trump&candidate_name_dem=Biden")

#result = response.json()['results']

#states = {}
for x in result:
    state = x
    dem = result[x]['poll_dem']
    rep = result[x]['poll_rep']
    states[state] = {"dem" : dem, "rep" : rep}

## Not all the states from 270towin have polling data. Instead of using
## polling data, we take a shortcut and assign the state to one part
## in votes.csv.
with open('percents.csv', newline='') as f:
    reader = csv.reader(f)
    for v,s,p in reader:
        if (s not in states.keys()):
            states[s] = {'win_d' : float(p)}
        elif p:
            states[s] = {'win_d' : float(p)}
        states[s]["votes"] = int(v)

## Additional polling data can be found at 538.
## Take a look at
## https://fivethirtyeight.com/features/polls-policy-and-faqs/
## Some examples.
## https://data.fivethirtyeight.com/#polls
## https://projects.fivethirtyeight.com/polls-page/president_polls.csv


## result contains an entry which is the national polling data,
## denoted by '0'.  We remove it here.
states.pop('0', None)

std_d = 8.5
skew = -3 ## Make skew negative to favor Republicans, positive for Dems
skew_dem = 0.3 ## percentage of undecided voters that will vote Democrat

def win_dem (dem, rep, s):
    undecided = 100 - (dem + rep)

    # undecided voters are assigned 50/50
    dem_adj = undecided * skew_dem + dem + s

    if numpy.random.default_rng().normal(dem_adj, std_d) > 50:
        return 1
    else:
        return 0

def simulate ():
    votes_dem, votes_rep = 0, 0;
    for s,v in states.items():
        win_d = 0
        if 'win_d' in v:
            win_d = v['win_d'] > numpy.random.default_rng().random()
        else:
            win_d = win_dem (v['dem'], v['rep'], skew)

        if win_d > 0:
            votes_dem += v['votes']
        else:
            votes_rep += v['votes']

    ## Tiebreaks go to the Republicans
    if votes_dem > 269:
        return 1
    else:
        return 0

def run_sims():
    wins_dem = 0;
    iterations = 10000;
    for _ in range (iterations):
        wins_dem += simulate()

    print (wins_dem / iterations)
