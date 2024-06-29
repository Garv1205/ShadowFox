# task 1
# a
pi = 22/7  
print(type(pi))
print("-------------------x---------------")
# B
# Corrected code
my_number = 4  # Using a descriptive variable name
print(my_number) 
print("-------------------x---------------")
# C
principal = 10000  # Principal amount
rate = 5           # Rate of interest (in percentage)
time = 3           # Time period (in years)
simple_interest = principal * rate * time / 100

print("Simple Interest for 3 years:", simple_interest)

# task 2
def format_string(number, letter):
  # Using f-strings for cleaner and more modern formatting
  formatted_string = f"{number}{letter}"
  return formatted_string
print("-------------------x---------------")
# Calling the function and printing the result
result = format_string(145, 'o')
print(result)  # This will output "145o"
print("-------------------x---------------")
# Representation used: f-string

# Circle Area calculation
pi = 3.14
radius = 84
circle_area = pi * radius**2

print(f"Circle Area: {circle_area:.2f} square meters")  # Print with 2 decimal places for clarity
print("-------------------x---------------")
# Water in the pond (assuming 1.4 liters per square meter)
water_per_square_meter = 1.4
total_water = circle_area * water_per_square_meter
# Printing total water without decimals (integer part)
print(f"Total Water in the Pond: {int(total_water)} liters (rounded down)")
print("-------------------x---------------")
# Speed calculation
distance = 490
time_in_seconds = 7 * 60  # Convert minutes to seconds
speed = distance / time_in_seconds
# Printing speed without decimals (integer part)
print(f"Speed: {int(speed)} meters per second (rounded down)")
print("-------------------x---------------")

# task 4
#  BMI Category Determination
def calculate_bmi(weight, height):
  bmi = weight / (height * height)
  return bmi

def determine_bmi_category(bmi):
  if bmi >= 30:
    print("Obesity")
  elif bmi >= 25:
    print("Overweight")
  elif bmi >= 18.5:
    print("Normal")
  else:
    print("Underweight")

# Get user input for height and weight
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Determine and print BMI category
determine_bmi_category(bmi)

print("-------------------x---------------")

# City-Country Mapping
countries = {
  "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
  "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
  "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

def find_city_country(city):
  for country, cities in countries.items():
    if city.lower() in cities:
      print(f"{city.capitalize()} is in {country}")
      return  # Early exit after finding the country

  print("City not found")

# Get user input for city name
city = input("Enter a city name: ")

# Find and print city-country mapping
find_city_country(city)
countries = {
  "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
  "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
  "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

def find_city_country(city):
  for country, cities in countries.items():
    if city.lower() in cities:
      return country
  return None

def are_cities_in_same_country(city1, city2):
  country1 = find_city_country(city1.lower())
  country2 = find_city_country(city2.lower())

  if country1 == country2 and country1 is not None:
    print(f"Both cities, {city1} and {city2}, are in {country1}")
  else:
    print(f"{city1} and {city2} don't belong to the same country")

# Get user input for city names
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Check and print if cities are in the same country
are_cities_in_same_country(city1, city2)

print("-------------------------x--------------------")

# Simulating Dice Rolls
import random

# Number of times to roll the die
num_rolls = 20

# Count for each outcome
ones = 0
sixes = 0
two_sixes_in_a_row = 0
previous_roll = None

for _ in range(num_rolls):
  # Roll the die (1-6)
  current_roll = random.randint(1, 6)

  # Count occurrences
  if current_roll == 1:
    ones += 1
  elif current_roll == 6:
    sixes += 1
    if previous_roll == 6:
      two_sixes_in_a_row += 1
  previous_roll = current_roll

# Print statistics
print(f"Number of times rolled a 1: {ones}")
print(f"Number of times rolled a 6: {sixes}")
print(f"Number of times rolled two 6s in a row: {two_sixes_in_a_row}")

print("-------------------------x--------------------")

# Workout Routine with Jumping Jacks

total_jumping_jacks = 100
completed_jumping_jacks = 0

while completed_jumping_jacks < total_jumping_jacks:
  # Perform 10 jumping jacks
  completed_jumping_jacks += 10

  print(f"You completed {completed_jumping_jacks} jumping jacks.")

  # Ask if tired (case-insensitive)
  tired = input("Are you tired? (yes/no) ").lower()

  # Check if user wants to skip remaining sets
  if tired in ("yes", "y"):
    skip_remaining = input("Do you want to skip the remaining sets? (yes/no) ").lower()
    if skip_remaining in ("yes", "y"):
      break

  # Print remaining jumping jacks if not tired
  if completed_jumping_jacks < total_jumping_jacks:
    remaining_jumping_jacks = total_jumping_jacks - completed_jumping_jacks
    print(f"{remaining_jumping_jacks} jumping jacks remaining.")

# Print completion message
if completed_jumping_jacks == total_jumping_jacks:
  print("Congratulations! You completed the workout!")

print("-------------------------x--------------------")

# Task 6

#  List of Friends' Names and Length Tuples:
# List of friends' names
friends_names = ["harsh","garv","kunj","prit"]

# List of tuples with name and length
friends_names_with_length = [(name, len(name)) for name in friends_names]

# Print the list of tuples
print(friends_names_with_length)

print("-------------------------x--------------------")

# Trip Expense Tracking
your_expenses = {
  "Hotel": 1200,
  "Food": 800,
  "Transportation": 500,
  "Attractions": 300,
  "Miscellaneous": 200
}

partner_expenses = {
  "Hotel": 1000,
  "Food": 900,
  "Transportation": 600,
  "Attractions": 400,
  "Miscellaneous": 150
}

# Calculate total expenses for each
your_total_expense = sum(your_expenses.values())
partner_total_expense = sum(partner_expenses.values())

print("Your total expense:", your_total_expense)
print("Partner's total expense:", partner_total_expense)

# Determine who spent more
if your_total_expense > partner_total_expense:
  print("You spent more overall.")
elif your_total_expense < partner_total_expense:
  print("Your partner spent more overall.")
else:
  print("You and your partner spent the same amount overall.")

# Find category with significant difference (assuming significant difference is 100 or more)
significant_difference = 100
max_difference_category = None
max_difference = 0

for category, amount in your_expenses.items():
  partner_amount = partner_expenses.get(category, 0)  # Handle missing category in partner's expenses
  difference = abs(amount - partner_amount)
  if difference >= significant_difference and difference > max_difference:
    max_difference_category = category
    max_difference = difference

if max_difference_category:
  print(f"Significant difference in spending for category: {max_difference_category} (Difference: {max_difference})")
else:
  print("No significant difference in spending categories found.")

# Task 9
class MobilePhone:
  """Base class representing a mobile phone."""

  def __init__(self, screen_type="Touch Screen", network_type="4G/5G", dual_sim=True,
               front_camera="8MP", rear_camera="16MP", ram="3GB", storage="32GB"):
    self.screen_type = screen_type
    self.network_type = network_type
    self.dual_sim = dual_sim
    self.front_camera = front_camera
    self.rear_camera = rear_camera
    self.ram = ram
    self.storage = storage

  def make_call(self, number):
    print(f"Dialing {number}...")

  def receive_call(self):
    print("Incoming call...")

  def take_a_picture(self):
    print(f"Taking a picture with {self.rear_camera} camera.")


class Apple(MobilePhone):
  def __init__(self, model, screen_size="5.5 inches", os="iOS", **kwargs):
    super().__init__(**kwargs)  # Call the parent class constructor with remaining arguments
    self.model = model
    self.screen_size = screen_size
    self.os = os

  def make_call(self):
    print(f"Making a FaceTime call...")
    
class Samsung(MobilePhone):

  def __init__(self, model, battery="4000mAh", **kwargs):
    super().__init__(**kwargs)  # Call the parent class constructor with remaining arguments
    self.model = model
    self.battery = battery

# Create Apple phone objects
iphone_11 = Apple("iPhone 11", screen_size="6.1 inches", front_camera="12MP", rear_camera="Dual 12MP")
iphone_13 = Apple("iPhone 13", os="iOS 16", screen_type="Super Retina XDR", ram="4GB", storage="128GB")

# Create Samsung phone objects
galaxy_s22 = Samsung("Galaxy S22", rear_camera="Triple 12MP", storage="256GB")
galaxy_a53 = Samsung("Galaxy A53", battery="5000mAh", front_camera="32MP")

# Call methods on the objects
iphone_11.make_call()  # Output: Making a FaceTime call...
iphone_13.take_a_picture()  # Output: Taking a picture with Dual 12MP camera.
galaxy_s22.receive_call()  # Output: Incoming call...