function checkInput(div) {
		
		/* check empty input values */
		
		var inputs = div.getElementsByTagName("INPUT");
		var len = inputs.length;

		/* input values: not 0 & not the last! */
		
		for (var i = 1; i < len-1; i++) {
			var name = inputs[i].getAttribute("name");
			if (document.getElementsByName(name)[0].value == '')
				return -1;
		}
		return 0;
	}

	var i = 0;

	function displayForm() {

		/* div id */
		
		var div = document.getElementsByTagName("DIV")[i];
		var actlForm = div.getAttribute("id");
		
		/* next div id */
		
		var nextForm = actlForm.slice(0,-1) + String(parseInt(actlForm.substr(actlForm.length-1))+1);
		
		if (checkInput(div) != 0)
			return alert("Figyelem: űres mező! / Warning: empty field! ");
		else {
			var disapp = document.getElementById(actlForm);
			disapp.style.display = "none";

			var disapp = document.getElementById(nextForm);
			disapp.style.display = "block";
		}

		i++;
	}