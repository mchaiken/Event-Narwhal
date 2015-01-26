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
    results = db.users.find({"_id":fb_id})
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
def add_event(id,name,theme,fb, description, date, location, attending, declined, maybe, not_responded):
    return db.users.update({"_id":id},{"$addToSet":{"events":{ "name":name,"description":description,"theme":theme,"date":date,"location":location,"facebook-id":fb,"attending":attending, "declined":declined,"maybe":maybe, "not-responded":not_responded}}})


def remove_event(id,index):
    events = get_events(id)
    events.pop(index)
    print "EVENTS:"
    print events
    db.users.update({"_id":id},{"$set":{"events":events}})
    print db.users.find_one({"_id":id}).get("name")
    return True


#get a user's events
def get_events(id):
    return db.users.find_one({"_id":id}).get("events")


#get those attending a given event with the user's ID and the Index of the event
def get_event(id,index):
    events=get_events(id)
    return events[int(index.encode("utf8"))]


def update_8tracks(id,index,link):
    events=get_events(id)
    events[index]["8tracks"]=link
    db.users.update({"_id":id},{"$set":{"events":events}})

def update_all(id,index,name,theme,fb):
    events=get_events(id)
    events[index]["theme"]=theme
    events[index]["name"]=name
    events[index]["facebook-id"]=fb
    db.users.update({"_id":id},{"$set":{"events":events}})


def update_yummly(id,index,link):
    events=get_events(id)
    events[index]["food"]=link
    db.users.update({"_id":id},{"$set":{"events":events}})

#update an event
def update_event(id, index, description, date, location, attending, declined, maybe, not_responded):
    #finding event to update
    events = get_event(id)
    #new info gotten from app.py using the FB.py methods
    events[index]["name"] = name
    events[index]["description"] = description
    events[index]["date"] = date
    events[index]["location"] = location
    events[index]["attending"] = attending
    events[index]["declined"] = declined
    events[index]["maybe"] = maybe
    events[index]["not-responded"] = not_responded
    #how do i do this part i dont know mongo
    #db.users.update({"_id":id}{"events"[index]:event})
    db.users.update({"_id":id},{"$set":{"events":events}})

#get those attending a given event with the user's ID and the Index of the event
def get_attending(id,index):
    events=get_events(id)
    return events[int(index.encode("utf8"))]["attending"]


#not sure if this should be in the yummly section or not so I will comment it out
'''
    def get_recipes(id, index):
    #how do you find the right event?
    events = get_events(id)
    return db.users.find_one({"_id":id}).get("events, name=ename, food-selections}
    
    
    #Testing
    '
    add_event(123456789,"Halloween Party","spooookkyyyy","kittens","pizza","10/31/15","my house","http://STUFF",["abby","sophia"],["nadia"],["jenny"],not_responded=["benedict"])
    
    
    register_user("mchaiken",123456789);
    print add_event(123456789,"Birthday","A party for my bday gonna be lost a fun","kittens","pizza","10/31/15","my house","http://STUFF",["abby","sophia"],["nadia"],["jenny"],not_responded=["benedict"])
    
    events= get_events(123456789)
    print "FIRST"
    
    for event in events:
    print event
    print "\n\n"
    remove_event(123456789,0);
    print "SECOND"
    events=get_events(123456789);
    for event in events:
    print event
    print "\n\n"
    #print get_attending(123456789,0);
    
    '''
