"""Testes para a função soma do módulo app."""

from app import soma

def test_soma():
    """Testa se a função soma retorna a soma correta de dois inteiros."""
    assert soma(2, 3) == 5
