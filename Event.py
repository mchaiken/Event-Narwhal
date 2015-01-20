#allows for reading of the event
#in handling, we can get cover photo, description, times, location, name
#owner, parent group, privacy, photos, videos, pics, the wall, rsvp of all


#pip install facebook-sdk
import facebook

#fb setup
graph = facebook.GraphAPI("oauth_access_token")
#unsure what to do here because the access token changes with every login


#returns a dict of all events
def getEvents():
        return graph.get_connections(id = "me", connection_name = "events")
        




