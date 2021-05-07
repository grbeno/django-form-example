import cv2
import io
import matplotlib.pyplot as plt
    
def showImg():
    img = cv2.imread('images\K_09.24.PNG')
	fig = plt.figure()
	buf = io.BytesIO()
	fig.savefig(buf, format='png')
	buf.seek(0)
	string = base64.b64encode(buf.read())
	uri = 'data:image/png;base64,' + urllib.parse.quote(string)
	
	context = {'image': uri}

	return render(request,'results.html',context)

def getCoord(fig):
	points = []
	cid = fig.canvas.mpl_connect('button_press_event', onclick)
	return points
	
def onclick(event):
	points.append((event.xdata,event.ydata))
	plt.plot(event.xdata, event.ydata, '.', color='red', markersize=16)
	fig.canvas.draw() """