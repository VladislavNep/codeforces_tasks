import re
from tdparser import Lexer, Token


# определяем типы символов и их повидения как токен
class Integer(Token):
    regexp = r'\d+'  # символ

    def nud(self, context):
        """
        Описывает, что происходит с этим токеном, когда он находится в начале выражения.
        :param context:
        :return:
        """
        return int(self.text)


class Addition(Token):
    regexp = r'\+'
    lbp = 10  # приоритет операции

    def led(self, left, context):
        return left + context.expression(self.lbp)


class Multiplication(Token):
    regexp = r'\*'
    lbp = 20

    def led(self, left, context):
        """
        Описывает, что происходит с этим токеном при появлении внутри
        конструкции (слева от остальной части конструкции).
        :param left:
        :param context:
        :return:
        """
        return left * context.expression(self.lbp)


class Division(Token):
    regexp = r'/'
    lbp = 20

    def led(self, left, context):
        return left // context.expression(self.lbp)


class RightParen(Token):
    def __repr__(self):
        return '<)>'


class LeftParen(Token):
    match = RightParen

    def nud(self, context):
        expr = context.expression()
        context.consume(expect_class=self.match)
        return expr

    def __repr__(self):
        return '<(>'


# регистрация токенов
lexer = Lexer()
lexer.register_tokens(Integer, Addition, Multiplication, Division)
lexer.register_token(LeftParen, re.compile(r'\('))
lexer.register_token(RightParen, re.compile(r'\)'))


def parse(text):
    """Преобразует лексические токены в представление"""
    return lexer.parse(text)


print("(((10+1)*(5+6/(3+1))+4*(3+1)))")
print(f'Результат вычеслений после разбора: {parse("(((10+1)*(5+6/(3+1))+4*(3+1)))")}')
