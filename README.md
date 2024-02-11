# dead-hands-dice
Determines the correct number of dice to roll to maximize your chance of winning this game.  
Game summary:  
* Each player chooses any number of d6s to roll  
* Everyone rolls all their dice at the same time
* The person with the highest dice sum wins, but anyone who rolled a 1 loses

Create and activate virtualenv:  
`$ virtualenv --python python3 dhd-venv`  
`$ source dhd-venv/bin/activate`  

Install project requirements:   
`$ pip install -r requirements.txt`

Run analysis:  
`$ python3 dhd-analysis.py`


**Results**

The best strategy is to roll 5 or 6 dice:

![Best is rolling 5 or 6 dice](/images/strategy_results.png)

This plot includes the expected dice sum (assuming no 1s) and the probability of not losing (right hand axis):

![Includes expectes dice sum and probability of not losing](/images/all_results.png)


