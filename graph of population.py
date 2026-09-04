import matplotlib.pyplot as plt

# Starting population
population = float(input("Enter the starting population: "))

# Annual growth rate
growth_rate = float(input("Enter the annual growth rate (recommended 0.05 for 5%): "))

# Number of years
years = int(input("Enter the number of years to simulate: "))

# Lists to store the data
year_list = []
population_list = []

# Simulate population growth
for year in range(years + 1):
    year_list.append(year)
    population_list.append(population)

    # Increase population
    population = population * (1 + growth_rate)

# Create the graph
plt.plot(population_list, year_list, marker="o")

# Add labels and title
plt.title("Population Growth Simulator")
plt.xlabel("Population")
plt.ylabel("Years")

# Add grid
plt.grid(True)

# Show graph
plt.show()