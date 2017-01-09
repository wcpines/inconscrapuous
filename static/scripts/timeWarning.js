// Not working yet...
var div = document.querySelector('.alert-info')
var err = document.querySelector(".alert-error")
var message = "Note: Script takes 1 sec per page scraped"

function timeWarning(){
  err.remove()
  setTimeout( () => {
    "use strict";
    div.innerHTML += `<div class="alert"> ${message} </div>`
  }, 3000);
};

