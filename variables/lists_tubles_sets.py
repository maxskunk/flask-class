# grades = [77,80,90,95,100,105,107]
#
# print(sum(grades)/len(grades))
# print("You Know {}!".format(grades))


#
def who_do_you_know():
    people = input("Enter the people you know, separated by commas")
    people_list = people.split(",")#inputList.split
    people_without_spaces = []
    for person in people_list:
        people_without_spaces.append(person.strip())
    return people_without_spaces

def ask_user():
    person = input("Who do you know?")
    if person in who_do_you_know():
        print("You know this person")


ask_user()
