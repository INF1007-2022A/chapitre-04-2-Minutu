#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	name_splitted=name.split('-')
	Name=name_splitted[0].capitalize()
	return f'Bonjour {Name}'

def get_random_sentence(animals, adjectives, fruits):
	adjective=adjectives[random.randrange(0,len(adjectives))]
	animal=animals[random.randrange(0,len(animals))]
	fruit=fruits[random.randrange(0, len(fruits))]
	return f'Aujourd\'hui, j\'ai vu un {animal} s\'emparer d\'un panier {adjective} plein de {fruit}'

def encrypt(text, shift):
	result=''
	for letter in text:
		encrypted_letter=letter
		if letter.isalpha():
			index=ord(letter.upper())-ord('A')
			encrypted_index=(index+shift)%26
			encrypted_letter=chr(encrypted_index+ord('A'))
		result+=encrypted_letter
	return result

def decrypt(encrypted_text, shift):
	return encrypt(encrypted_text, -shift)


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
