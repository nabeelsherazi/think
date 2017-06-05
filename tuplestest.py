fisherman_gear = [
("Bob", ["Rapala Countdown", "Rapala Floater", "Abu Garcia Rod", "St. Croix Reel"]),
("Joe", ["Generic Spinner", "Frog Popper", "Walmart Rod", "Walmart Reel"]),
("Billy", ["Rapala Floater", "Generic Spinner", "Abu Garcia Rod", "Walmart Reel"])]

abugarcia_counter = 0
stcroix_counter = 0
print(len(fisherman_gear), "fisherman in total.")
for (fisherman, gear) in fisherman_gear:
    print(fisherman, "owns", gear)
for (fisherman, gear) in fisherman_gear:
    for g in gear:
        if "Walmart" in gear or "Generic" in g:
            print(fisherman, "is a cheap hoe.")
            break
    print(fisherman, "has", len(gear), "pieces of gear in total.")
    rapala_counter = 0
    for g in gear:
        if "Rapala" in g:
            rapala_counter += 1
    if rapala_counter >= 1:
        print(fisherman, "reps", rapala_counter, "pieces of gear from Rapala. What a sellout.")
    for g in gear:
        if "Abu Garcia" in g:
            abugarcia_counter += 1
        elif "St. Croix" in g:
            stcroix_counter += 1
print(abugarcia_counter, "fisherman had some Abu Garcia gear.")
print(stcroix_counter, "fisherman had some St. Croix gear.")
print("Isn't that wild?")
input()
