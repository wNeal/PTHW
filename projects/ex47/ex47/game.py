#!/usr/bin/python2
class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        print "Direction: {}".format(direction)
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
