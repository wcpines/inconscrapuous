var condition = true

var converter = new showdown.Converter()

var markdownContent = document.querySelector("#toc-list").innerHTML

var tocContent = document.querySelector("#toc-list").textContent

var lines = tocContent.split(/\n/).filter( (line) => !line.match(/^\s*$/) ).map(
  (line) => line.trim() )

var htmlContent = lines.map( (line) => converter.makeHtml(line.trim()) ).join("\n")

function previewMarkdown(){
  var div = document.getElementById("toc-list")
  if (condition){
    div.innerHTML = htmlContent
    condition = !condition
  }else{
    div.innerHTML = markdownContent
    condition = !condition
  }
}
