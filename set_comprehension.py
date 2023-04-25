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
