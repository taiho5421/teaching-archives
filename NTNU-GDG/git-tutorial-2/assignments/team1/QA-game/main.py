import os

def load_question(filename):
    """
    從指定的 txt 檔案中讀取題目與答案。
    檔案格式假設第一行為 "Question: <題目>"，第二行為 "Answer: <答案>"。
    程式會自動剝除 "Question:" 與 "Answer:" 標籤。
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if len(lines) < 2:
                print(f"{filename} 格式錯誤，內容不足。")
                return None, None

            # 取得並剝除標籤 "Question:" 與 "Answer:"
            question_line = lines[0].strip()
            answer_line = lines[1].strip()

            if question_line.startswith("Question:"):
                question = question_line[len("Question:"):].strip()
            else:
                question = question_line

            if answer_line.startswith("Answer:"):
                answer = answer_line[len("Answer:"):].strip()
            else:
                answer = answer_line

            return question, answer
    except Exception as e:
        print(f"讀取 {filename} 時發生錯誤：{e}")
        return None, None

def play_game():
    score = 0
    total_levels = os.listdir("levels")
    # 過濾出所有的 txt 檔案
    total_levels = [f for f in total_levels if f.endswith(".txt") and f.startswith("level")]
    total_levels.sort()  # 確保關卡按照順序排列
    total_levels = len(total_levels)
    if total_levels == 0:
        print("沒有找到任何關卡檔案，請檢查 levels 資料夾。")
        return

    print("歡迎來到 QA Game！總共 8 關，答對會加分。")
    print("=" * 40)

    # 遍歷每一關的檔案
    for i in range(1, total_levels + 1):
        file_path = os.path.join("levels", f"level{i}.txt")
        question, answer = load_question(file_path)
        if not question or not answer:
            print(f"第 {i} 關題目讀取失敗，跳過此關卡。")
            continue

        print(f"第 {i} 關：")
        print(question)
        user_input = input("你的答案是：")

        # TODO: 可以進一步擴充答案比對的邏輯（例如忽略大小寫、空白符號等）
        if user_input.strip().lower() == answer.lower():
            print("回答正確！")
            score += 1
        else:
            print(f"回答錯誤，正確答案是：{answer}")
        print("-" * 40)

    print(f"遊戲結束，你的總分是：{score} / {total_levels}")

if __name__ == "__main__":
    play_game()