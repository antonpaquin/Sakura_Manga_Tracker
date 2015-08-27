window.onpageshow = function(event) {
  var request = new XMLHttpRequest();
  request.open("GET",'index.py?page=updates&nocache='+new Date().getTime(),true);
  request.onreadystatechange=function() {
    if (request.readyState==4 && request.status==200) {
      console.log('readystatechange');
      resetBorders(JSON.parse(request.responseText));
    }
  }
  request.send();
}
var r;
function resetBorders(response) {
  r = response;
  for (var name in response) {
    console.log(name + " to " + response[name]);
    document.getElementById([name]).className = response[name];
  }
}
