import random

# Anagram sets
anagrams = {
    "AEINORT": ["NOTAIRE", "OTARINE"],
    "AEEIORT": ["ETAERIO"],
    "ADEINOR": ["ANEROID"]
}

# Main loop
keys = list(anagrams.keys())
random.shuffle(keys)

while keys:
    prompt = keys.pop()
    print(f"Guess a word for: {prompt}")
    
    guess = input("> ").strip().upper()
    
    if guess in anagrams[prompt]:
        print("Correct!\n")
    else:
        print("Wrong!\n")
    
    if keys:
        cont = input("Press Enter for next word or type 'quit' to exit: ").strip().lower()
        if cont == "quit":
            break
