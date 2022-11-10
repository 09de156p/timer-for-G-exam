# ライブラリのインポート
import time
import sys
import winsound

def count_timer(q, m, m_remain):
    """問題数をカウント"""
    # 試験時間-予備の時間（秒）
    s = (m*60)-(m_remain*60)

    print("="*5 + "試験開始（", round(s/q, 2), f"秒ごとに{q}問カウント）" + "="*5)
    for q_count in range(1, q+1):
        for s_count in range(int(s/q)):

            if s_count == int(s/q)-1:
                s_count += 1         
                
                # ビープ音を一秒鳴らす
                frequency = 700
                duration = 1000 #1,000ミリ秒
                winsound.Beep(frequency, duration)

                sys.stdout.write("\r%d" % s_count + "秒経過")
                sys.stdout.flush()

            else:
                s_count += 1
                time.sleep(1)
                sys.stdout.write("\r%d" % s_count + "秒経過")
                sys.stdout.flush()
            
        print("\n" + "-"*5 + f"{q_count}問／{q}問終了!" + "-"*5)
        
    print("="*5 + "試験終了" + "="*5)

if __name__ == "__main__":
    # 問題数
    q = 220
    # 試験時間（120分）
    m = 120
    # 予備の時間（10分）
    m_remain = 10
    # 試験時間をカウントする関数実行
    count_timer(q, m, m_remain)