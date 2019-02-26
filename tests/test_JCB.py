#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `binlist` package."""

import pytest

import binlist


@pytest.fixture
def test_cards():
    """
    JCB test cards
    """
    return [
        # Braintree test cards,
        "3530111333300000",
        "3566002020360505",
        # Stripe test cards
        "3530111333300000",
        "3566002020360505",
        # WorldPay test cards
        "3528000700000000",
    ]


def test_content(test_cards):
    for item in test_cards:
        assert binlist.BIN(item).lookup() == binlist.network.JCB
