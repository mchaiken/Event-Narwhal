#allows for reading of the event
#in handling, we can get cover photo, description, times, location, name
#owner, parent group, privacy, photos, videos, pics, the wall, rsvp of all
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
