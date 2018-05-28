#!/usr/bin/python
# coding=utf-8
import random


# Class for 'Rock, paper, scissors'
class Thing:
    def __init__(self):
        self.__what = ''

    # Method for creating rock, paper or scissors (randomly)
    def randoms(self):
        self.Choices = ["rock", "papor", "scissors"]
        self.__what = random.choice(self.Choices)

    # Method returning the value for __what variable
    def get_what(self):
        return self.__what
