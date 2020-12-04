from pythonds.basic.stack import Stack


class ConvertToPostfix:
    def __init__(self, expr):
        self.expr = expr
        self.prec_set = {'+', '-', '*', '/'}
        self.var = "qwertyuiopasdfghjklzxcvbnm"

    def infix_to_postfix(self):
        prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
        op_stack = Stack()
        postfix_list = []
        token_list = list(self.expr)

        for token in token_list:
            if token in self.var:
                postfix_list.append(token)
            elif token == '(':
                op_stack.push(token)
            elif token == ')':
                top_token = op_stack.pop()
                while top_token != '(':
                    postfix_list.append(top_token)
                    top_token = op_stack.pop()
            else:
                while (not op_stack.isEmpty()) and \
                        (prec[op_stack.peek()] >= prec[token]):
                    postfix_list.append(op_stack.pop())
                op_stack.push(token)

        while not op_stack.isEmpty():
            postfix_list.append(op_stack.pop())
        return f"{self.expr} -> {''.join(postfix_list)}"

    def prefix_to_postfix(self):
        stack_list = []
        expr = self.expr[::-1]

        for i in expr:
            if i in self.prec_set:
                a = stack_list.pop()
                b = stack_list.pop()
                temp = a + b + i
                stack_list.append(temp)
            else:
                stack_list.append(i)

        return f"{self.expr} -> {stack_list[0]}"

    def convert(self):
        if (self.expr[0] or self.expr[1]) in self.prec_set:
            return self.prefix_to_postfix()
        elif (self.expr[0] or self.expr[1]) in self.var:
            return self.infix_to_postfix()


# этакий бонус)
# мы можем воспользоваться функцией convert()
# и она сама определит форму записи "префиксный" или "инфиксный"
obj_1 = ConvertToPostfix("*-a/bc-/akl").convert()
obj_3 = ConvertToPostfix("a*b+c*d").convert()

# Или можем явно указать функцию конвертации
obj_2 = ConvertToPostfix("++a*bcd").prefix_to_postfix()
obj_4 = ConvertToPostfix("(a+b)*c-(d-e)*(f+g)").infix_to_postfix()

print(obj_1)
print(obj_2)
print(obj_3)
print(obj_4)
