# learningml

## jupyter notebook インストール
[参考](https://qiita.com/naohiro2g/items/3368baa8fc93eff00e49)
```
・jupyter notebook install
$ xcode-select --install
$ brew install python3
$ sudo easy_install pip
$ /usr/local/Cellar/python/3.7.2_2/bin/pip3 install jupyter --user

・TensorFlow install
$ pip3 install tensorflow

・jupyter notebook 起動
$ /Users/ogalush/Library/Python/3.7/bin/jupyter notebook
→ ブラウザ → New → Python3を開くとPythonスクリプトを入力できる.｀｀｀
```

## StrengthsFinderのサンプルデータ取得
```
・Jupyter Notebookで実行する.
import sys
sys.path.append('/Users/ogalush/Documents/eclipse-workspace/test/learningml')
import strengthsFinder
import json
st = strengthsFinder.strengthsFinder()
user = {}
for i in range(0,3,1):
  userName = "user" + str(i)
  user[userName] = st.setStrangthValue(st.getStrengthDict())

## 画面出力 https://docs.python.org/ja/3/library/json.html
print(json.dumps(user, ensure_ascii=False, sort_keys=True, separators=(',', ': '), indent=1))
```
