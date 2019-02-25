#!/usr/bin/env python3

import randomness


def test_randrnr_exists():
    assert 'randnr' in dir(randomness), "You need to write the randnr class"
    _ = randomness.randnr()


def test_randnr_randint():
    r1 = randomness.randnr(1)
    i1 = r1.randint()
    assert i1 == 1015568748, "Wrong sequence from randint for seed '1'"
    i2 = r1.randint()
    assert i2 == 1586005467, "Wrong sequence from randint for seed '1'"
    i3 = r1.randint()
    assert i3 == 2165703038, "Wrong sequence from randint for seed '1'"


def test_randnr_random():
    r1 = randomness.randnr(1)
    i1 = r1.random()
    assert i1 == 0.23645552527159452, "Wrong sequence from random for seed '1'"
    i2 = r1.random()
    assert i2 == 0.3692706737201661, "Wrong sequence from random for seed '1'"
    i3 = r1.random()
    assert i3 == 0.5042420323006809, "Wrong sequence from random for seed '1'"    


def test_randnr_exp():
    r1 = randomness.randnr(1)
    i1 = r1.exp(1)
    assert i1 == 0.26978390490222603, "Wrong sequence from exp(1) for seed '1'"
    i2 = r1.exp(1)
    assert i2 == 0.46087846840742835, "Wrong sequence from exp(1) for seed '1'"
    i3 = r1.exp(1)
    assert i3 == 0.7016674397006556, "Wrong sequence from exp(1) for seed '1'"


def test_randnr_gaus():
    r1 = randomness.randnr(1)
    i1 = r1.gauss()
    assert i1 == -0.8526897819421493, "Wrong sequence from random for seed '1'"
    i2 = r1.gauss()
    assert i2 == 0.7867476733784203, "Wrong sequence from random for seed '1'"
    i3 = r1.gauss()
    assert i3 == -1.6179551251263622, "Wrong sequence from random for seed '1'"
