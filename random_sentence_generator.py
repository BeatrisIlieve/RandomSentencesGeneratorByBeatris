# importing colorama module in order to add colours to the text
import colorama
from colorama import Fore, Style

# importing random module
import random

# welcoming the user
my_list = ['Welcome', 'to', 'A','Random', 'Sentence', 'Generator', 'game','!\n']
for starting_index in range(len(my_list), -1, -1):
    if starting_index % 2 == 0:
        my_list.insert(starting_index, f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}")
    else:
        my_list.insert(starting_index, f"{Fore.LIGHTBLUE_EX}")
print(" ".join(my_list))

# greeting the user
def say_hello(first_name):
    print(f"Hello, {first_name}!")


name = input("Please, enter your name: ")
say_hello(name)

print()

# inviting the user to start generating random sentences
input(f"{Fore.LIGHTCYAN_EX}Enter {Fore.WHITE}[y] {Fore.LIGHTCYAN_EX}to generate a random sentence: ")
print()

# creating lists with all the words we will use to create a random sentences
names = ["Marilyn Monroe", "Donald Trump", "Adolf Hitler", "Albert Enstein", "Michael Jackson", "Charlie Chaplin",
         "Madonna", "Vladimir Putin", "Cristiano Ronaldo", "Walt Disney", "Lady Gaga", "George Clooney", "Beethoven",
         "Isaac Newton", "Bill Gates", "Mark Zuckerberg", "Lenin", "Al Pacino", "Justin Bieber", "Brad Pitt",
         "Justin Timberlake", "Elon Musk"]

places = ["Camelot", "Arcadia", "El Dorado", "Fairy Land", "Never Land ", "the Promised Land", "Shangri La",
          "the Underworld", "Utopia", "Wonderland"]

verbs = ["approaches", "bounces back", "chases after", "climbs to", "crawls under", "dances with",
         "dives into", "drags out", "flees to", "flies above", "hurries up", "jumps over",
         "moves away", "rushes to", "shakes like", "skips to", "slides into", "stretches",
         "walks toward", "waltzes with", "zips"]

nouns = ["a history", "an art", "some information", "the government", "any music", "a theory", "a law", "a power",
         "the economics", "the love", "a science", "a library", "a society", "an oven", "an exam", "the physics",
         "a boyfriend", "a girlfriend", "the philosophy", "the chemistry", "an imagination", "a poetry", "a guitar",
         "a lady", "a gentleman", "a poet", "a shirt", "the sky", "a cat", "a dolphin", "an icecream", "some pleasure",
         "a dress", "some wine"]

adverbs = ["cautiously", "enthusiastically", "gently", "doubtfully", "gracefully", "cheerfully", "excitedly",
           "courageously", "cruelly", "elegantly", "gladly", "happily", "stylishly"]

details = ["at a nearby farm", "by the side of the river", "in the mountains", "in the toy department", " in the lake",
           "on the beach", "in the helicopter", "by the fireplace", "in the Solar System", "on the sofa",
           "through a forest", "on New Year’s Eve", "at the restaurant", "in the library"]

#creating a function that returns random words every time
def get_random_word(words):
    return random.choice(words)

# looping until the user chooses to continue generating random sentences
while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    print(f"{Fore.LIGHTYELLOW_EX}{random_name} from {random_place} {random_verb} "
          f"{random_noun} {random_adverb} {random_detail}.")
    print()
    input(f"{Fore.LIGHTCYAN_EX}Enter {Fore.WHITE}[y] {Fore.LIGHTCYAN_EX}to generate a random sentence: ")
    print()
