#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 gnebbia <nebbionegiuseppe@gmail.com>
#
# Distributed under terms of the GPLv3 license.

"""
This is the class generating random network elements
"""
import random
import ipaddress
from faker import Faker


def gen_user(seed=None):
    """ 
    Generate a random username

    Arguments:
    seed      -- Seed to provide for randomness

    Returns:
    username  -- a string representing a username
    """
    Faker.seed(seed)
    return Faker().user_name()

def gen_ipv4net(seed=None, cidr_type="C", is_private=True):
    """ 
    Generate a random IPv4 network space

    Arguments:
    seed          -- integer seed to provide for randomness
    is_private    -- boolean, if true the network address represents
                     a private network as for RFC 1918
    cidr_type     -- string, can assume values:
                     "A", for a class A network
                     "B", for a class B network
                     "C", for a class C network

    Returns:
    IPv4 net address  -- a string representing an IPv4 network
    """
    Faker.seed(seed)
    return Faker().ipv4(network=True,
            address_class=str.upper(cidr_type),
            private=is_private)

def gen_ipv6net(seed=None):
    """ 
    Generate a random IPv6 network space

    Arguments:
    seed          -- integer seed to provide for randomness

    Returns:
    IPv6 net address  -- a string representing an IPv6 network
    """
    Faker.seed(seed)
    return Faker().ipv6(network=True)

def get_all_hosts(ipnet):
    """ 
    Generate the list of all possible hosts within a network

    Arguments:
    ipnet   --   an IP network address in the form
                 <ip>/subnet such as 192.168.1.0/24
                 or 69f6:a34:2efb:19ca:d40::/74

    Returns:
    all hosts -- a generator for all IP address objects 
                 that represent all the possible hosts 
                 that can exist within the specified network
    """
    return ipaddress.ip_network(ipnet).hosts()


def gen_hosts(ipnet, seed=None, n=3, sequential=True):
    """ 
    Generates a sample of size n of random hosts
    within an IP network

    Arguments:
    ipnet        -- an IP network address in the form
                    <ip>/subnet such as 192.168.1.0/24
    n            -- sample size
    sequential   -- boolean, if true the generated addresses are
                    sequential

    Returns:
    random hosts -- a list of n hosts as IPAddress
                    objects extracted from the ipv4net address
    """
    if sequential:
        return [next(get_all_hosts(ipnet)) for _ in range(n)]

    random.seed(seed)
    return random.sample(list(get_all_hosts(ipnet)), n)





# Extract n random addresses from an IPv6 space
# solution 1: we can just get the addresses sequentially
# with next(gen)
# solution 2: we can take a sample of n (e.g., 10 elements, 
# and take a random address from there, and then iterate
# this procedure numelem times
