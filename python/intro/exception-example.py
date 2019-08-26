import sys

# Handle all the exceptions!
#Setup
actor = {"name": "John Cleese", "rank": "awesome"}

#Function to modify, should return the last name of the actor - think back to previous lessons for how to get it
def get_last_name():
    return actor["name"].split()[1]

def get_last_name_nok():
    return actor["last_name"]

#Test code
try:
    lastName = get_last_name()
    print("The actor's last name is %s" % lastName)

    lastName = get_last_name_nok()
    print("The actor's last name is %s" % lastName)

except:
    print("Unexpected error:", sys.exc_info()[0])
