import tweepy
from tweepy.auth import OAuthHandler

# YOUR KEEEEYS

ACCESS_KEY = ""
ACCESS_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

n = False

while n == False:
    print("Verify authentication: Type 1 \nCheck some user's details: Type 2")
    print("Follow some user: Type 3\nPost something: Type 4\nChange bio: Type 5")
    print("Last posts with #kutopusu: Type 6")
    n = int(input("Input: "))

    if n == 1:
        try:
            api.verify_credentials()
            print("Status: Ok")
        except:
            print("Status: Error")

    elif n == 2:
        y = input("User you want to know the details: ")
        user = api.get_user(y)
        print("Details:")
        print("Name:", user.name)
        print("Description:", user.description)
        try:
            if user.location[0] is True:
                print("Local:", user.location)
        except:
            print("Local: Unknown")

    elif n == 3:
        z = input("User you want to follow: ")
        api.create_friendship(z)
        print (z, "was followed")

    elif n == 4:
        x = input("Post: ")
        api.update_status(x)
        print("The message", "'", x, "'", "was sent")

    elif n == 5:
        b = input("Bio: ")
        api.update_profile(description = b)
        print ("Bio changed to: ", b)

    elif n == 6:
        for tweet in api.search(q = "#kutopusu", rpp = 20):
    else:
        print("Invalid input")
    print("")
    cont = input("Continue? (y/n) \nInput: ")
    print("")
    cont = cont.lower()
    if cont == "y":
        n = False
    elif cont == "n":
        n = True
    else:
        print("I will consider that as a no :)")
        n = True
