from django.shortcuts import render


def video(request, slug):  # pragma: no cover
    videos = {
        'motivacao': {'titulo': 'Video Aperitivos: Motivação', 'vimeo_id': '515479903'},
        'jessica-gata': {'titulo': 'Jessica e a sua gatinha', 'vimeo_id': '515125492'},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
