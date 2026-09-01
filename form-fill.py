"""
This python file is a form filling code for the form and gets a instatnes message with the personal quote at the end.
"""
import random
def name_fl(first_name: str, last_name:str) -> str :
    """
    This functiin is to concate the first and last names.
    """
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_details(name: str, age: int, place: str):
    """
    This functions get details of the name, age, place and returns a sentence with all of it.
    """
    sentence = name.title() + " is " + str(age) + " old and from " + place.title()
    return sentence

def generate_thank_notes(name: str) -> str:
    """
    This function generate the random thank you notes.
    """
    note_list = [
        "Thats the great time with you ",
        "Thank you ",
        "Visit again! ",
        "Be Grateful! ",
        "Thats nice serving you! "
    ]
    sentence = note_list[random.randint(0, len(note_list))] + name.title()
    return sentence


first_name = input("Enter your First Name:")
last_name = input("Enter your last Name: ")
age = int(input("Enter your age: "))
place = input("Enter your place: ")
name = name_fl(first_name , last_name )
print(get_details(name, age, place))
print(generate_thank_notes(name))
