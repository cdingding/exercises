
def findFriends(persons, friends): # things we want, and source we can use with condition: index for tuple pairs
    d = {}
    pairs = zip(persons, friends)
    for person in persons:
        fs = [f for (p,f) in pairs if p == person]
        d[person] = len(set([f for (p, f) in pairs if p in fs]))
    return d

if __name__ == "__main__":
    persons = ['Alice', 'Alice', 'Bob', 'Carol', 'Donald']
    friends = ['Bob', 'Donlad', 'Carol', 'Alice', 'Carol']
    print zip(persons, friends)
    print findFriends(persons, friends)