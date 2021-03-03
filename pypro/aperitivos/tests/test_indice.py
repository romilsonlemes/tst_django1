import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):  # pragma: no cover
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):  # pragma: no cover
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Video Aperitivos: Motivação',
        'Jessica e a sua gatinha'
    ]
)
def test_titulo_video(resp, titulo):  # pragma: no cover
    assert_contains(resp, titulo)


@pytest.mark.parametrize(
    'slug',
    [
        'motivacao',
        'jessica-gata'
    ]
)
def test_link_video(resp, slug):  # pragma: no cover
    video_link = reverse('aperitivos:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')
