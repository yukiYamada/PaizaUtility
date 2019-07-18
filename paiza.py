import unittest
class Output():
    # 入力例
    input_lines = [3,28,16,777]
    # テスト結果
    expected = "perfect\nnearly\nneither"
    @staticmethod
    def main():     
        out = Output()
        print(out.mainlogic())

    def mainlogic(self):      
        try:
            result = ""
            #mainlogic
            return result
        except Exception as e:
            print(e)        

    input_lines_cursor = 0
    def input(self):
        self.input_lines_cursor += 1
        return self.input_lines[self.input_lines_cursor-1]

# 提出前確認用テストコード
class Testlogic(unittest.TestCase):
    def test_logic(self):
        actual = Output()
        self.assertEqual(Output.expected, actual.mainlogic())

if __name__ == "__main__":
    unittest.main()
    #Output.main()