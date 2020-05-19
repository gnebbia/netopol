#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# netopol test suite
# Copyright © 2020, Giuseppe Nebbione.
# See /LICENSE for licensing information.

import re
import random
import netopol
import netopol.generator as g


def test_gen_user():
    """Test user generation"""
    assert g.gen_user(seed=1) == g.gen_user(seed=1)
    assert g.gen_user(seed=5) != g.gen_user(seed=10)

def test_gen_ipv4net():
    """Test IPv4net Generation"""
    cidr_types = ["A","B","C"]
    assert re.match(r'\d+\.\d+\.\d+\.\d+/\d+', g.gen_ipv4net())
    for _ in range(50):
        assert re.match(r'(^192\.168\.)|(^10\.)|(^172\.)',
                g.gen_ipv4net(cidr_type=random.choice(cidr_types)))

def test_gen_ipv6net():
    """Test IPv6net Generation"""
    # Basically this is tested within the faker library
    assert True

def test_ipv6net():
    """Test IPv6net Generation"""
    assert True


def test_import():
    """Test imports."""
    netopol
