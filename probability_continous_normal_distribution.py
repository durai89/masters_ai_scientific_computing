def continous_normal_distribution(mean, s_deviation, np_dist_size):
    # Use numpy to draw random samples from normal distribution
    c = np.random.normal(mean, s_deviation, np_dist_size)
    count, bins, ignored = plt.hist(c, 300, density=True)
    plt.xlabel('bulb lifetime (in days)')
    plt.ylabel('probability')

    # Work out mean and standard deviation with numpy.
    np_mean = np.mean(c)
    np_sd = np.std(c)

    # Plot continous distribution function
    plt.plot(bins, 1 / (s_deviation * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - mean) ** 2 / (2 * s_deviation * 2)), linewidth=3, color='y')
    plt.show()

    return np_mean, np_sd

def get_continous_distibution_fn_area(coord1, coord2, mean, sd):
    y1 = 0.5 * math.erf(-(coord1-mean)/(sd*math.sqrt(2.0)))
    y2 = 0.5 * math.erf(-(coord2-mean)/(sd*math.sqrt(2.0)))
    return abs(y2 + y1) if coord1 < 0 and coord2 > 0 else abs(y2 - y1)

def test_experiment_continous_normal_distribution():
    np_mean, np_sd = continous_normal_distribution(300, 50, 5000)

    print ("Mean :{}".format(np_mean))

    print ("Standard deviation :{}".format(np_sd))
    probability = get_continous_distibution_fn_area(100, 200, np_mean, np_sd)

    print ("Probability of ACME light bulb lasting for atmost 365 days is {}".format(probability))