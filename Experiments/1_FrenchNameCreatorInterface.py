"""
French Name Generator
by Jiwoki

This programe allow you to generat a full french name by selecting a first name.
"""

import random

def generate_first_name():
    first_name = [
        "Alice", "Ambre", "Anna", "Camille", "Chloé", "Clara", "Emma", "Inès",
        "Jade", "Jeanne", "Julie", "Léa", "Léna", "Lina", "Louise", "Lucie",
        "Manon", "Margot", "Marie", "Mia", "Nina", "Océane", "Rose", "Sarah",
        "Zoé", "Adèle", "Agathe", "Alba", "Anaïs", "Charlotte", "Élise",
        "Eva", "Juliette", "Lola", "Maëlle", "Mathilde", "Noémie", "Romane",
        "Salomé", "Victoire",
        "Adam", "Alexandre", "Antoine", "Arthur", "Axel", "Baptiste", "Gabriel",
        "Hugo", "Jules", "Julien", "Léo", "Liam", "Louis", "Lucas", "Maël",
        "Mathis", "Nathan", "Noah", "Nolan", "Paul", "Raphaël", "Thomas",
        "Théo", "Victor", "Aaron", "Adrien", "Alexis", "Bastien", "Clément",
        "Ethan", "Gabin", "Gaspard", "Henri", "Jean", "Léon", "Maxime",
        "Milo", "Nicolas", "Oscar", "Pierre", "Rémi", "Romain", "Sacha",
        "Samuel", "Simon", "Timéo", "Tristan", "Yanis", "Yann"
    ]
    return first_name[random.randint(0,len(first_name))]

#func. used to add a second name to the first
def add_second_name(final_name):
    second_name_list = [
        "Martin", "Bernard", "Thomas", "Petit", "Robert",
        "Richard", "Durand", "Dubois", "Moreau", "Laurent",
        "Simon", "Michel", "Lefebvre", "Leroy", "Roux",
        "David", "Bertrand", "Morel", "Fournier", "Girard",
        "Bonnet", "Dupont", "Lambert", "Fontaine", "Rousseau",
        "Vincent", "Muller", "Lefèvre", "Faure", "André",
        "Mercier", "Blanc", "Guérin", "Boyer", "Garnier",
        "Chevalier", "François", "Legrand", "Gauthier", "Garcia",
        "Perrin", "Robin", "Clement", "Morin", "Nicolas",
        "Henry", "Roussel", "Mathieu", "Gautier", "Masson",
        "Marchand", "Duval", "Denis", "Dumont", "Marie",
        "Lemaire", "Noël", "Meyer", "Dufour", "Meunier",
        "Brun", "Blanchard", "Giraud", "Joly", "Rivière",
        "Lucas", "Brunet", "Gaillard", "Barbier", "Arnaud",
        "Martinez", "Gerard", "Roche", "Renard", "Schmitt",
        "Roy", "Leroux", "Colin", "Vidal", "Caron",
        "Picard", "Roger", "Fabre", "Aubert", "Lemoine",
        "Renaud", "Dumas", "Lacroix", "Olivier", "Philippe",
        "Tyrel","Jolie"
    ]

    final_result= final_name + " " + second_name_list[random.randint(0,14)]
    return final_result

# Main func. used to check for validity of the messy name
def messy_name_validator(messy_name):
    if messy_name == "":
        messy_name = generate_first_name()
    if len(messy_name) < 3: # No short names
        print("Too short!")
        return " ", False
    if len(messy_name) > 16: # No long names
        print("Too long!")
        return " ", False
    if messy_name.count('-') or messy_name.count(' ') > 1: # only one separator
        print("Make it more simple!")
        return " ", False
    if not messy_name.isalpha(): # only letters
        print("No numbers or symbols, sacrebleu!")
        return " ", False
    # Create compound name
    first_treatment = messy_name.replace('-',' ')
    second_treatment = first_treatment.split(' ')
    final_name = "-".join(second_treatment).title()
    final_result = add_second_name(final_name)

    return final_result, True

is_messy_name_valid = False
# while the name is not valid you must input a valid one
while is_messy_name_valid == False: 
    messy_name = input("> : ")
    final_result, is_messy_name_valid = messy_name_validator(messy_name.strip())

print(final_result)
