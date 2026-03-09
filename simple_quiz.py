print("Welcome to the Quiz Game!")

questions = {
    "Who is the main protagonist of Naruto? ": "naruto",
    "What is Naruto's signature move? ": "rasengan",
    "In Demon Slayer, what are the demon hunters called? ": "demon slayers",
    "Who wields Sun Breathing in Demon Slayer? ": "tanjiro",
    "What village is Naruto from? ": "konoha",
    "What is the demon king in Demon Slayer? ": "muzan",
    "Who is Naruto's rival and teammate? ": "sasuke",
    "What is Tanjiro's sister's name? ": "nezuko",
    
    # 20+ NEW Naruto questions
    "Who sealed the Nine-Tails inside Naruto? ": "minato",
    "What is the name of the elite ninja group protecting the Hokage? ": "anbu",
    "Which sannin trained Sakura? ": "tsunade",
    "What is Gaara's village? ": "suna",
    "Who is the leader of Akatsuki? ": "pain",
    "What eye power does Kakashi have? ": "sharingan",
    "What is Rock Lee's forbidden technique? ": "primary lotus",
    "Who killed the Third Hokage? ": "orochimaru",
    "What is Naruto's favorite food? ": "ramen",
    "What bridge is named after Naruto? ": "naruto bridge",
    "What is Itachi's clan? ": "uchiha",
    "Who is the Fourth Hokage? ": "minato",
    "What animal is sealed in Naruto? ": "nine tails",
    "What jutsu multiplies Naruto? ": "shadow clone",
    
    # NEW Demon Slayer questions
    "Who leads the Demon Slayer Corps? ": "kagaya ubuyashiki",
    "What swords kill demons? ": "nichirin",
    "What flower kills demons? ": "wisteria",
    "Who has a boar mask? ": "inosuke",
    "What is the strongest breathing style? ": "sun breathing",
    "Who is the Stone Hashira? ": "gyomei",
    "Who is Zenitsu's former companion demon? ": "kaigaku",
    "What is Nezuko's muzzle made of? ": "bamboo"
}

score = 0

for question in questions:
    
    answer = input(question).lower()
    
    if answer == questions[question]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Your final score is:", score)


