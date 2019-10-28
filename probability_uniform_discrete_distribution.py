def dice_roll_experiment(experiment_count):
    probability_distribution_exp = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    # Run experiment for multiple iterations - record probability distribution
    for i in range(experiment_count):
        experiment_result = random.randint(1, 6)
        probability_distribution_exp[experiment_result] += 1 / experiment_count

    # Calculate expected value
    expected_value = 0
    for (k, v) in probability_distribution_exp.items():
        expected_value += k * v

    # Work out variance for the distribution.
    variance = 0
    for (k, v) in probability_distribution_exp.items():
        variance += math.pow((k - expected_value), 2) * v

    return probability_distribution_exp, expected_value, math.sqrt(variance)

def execute_dice_roll_experiment():
    probability_distribution, mean, standard_deviation = dice_roll_experiment(5000)

    print (" -- Experiment's Probability distribution table----")
    print ("{:<8} {:<15}".format('Dice roll result', 'probability'))
    for (k, v) in probability_distribution.items():
        print ("{:<8} {:<15}".format(k, round(v, 4)))

    print ("Expected value is : {}".format(mean))
    print ("Standard deviation is : {}".format(standard_deviation))

    plt.xlabel('dice sides')
    plt.ylabel('probability')
    plt.title('Discrete uniform Probability distribution of rolling a dice')
    plt.axhline(y=0.16666, color='black', linestyle='-')
    plt.bar(probability_distribution.keys(), probability_distribution.values())
    plt.show()