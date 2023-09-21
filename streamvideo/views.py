from django.shortcuts import render
from dotenv import load_dotenv
import os
from .models import VideoCamera
from django.http import StreamingHttpResponse, HttpResponse 
# Create your views here.
import time
load_dotenv()
URL = os.getenv("URL")


def gen():
    """
    Generate image collection streamming.

    Yields:
        _type_: _description_
    """
    camera = VideoCamera(URL=URL)
    while True:
        try:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        except:
            camera = VideoCamera(URL=URL)
        
    
        
def mask_feed(request):
    """
    Image datastream to request.

    Args:
        request (request): request session.

    Returns:
        StreamingHttpResponse: image datastream.
    """
    return StreamingHttpResponse(gen(),
                    content_type='multipart/x-mixed-replace; boundary=frame')

def test(request) -> HttpResponse:
    """
    Render video.html for user.

    Args:
        request (request): request session.

    Returns:
        HttpResponse: HttpResponse.
    """
    return render(request, "video.html")
