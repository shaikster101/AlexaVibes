import random 

motivation = [
'Here is a quote: The best way to predict your future is to create it.',
'Here is a quote from Earl Nightingale: Do not let the fear of the time it will take to accomplish something stand in the way of your doing it. The time will pass anyway; we might just as well put that passing time to the best possible use.',
'Here is a quote from Zig Ziglar: People often say that motivation does not last. Well, neither does bathing - that is why we recommend it daily.',
'Here is a quote from Yoda: Do, or do not. There is no try.',
'Here is a quote from Spock: One can begin to reshape the landscape with a single flower.',
'Here is a quote from Arlen Price: Where the heart is willing, it will find a thousand ways. Where it is unwilling, it will find a thousand excuses.',
'Here is a quote from George Bernard Shaw: People are always blaming their circumstances for what they are. I do not believe in circumstances. The people who get on in this world are the people who get up and look for the circumstances they want, and if they cannot find them, make them.',
'Here is a quote from Charles Buxton: You will never find time for anything. If you want time you must make it.',
'Here is a quote from Victor Kiam: Procrastination is the assassin of opportunity.',
'Here is a quote from The Office by Wayne Gretzky: You miss 100 percent of the shots you dont take.',
'Here is a quote from Lloyd Jones: Those who try to do something and fail are infinitely better than those who try to do nothing and succeed.',
'Here is a quote from LeBron James: The best teacher in life is experience.',
'Here is a quote from Abraham Lincoln: In the end, it is not the years in your life that count - it is the life in your years.',
'Here is a quote from Frasier Crane: In the end, what we regret most are the chances we never took.',
'Here is a quote from Zig Ziglar: What you get by achieving your goals is not as important as what you become by achieving your goals.'
]


def joke():
    quote = motivation[random.randint(0,len(motivation)-1)]
    return quote
