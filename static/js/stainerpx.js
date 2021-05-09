
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

/* function MarkPoints(image, posx, posy) {
  var ctx = image.getContext("2d");
  ctx.fillStyle = "red";
  ctx.fillRect(posx, posy, 15, 15);
} */

var arr = []

function GetCoordinates(e) {
  
  //Teszt
  var PosX0 = 0;
  var PosY0 = 0;

  var PosX = 0;
  var PosY = 0;
  var ImgPos;
  
  ImgPos = FindPosition(myImg);
  
  if (!e) 
    var e = window.event;

  // Only for rightclick!
  if ("which" in e)  // Firefox, Safari/Chrome & Opera
      rightClick = e.which == 1; 
  else if ("button" in e)  // IE, Opera 
      rightClick = e.button == 1; 

  if(rightClick) {

    if (e.pageX || e.pageY) {
      PosX0 = e.pageX;
      PosY0 = e.pageY;
    }
    else if (e.clientX || e.clientY) {
        PosX0 = e.clientX + document.body.scrollLeft
          + document.documentElement.scrollLeft;
        PosY0 = e.clientY + document.body.scrollTop
          + document.documentElement.scrollTop;
    }

    PosX = PosX0 - ImgPos[0];
    PosY = PosY0 - ImgPos[1];
     
    if(PosX >= 0 && PosY >= 0 ) {
      
      //Teszt
      document.getElementById("PosX0").innerHTML = PosX0;
      document.getElementById("PosY0").innerHTML = PosY0;
      document.getElementById("ImgPos[0]").innerHTML = ImgPos[0];
      document.getElementById("ImgPos[1]").innerHTML = ImgPos[1];

      //Poz
      document.getElementById("x").innerHTML = PosX;
      document.getElementById("y").innerHTML = PosY;

      //Coords Array
      arr.push([PosX, PosY] + '<br>');
      document.getElementById("coordsArr").innerHTML = arr;

     //MarkPoints(myImg,PosX,PosY);

     //return [PosX, PosY];
    }
  }
}

