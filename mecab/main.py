import MeCab

mecab = MeCab.Tagger()
print(mecab.parse("私はYahooプレミアム会員になりました。"))
