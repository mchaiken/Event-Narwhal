from pymongo import Connection

#mongo setup
conn = Connection()
db = conn["event_narwhal"]

def register_user(user_name,fb_id):
    db.users.insert({ "_id":fb_id, "name":user_name , "events":[] })
    return True

def add_event(id,name,theme,food_selection,date,location, facebook_link, attending,declined, maybe, not_responded):
    db.users.update({"_id":id},{"$addToSet":{"events":{ "name":name,"theme":theme,"food-selection":food_selection,"date":date,"location":location,"facebook-link":facebook_link,"attending":attending, "declined":declined, "maybe":maybe, "not-responded":not_responded}}})
    return True
def get_events(id):
    return db.users.find_one({"_id":id}).get("events")

def add_to_do
def get_attending(id,index):
    events=get_events(id)
    return events[0]["attending"]
                  
                  
                  
                  
'''
print add_event(123456789,"party2","halloween","pizza","10/31/15","my house","http://STUFF",["abby","sophia"],["nadia"],["jenny"],["benedict"])
events= get_events(123456789)
for event in events:
    print event
    print "\n\n"

'''

print get_attending(123456789,0);