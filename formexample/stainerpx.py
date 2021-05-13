import cv2
import io
import matplotlib.pyplot as plt

class ImageCoords():

    img = cv2.imread('images\K_09.24.PNG')
    fig = plt.figure()

    def showImg(self):
        
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = 'data:image/png;base64,' + urllib.parse.quote(string)
        
        context = {'image': uri}

        return context

    def getCoord(self):
        points = []
        cid = fig.canvas.mpl_connect('button_press_event', self.__onclick)
        return points
        
    def __onclick(self,event):
        points.append((event.xdata,event.ydata))
        plt.plot(event.xdata, event.ydata, '.', color='red', markersize=16)
        fig.canvas.draw()