# Prompt the user for their current age
from datetime import datetime
current_age = int(input("How old are you?: "))
# Calculate the age in 2050
years_to_2050 = 2050 - datetime.now().year # 27 years
age_in_2050 = current_age + years_to_2050
print(f"In 2050, you will be {age_in_2050} years old.")


