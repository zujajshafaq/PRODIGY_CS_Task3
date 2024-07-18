import re

def password_strength(password):
    str = 0
    feedback = []

    # Length criteria
    if len(password) >= 8:
        str += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase and lowercase criteria
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        str += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")

    # Numbers criteria
    if re.search(r'[0-9]', password):
        str += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Special characters criteria
    if re.search(r'[@$!%*?&#]', password):
        str += 1
    else:
        feedback.append("Password should contain at least one special character.")

    return str, feedback

def main():
    password = input("Enter a password to check its strength: ")
    str, fb = password_strength(password)
    
    print(f"Password Strength: {str}")
    for comment in fb:
        print(comment)
    
    if str == 4:
        print(" Strong Password.")
    else:
        print("Not Strong password.")

if __name__ == "__main__":
    main()
