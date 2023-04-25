#
#   Set comprehension
#
#   Set comprehension works like list comprehension and accepts the same syntax that list comprehension accepts
#   Its a elegant and quick way to create sets based on loops with conditions
#
#   expression one: {expression for item in iterable}
#   expression two: {expression for item in iterable if condition}
#
#
#   It's a good way to obtain a filter effect:
#
#   html = {x for x in files if x.lower().endswith((".htm", ".html"))}

alpha_numeric_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f',
                     'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
