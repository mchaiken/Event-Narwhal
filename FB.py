import facebook
def Graph(token):
        return facebook.GraphAPI(token);

def getEvents(token):
        graph = Graph(token)
        return graph.get_connections("me", "events")
def getID(token):
        graph = Graph(token)
        return graph.get_object("me")["id"]
