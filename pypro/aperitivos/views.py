from django.shortcuts import render


def video(request, slug):  # pragma: no cover
    video = {'titulo': 'Video Aperitivos: Motivação', 'vimeo_id': '515479903'}
    return render(request, 'aperitivos/video.html', context={'video': video})
