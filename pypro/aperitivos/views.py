from django.shortcuts import render


def video(request, slug):  # pragma: no cover
    return render(request, 'aperitivos/video.html')
