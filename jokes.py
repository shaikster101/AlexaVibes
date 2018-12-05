import random

jokes = ['Did you hear about the crook who stole a calendar? He got twelve months.',
'I own the world’s worst thesaurus. Not only is it awful, it’s awful.',
'Why do Dasher and Dancer love coffee? They’re Santa’s star bucks!',
'What’s a banana peel’s favorite pair of shoes? Slippers',
'What does the Gingerbread Man use to make his bed? Cookie sheets',
'What do you call an outlaw who steals gift wrapping from the rich to give to the poor? Ribbon Hood.',
'What did the big flower say to the little flower? Hi, bud!',
'If pilgrims traveled on the Mayflower, what do college students travel on? Scholar ships.',
'How is the alphabet different on Christmas from every other day? There is Noel.',
'What did the turkey say before it was roasted? Boy, I’m stuffed.',
'Why do turkeys always go gobble gobble? They never learned good table manners.',
'What do you call a running turkey? Fast food.',
'Why was King Arthur’s army too tired to fight? It had too many sleepless knights.',
'Which countrys capital has the fastest-growing population? Ireland. Every day it is Dublin.',
'What did the gym coach say to the cat? Have you paid your annual fleas?',
'Which fruit is a vampire’s favorite? A nectarine.',
'The barista says, how do you take your coffee? The coffee snob goes: very, very seriously.',
'Yesterday, a clown held the door open for me. It was such a nice jester!',
'How long do chickens work? Around the cluck!',
'What do you call sad coffee? Despresso.',
'What is the difference between a hippo and a Zippo? A hippo is really heavy, and a Zippo is a little lighter.',
'Why couldn’t the sesame seed leave the casino? He was on a roll!',
'Who’s a dessert’s favorite actor? Robert Brownie, Jr.',
'What do you call a cat that throws all the most expensive parties? The Great Catsby',
'Why did the skeleton climb up the tree? Because a dog was after his bones!',
'Why do birds fly south in the Fall? Because it’s too far to walk.',
'What did the leopard say after finishing a delicious meal? That hit the spot!',
'What’s the first thing you should do if a bull charges you? Pay him!',
'What is Forrest Gumps email password? 1Forrest.',
'How does a hurricane see? With its eye.',
'I wrote a song about a tortilla. Well actually, it’s more of a wrap.',
'Two antennas met on a roof, fell in love and got married. The ceremony was not much, but the reception was excellent.',
'What did the ocean say to the sailboat? Nothing, it just waved.',
'What lies at the bottom of the ocean and twitches? A nervous wreck.',
'Can bees fly in the rain? Not without their yellow jackets.',
'What does a dolphin say when he’s confused? Can you please be more Pacific?'
]

def joke():
    joke = jokes[random.randint(0,len(jokes)-1)]
    return joke
