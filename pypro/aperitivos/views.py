from django.shortcuts import render

from pypro.aperitivos.models import Video

videos = [
    Video(slug='motivacao', titulo='Video Aperitivos: Motivação', vimeo_id='515479903'),
    Video(slug='jessica-gata', titulo='Jessica e a sua gatinha', vimeo_id='515125492'),
]


videos_dct = {v.slug: v for v in videos}


def indice(request):  # pragma: no cover
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):  # pragma: no cover
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
