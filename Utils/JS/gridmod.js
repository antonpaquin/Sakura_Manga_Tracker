function additem(comic) {
  document.getElementById('add'+comic).className = "button hidden"
  document.getElementById('remove'+comic).className = "button"
  ajax('add',comic);
}

function removeitem(comic) {
  document.getElementById('add'+comic).className = "button"
  document.getElementById('remove'+comic).className = "button hidden"
  ajax('remove',comic);
}

function ajax(method, comic) {
  var request = new XMLHttpRequest();
  request.open("POST","settings.py?page=gridp",true);
  params = 'method='+method+'&title=' + comic;
	request.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  request.send(params);
}
