from django.shortcuts import render
from django.http import HttpResponse
import yt_dlp

# Create your views here.
def download_video(request):
    if request.method=="POST":
        url = request.POST.get('url')

        ydl_opts={
            'format': 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                return HttpResponse("Video Downloaded.")
        except Exception as e:
            return HttpResponse("Error:", str(e))

    return render(request, 'downloader/index.html')
