//modal
var modal = document.getElementById("myModal");
var login_link = document.getElementById("login");
var close_login = document.getElementsByClassName("close")[0];

//searchbar
var search_bar = document.getElementsByClassName("search_bar");

console.log('connected');

//modal functions

login_link.onclick = function() {
  modal.style.display = "block";
}

close_login.onclick = function() {
  modal.style.display = "none";
}
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

$('#myForm').submit(function(){
  // event.preventDefault();
  return false;
});
//search_bar
search_bar.onclick = function() {
  search_bar.style.borderStyle = "hidden";
}

//********* facebook login *********//
window.fbAsyncInit = function() {
  FB.init({
    appId      : '{your-app-id}',
    cookie     : true,
    xfbml      : true,
    version    : '{api-version}'
  });

  FB.AppEvents.logPageView();

};

(function(d, s, id){
   var js, fjs = d.getElementsByTagName(s)[0];
   if (d.getElementById(id)) {return;}
   js = d.createElement(s); js.id = id;
   js.src = "https://connect.facebook.net/en_US/sdk.js";
   fjs.parentNode.insertBefore(js, fjs);
 }(document, 'script', 'facebook-jssdk'));

 function checkLoginState() {
  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });
}

var finished_rendering = function() {
  console.log("finished rendering plugins");
  var spinner = document.getElementById("spinner");
  spinner.removeAttribute("style");
  spinner.removeChild(spinner.childNodes[0]);
}
FB.Event.subscribe('xfbml.render', finished_rendering);

//********* google login *********//
function onSuccess(googleUser) {
  console.log('Logged in as: ' + googleUser.getBasicProfile().getName());
}
function onFailure(error) {
  console.log(error);
}
function renderButton() {
  gapi.signin2.render('my-signin2', {
    'scope': 'profile email',
    'width': 240,
    'height': 50,
    'longtitle': true,
    'theme': 'dark',
    'onsuccess': onSuccess,
    'onfailure': onFailure
  });
}
