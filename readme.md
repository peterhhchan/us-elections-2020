# us-elections-2020 #

Simple scripts to simulate possible outcomes in the 2020 US presidential elections.

## markets.py ##

Using betting data from [PredictIt] (predictit.org), simulate different election outcomes.  This script is quite fast, be sure to call `get_markets` once before calling `simulate`.

### Limitations ###

On PredictIt, the cost of each share (the implied probability) does not necessarily equal what the market believes is the true probability. For example, shares of California trading at 95 cents each at the time of writing imply a Democratic win 95% of the time, but in practice, the Democrats will hold the state of California nearly 99+% of the time. Various reasons for why this inefficiency exist, including the time-value of money and fees charged by PredictIt for withdrawal.


## elections.py ##

This script uses state-by-state polling data to generate the likelihood a candidate will win that state. (In the code, the likelihood is a probability represented by a simple normal distribution.) We can optionally introduce a global bias on the polling data, biasing the results towards either candidate. More sophisticated models are possible.


Polling data is obtained from [270towin](https://www.270towin.com/2020-polls-biden-trump/).

## Discussion ##
Preliminary results suggest the polling data strongly favours Democrats.

## Additional Reading ##
https://ig.ft.com/us-election-2020/
https://projects.fivethirtyeight.com/2020-election-forecast/


