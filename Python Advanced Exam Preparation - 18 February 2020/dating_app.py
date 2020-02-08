from collections import deque


def match(males, females):
    males = [male for male in males if not male <= 0]
    females = deque([female for female in females if not female <= 0])
    matches_count = 0

    while len(males) > 0 and len(females) > 0:
        male = males.pop()
        female = females.popleft()
        if male % 25 == 0:
            males.pop()
            females.appendleft(female)
            continue
        if female % 25 == 0:
            females.pop()
            males.append(male)
            continue

        if not male == female:
            male -= 2
            if not male <= 0:
                males.append(male)
        else:
            matches_count += 1

    print(f"Matches: {matches_count}")

    males = [str(male) for male in males]
    females = [str(female) for female in females]

    if not len(males) == 0:
        print(f"Males left: {', '.join(list(reversed(males)))}")
    else:
        print("Males left: none")

    if not len(females) == 0:
        print(f"Females left: {', '.join(females)}")
    else:
        print("Females left: none")


males = list(map(int, input().split()))
females = list(map(int, input().split()))
match(males, females)

