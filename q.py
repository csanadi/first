import math


class InvalidCoefficientError(ValueError):
    def __init__(self) -> None:
        super().__init__("Az 'a' együttható nem lehet 0 (nem másodfokú egyenlet).")


class QuadraticSolver:
    def __init__(self, a: float, b: float, c: float) -> None:
        if a == 0:
            raise InvalidCoefficientError()
        self.a = a
        self.b = b
        self.c = c

    def _discriminant(self) -> float:
        return self.b**2 - 4 * self.a * self.c

    def solve(self) -> tuple[complex, complex]:
        d = self._discriminant()
        two_a = 2 * self.a
        if d >= 0:
            sqrt_d = math.sqrt(d)
            x1 = complex((-self.b + sqrt_d) / two_a)
            x2 = complex((-self.b - sqrt_d) / two_a)
        else:
            real = -self.b / two_a or 0.0  # elkerüli a -0.0 megjelenését
            imag = math.sqrt(-d) / two_a
            x1 = complex(real, imag)
            x2 = complex(real, -imag)
        return x1, x2


def _format_root(root: complex) -> str:
    if root.imag == 0:
        return f"{root.real:g}"
    return (
        f"{root.real:g} + {root.imag:g}i"
        if root.imag > 0
        else f"{root.real:g} - {abs(root.imag):g}i"
    )


def main() -> None:
    print("Másodfokú egyenlet megoldója: ax² + bx + c = 0")
    print("------------------------------------------------")
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
    except ValueError:
        print("Hiba: csak számot adhatsz meg.")
        return

    try:
        solver = QuadraticSolver(a, b, c)
    except InvalidCoefficientError as e:
        print(f"Hiba: {e}")
        return

    x1, x2 = solver.solve()
    d = solver._discriminant()

    b_str = f"+ {b:g}" if b >= 0 else f"- {abs(b):g}"
    c_str = f"+ {c:g}" if c >= 0 else f"- {abs(c):g}"
    print(f"\nEgyenlet: {a:g}x² {b_str}x {c_str} = 0")
    print(f"Diszkrimináns: D = {d:g}")

    if x1 == x2:
        print(f"Kétszeres gyök: x = {_format_root(x1)}")
    elif d < 0:
        print("Komplex gyökök:")
        print(f"  x₁ = {_format_root(x1)}")
        print(f"  x₂ = {_format_root(x2)}")
    else:
        print(f"x₁ = {_format_root(x1)}")
        print(f"x₂ = {_format_root(x2)}")


if __name__ == "__main__":
    main()
