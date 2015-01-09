FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
    return console.log(response["authResponse"]["userID"]);
}

#handles response and returs the userID
