import pytest


def test_demo2_methodA(oneTimeSetUp, setUp):  # zamiana miejsca powoduje odwrotne działanie w teście
    print('Uruchamiam conftest demo2 methodA')     

def test_demo2_methodB(oneTimeSetUp, setUp):
    print('Uruchamiam conftest demo2 methodB')