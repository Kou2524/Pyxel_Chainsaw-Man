import pyxel

# Pyxel初期化:幅160×高さ120ピクセル、タイトル設定
pyxel.init(160, 120, title="Pyxel Title Test")

# 画像を読み込む(GitHubのURLに置き換えてね)
pyxel.image(0).load(0, 0, "https://raw.githubusercontent.com/Kou2524/Pyxel_Chainsaw-Man/main/IRIS-OUT_1536.PNG")

# 描画関数
def draw():
    pyxel.cls(0)  # 画面をクリア(0=黒)
    pyxel.blt(0, 0, 0, 0, 0, 160, 120)  # 画像を画面に描画

# Pyxelループ開始(描画関数だけ呼び出す)
pyxel.run(lambda: None, draw)
