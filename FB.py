import facebook
def Graph(token):
        return facebook.GraphAPI(token);

def getEvents(token):
        graph = Graph(token)
        return graph.get_connections("me", "events")

def

def getID(token):
        graph = Graph(token)
        return graph.get_object("me")["id"]

def getGuests(token, event):
        
#to make:
#getGuests  
#optional: getAttending   getNotAttending   getMaybe   getUnknown 
