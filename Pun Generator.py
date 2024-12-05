import random

punList = ['Did you hear about the guy who had his whole left side cut off? He is all right now.',
           'Road work ahead? I sure hope it does!',
          'What do you call an old snowman? Water.']

ranNum = random.randint(0, len(punList) - 1)

print(punList[ranNum])
