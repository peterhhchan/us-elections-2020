# us-elections-2020 #

Simple scripts to simulate possible outcomes in the 2020 US presidential elections.

## markets.py ##

A script to simulate election outcomes using betting data from [PredictIt](www.predictit.org).  This script is quite fast, be sure to call `get_markets` once before calling `simulate`. You can see the script in action [here](https://github.com/peterhhchan/us-elections-2020/blob/master/notebooks/PredictItSimulator/predictit.ipynb).

### Limitations ###

On PredictIt, the cost of each share (the implied probability) does not necessarily equal what the market believes is the true probability. For example, shares of California trading at 95 cents each at the time of writing imply a Democratic win 95% of the time, but in practice, the Democrats will hold the state of California nearly 99+% of the time. Various reasons for why this inefficiency exist, including the time-value of money and fees charged by PredictIt for withdrawal.

Nebraska and Maine uses the congressional district method to assign their votes. However, their electoral votes are assigned using the winner-take-all system in our simulations.

## elections.py ##

This script uses state-by-state polling data to generate the likelihood a candidate will win that state. (In the code, the likelihood is a probability represented by a simple normal distribution.) We can optionally introduce a global bias on the polling data, biasing the results towards either candidate. More sophisticated models are possible.


Polling data is obtained from [270towin](https://www.270towin.com/2020-polls-biden-trump/).

### Limitations ###
Polls suffer from many biases, their reach may not represent the demographics of the electorate on voting day, nor will they necessarily reflect how voters will vote on election day.  More sophisticated polls and models will adjust for these individual biases, as well as incumbency effects and the current state of the economy (which favors the incumbent).  

Once again, Nebraska and Maine uses the congressional district method to assign their votes. However, their electoral votes are assigned using the winner-take-all system in our simulations.


## Additional Reading ##
https://ig.ft.com/us-election-2020/
https://projects.fivethirtyeight.com/2020-election-forecast/


