
'''
<form action="/wherewearedirecting" method ="GET">
<input type="text" name="search">
<button type="submit">Submit </button>
</form>
we will need to have a feature that will allow for specific searches 
Supported Holidays
Christmas, Summer, Thanksgiving, New Year, Super Bowl / Game Day, Halloween, Hanukkah, 4th of July
'''


def getResults(id):
    if attribute == "holiday":
        url ="http://api.yummly.com/v1/api/recipes?maxResult=100&_app_id=dd74dd78&_app_key=992e5769b7da1040ad87d47328a4182e&q=&allowedHoliday[]=holiday^holiday-"+ id.lower()
    if attribute == "ingrediant":
         url=""" http://api.yummly.com/v1/api/recipes?maxResult=100&_app_id=dd74dd78&_app_key=992e5769b7da1040ad87d47328a4182e"""
         for ingredient in ingredients:
             if ingredient[0]==" ":
                 ingredient= ingredient[1:]
                 url+="&allowedIngredient[]="+ingredient.lower()
    #print url
    request = urllib2.urlopen(url)
    result = request.read()
    #print url
    return json.loads(result)

m,mn,n 

def getRecipe(id):
    url="http://api.yummly.com/v1/api/recipe/"+id+"?_app_id=dd74dd78&_app_key=992e5769b7da1040ad87d47328a4182e"
    #print url
    request = urllib2.urlopen(url)
    result = request.read()
    #print url
    return json.loads(result)

