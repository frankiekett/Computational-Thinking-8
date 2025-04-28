import random
# Pick a word at random
word_list = ["apple","about","actor","adore","after","again","align","alike","allow","amaze","angel","angry","apart","apply","arise","asset","atone","audio","audit","awake","aware","beach","beady","beams","beast","begin","being","belly","below","beset","besty","bible","bison","blame","bliss","block","blood","bluff","blush","board","boast","boils","bonus","booze","brake","brave","brawl","bread","breed","bribe","brick","broth","brown","brute","build","burnt","burst","bushy","cable","campy","candy","canal","canny","cause","charm","cheap","check","chill","chip","chose","clamp","clash","clasp","class","clear","clerk","click","cliff","climb","clock","clogs","close","cluck","cocoa","coils","coins","color","comet","cooky","cools","copper","coral","corer","corky","cosmo","cough","crops","crown","crush","curbs","curve","cyber","dance","danger","dealt","death","debar","debts","decks","deeds","depth","dirty","ditch","docks","doing","donor","door","doubt","draft","drain","drake","dream","dress","drink","drive","drove","dryly","doubt","drown","elbow","email","enact","enter","entry","equal","event","every","exert","exist","extra","faith","fancy","fears","feast","felts","fewer","fever","fines","fixes","flame","flaps","flash","fleet","flood","fluff","focus","force","fores","forth","found","frame","frank","front","froze","frown","fuddy","gains","gally","gaped","gates","gayer","gear","gears","goals","goofy","gory","grasp","grate","grave","grind","grape","grows","group","gushy","habit","haste","havey","heals","heart","heavy","herbs","hitch","hoard","hoist","holds","house","hover","hurry","hurts","hype","idyll","image","imply","incus","infer","inks","input","irate","items","issue","jacks","jaded","jelly","jolly","joint","jumpy","judge","jumps","jumpy","june","kicks","kings","knack","knees","knock","known","lapse","latch","lateral","leads","leads","leads","lends","leaps","least","leash","leaks","liars","light","lobby","louds","liver","lions","lifts","lobby","loose","loops","loyal","lunar","lunch","lures","maker","mainy","mines","meals","miser","march","money","moves","moose","molly","newer","names""ocean","offer","often","opine","order","other","ought","owner","paint","party","peach","peace","peppy","piano","piece","piles","place","plaza","plume","plumb","point","poise","poker","polls","porch","proud","prose","prune","purse","raise","rally","raven","reach","ready","reply","right","rival","roast","robin","rocky","rough","round","route","ruble","ruler","rumpy","salts","sandy","scale","scene","score","scout","scrap","seeds","seers","seize","sense","serve","seven","shape","share","sheen","shoes","shoot","shore","shrub","shrub","sight","signs","silly","since","siree","skate","skirt","slash","slink","sleep","slice","slink","smash","smile","smoke","socks","soapy","solar","sorry","south","space","speak","spear","speed","spell","spice","spine","spoon","stack","stain","stare","stays","steel","stone","store","straw","stuck","stunt","sugar","super","sweet","sworn","taken","tasty","teach","thick","thief","thing","think","third","those","throw","thump","tight","tilde","timey","tonal","tools","tooth","topaz","total","touch","tower","track","trait","traps","treat","trend","trial","tried","troop","trove","truth","turns","ultra","under","unite","until","upper","urban","used","usher","vocal","voter","vowel","wager","wakes","waste","water","watch","weakly","weary","weave","whale","where","which","white","whole","whose","wider","widow","winks","wipes","woman","women","worry","worse","world","wound","write","wrong","yacht","yearn","yellow","yells","yokes","young"]
hidden_word = random.choice(word_list)

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # second letter (in python, counting starts at 0 not 1)
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # third letter (in python, counting starts at 0 not 1)
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # fourth letter (in python, counting starts at 0 not 1)
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # fifth letter (in python, counting starts at 0 not 1)
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i+1} guesses")
