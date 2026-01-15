from src.exec_check import checkA

def test_contains_A():

    # "A" を含む場合

    # (※) assert というのは ざっくり言うと
    # 「checkA("A") を実行して結果が 1 になるか確認して」のような機能です。
    # 演習では「結果をファイルに出力して、正解データと比較する」のような
    # 話をしたかと思いますが、それに該当することを pytest でやってくれるものです。

    # 単体文字
    assert checkA("A") == 1

    # 先頭
    assert checkA("APPLE") == 1

    # 途中
    assert checkA("TABLE") == 1

    # 最後
    assert checkA("CUBA") == 1

    # 複数
    assert checkA("BANANA") == 1



def test_contains_B():

    # "B" を含む場合
    # ※ 演習なので単純化のため省略してますが、実践では "A" の場合と同様の熱量でテストケースを作ってください。

    # 単体文字
    assert checkA("B") == 2



def test_contains_C():

    # "C" を含む場合
    # ※ 演習なので単純化のため省略してますが、実践では "A" の場合と同様の熱量でテストケースを作ってください。

    # 単体文字
    assert checkA("C") == 3



def test_does_not_contain_abc():
    # "A", "B", "C" を含まない場合
    assert checkA("DFGHIJK") == 0
    assert checkA("123") == 0
    assert checkA("") == 0  # 空文字



def test_case_sensitivity():
    # 小文字の "a" は含まないと判定されることを確認（大文字小文字の区別）
    assert checkA("apple") == 0

    # 小文字の "b" は含まないと判定されることを確認（大文字小文字の区別）
    assert checkA("b") == 0

    # 小文字の "c" は含まないと判定されることを確認（大文字小文字の区別）
    assert checkA("c") == 0



