#!/usr/bin/python2
from nose.tools import *
from ex49 import lexicon, ex49

def test_peek():
    result = lexicon.scan("the bear go")
    empty_result = []
    assert_equal(ex49.peek(empty_result), None)
    assert_equal(ex49.peek(result), "stop")

def test_match():
    result = lexicon.scan("the bear go")
    empty_result = []
    assert_equal(ex49.match(empty_result, "verb"), None)
    assert_equal(ex49.match(result, "stop"), ("stop", "the"))
    assert_equal(ex49.match(result, "noun"), ("noun", "bear"))

def test_skip():
    result = lexicon.scan("the bear go")
    empty_result = []
    assert_equal(ex49.skip(result, "stop"), None)
    assert_equal(ex49.skip(empty_result, "error"), None)

def test_parse_verb():
    result = lexicon.scan("the go")
    empty_result = []
    assert_equal(ex49.parse_verb(result), ("verb","go"))
    assert_raises(ex49.ParserError, ex49.parse_verb, empty_result)

def test_parse_object():
    err = lexicon.scan("the go")
    result = lexicon.scan("the bear")
    assert_equal(ex49.parse_object(result), ("noun","bear"))
    assert_raises(ex49.ParserError, ex49.parse_object, err)

def test_parse_subject():
    err = lexicon.scan("the go")
    result = lexicon.scan("kill the bear")
    assert_equal(ex49.parse_subject(result, ("noun","player")), (("noun","player"), ("verb","kill"), ("noun","bear")))
    assert_raises(ex49.ParserError, ex49.parse_subject, err, ("noun","player"))

def test_parse_sentence():
    err = lexicon.scan("this will error")
    result = lexicon.scan("the princess kill the bear")
    result2 = lexicon.scan("kill the bear")
    assert_equal(ex49.parse_sentence(result), (("noun","princess"), ("verb","kill"), ("noun","bear")))
    assert_equal(ex49.parse_sentence(result2), (("noun","player"), ("verb","kill"), ("noun","bear")))
    assert_raises(ex49.ParserError, ex49.parse_sentence, err)

"""
def parse_sentence(word_list):
    skip(word_list, 'stop')
    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_sentence(word_list, subj)
    elif start == 'verb':
        # assume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object or verb not: {}".format(start)
"""
