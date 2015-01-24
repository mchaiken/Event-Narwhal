import facebook
def Graph(token):
        return facebook.GraphAPI(token);
#to get only your events, parse through event data to see who owner is and if you arent then just delete that one
def getAllEvents(token):
        graph = Graph(token)
        return graph.get_connections("me", "events")["data"]

def getEvent(token, ID):
        graph = Graph(token)
        return graph.get_object(ID)

def getName(token):
        graph = Graph(token)
        return graph.get_object("me")["name"]

def getID(token):
        graph = Graph(token)
        return graph.get_object("me")["id"]

def getGuests(token, EventID):
        graph = Graph(token)
        return graph.get_connections(EventID, "invited")["data"]
        
#to make:
#getGuests  
#optional: getAttending   getNotAttending   getMaybe   getUnknown 
