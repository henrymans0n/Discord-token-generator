
## WARNING



                THIS PROJECT IS PURELY FOR EDUCATIONAL PURPOSES ONLY 
                        AND IS A PROOF OF CONCEPT (POC)
                I AM NOT TO BE BLAMED FOR ANY MISUSE OF THE PROJECT
# Discord token generator and validator

A python script that generates (N) Amount of discord tokens, to be validated in the hopes that one/some of the tokens are valid.




Note: There is a very low chance of an actual valid token to be generated.

# Tested on:

Windows:  ✅
Linux:    ✅

# How it works:

1 -> The python script creates a txt file with (N) amount of tokens that you requested.
2 -> The python script will then validated the tokens generated one by one.
3 -> Following results will be displayed on terminal: [token] + [valid/invalid]
4 -> IF a token is found to be valid, it will be saved in a different txt file as a valid one.

## Run Locally  


Clone the project

```bash
  git clone https://github.com/henrymans0n/Discord-token-generator
```

Go to the project directory

```bash
  cd Discord-token-generator/Discord-token-generator
```

Install dependencies

```bash
  pip install discord.py
  pip install requests
```

Start the script

```bash
  python3 discord_gen_validator.py
```

