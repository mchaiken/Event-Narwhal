import facebook
def Graph(token):
        return facebook.GraphAPI(token);

def getAllEvents(token):
        graph = Graph(token)
        return graph.get_connections("me", "events")

def getEvent(token, ID):
        graph = Graph(token)
        return graph.get_object(ID)

def getName(token):
        graph = Graph(token)
        return graph.get_object("me")["name"]

def getID(token):
        graph = Graph(token)
        return graph.get_object("me")["id"]

def getGuests(token, event):
        graph = Graph(token)
        return event["invited"]
        
#to make:
#getGuests  
#optional: getAttending   getNotAttending   getMaybe   getUnknown 
