from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video('motivacao', 'Video Aperitivos: Motivação',  '515479903'),
    Video('jessica-gata', 'Jessica e a sua gatinha',  '515125492'),
]


videos_dct = {v.slug: v for v in videos}


def indice(request):  # pragma: no cover
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):  # pragma: no cover
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
