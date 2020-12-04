def prime(fn):
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper


class FSM:
    def __init__(self):
        # инициализация
        self.start = self._create_start()
        self.q1 = self._create_q1()
        self.q2 = self._create_q2()
        self.q3 = self._create_q3()

        # установка текущего состояния системы
        self.current_state = self.start
        # флаг остановки, чтобы обозначить,
        # что итерация остановлена из-за плохого
        # входа, для которого переход не был определен.
        self.stopped = False

    def send(self, char):
        """
        Функция отправляет текущий ввод в current_state.
        Она захватывает исключение StopIteration и помечает флаг stopped.
        """
        try:
            self.current_state.send(char)
        except StopIteration:
            self.stopped = True

    def does_match(self):
        """
        Функция в любой момент времени возвращает True если
        текущее состояние соответствует заданному выражению.
        Это делается путем сравнения текущего состояния с конечным состоянием `q3`.
        Она также проверяет наличие флага stopped, который назначается,
        при неправильного вводе и дальнейшея итерация FSM должна была быть остановлена.
        """
        if self.stopped:
            return False
        return self.current_state == self.q3

    @prime
    def _create_start(self):
        # Подождем, пока ввод не будет получен.
        # после получения сохраним ввод в `char`
        while True:
            char = yield
            # в зависимости от того, что мы получили
            # в качестве входных данных
            # изменить текущее состояние fsm
            if char == 'a':
                # при получении `a` состояние перемещается в` q1`
                self.current_state = self.q1
            else:
                # при получении любого другого ввода, разорвать петлю
                break

    @prime
    def _create_q1(self):
        while True:
            char = yield
            if char == 'b':
                self.current_state = self.q2
            elif char == 'c':
                self.current_state = self.q3
            else:
                break

    @prime
    def _create_q2(self):
        while True:
            char = yield
            if char == 'b':
                self.current_state = self.q2
            elif char == 'c':
                self.current_state = self.q3
            else:
                break

    @prime
    def _create_q3(self):
        while True:
            char = yield
            break


def grep_regex(text):
    evaluator = FSM()
    for ch in text:
        evaluator.send(ch)
    return evaluator.does_match()
