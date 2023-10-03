#!/usr/bin/env python3
"""
This is the introduction banner
"""


#Run-time code
def main():
    
	#User character selection
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n>>")
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n>>")

    #Dictionary of characters
    marvelchars= {
	"Starlord":
	  {"real name": "peter quill",
	  "powers": "dance moves",
	  "archenemy": "Thanos"},

	"Mystique":
	  {"real name": "raven darkholme",
	  "powers": "shape shifter",
	  "archenemy": "Professor X"},

	"Hulk":
	  {"real name": "bruce banner",
	  "powers": "super strength",
	  "archenemy": "adrenaline"}
	             }
	  
	  #function for the phrase
	  def char_print():
		print(f"{marvelchars[char_name]} \'s {char_stat} is : {marvelchars[char_name](char_stat)}")

	char_print()




#Call main function
if __name__ == "__main__":
	main()
