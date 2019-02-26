#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `binlist` package."""

import pytest

import binlist


@pytest.fixture
def test_cards():
    """
    AmEx test cards
    """
    return [
        # Auth.Net test cards
        "370000000000002",
        # Braintree test cards,
        "378282246310005",
        "371449635398431",
        # Stripe test cards
        "378282246310005",
        "371449635398431",
        # WorldPay test cards
        "34343434343434",
    ]


def test_content(test_cards):
    for item in test_cards:
        assert binlist.BIN(item).lookup() == binlist.network.AmEx
