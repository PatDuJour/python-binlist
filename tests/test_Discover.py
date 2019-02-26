#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `binlist` package."""

import pytest

import binlist


@pytest.fixture
def test_cards():
    """
    Discover test cards
    """
    return [
        # Auth.Net test cards
        "6011000000000012",
        # Braintree test cards,
        "6011111111111117",
        "6011000990139424",
        # Stripe test cards
        "6011111111111117",
        "6011000990139424",
        # WorldPay test cards
        "6011000400000000",
    ]


def test_content(test_cards):
    for item in test_cards:
        assert binlist.BIN(item).lookup() == binlist.network.Discover
