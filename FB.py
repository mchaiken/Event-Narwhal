import facebook
def Graph(token):
        return facebook.GraphAPI(token);
#to get only your events, parse through event data to see who owner is and if you arent then just delete that one
def getAllEvents(token):
        graph = Graph(token)
        return graph.get_connections("me", "events")["data"]

def getHostedEvents(token):
        graph = Graph(token)
        events = getAllEvents(token)
        hosted = []
        for x in events:
                event = getEvent(token, x["id"])
                if event["owner"]["id"] == getID(token):
                        hosted.append(event)
        return hosted

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

def getAttending(token, EventID):
        graph = Graph(token)
        return graph.get_connections(EventID, "attending")["data"]

def getDeclined(token, EventID):
        graph = Graph(token)
        return graph.get_connections(EventID, "declined")["data"]

def getMaybe(token, EventID):
        graph = Graph(token)
        return graph.get_connections(EventID, "maybe")["data"]

def getUnknown(token, EventID):
        graph = Graph(token)
        return graph.get_connections(EventID, "noreply")["data"]

#to make:
#getGuests  
#optional: getAttending   getNotAttending   getMaybe   getUnknown 
