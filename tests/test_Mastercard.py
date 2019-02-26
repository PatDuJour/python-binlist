#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `binlist` package."""

import pytest

import binlist


@pytest.fixture
def test_cards():
    """
    Mastercard test cards
    """
    return [
        # Auth.Net test cards
        "5424000000000015",
        # Braintree test cards,
        "5555555555554444",
        "5105105105105100",
        # Stripe test cards
        "5555555555554444",
        "5200828282828210",
        "5105105105105100",
        # WorldPay test cards
        "5454545454545454",
    ]


def test_content(test_cards):
    for item in test_cards:
        assert binlist.BIN(item).lookup() == binlist.network.Mastercard
