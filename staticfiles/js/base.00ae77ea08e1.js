// A képernyő felbontása az ablak betöltésekor - resolution of the screen

	window.onload = function getResolution() { 
		var screenInfo = document.getElementById('screen');
		screenInfo.innerHTML += "Screen info - resolution: " + screen.width + "x" + screen.height + " px";
	}
		