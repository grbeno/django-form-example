let pointSize = 3;
var points = [];
var timeout = 300;
var clicks = 0;

function getPosition(event) {
  var rect = canvas.getBoundingClientRect();
  return {
    x: event.clientX - rect.left,
    y: event.clientY - rect.top
  };
}

function drawCoordinates(point, r) {

//var ctx = canvas.getContext("2d");
//ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

ctx.fillStyle = "#ff2626"; // Red color
ctx.beginPath();
ctx.arc(point.x, point.y, pointSize, 0, Math.PI * 2, true);
ctx.fill();
}

canvas.addEventListener("click", function(e) {
  clicks++;
  var m = getPosition(e);
  // this point won't be added to the points array
  // it's here only to mark the point on click since otherwise it will appear with a delay equal to the timeout
  
  drawCoordinates(m, pointSize);
  
  if (clicks == 1) {
    setTimeout(function() {
      if (clicks == 1) {
        // on click add a new point to the points array
        points.push(m);
      } else { // on double click 
        // 1. check if point in path
        for (let i = 0; i < points.length; i++) {
          ctx.beginPath();
          ctx.arc(points[i].x, points[i].y, pointSize, 0, Math.PI * 2, true);

          if (ctx.isPointInPath(m.x, m.y)) {
            points.splice(i, 1); // remove the point from the array
            break;// if a point is found and removed, break the loop. No need to check any further.
          }
        }

        //clear the canvas
        ctx.clearRect(0, 0, cw, ch);
      }

      points.map(p => {
        drawCoordinates(p, pointSize);
      });
      clicks = 0;
    }, timeout);
  }
});

