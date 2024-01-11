oseti
==========
|circleci| |coveralls| |pyversion| |version| |license|

Dictionary based Sentiment Analysis for Japanese

INSTALLATION
==============

::

 $ pip install oseti


USAGE
============

.. code:: python

  import oseti

  analyzer = oseti.Analyzer()
  analyzer.analyze('天国で待ってる。')
  # => [1.0]
  analyzer.analyze('遅刻したけど楽しかったし嬉しかった。すごく充実した！')
  # => [0.3333333333333333, 1.0]

  analyzer.count_polarity('遅刻したけど楽しかったし嬉しかった。すごく充実した！')
  # => [{'positive': 2, 'negative': 1}, {'positive': 1, 'negative': 0}])
  analyzer.count_polarity('そこにはいつもと変わらない日常があった。')
  # => [{'positive': 0, 'negative': 0}]

  analyzer.analyze_detail('お金も希望もない！')
  # => [{'positive': [], 'negative': ['お金-NEGATION', '希望-NEGATION'], 'score': -1.0}])
  analyzer.analyze_detail('お金がないわけではない')
  # => [{'positive': ['お金'], 'negative': [], 'score': 1.0}]

  # Applying user's dictionary
  analyzer = oseti.Analyzer(word_dict={'カワイイ': 'p', 'ブサイク': 'n'},
                            wago_dict={'イカ する': 'ポジ', 'まがまがしい': 'ネガ'})
  analyzer.analyze_detail("カワイイ")
  # => [{'positive': ['カワイイ'], 'negative': [], 'score': 1.0}]
  analyzer.analyze_detail("ブサイクだ")
  # => [{'positive': [], 'negative': ['ブサイク'], 'score': -1.0}]
  analyzer.analyze_detail("まがまがしい")
  # => [{'positive': [], 'negative': ['まがまがしい'], 'score': -1.0}]
  analyzer.analyze_detail("イカすよ")
  # => [{'positive': ['イカ する'], 'negative': [], 'score': 1.0}]

ACKNOWLEDGEMENT
=================

This module uses 日本語評価極性辞書（用言編）ver.1.0 and 日本語評価極性辞書（名詞編）ver.1.0

- 小林のぞみ，乾健太郎，松本裕治，立石健二，福島俊一. 意見抽出のための評価表現の収集. 自然言語処理，Vol.12, No.3, pp.203-222, 2005. / Nozomi Kobayashi, Kentaro Inui, Yuji Matsumoto, Kenji Tateishi. Collecting Evaluative Expressions for Opinion Extraction, Journal of Natural Language Processing 12(3), 203-222, 2005.

- 東山昌彦, 乾健太郎, 松本裕治. 述語の選択選好性に着目した名詞評価極性の獲得. 言語処理学会第14回年次大会論文集, pp.584-587, 2008. / Masahiko Higashiyama, Kentaro Inui, Yuji Matsumoto. Learning Sentiment of Nouns from Selectional Preferences of Verbs and Adjectives. Proceedings of the 14th Annual Meeting of the Association for Natural Language Processing, pp.584-587, 2008.

Cited by
=========

Scientific paper
-----------------
- 田村匠, 丸山真佐夫. Character-Level CNNを用いた日本語評判分析. 情報処理学会第84回全国大会, Vol.2, pp.675-676, 2022.
- 安達 由洋, 近藤 友啓, 小林 孝充, 惠谷 菜央, 石井 解人. 感情語辞書を用いた日本語文の感情分析. 可視化情報学会誌, 2021, 41 巻, 161 号, p. 21-27, 2022.
- イー フエイチー, 望月 源. テレビ字幕データを用いた感情分析による「ある日の日本の気分」推定に関する研究. 言語処理学会 第28回年次大会 発表論文集, pp.857-862, 2022.
- 渡邉みさと, 沼部恵, 阿部沙亜弥, 尾上洋介. BuzzLead：TikTokの流行曲予測システム. 情報処理学会インタラクション2023, p.956-961, 2023.
- 丸山 正人, 竹川 高志. 個人の特性を反映した文章の類似度判定による小説推薦. DEIM Forum 2020 P2-26, 2020.
- 星野 雄介. ⾃然⾔語処理技術を⽤いた新型コロナウイルスに関する新聞社説の予備的分析―新聞社ごとの違いと研究の展望―. 武蔵野大学経営研究所紀要, p.113-148, 2022.
- Uģis Nastevičs. THE IMAGE OF LATVIA AND LATVIANS ON JAPANESE TWITTER: REFLECTIONS ON PEOPLE. Culture Crossroads, Vol. 17, p.93-113, 2021.
- Kazuko UNO. How to spread accurate scientific-based information in real time after large-scale disasters: a multifaceted research of radiation related information spreading on Twitter after 3.11. 2022.
- Tomoya Ohba, Candy Olivia Mawalim, Shun Katada, Haruki Kuroki, Shogo Okada. Multimodal Analysis for Communication Skill and Self-Efficacy Level Estimation in Job Interview Scenario. MUM 2022, P.110–120, 2022.
- Kunihiro Miyazaki, Takayuki Uchiba, Fujio Toriumi, Kenji Tanaka, Takeshi Sakaki. Retrospective Analysis of Controversial Subtopics on COVID-19 in Japan. ASONUM'21, p.510-517, 2022.

Slide
------
- Python ライブラリ開発における失敗談 〜開発者に選ばれるライブラリを作るために必要なこと〜 / pycon-jp-2022: https://speakerdeck.com/taishii/pycon-jp-2022

Blog
-----
- 肯否分析 [自然言語処理の餅屋]: https://www.jnlp.org/nlp/%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%83%9E%E3%82%A4%E3%83%8B%E3%83%B3%E3%82%B0/%E8%82%AF%E5%90%A6%E5%88%86%E6%9E%90
- メンヘラがツイートを形態素解析して気分の波を調べた結果www #Python - Qiita: https://qiita.com/yusuke_astro/items/dc38802b81f348189a98
- AKIBA.AWS ONLINE #09で「Amazon Comprehendから始める感情分析」について話しました #AKIBAAWS | DevelopersIO: https://dev.classmethod.jp/articles/talking-about-amazon-comprehend-and-sentiment-analysis-in-akiba-aws-online-09/
- Slackのtimesにネガポジ分析を掛けて1年を振り返る - susunshunのお粗末な記録: https://susunshun.hatenablog.com/entry/2019/12/25/173221

.. |circleci| image:: https://dl.circleci.com/status-badge/img/gh/ikegami-yukino/oseti/tree/master.svg?style=svg
        :target: https://dl.circleci.com/status-badge/redirect/gh/ikegami-yukino/oseti/tree/master

.. |coveralls| image:: https://coveralls.io/repos/ikegami-yukino/oseti/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/ikegami-yukino/oseti?branch=master
    :alt: coveralls.io

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/oseti.svg

.. |version| image:: https://img.shields.io/pypi/v/oseti.svg
    :target: http://pypi.python.org/pypi/oseti/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/oseti.svg
    :target: http://pypi.python.org/pypi/oseti/
    :alt: license
