import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains


@pytest.fixture
def videos(db):  # pragma: no cover
    return mommy.make(Video, 3)


@pytest.fixture
def resp(client, videos):  # pragma: no cover
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):  # pragma: no cover
    assert resp.status_code == 200


def test_titulo_video(resp, videos):  # pragma: no cover
    for video in videos:
        assert_contains(resp, video.titulo)


def test_link_video(resp, videos):  # pragma: no cover
    for video in videos:
        video_link = reverse('aperitivos:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')
