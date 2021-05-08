
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

var arr = []

function GetCoordinates(e) {
  
  var PosX = 0;
  var PosY = 0;
  var ImgPos;
  
  ImgPos = FindPosition(myImg);
  
  if (!e) var e = window.event;
  
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

  document.getElementById("x").innerHTML = PosX;
  document.getElementById("y").innerHTML = PosY;

  arr.push([PosX, PosY] + '<br>');
  document.getElementById("coordsArr").innerHTML = arr;

}

