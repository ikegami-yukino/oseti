# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nose.tools import assert_equal
import oseti


class TestAnalyzer(object):
    def test_split_per_sentence(self):
        a = oseti.Analyzer()
        actual = a._split_per_sentence('今日は雨。明日は雪?')
        assert_equal(len(list(actual)), 2)

    def test_lookup_wago(self):
        a = oseti.Analyzer()
        actual = a._lookup_wago('うんざり', [])
        assert_equal(actual, -1)
        actual = a._lookup_wago('軽い', ['尻', 'が'])
        assert_equal(actual, -1)
        actual = a._lookup_wago('どうでもいい', [])
        assert_equal(actual, None)

    def test_calc_sentiment_polarity(self):
        a = oseti.Analyzer()
        actual = a._calc_sentiment_polarity('最高な仕事')
        assert_equal(actual, 1)
        actual = a._calc_sentiment_polarity('貪欲じゃないじゃない。')
        assert_equal(actual, -1)
        actual = a._calc_sentiment_polarity('どうでもいい')
        assert_equal(actual, 0)

    def test_analyze(self):
        a = oseti.Analyzer()
        text = '遅刻したけど楽しかったし嬉しかった。すごく充実した！'
        actual = a.analyze(text)
        assert_equal(actual, [0.3333333333333333, 1.0])
