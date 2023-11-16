from math import sqrt


class Triang:
    def __init__(self, a: float, b: float, c: float) -> None:
        """
        Parameters:
            a (float) - Lado do triangulo.
            b (float) - Lado do triangulo.
            c (float) - Lado do triangulo.
        """
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """Calculo da área do triangulo.

        Returns:
            float: Retona a área.
        """
        a, b, c = self.a, self.b, self.c
        p = (a + b + c) * 0.5
        return sqrt(p * (p - a) * (p - b) * (p - c))

    def is_valid(self) -> bool:
        """Verifica se o triangulo é válido.

        Returns:
            bool: Retorna se o triangulo pe válido.
        """
        return self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b
