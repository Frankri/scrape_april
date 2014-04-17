def get_password():
    import random
    # Make a list of all of the words in our system dictionary
    f = open('/usr/share/dict/words')
    words = [x.strip() for x in f.readlines()]
    # Pick 2 random words from the list
    password = '-'.join(random.choice(words) for i in range(2)).capitalize()
    # Remove any apostrophes
    password = password.replace("'", "")
    # Add a random number to the end of our password
    password += str(random.randint(1, 9999))
    return password

print get_password()