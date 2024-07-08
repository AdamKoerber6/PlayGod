#element creator
#water air fire earth -----
 
#water fire = steam
#fire earth = lava
#fire air = lightning
#air earth = sand
#water earth = clay
#water air = rain

#water air fire earth steam lava lightning sand clay rain

#water + lava = stone
#air + sand = dust
#fire + sand = glass
#fire + clay = brick
#earth + lava = volcano
#earth + rain = mud
#steam + air = cloud
#steam + earth = geyser
#lightning + rain = storm

#water air fire earth steam lava lightning sand clay rain stone mud
#dust glass brick volcano cloud geyser storm

#air + cloud = tornado
#air + storm = hurricane
#fire + mud = dirt
#fire + stone = metal
#earth + volcano = mountain

#24 elements total

combinations = {
    ("water", "fire"): "steam",
    ("fire", "earth"): "lava",
    ("fire", "air"): "lightning",
    ("air", "earth"): "sand",
    ("water", "earth"): "clay",
    ("water", "air"): "rain",
    ("water", "lava"): "stone",
    ("air", "sand"): "dust",
    ("fire", "sand"): "glass",
    ("fire", "clay"): "brick",
    ("earth", "lava"): "volcano",
    ("earth", "rain"): "mud",
    ("steam", "air"): "cloud",
    ("steam", "earth"): "geyser",
    ("lightning", "rain"): "storm",
    ("air", "cloud"): "tornado",
    ("air", "storm"): "hurricane",
    ("fire", "mud"): "dirt",
    ("fire", "stone"): "metal",
    ("earth", "volcano"): "mountain"
}

all_elements = ["water", "air", "fire", "earth", "steam", "lava", "lightning", "sand", "clay", "rain", "stone", "mud", "dust", "glass", "brick", "volcano", "cloud", "geyser", "storm", "tornado", "hurricane", "dirt", "metal", "mountain"]
elements_discovered = ["water", "air", "fire", "earth"]

#game_start
print("Welcome, combine elements to create more elements.")
print("Elements currently known: {}/24".format(len(elements_discovered)))
print(elements_discovered)


while (True):

    input_string = input("Enter two elements to combine (or 'exit' to quit): ")

    if input_string == "exit":
        break

    input_string = input_string.split()
    

    if len(input_string) != 2:
        print("Please enter exactly two elements.")
        continue

    combine_element1, combine_element2 = input_string
    if (combine_element1, combine_element2) in combinations:
        result = combinations[(combine_element1, combine_element2)]
    elif (combine_element2, combine_element1) in combinations:
        result = combinations[(combine_element2, combine_element1)]
    else:
        print("These elements do not combine into anything new.")
        continue

    if result not in elements_discovered:
        print(f"New element discovered: {result}")
        elements_discovered.append(result)
    else:
        print(f"You already discovered: {result}")
    
    print("Elements currently known: {}/24".format(len(elements_discovered)))
    print(elements_discovered)

print("Thank you for playing")