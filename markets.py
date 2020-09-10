import csv
import numpy
import json
import urllib.request
import re

states = {}
with open('votes.csv', newline='') as f:
    reader = csv.reader(f)
    for v,s,p in reader:
        states[s] = int(v)

abbrvs = {}
with open('abbrvs.csv', newline='') as f:
    reader = csv.reader(f)
    for s,a in reader:
        abbrvs[a] = s

## Maps State abbreviations to votes for that state, {'AL' : 9, etc}
avs = {}
for a,s in abbrvs.items():
    avs[a] = states[s]


## Democratic win probabilities for each state based on betting data from predictit.org
## In reality, states with 95% probability to win like California will win 99.9%+ of the time
win_prob = {}
def get_markets():
    markets = json.loads(urllib.request.urlopen('https://www.predictit.org/api/marketdata/all/').read())['markets']
    for m in markets:
        sn = m['shortName']
        match = re.search("^Which party will win ([A-Z]{2}) in 2020\?$", sn)

        if match:
            for c in m['contracts']:
                if c['name'] == 'Democratic':
                    win_prob[match[1]] = c['lastTradePrice']
        elif sn == "Which party will win WY 2020?":
            ## There is a type in the name for Wyoming.
            for c in m['contracts']:
                if c['name'] == 'Democratic':
                    win_prob['WY'] = c['lastTradePrice']



get_markets()


def simulate(n):
    rs = numpy.random.rand(n, len(win_prob))

    wps = sorted(win_prob.items(), key=lambda x: x[0])
    vs_sorted=numpy.fromiter(avs.values(), dtype=int)
    ps_sorted= numpy.fromiter(dict(wps).values(), dtype=float)

    sims_won = 0
    for r in rs:
        wins = numpy.greater(ps_sorted , r)
        total_votes_won = numpy.sum(numpy.multiply(wins, vs_sorted))
        if total_votes_won > 269: ## Tie breaks go to republicans
            sims_won+=1

    return sims_won / n
