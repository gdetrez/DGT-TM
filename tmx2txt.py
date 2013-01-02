#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tmx2txt
This is a simple script that reads a TMX (translation memory) file
and extracts segments for one or more languages.

The format of the output is a simple txt file with one segment per line.
"""
from __future__ import division
import xml.sax
import os, sys
import random
import unittest

class Walkerrandom:
  """ Walker's alias method for random objects with different probablities
  from http://code.activestate.com/recipes/576564-walkers-alias-method-for-random-objects-with-diffe/
  """

  def __init__( self, weights, keys=None ):
    """ builds the Walker tables prob and inx for calls to random().
        The weights (a list or tuple or iterable) can be in any order;
        they need not sum to 1.
    """
    n = self.n = len(weights)
    self.keys = keys
    sumw = sum(weights)
    prob = [w * n / sumw for w in weights]  # av 1
    inx = [-1] * n
    short = [j for j, p in enumerate( prob ) if p < 1]
    long = [j for j, p in enumerate( prob ) if p > 1]
    while short and long:
        j = short.pop()
        k = long[-1]
        # assert prob[j] <= 1 <= prob[k]
        inx[j] = k
        prob[k] -= (1 - prob[j])  # -= residual weight
        if prob[k] < 1:
            short.append( k )
            long.pop()
    self.prob = prob
    self.inx = inx

  def __str__( self ):
    """ e.g. "Walkerrandom prob: 0.4 0.8 1 0.8  inx: 3 3 -1 2" """
    probstr = " ".join([ "%.2g" % x for x in self.prob ])
    inxstr = " ".join([ "%.2g" % x for x in self.inx ])
    return "Walkerrandom prob: %s  inx: %s" % (probstr, inxstr)

  def random( self ):
    """ each call -> a random int or key with the given probability
        fast: 1 randint(), 1 random.uniform(), table lookup
    """
    u = random.uniform( 0, 1 )
    j = random.randint( 0, self.n - 1 )  # or low bits of u
    randint = j if u <= self.prob[j] \
        else self.inx[j]
    return self.keys[randint] if self.keys \
        else randint

class TMXContentHandler(xml.sax.ContentHandler):

  def __init__(self, outputs, split=None):
    xml.sax.ContentHandler.__init__(self)
    # Parameters
    if split:
      self.bins = Walkerrandom(split)
    self.split = split is not None
    self.outputs = outputs
    
    # State
    self.lang = None
    self.i = 0
    self.bin = None

  def startElement(self, name, attrs):
    if name == "tu":
      if self.split:
        self.bin = self.bins.random()
    if name == "tuv":
      lang = attrs['lang']
      if lang in self.outputs:
        self.lang = lang

  def characters(self,content):
    if self.lang:
      content = content.strip()
      assert content.find("\n") == -1, "Found new line at %d" % content.find("\n")
      self.write(content)

  def write(self,s):
    assert self.lang is not None
    if self.split:
      assert self.bin is not None
      self.outputs[self.lang][self.bin].write(s)
    else:
      self.outputs[self.lang].write(s)

  def endElement(self, name):
    if name == "tuv" and self.lang is not None:
      self.write("\n")
      self.lang = None
    if name == "tu":
      self.bin = None

    self.i += 1

def mkFilename(oldname,*exts):
  base,_ = os.path.splitext(oldname)
  return ".".join((base,) + exts)

if __name__ == "__main__":
  import argparse, codecs

  parser = argparse.ArgumentParser(description='Extract segments from TMX files')
  parser.add_argument('corpus', metavar='CORPUS.TMX', type=unicode,
                      help='The tmx file')
  parser.add_argument('languages', metavar='LANG', type=unicode, nargs='+',
                      help='Languages to extract')
  parser.add_argument('--split', dest='split', metavar=('TRAIN','DEV','TEST'),
                      type=int, nargs=3, action='store', default=None,
                      help='Split the corpus in multiple parts')
  args = parser.parse_args()


  outputs = {}
  try:
    for l in args.languages:
      if args.split:
        outputs[l] = [
          codecs.open(mkFilename(args.corpus,l,t,"txt"),'w','utf-8')
          for t in ("train","dev","test")]
      else:
        outputs[l] = codecs.open(mkFilename(args.corpus,l,"txt"), 'w', 'utf-8')

    source = open(args.corpus, 'r')
    xml.sax.parse(source, TMXContentHandler(outputs, args.split))
  finally:
    for l in outputs:
      if isinstance(outputs[l],list):
        for f in outputs[l]: f.close()
      else:
        outputs[l].close()


###############################################################################
###############################################################################
###############################################################################
# TESTS
#
# This section contains some tests for the different part of the program.
# Use nosetests to run.
from collections import defaultdict
from StringIO import StringIO

class TestMkFilename(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_simple(self):
      name = mkFilename("file.tmx","jpg")
      self.assertEqual("file.jpg",name)

    def test_multiple(self):
      name = mkFilename("file.tmx","a", "b", "c")
      self.assertEqual("file.a.b.c",name)


class TestWalkerrandom(unittest.TestCase):

  def setUp(self):
    pass

  def test_bins(self):
    weights = [1,2,3]
    N = 100000
    wrandom = Walkerrandom(weights)
    result = defaultdict(lambda: 0)
    for i in range(N):
      result[wrandom.random()] += 1
    print result
    for i,w in enumerate(weights):
      self.assertAlmostEqual(w/sum(weights),result[i]/N, places=2)


class TestTMXContentHandler(unittest.TestCase):
  xml = """<?xml version="1.0" ?>
<!DOCTYPE tmx SYSTEM "tmx11.dtd">
<tmx version="version 1.1">
<body>
<tu>
<prop type="Txt::Doc. No.">22004A0520(01)R(01)</prop>
<tuv lang="fr"><seg>Un éléphant dans in magasin de poecelaine</seg></tuv>
<tuv lang="en"><seg>A bull in a china shop</seg></tuv>
</tu>
</body>
</tmx>
"""

  def test_handler(self):
    outputs = {
      'fr': StringIO(),
      'en': StringIO()
      }
    xml.sax.parse(StringIO(self.xml), TMXContentHandler(outputs))
    self.assertEqual(u"Un éléphant dans in magasin de poecelaine\n",
                     outputs['fr'].getvalue())
    self.assertEqual(u"A bull in a china shop\n",
                     outputs['en'].getvalue())    

###############################################################################
###############################################################################
###############################################################################