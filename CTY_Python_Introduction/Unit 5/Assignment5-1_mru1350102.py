#functions
def population_density(population, area):
    return population / area

def state_population_density(state_name, population_density):
    print("%s's population density is %d people per square mile" % (state_name, population_density))

#call functions
state_population_density("Maryland", population_density(6.052 * 1000000, 12407))
state_population_density("Pennsylvania", population_density(12.81 * 1000000, 46055))
state_population_density("Virginia", population_density(8.4 * 1000000, 42775))
                         

