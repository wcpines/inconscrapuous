var previewButton = document.querySelector("#preview-markdown")

// used to toggle preview
var condition = true

// https://github.com/showdownjs/showdown
var converter = new showdown.Converter()

// includes html tags to be able to render it to page as literal markdown
var tocContent = document.querySelector("#toc-list").innerHTML

// includes only pure markdown text
var markdownContent = document.querySelector("#toc-list").textContent

var lines = markdownContent.split(/\n/).filter( (line) => !line.match(/^\s*$/) ).map(
  (line) => line.trim() )

var htmlContent = lines.map( (line) => converter.makeHtml(line.trim()) ).join("\n")

function previewMarkdown(){
  var div = document.getElementById("toc-list")
  if (condition){
    div.innerHTML = `<br><div class="sliding-middle-out" id="markdown-preview">${htmlContent}</div>`
    previewButton.innerText = "Show Raw"
    condition = !condition
  }else{
    div.innerHTML = tocContent
    previewButton.innerText = "Preview Markdown"
    condition = !condition
  }
}
