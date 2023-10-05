#!/usr/bin/env python3
"""
Camilo Castro
"""
#Globals
#user collection
usr_name = input("Please enter your name:\n>")          
usr_name = usr_name.title()    
usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))


#function for zodiac
def zodiac():
    sign_formula = usr_date % 12
    Zodiac = [
        "your zodiac sign is Rabbit, you are vigilant, witty, quick-minded, and ingenious.",
        "your zodiac sign is Rat, you are artistic, sociable, industrious, charming, and intelligent.",
        "your zodiac sign is Tiger, you are courageous, enthusiastic, confident, charismatic, and a leader.",
        "your zodiac sign is Ox, you are strong, thorough, determined, loyal, and reliable.",
        "your zodiac sign is Dragon, you are talented, powerful, lucky, and successful.",
        "your zodiac sign is Snake, you are wise, like to work alone, and determined.",
        "your zodiac sign is Horse, you are animated, active, and energetic.",
        "your zodiac sign is Sheep, you are creative, resilient, gentle, mild-mannered, and shy.",
        "your zodiac sign is Monkey, you are sharp, smart, curious, and mischievious.",
        "your zodiac sign is Rooster, you are hardworking, resourceful, courageous, and talented.",
        "your zodiac sign is Dog, you are loyal, honest, cautious, and kind.",
        "your zodiac sign is Pig, you are a symbol of wealth, honesty, and practicality.",
        ]
    print(f'{usr_name} {Zodiac[sign_formula]}')

#Run-time code
def main():
    zodiac()



#Call main function
if __name__ == "__main__":
    main()
