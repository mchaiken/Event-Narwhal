var button = document.getElementById("button");
button.addEventListener("click", function(e){
    FB.login(function(response){
	statusChangeCallback(response);
    });
});

var statusChangeCallback = function(resposne){
    if (//continue handling this



