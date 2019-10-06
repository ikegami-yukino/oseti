# -*- coding: utf-8 -*-
from nose.tools import assert_equal
import oseti


class TestAnalyzer(object):
    def test_lookup_wago(self):
        a = oseti.Analyzer()
        actual = a._lookup_wago('うんざり', [])
        assert_equal(actual, 'うんざり')
        actual = a._lookup_wago('軽い', ['尻', 'が'])
        assert_equal(actual, '尻 が 軽い')
        actual = a._lookup_wago('どうでもいい', [])
        assert_equal(actual, '')

    def test_has_arujanai(self):
        a = oseti.Analyzer()
        actual = a._has_arujanai('やる気あるじゃない')
        assert_equal(actual, True)
        actual = a._has_arujanai('やる気ないじゃない')
        assert_equal(actual, False)

    def test_calc_sentiment_polarity(self):
        a = oseti.Analyzer()
        actual = a._calc_sentiment_polarity('最高な仕事')
        assert_equal(actual, [['最高', 1]])
        actual = a._calc_sentiment_polarity('貪欲じゃないじゃない。')
        assert_equal(actual, [['貪欲', -1]])
        actual = a._calc_sentiment_polarity('どうでもいい')
        assert_equal(actual, [])
        actual = a._calc_sentiment_polarity('お金も希望もある')
        assert_equal(actual, [['お金', 1], ['希望', 1]])
        actual = a._calc_sentiment_polarity('お金とか希望なりない')
        assert_equal(actual, [['お金-NEGATION', -1], ['希望-NEGATION', -1]])
        actual = a._calc_sentiment_polarity('お金だの希望だの喜びだのない')
        assert_equal(actual, [['お金-NEGATION', -1], ['希望-NEGATION', -1], ['喜び-NEGATION', -1]])
        actual = a._calc_sentiment_polarity('お金と希望や喜びがない')
        assert_equal(actual, [['お金-NEGATION', -1], ['希望-NEGATION', -1], ['喜び-NEGATION', -1]])
        actual = a._calc_sentiment_polarity('お金があるじゃない')
        assert_equal(actual, [['お金', 1]])

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

    def test_analyze_detail(self):
        a = oseti.Analyzer()
        text = '遅刻したけど楽しかったし嬉しかった。すごく充実した！'
        actual = a.analyze_detail(text)
        assert_equal(actual, [{'positive': ['楽しい', '嬉しい'], 'negative': ['遅刻'], 'score': 0.3333333333333333},
                              {'positive': ['充実'], 'negative': [], 'score': 1.0}])
        actual = a.analyze_detail('お金も希望もない！')
        assert_equal(actual, [{'positive': [], 'negative': ['お金-NEGATION', '希望-NEGATION'], 'score': -1.0}])
        actual = a.analyze_detail('お金がないわけではない')
        assert_equal(actual, [{'positive': ['お金'], 'negative': [], 'score': 1.0}])
