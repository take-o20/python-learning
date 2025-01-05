import MeCab

mecab = MeCab.Tagger()
print(mecab.parse("死は生の対極としてではなく、その一部として存在している。"))
