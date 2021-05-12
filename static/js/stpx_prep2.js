
function FindPosition(image) {

    if(typeof( image.offsetParent ) != "undefined") {
        for(var x = 0, y = 0; image; image = image.offsetParent) {
            x += image.offsetLeft;
            y += image.offsetTop;
        }
        return [ x, y ];
    }
        else {
            return [ image.x, image.y ];
        }
}

function MarkPoints() {
  
  var ctx = canvas.getContext("2d");
  ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
  
  var pointSize = 5; // Size of the point.
  ctx.font = "12px Courier";
  
  for (var i = 0; i < coords.length; i++) {
    ctx.beginPath(); //Start path
    ctx.arc(coords[i].x, coords[i].y, pointSize, 0, Math.PI * 2, true); // Draw a point
    ctx.fillStyle = "#33FF36"; // text color
    ctx.fillText( '(' + coords[i].x + ';' + coords[i].y + ')', coords[i].x+5, coords[i].y+5);
    ctx.fillStyle = "red"; // point color
    ctx.fill();
    ctx.closePath();
  }

}

var coords = [];

function GetCoordinates(e) {

  var x = 0;
  var y = 0;
  var ImgPos;
  ImgPos = FindPosition(canvas);
  
  if (!e) 
    var e = window.event;

    // Only for rightclick!
    if ("which" in e) { // Firefox, Safari/Chrome & Opera
        leftClick = e.which == 1;
        rightClick = e.which == 3;
    } 
    else if ("button" in e) {  // IE, Opera 
        leftClick = e.button == 1;
        rightClick = e.button == 3;
    }
      
    if (e.pageX || e.pageY) {
        x = e.pageX;
        y = e.pageY;
    }
    else if (e.clientX || e.clientY) {
        x = e.clientX;
        y = e.clientY;
    }

    x = x - ImgPos[0];
    y = y - ImgPos[1];

    if (leftClick) {

        if( x >= 0 && y >= 0 ) {
            //Pos(x & y)
            document.getElementById("x").innerHTML = x;
            document.getElementById("y").innerHTML = y;
            //Coords Array
            coords.push([x, y]);
        }
        
        div = document.getElementById("coordsArr");
        var node = document.createElement("P");
        div.appendChild(node);
        node.innerHTML = coords[coords.length-1];
        
        var ctx = canvas.getContext("2d");
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
        
        node.addEventListener("click", function(e) { // canvas..."dblclick" ???
            for (var i = 0; i < coords.length; i++) {
                if (coords[i].node == e.target) { // !
                //MarkPoints();
                //ctx.beginPath(); //Start path
                //ctx.arc(coords[i].x, coords[i].y, 5, 0, Math.PI * 2, true); // Draw a point
                //if (ctx.isPointInPath(x, y)) {
                    coords.splice(i, 1);
                    break;
                }    
            }
            //ctx.clearRect(0, 0, canvas.width, canvas.height);
            div.removeChild(e.target); // !
            MarkPoints();
        });
        
        coords.push({ // ???
            x,
            y,
            node: node
        });
        
        MarkPoints(); 

    } //leftClick

} // function

