# -*- coding: utf-8 -*-
from nose.tools import assert_equal
import oseti


class TestAnalyzer(object):
    def test_lookup_wago(self):
        a = oseti.Analyzer()
        actual = a._lookup_wago('うんざり', [])
        assert_equal(actual, -1)
        actual = a._lookup_wago('軽い', ['尻', 'が'])
        assert_equal(actual, -1)
        actual = a._lookup_wago('どうでもいい', [])
        assert_equal(actual, None)
    def test_has_arujanai(self):
        a = oseti.Analyzer()
        actual = a._has_arujanai('やる気あるじゃない')
        assert_equal(actual, True)
        actual = a._has_arujanai('やる気ないじゃない')
        assert_equal(actual, False)

    def test_calc_sentiment_polarity(self):
        a = oseti.Analyzer()
        actual = a._calc_sentiment_polarity('最高な仕事')
        assert_equal(actual, [1])
        actual = a._calc_sentiment_polarity('貪欲じゃないじゃない。')
        assert_equal(actual, [-1])
        actual = a._calc_sentiment_polarity('どうでもいい')
        assert_equal(actual, [])

    def test_count_polarity(self):
        a = oseti.Analyzer()
        text = '遅刻したけど楽しかったし嬉しかった。すごく充実した！'
        actual = a.count_polarity(text)
        assert_equal(actual, [{'positive': 2, 'negative': 1}, {'positive': 1, 'negative': 0}])
        text = 'そこにはいつもと変わらない日常があった。'
        actual = a.count_polarity(text)
        assert_equal(actual, [{'positive': 0, 'negative': 0}])

    def test_analyze(self):
        a = oseti.Analyzer()
        text = '遅刻したけど楽しかったし嬉しかった。すごく充実した！'
        actual = a.analyze(text)
        assert_equal(actual, [0.3333333333333333, 1.0])
        text = 'そこにはいつもと変わらない日常があった。'
        actual = a.analyze(text)
        assert_equal(actual, [0.0])
