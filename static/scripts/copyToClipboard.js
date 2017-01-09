// previewMarkdown.js
// var tocContent = document.querySelector("#toc-list").innerHTML

var copyDiv = document.querySelector("#toc-list")
var selection = window.getSelection();
var range = document.createRange();
var copyButton = document.querySelector("#copy-to-clipboard")

function copyToClipboard(){
  // handle IE/Opera?
  copyDiv.innerHTML = tocContent
  if (document.body.createTextRange){
    range.moveToElementText(copyDiv);
    range.select();
    // vs chrome/ff ?
  } else {
    range.selectNodeContents(copyDiv);
    selection.removeAllRanges();
    selection.addRange(range);
  }
  document.execCommand('copy')
  selection.removeAllRanges();
  copyButton.innerText = "Copied!"
}
