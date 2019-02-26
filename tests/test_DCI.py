#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `binlist` package."""

import pytest

import binlist


@pytest.fixture
def test_cards():
    """
    DCI test cards
    """
    return [
        # Auth.Net test cards
        "38000000000006",
        # Braintree test cards,
        "30569309025904",
        "38520000023237",
        # Stripe test cards
        "30569309025904",
        "38520000023237",
        # WorldPay test cards
        "36700102000000",
        "36148900647913",
    ]


def test_content(test_cards):
    for item in test_cards:
        assert binlist.BIN(item).lookup() == binlist.network.DCI
