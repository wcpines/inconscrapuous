// Not working yet...
var div = document.getElementsByClassName('alert-info')[0];
var message = "Note: Script takes 1 sec per page scraped"

function timeWarning(){
  setTimeout( () => {
    "use strict";
    div.innerHTML += `<div class="alert"> ${message} </div>`
  }, 3000);
};
