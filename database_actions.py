from pymongo import Connection

#mongo setup
conn = Connection()
db = conn["event_narwhal"]

#inserts the user's fb id and username into the collection
def register_user(user_name,fb_id):
    db.users.insert({ "_id":fb_id, "name":user_name , "events":[] })
    return True

#True if user has registered through fb, False otherwise
def isRegistered(fb_id):
    result = db.users.find({"_id":fb_id})
    i=0
    for result in results:
        i+=1
    if i == 1:
        return True
    return False

#returns dictionary of user's info including fb_id username and events
def login_user(fb_id):
    return db.users.find_one({"_id":fb_id})

#create a new event
def add_event(id,name,theme,food_selection,date,location, facebook_link, attending,declined, maybe, not_responded):
    db.users.update({"_id":id},{"$addToSet":{"events":{ "name":name,"theme":theme,"food-selection":food_selection,"date":date,"location":location,"facebook-link":facebook_link,"attending":attending, "declined":declined,"maybe":maybe, "not-responded":not_responded}}})
    return True

#get a user's events
def get_events(id):
    return db.users.find_one({"_id":id}).get("events")

#get those attending a given event with the user's ID and the Index of the event
def get_event(id,index):
    events=get_events(id)
    return events[id]

#get those attending a given event with the user's ID and the Index of the event
def get_attending(id,index):
    events=get_events(id)
    return events[0]["attending"]
                  
                  
                  
#Testing
'''

print add_event(123456789,"party2","halloween","pizza","10/31/15","my house","http://STUFF",["abby","sophia"],["nadia"],["jenny"],not_responded=["benedict"])
events= get_events(123456789)
for event in events:
    print event
    print "\n\n"

#print get_attending(123456789,0);
'''