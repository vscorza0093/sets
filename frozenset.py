class Person:
    def __init__(self):
        self.name = "Vinicius"

imutable_set = frozenset({7, 6, 3, "string", Person()})
print(imutable_set)


tuples_are_ok = frozenset({("tuple","collection","is","hashable","type")})
frozenset_too = frozenset(imutable_set)

print(tuples_are_ok)
print(frozenset_too)


