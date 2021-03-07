# 日時関連の命令を使ときに宣言
from datetime import datetime

# 現在時刻を取得して任意の書式で表示
t = datetime.now()
fmt = t.strftime('%Y年%m月%d日 %H時%M分%S秒')
print(fmt)

# 2022/01/01を指定してオブジェクトを作成
t = datetime(2022, 1, 1)
#　日付を表示
print(t.strftime('%Y年%m月%d日 %H時%M分%S秒'))# 結果例：2022年01年01日

# 予定日を指定
yoteibi = datetime(2025, 4, 13)
# 今日の指定
now = datetime.now()
# 日時計算
delta = yoteibi - now
# 結果を表示
print('あと'+str(delta.days+1)+'日です')
