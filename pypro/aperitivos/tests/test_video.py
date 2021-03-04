import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains


'''Fixture para popular dados na base de dados para realizar testes'''


@pytest.fixture
def video(db):
    return mommy.make(Video)


@pytest.fixture
def resp(client, video):  # pragma: no cover
    return client.get(reverse('aperitivos:video', args=(video.slug, )))


@pytest.fixture
def resp_video_nao_encontrado(client, video):  # pragma: no cover
    return client.get(reverse('aperitivos:video', args=(video.slug+'video_nao_existente', )))


def test_status_code(resp):  # pragma: no cover
    assert resp.status_code == 200


def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):  # pragma: no cover
    assert resp_video_nao_encontrado.status_code == 404


def test_titulo_video(resp, video):  # pragma: no cover
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp, video):  # pragma: no cover
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}"')
