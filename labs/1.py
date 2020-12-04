import unittest

root = {
    'var': "qwertyuiopasdfghjklzxcvbnm",
    'unar_opr': "*+/-",
    'bin_opr': "$"
}


def language_recognition(expr, i=0, var=0, opr=0):
    """
    Хитрый рекурсивный подход
    """

    if i == len(expr):
        if opr == var - 1:
            return True
        else:
            return False

    if expr[i] in root['unar_opr']:
        opr += 1
        return language_recognition(expr, i+1, var, opr)

    elif expr[i] in root['var']:
        var += 1
        return language_recognition(expr, i+1, var, opr)

    elif expr[i] in root['bin_opr'] and expr[i+1] in root['unar_opr']:
        return language_recognition(expr, i+1, var, opr)

    else:
        return False


class LanguageRecognitionTest(unittest.TestCase):
    """
    2 набора тестов, на правильное построение и неправлиное. Сравнивает ответ программы с установленным ответом в тесте.
    return: OK or error(и описание в каком тесте и какой набор не прошел проверку)
    """

    def test_true(self):
        arr_test = ["**abc", "+a/bc", "*/abc", "+a-*/bcd*uk", "+*-abc//ghj", "$+a-*/bcd*uk", "+*-abc$//ghj"]
        for i in arr_test:
            result = language_recognition(i)
            print(result, i)
            self.assertEqual(result, True)

    def test_false(self):
        arr_test = ["*abc", "+a/b*c", "*/ab$c", "+a*/bcd*uk", "+*-abc/ghj**", "$+a-*/bc$d*uk"]
        for i in arr_test:
            result = language_recognition(i)
            print(result, i)
            self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
