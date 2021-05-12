function FindPosition(image) {
  
  if(typeof( image.offsetParent ) != "undefined") {
    for(var posX = 0, posY = 0; image; image = image.offsetParent) {
      posX += image.offsetLeft;
      posY += image.offsetTop;
    }
    return [ posX, posY ];
    }
    else {
      return [ image.x, image.y ];
    }
}

function MarkPoints() {
  
  var ctx = canvas.getContext("2d");
  ctx.drawImage(img, 0, 0, cw, ch);
  var pointSize = 5; // Size of the point.
  ctx.font = "12px Courier";
  
  for (var a = 0; a < coords.length; a++) {
    ctx.beginPath(); //Start path
    ctx.arc(coords[a].PosX-5, coords[a].PosY-5, pointSize, 0, Math.PI * 2, true); // Draw a point
    ctx.fillStyle = "#33FF36"; // text color
    ctx.fillText( '(' + coords[a].PosX + ';' + coords[a].PosY + ')', coords[a].PosX, coords[a].PosY);
    ctx.fillStyle = "red"; // point color
    ctx.fill();
    ctx.closePath();
  }

}

var coords = [];

function GetCoordinates(e) {

  var PosX = 0;
  var PosY = 0;
  var ImgPos;
  
  ImgPos = FindPosition(canvas);
  
  if (!e) 
    var e = window.event;

  // Only for rightclick!
  if ("which" in e)  // Firefox, Safari/Chrome & Opera
      rightClick = e.which == 1; 
  else if ("button" in e)  // IE, Opera 
      rightClick = e.button == 1; 

  if(rightClick) {

    if (e.pageX || e.pageY) {
      PosX = e.pageX;
      PosY = e.pageY;
    }
    else if (e.clientX || e.clientY) {
        PosX = e.clientX + document.body.scrollLeft
          + document.documentElement.scrollLeft;
        PosY = e.clientY + document.body.scrollTop
          + document.documentElement.scrollTop;
    }

    PosX = PosX - ImgPos[0];
    PosY = PosY - ImgPos[1];
     
    if(PosX >= 0 && PosY >= 0 ) {
      
      //Poz
      document.getElementById("x").innerHTML = PosX;
      document.getElementById("y").innerHTML = PosY;

      //Coords Array
      coords.push([PosX, PosY]);
      
      div = document.getElementById("coordsArr");
      var node = document.createElement("P");
      div.appendChild(node);
      node.innerHTML = coords[coords.length-1];

      //Marker points
      //MarkPoints();
      
      node.addEventListener("click", function(e) {
        
        for (var a = 0; a < coords.length; a++) {
          if (coords[a].node == e.target) {
            coords.splice(a, 1);
            break;
          }
        }
        div.removeChild(e.target);
        MarkPoints();
        });
        
        //Teszt:
        //div2 = document.getElementById("test");
        //div2.innerHTML = coords;

        coords.push({ // ???
          PosX,
          PosY,
          node: node
        });
        
        MarkPoints();

    }
  }
}

