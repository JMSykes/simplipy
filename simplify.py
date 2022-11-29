class simplify:
    def __init__(self,equation):
        self.parts = {'left_side':{},'right_side':{}}
        self.equation = equation
        self.left_side = equation.split('=')[0].strip()
        self.right_side = equation.split('=')[1].strip()

        var = ''

        for character in self.left_side:
            alph = 'abcdefghijklkmnopqrstuvwxyz'
            if character.lower() in alph:
                var += character
            elif (character.lower() not in alph) and (len(var) > 0):
                break

        def parenthetic_contents(string):
            stack = []
            for i, c in enumerate(string):
                if c == '(':
                    stack.append(i)
                elif c == ')' and stack:
                    start = stack.pop()
                    yield (len(stack), string[start + 1: i])


        self.parts['left_side']['p'] = list(parenthetic_contents(self.left_side))
        self.parts['right_side']['p'] = list(parenthetic_contents(self.right_side))


        self.variable = var

