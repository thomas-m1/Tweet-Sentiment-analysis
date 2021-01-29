# Thomas Michalski
# Assignment 3 - Sentiment Analysis
# March 25th, 2019
#this file is called on from the main file

def area(tweetValue, latitude, longitude):
    if latitude >= 24.660845 and latitude <= 49.189787: # checks what location tweet is from
        if longitude < -67.444574 and longitude >= -87.518395:
            result = "e" + str(tweetValue)
        elif longitude < -87.518395 and longitude >= -101.998892:
            result = "c" + str(tweetValue)
        elif longitude < -101.998892 and longitude >= -115.236428:
            result = "m" + str(tweetValue)
        elif longitude < -115.236428 and longitude >= -125.242264:
            result = "p" + str(tweetValue)
        else:
            result = "null"
    else:
        result = "null"
    return result

def compute_tweets(tweets, keywords):


    pacValue = 0
    cenValue = 0
    mouValue = 0
    easValue = 0
    nulValue = 0

    pacTweets = 0
    cenTweets = 0
    mouTweets = 0
    easTweets = 0

# opens files
    twitter = open("tweets.txt", "r",encoding="utf‐8")
    keys = open("keywords.txt", "r",encoding="utf‐8")

    keyNums = []
    keyList = []

#loop is used to assess the key words file and make lists of the key words and their corresponding values
    for line in keys:
        word = line
        word = word.split(",")
        number = word[1]
        number = number.rstrip("\n")
        number = int(number)
        keyNums.append(number)
        keyList.append(word[0])

    for line in twitter:
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        tweetValue = 0
        words = []
        line1 = line

        line1 = line1.split()#splits line
        length = len(line1)

        for i in range (5, (length)):
            word = line1[i]
            word = word.lower()
            no_punct = ""
            for char in word:
                if char not in punctuations:
                    no_punct = no_punct + char
            words.append(no_punct)

        num = len(words)
        keywords = 1

        for i in range(0, num):
            if words[i].isalpha() == True:
                for j in range (0, 54):
                    if words[i] == keyList[j]:
                        tweetValue += keyNums[j]
                        keywords += 1

        tweetValue = tweetValue / keywords

#strips characters
        long = line1[1]
        lat = line1[0]
        lat = lat.strip("[")
        lat = lat.strip(",")
        long = long.strip("]")

        lat = float(lat)
        long = float(long)

        call = area(tweetValue, lat, long)

        leg = len(call)

#determines location and its association
        if call[0] == "n":
            nulValue += 1
        else:
            if call[0] == "p":
                pac = float(call[1:leg])
                if pac != 0:
                    pacValue += pac
                    pacTweets += 1
            elif call[0] == "c":
                cenValue += float(call[1:leg])
                cen = float(call[1:leg])
                if cen != 0:
                    cenValue += cen
                    cenTweets += 1
            elif call[0] == "m":
                mou = float(call[1:leg])
                if mou != 0:
                    mouValue += mou
                    mouTweets += 1
            elif call[0] == "e":
                eas = float(call[1:leg])
                if eas != 0:
                    easValue += eas
                    easTweets += 1

#does calculations
    pacValue = pacValue / pacTweets
    cenValue = cenValue / cenTweets
    mouValue = mouValue / mouTweets
    easValue = easValue / easTweets


    pacific = [pacValue, pacTweets]
    central = [cenValue, cenTweets]
    mountain = [mouValue, mouTweets]
    eastern = [easValue, easTweets]
    result = [pacific, central, mountain, eastern]

    return result
