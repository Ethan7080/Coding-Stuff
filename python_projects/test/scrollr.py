users = ['Evilcorp','eatHalf','flyGreen']
bios = ["Your best choice. Most likely, your only choice","Half the food for twice the price", "Eco-friendly flying: it's not just for birds anymore"]
locations = ['Classified','San Francisco, CA','Chicago, IL']
verifications = ['Verified Plus','Verified','Verified']
followers = [800000000,6000000,1500000]
following = [0,120,20]
def get_user_bio(username):
    for i in range(len(bios)):
        if users[i] == username:
            return bios[i]
def get_user_location(username):
    for i in range(len(locations)):
        if users[i] == username:
            return locations[i]
def get_user_follower_count(username):
    for i in range(len(followers)):
        if users[i] == username:
            return followers[i]
def get_user_verification(username):
    for i in range(len(verifications)):
        if users[i] == username:
            return verifications[i]
def get_user_following_count(username):
    for i in range(len(following)):
        if users[i] == username:
            return following[i]

