"""
French Name Generator
by Jiwoki

This programe allow you to generat a full french name by selecting a first name and pick a second name randomly for you!  
"""

# Main func. used to check for validity of the messy name
def messy_name_validator(messy_name):
    if len(messy_name) < 3: # No short names
        print("Too short!")
        return " ", False
    if len(messy_name) > 14: # No long names
        print("Too long!")
    if messy_name.count('-') or messy_name.count(' ') > 1: # only one separator
        print("Make it more simple!")
        return " ", False
    if not messy_name.isalpha(): # only letters
        print("No numbers or symbols, sacrebleu!")
        return " ", False
    # Create compound name
    first_treatment = messy_name.replace('-',' ')
    second_treatment = first_treatment.split(' ')
    final_result = "-".join(second_treatment).title()

    return final_result, True

is_messy_name_valid = False
# while the name is not valid you must input a valid one
while is_messy_name_valid == False: 
    messy_name = input("Enter your name: ")
    final_result, is_messy_name_valid = messy_name_validator(messy_name.strip())

print(final_result)
