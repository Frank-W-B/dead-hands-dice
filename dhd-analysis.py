import random
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
plt.style.use('bmh')


class Die:
    def __init__(self, n_sides: int = 6, lose_on: int = 1):
        self.n_sides = n_sides
        self.lose_on = lose_on
        self.roll()

    def __repr__(self):
        return f'd{self.n_sides}: {self.value}'

    def roll(self):
        self.value = random.randint(1, self.n_sides)


class Strategy:
    def __init__(self, die: Die, number_dice: int):
        self.die = die
        self.number_dice = number_dice
        self.expectation_die = self._expectation_one_die_not_losing()
        self.expectation_dice = self._expectation_dice_not_losing()
        self.prob_strat_not_losing = self._probability_not_losing()
        self.expectation_overall = self._find_strategy_expectation()

    def _expectation_one_die_not_losing(self) -> float:
        num_sides_not_losing = self.die.n_sides - 1
        prob_side = 1 / num_sides_not_losing
        expectation = prob_side * sum([val for val in range(1, self.die.n_sides + 1)
                                       if val != self.die.lose_on])
        return expectation

    def _expectation_dice_not_losing(self) -> float:
        return self.expectation_die * self.number_dice

    def _probability_not_losing(self) -> float:
        num_sides_not_losing = self.die.n_sides - 1
        return (num_sides_not_losing / self.die.n_sides)**self.number_dice

    def _find_strategy_expectation(self) -> float:
        return self.expectation_dice * self.prob_strat_not_losing

    def __repr__(self):
        return (f'dice: d{self.die.n_sides}, # dice rolled: {self.number_dice}, '
                f'dice roll expectation (not losing): {self.expectation_dice:0.1f}, '
                f'probability of not losing: {self.prob_strat_not_losing:0.2f}, '
                f'expectation: {self.expectation_overall:0.2f}')


def plot_results(strategies: list[Strategy]):
    num_sides = strategies[0].die.n_sides
    number_dice_rolled = []
    dice_roll_expectation = []
    probability_not_losing = []
    strategy_expectation = []
    for strategy in strategies:
        number_dice_rolled.append(strategy.number_dice)
        dice_roll_expectation.append(strategy.expectation_dice)
        probability_not_losing.append(strategy.prob_strat_not_losing)
        strategy_expectation.append(strategy.expectation_overall)
 
    fig, ax1 = plt.subplots(figsize=(7, 5))
 
    ax1.set_xlabel(f'Number of d{num_sides}s rolled')
    ax1.set_ylabel('Dice sum')
    ax1.plot(number_dice_rolled, dice_roll_expectation, color='blue',
             label='Expected roll sum (without loss)')
    ax1.plot(number_dice_rolled, strategy_expectation, color='green',
             label='Expected roll x probability')
    ax1.set_ylim((0, 50))
    loc = plticker.MultipleLocator(base=1.0)
    ax1.xaxis.set_major_locator(loc)
 
    ax2 = ax1.twinx()
    ax2.set_ylabel('Probability of not losing', color='red')
    ax2.plot(number_dice_rolled, probability_not_losing, color='red',
             label='Probability of not losing')
    ax2.set_ylim((0, 1))
    ax2.tick_params(axis='y', labelcolor='red')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    fig.tight_layout()
    plt.savefig('images/all_results.png', dpi=100)
    plt.close()
   
    fig, ax = plt.subplots(figsize=(6.5, 5))
    ax.set_xlabel(f'Number of d{num_sides}s rolled')
    ax.set_ylabel(f'Expected value')
    ax.plot(number_dice_rolled, strategy_expectation, color='green',
            marker='o',
            label='Expected roll x probability of not losing')
    loc = plticker.MultipleLocator(base=1.0)
    ax.xaxis.set_major_locator(loc)
    ax.legend()
    fig.tight_layout()
    plt.savefig('images/strategy_results.png', dpi=100)
    print('Results written.')


if __name__ == '__main__':
    n_sides = 6  # the number of sides on the dice
    
    num_dice_to_roll = list(range(1, 16))
    die = Die(n_sides)
    strategies = []
    for num_dice in num_dice_to_roll:
        strategy = Strategy(die=die, number_dice=num_dice)
        print(strategy)
        strategies.append(strategy)
    plot_results(strategies)
