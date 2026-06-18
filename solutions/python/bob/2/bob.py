def response(hey_bob):
    if hey_bob == None or hey_bob.strip() == "":
        return "Fine. Be that way!"
    letters:str = hey_bob.strip()
    if letters.isupper() and letters[len(letters)-1] == "?":
        return "Calm down, I know what I'm doing!"
    if letters[len(letters)-1] == "?":
        return "Sure."
    if letters.isupper():
        return "Whoa, chill out!"
    return "Whatever."