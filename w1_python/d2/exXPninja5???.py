#Keep asking the user to input the longest sentence they can without the character “A”.
#Each time a user successfully sets a new longest sentence, print a congratulations message.

# Step 1: Initialize the longest_sentence variable
longest_sentence = ""  # Start with an empty string as the longest sentence

# Step 2: Use a loop to keep asking for input
while True:
    user_input = input('write the longest sentence without the character A: ')
    user_input_length = len(user_input)

    if 'a' not in user_input:
        print("congrats! you did, but do better!")
        print(f"Your sentence was {user_input_length} chars long")
        
    else:
        print("You have an A in your sentence")