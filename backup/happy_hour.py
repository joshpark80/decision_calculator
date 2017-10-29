import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samule L. Jackson"]

random_bar = random.choice(bars)
random_person1 = random.choice(people)
random_person2 = random.choice(people)

print("How about you go to %s with %s and %s?" % (random_bar, random_person1, random_person2))
