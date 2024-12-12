import random

punList = ['Did you hear about the guy who had his whole left side cut off? He is all right now.',
           'Road work ahead? I sure hope it does!',
           'Why dont elves like to share? Because theyre elfish.',
           'What do you get when you cross a snowman with a vampire? Frostbite.',
           'The existence of watermelons can only mean there is an earthmelon firemelon and airmelon. These are the elemelons.',
           'Why did only one letter in the alphabet receive Christmas presents? Because the rest were not E.',
           'Why did the little drummer boy go to bed early? He was beat.',
           'Why was six afraid of seven? Because seven ate nine.',
           'How did the skeleton know it was going to rain? He felt it in his bones.',
           'What do you call an exploding duck? A firequacker.']

print("How many puns should be generated? Pick a number between 1 and ", len(punList))
punAmount = int(input())
while punAmount <= 1 or punAmount >= len(punList):
    print("Out of range. Pick a number in range")
    punAmount = int(input())

ranList = []

def printPun():
    ranNum = random.randint(0, len(punList) - 1)
    ranList.append(ranNum)
    for i in range (len(ranList)):
            while ranNum == ranList[i]:
                    ranNum = random.randint(0, len(punList) - 1)

for i in range (punAmount):
    printPun()
    
for i in range (len(ranList)):
    print(punList[i])
