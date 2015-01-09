#allows for reading of the event
#in handling, we can get cover photo, description, times, location, name
#owner, parent group, privacy, photos, videos, pics, the wall, rsvp of all


#pip install facebook-sdk
import facebook

#fb setup
graph = facebook.GraphAPI(oauth_access_token)

events = graph.get_connections(id = "me", connection_name = "events")

'''/* make the API call */
FB.api(
    "/{event-id}",   #event id would go here
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
'''


