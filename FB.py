import facebook
def Graph(token):
        return facebook.GraphAPI(token);


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
        ppl = graph.get_connections(EventID, "invited")["data"]
        fin = []
        for x in ppl:
                fin.append(x["name"])
        return fin

def getAttending(token, EventID):
        graph = Graph(token)
        ppl = graph.get_connections(EventID, "attending")["data"]
        fin = []
        for x in ppl:
                fin.append(x["name"])
        return fin


def getDeclined(token, EventID):
        graph = Graph(token)
        ppl = graph.get_connections(EventID, "declined")["data"]
        fin = []
        for x in ppl:
                fin.append(x["name"])
        return fin


def getMaybe(token, EventID):
        graph = Graph(token)
        ppl = graph.get_connections(EventID, "maybe")["data"]
        fin = []
        for x in ppl:
                fin.append(x["name"])
        return fin


def getUnknown(token, EventID):
        graph = Graph(token)
        ppl = graph.get_connections(EventID, "noreply")["data"]
        fin = []
        for x in ppl:
                fin.append(x["name"])
        return fin


def getLocation(token, EventID): #may return None if no location has been set
        graph = Graph(token)
        try:
                return graph.get_object(EventID)["location"]
        except:
                return None

        
def getStartTime(token, EventID): #may return None if no start time has been set
        graph = Graph(token)
        try:
                return graph.get_object(EventID)["start_time"]
        except:
                return None

def getEndTime(token, EventID): #may return None if no end time has been set
        graph = Graph(token)
        try:
                return graph.get_object(EventID)["end_time"]
        except:
                return None
        
def getEventName(token, EventID):
        graph = Graph(token)
        return graph.get_object(EventID)["name"]

def getDescription(token, EventID): #may return None if no description has been set
        graph = Graph(token)
        try:
                return graph.get_object(EventID)["description"] 
        except:
                return None

def getEventPhotos(token, EventID): #may return an empty list if no EventPhotos exist
        graph = Graph(token)
        return graph.get_connections(EventID, "photos") ["data"]


def getEventVideos(token, EventID): #may return an empty list if no EventVideos exist
        graph = Graph(token)
        return graph.get_connections(EventID, "videos") ["data"]
        


def getEventPicture(token, EventID): #may return an empty list if no Event profile pic exists
        graph = Graph(token)
        return graph.get_connections(EventID, "picture") ["data"]
        

        




#to make:
#getGuests  
#optional: getAttending   getNotAttending   getMaybe   getUnknown 
