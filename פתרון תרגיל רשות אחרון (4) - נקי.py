import seaborn as sb
import re
import numpy as np
df = sb.load_dataset('titanic')

num_of_passengers = df['survived'].count()
num_of_survivers = len(df[df['survived'] == 1])
num_of_dead = len(df[df['survived'] == 0])
men = df['sex'] == 'male'
women = df['sex'] == 'female'
men_alive = (df['sex'] == 'male') & (df['survived'] == 1)
women_alive = (df['sex'] == 'female') & (df['survived'] == 1)
men_dead = (df['sex'] == 'male') & (df['survived'] == 0)
women_dead = (df['sex'] == 'female') & (df['survived'] == 0)
adult_men = (df['sex'] == 'male') & (df['age'] > 18)
not_adult_men = (df['sex'] == 'male') & (df['age'] < 18)
adult_women = (df['sex'] == 'female') & (df['age'] > 18)
not_adult_women = (df['sex'] == 'female') & (df['age'] < 18)
Southampton = df['embarked'] == 'S'
Cherbourg = df['embarked'] == 'C'
Queenstown = df['embarked'] == 'Q'
traveled_alone = df['alone'] == True
not_traveled_alone = df['alone'] == True
third_class = df['pclass'] == 3
seconed_class = df['pclass'] == 2 
first_class = df['pclass'] == 1


def p_name():
    name = input('Please enter your name here: ').capitalize()
    for i in range (1, 3):
        if name.isalpha() == False:
            print("We except names with letters only.")
            name = input('Please enter your name here: ').capitalize()
        else:
            print(f"Thank you {name}. let's proceed.")
            return name
    if name.isalpha() == False:
        print('We are going to adjust your answer so it will contains letters only')
        name = re.sub('[^a-zA-Z]', ' ', name)

def p_age():
    age = int(input('Please enter your age here: '))
    if age < 1 or age > 100:
        print('You cannot go aboard!')
        return False
    else:
        print('Thank you. A few questions more.')
        return True
        

def p_background():
    alone = input('Are you traveling alone? Type "Y" or "N": ').lower()
    location = input('Are you coming from Southampton, Cherbourg or Queenstown. Type "S", "C" or "Q": ').lower()
    print('Thank you. Just a few more steps...')
    return alone, location

def p_gender():
    p_gender = input('Please enter your gender here: ').lower()
    if p_gender == 'm' or p_gender == 'male' or p_gender == '0':
        p_gender = 'M'
    elif p_gender == 'f' or p_gender == 'female' or p_gender == '1':   
        p_gender = 'F'
    else: 
        print('please try again, type "M" or "F".')
        p_gender()
    return p_gender
    

def p_class():
    third_class_avg = df['fare'][df['pclass'] == 3].mean()
    second_class_avg = df['fare'][df['pclass'] == 2].mean()
    first_class_avg = df['fare'][df['pclass'] == 1].mean()
    p_price = int(input('how much are you willing to pay? '))
    a = abs(p_price - first_class_avg)
    b = abs(p_price - second_class_avg)
    c = abs(p_price - third_class_avg)
    if a > b:
        if b > c:
           print('you bought a ticket to third class...')
           p_class = 'third class'
           return p_class
        else:
           print('you bought a ticket to seconed class.')
           p_class = 'seconed class'
           return p_class
    else: #(a < b)
        if a > c:
           print('you bought a ticket to third class...')
           p_class = 'third class'
           return p_class
        else:
           print('you bought a ticket to first class!!') 
           p_class = 'first class'
           return p_class           
    

def tickiting():
    random_number = np.random.randint(9, size = 6)
    if random_number not in list_of_tickets_number:
       list_of_tickets_number.append(random_number)
       print(f'Your ticket number is {random_number}')
       return random_number
    else:
      tickiting()  


def serviver_rates(alone, location, p_gender, p_class):
    if alone == 'y':
        alone = traveled_alone
    else:
        alone = not_traveled_alone
    if location == 's':
        location = Southampton
    elif location == 'q':
        location = Queenstown
    else:
        location = Cherbourg
    if p_gender == 'M':
        gender = men
        alive = men_alive
    else:
        gender = women
        alive = women_alive
    if p_class == 'third class':
        classs = third_class
    elif p_class == 'seconed class':
        classs = seconed_class
    else:
        classs = first_class
    
    survival_rate = int((len(df[(alone) & (location) & (gender) & (classs) & (alive)])/ len(df[(gender) & (location) & (alone) & (classs)]))* 100)
    return survival_rate


def printing(p_class, name, p_gender, survival_rate):
    if p_gender == 'M':
        nick = 'Mr.'
    else:
        nick = 'Mrs.'
    with open(f'Ticket {ticket_number}', 'w') as file:
        file.write(f'Welcome aboard {nick}{name}, this is a ticket to {p_class}' + '\n')
        file.write(f"Just a fun FYI - you'r survival rate is {survival_rate}%" + '\n')
        file.write("we're crossing fingers for you")
        

list_of_tickets_number = []

print('Greetings New Passenger!')
name = p_name()
if p_age() == True:
  alone, location = p_background()
  p_gender = p_gender()
  p_class = p_class()
  ticket_number = tickiting()
  survival_rate = serviver_rates(alone, location, p_gender, p_class)
  printing(p_class, name, p_gender, survival_rate)
  print('Your ticket has been printed for you. Good bye. Have a nice day :)')
else:
  print('Good bye. Have a nice day :)')
    

 
    
    
    
    
    

