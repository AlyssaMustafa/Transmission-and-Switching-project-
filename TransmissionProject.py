import math

def calculate_cells(city_size, population_density, avg_calls_per_user, avg_call_duration, max_channels_per_bs):
    cell_area = 2 * math.sqrt(3) * (max_channels_per_bs / (population_density * avg_calls_per_user * avg_call_duration))
    num_cells = math.ceil(city_size / cell_area)
    if num_cells <= 3:
        sectoring_level = 10
    elif num_cells <= 12:
        sectoring_level = 120
    elif num_cells <= 27:
        sectoring_level = 180
    else:
        sectoring_level = 360
    return num_cells, sectoring_level
city_size = eval(input("Enter the city size"))  # km2
population_density = eval(input("Enter the population desnity")) # users/km2
avg_calls_per_user = eval(input("Enter Average calls per user"))  # calls/user
avg_call_duration = eval(input("Enter the average call duration")) # minutes
max_channels_per_bs = eval(input("Enter the max channels per base stations"))

num_cells, sectoring_level = calculate_cells(city_size, population_density, avg_calls_per_user, avg_call_duration, max_channels_per_bs)

print(f"Number of cells required to cover the city: {num_cells}")
print(f"Sectoring level to be used: {sectoring_level}")
