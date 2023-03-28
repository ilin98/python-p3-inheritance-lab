#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name, knowledge = 0):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def learn(self, knowledge):
        self.knowledge = knowledge
