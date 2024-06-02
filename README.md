# Modern Software Development Project

Final project for CSCI 4322

## Description

This application combines Unreal Engine's immersive environments with a realistic Metahuman and emotion detection technology. Adding depth to the experience is the integration of the Eliza Therapist Chatbot, providing users with emotional support and guidance.

## Usage

### First, start the API

The API can be started from the root directory using the following terminal commands.
```
python .\API\apiServer.py
```

### Then, start the Unreal Engine project

- Install the Metahuman SDK from https://www.unrealengine.com/marketplace/en-US/item/66b869fa0d3748e78d422e59716597b6 to Unreal Engine. 
- Obtain an API token for the Metahuman SDK. This is not a free service, so we will not be providing our API token. 
- From the root directory, navigate to /Unreal/Metahuman.
- Double click Metahuman.uproject to open. 
- In Unreal Engine, navigate to Edit -> Project Settings -> Plugins -> Metahuman SDK. 
- Enter your API token, save, and close the Project Settings window. 
- From the Content Drawer, open the file named Level
- Press Play! 

Original files sourced from https://github.com/wadetb/eliza

# Appended From Original README
## Eliza chatbot in Python

Loosely based on Charles Hayden's version in Java, at http://chayden.net/eliza/Eliza.html. 

I feel that it is fairly complete. However there are some holes, as the library was written immediately prior to my discovery of Joseph Weizenbaum's own description of the original program, which is quite detailed, along with the original "doctor" script. Oh well. A copy of that article is provided in the repo as a reference to the correct behavior.

### Usage

Can be run interactively:

```
$ python eliza.py
How do you do.  Please tell me your problem.
> I would like to have a chat bot.
You say you would like to have a chat bot ?
> bye
Goodbye.  Thank you for talking to me.
```

...or imported and used as a library:

```python
import eliza

eliza = eliza.Eliza()
eliza.load('doctor.txt')

print(eliza.initial())
while True:
    said = input('> ')
    response = eliza.respond(said)
    if response is None:
        break
    print(response)
print(eliza.final())
```
