currentElement = 0;
params = {};
console.log('Loaded!');
needsAjax=true;
function saveName() {
	while (document.getElementsByTagName('img')[currentElement+1] !== undefined && document.body.scrollTop + window.innerHeight > document.getElementsByTagName('img')[currentElement+1].y) {
		currentElement += 1;
		needsAjax=true;
	}
	if (needsAjax) {
		needsAjax=false;
		sendAjax();
	}
	setTimeout(saveName, 200);
}
function getParams() {
	var urldata = window.location.search.substring(1).split('&');
	for (var i=0; i<urldata.length; i++) {
			s = urldata[i].split('=');
			params[s[0]] = s[1];
		}
}
function sendAjax() {
	page = currentElement+parseInt(params['page']);
	var request = new XMLHttpRequest();
	var s = "log.py?page=" + page + "&comic=" + params['comic'] + "&reason=page_scroll";
	request.open("POST",s,true);
	request.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	request.send();
}
setTimeout(saveName, 100);
getParams();