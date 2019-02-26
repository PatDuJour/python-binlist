#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `binlist` package."""

import pytest

import binlist


@pytest.fixture
def test_cards():
    """
    Visa test cards
    """
    return [
        # Auth.Net test cards
        '4007000000027',
        '4012888818888',
        '4111111111111111',
        # Braintree test cards
        '4111111111111111',
        '4005519200000004',
        '4009348888881881',
        '4012000033330026',
        '4012000077777777',
        '4012888888881881',
        '4217651111111119',
        '4500600000000061',
        # Stripe test cards
        '4242424242424242',
        '4012888888881881',
        '4000056655665556',
        # WorldPay test cards
        '4444333322221111',
        '4911830000000',
        '4917610000000000',
    ]


def test_content(test_cards):
    for item in test_cards:
        assert binlist.BIN(item).lookup() == binlist.network.Visa
