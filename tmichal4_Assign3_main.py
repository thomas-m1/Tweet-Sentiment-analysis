# Thomas Michalski
# Assignment 3 - Sentiment Analysis
# March 25th, 2019
#this is the main file

print("Hello, welcome to my twitter sentiment analysis\n") #introduction

from tmichal4_Assign3_sentiment_analysis import compute_tweets #importing second python file

#prompts user
first = input("Enter the first file name (tweets): ")
second = input("Enter the second file name (keywords): ")

result = compute_tweets(first, second)

#prints results
print("Pacific: " + format(result[0]))
print("Central: " + format(result[1]))
print("Mountain: " + format(result[2]))
print("Eastern: " + format(result[3]))
