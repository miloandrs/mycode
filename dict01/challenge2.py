#!/usr/bin/env python3
"""
This is the introduction banner
"""


#Run-time code
def main():
	challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
	trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
	nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

	print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")

	ojos = trial[2]["goggles"]
	gafas = trial[2]["eyes"]
	print(f"My {ojos}! The {gafas} do {trial[3]}! ")
	
	ojos = nightmare[0]["user"]["name"]["first"]
	gafas = nightmare[0]["kumquat"]
	nada = nightmare[0]["d"]
	print(f"My {ojos}! The {gafas} do {nada}! ")

#Call main function
if __name__ == "__main__":
	main()
