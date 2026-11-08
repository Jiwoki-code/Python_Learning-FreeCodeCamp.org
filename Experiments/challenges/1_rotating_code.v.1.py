import random

def create_multiplication():
    first_terme = random.randint(2, 9)
    second_terme = random.randint(2, 9)
    expression = str(first_terme) + ' x ' + str(second_terme) + ' = '
    result = first_terme * second_terme

    return expression, result

def setup_exercice():
    settings_valid = False
    print('At first, you must enter how many multiplication you want to solve\n(10 by default, 30 maximum)\n')
    while not settings_valid:
        this_many_multiplication = input('> ')
        if not this_many_multiplication.isnumeric():
            print('You should enter an integer!\n')
            continue
        else:
            this_many_multiplication = int(this_many_multiplication)
        if this_many_multiplication > 30:
            print('30 maximum!\n')
            continue
        if this_many_multiplication <= 0 or this_many_multiplication == '':
            this_many_multiplication = 10
        settings_valid = True
    print(f'You chose {this_many_multiplication} multiplications!\n')
    return this_many_multiplication    

def testing(this_many_multiplication):
    i = 0
    score = 0
    while i < this_many_multiplication:
        expression, result = create_multiplication()
        anwser = input(str(i+1) + " - " + expression)
        if int(anwser) == result:
            score += 1 
        i += 1
    return str(score) + '/' + str(this_many_multiplication)

def main():
    playing = True
    print("""    Welcome to our mind-calculating app!

    In this app you will be challenged by a number of multiplications of your choice
        
    Afterward a note is assign to your work but do not panic because
        
    .. in the end, there is always a way to become better! :)
    """)

    while playing:
        score = testing(setup_exercice())
        input(f"""
    Your score is : {score} !

    You can close the tab or try again by pressing enter.\n    Thanks for playing!\n""")

main()