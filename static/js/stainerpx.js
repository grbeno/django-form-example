
function InitPrepareImg(canvas,img) {
  
  var ctx = canvas.getContext("2d");
  
  canvas.width = img.width;
  canvas.height = img.height;
  ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

}

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

function MarkPoints(canvas,posx,posy) {
  
  var ctx = canvas.getContext("2d");
  var pointSize = 5; // Size of the point.
  
  ctx.fillStyle = "#33FF36"; // color
  ctx.beginPath(); //Start path
  ctx.arc(posx, posy, pointSize, 0, Math.PI * 2, true); // Draw a point
  ctx.fill(); // Close path and fill.

}

var arr = []
function GetCoordinates(e) {
  
  var PosX = 0;
  var PosY = 0;
  var ImgPos;
  
  ImgPos = FindPosition(myCanvas);
  
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
      arr.push([PosX, PosY] + '<br>');
      document.getElementById("coordsArr").innerHTML = arr;

      //Marker points
      MarkPoints(myCanvas,PosX,PosY);
    
    }
  }
}

