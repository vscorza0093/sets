# &#128013;  sets_studies
## Studying collection data type - Set


* Sets are mutable and ursorted collection, and can only store hashable and comparable objects, those objects that has the special method __hash__ that returns a unique hash number and persists during the object life and that could be compared by iguality with __eq__ special method. This aplly to the objects of imutable data type: tuple, frozenset, float, str, int


* We can create sets without the keys {}, using the function set(), but a empty set has to be created using the function set()


        empty_set = {}  -> wrong way to create a empty set
        empty_set2 = set()  -> correct way to create a empty set

* If we do not follow this condiction, we will not be able to use the method add() to add new values to the empty set

        empty_set2.add("first element")
        print(empty_set2)


* Sets, Lists, Dictionaries aren't hashable because its mutable, and every new item added would transform the hash number in a new number, so those collections can't be stored into a set

        wrong_set = {{"name":"vinicius", "lastname":"scorza"}, ["name", "lastname"]}

        print(wrong_set)

        tuple_set = {("tupla1", "tupla1.1"), ("tupla2", 2), frozenset({8, 5, 7})}
        print(tuple_set)

        * None
        print(tuple_set.__hash__)
        * <method-wrapper '__hash__' of str object at 0x00007FFB57E88C80>
        print("1".__hash__)
        * <method-wrapper '__hash__' of int object at 0x00007FFB57E7E328>
        print(int(1).__hash__)

* On the other hand, lists could store anything

        crazy_list = [{"set"}, {"dict": "onary"},
                      ["crazy", "list"], "oh gosh", 1, 0, 0]



        alpha_numeric_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f',
                             'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

        intermediate_set = {'1', '2', '3', '4', '5', 'f',
                            'g', 'h', 'j', 'k', 'l', 'm', 'p', 'v', 'z'}

* Sets, when iterated, returns it items in unordered way, theres no sort method to sets data type

* First method to get the difference between two sets
        difference_list = list(alpha_numeric_set.difference(intermediate_set))
        difference_list.sort()

        print(''.join(difference_list) + "-> first way")

* Second method to get the difference between two sets
        new_difference_list = list(alpha_numeric_set - intermediate_set)
        new_difference_list.sort()

        print(''.join(new_difference_list) + "-> second way")


* It's a good way to obtain a filter effect:

        html = {x for x in files if x.lower().endswith((".htm", ".html"))}

* Here we are selecting just the files that have the extension .htm or .html af transforming the input in a lower case string


## Frozenset

* Frozenset are a unordered and imutable collection data type, the only way to insert data into a frozenset is when we create it, so all the arguments has to be passed in time

        imutable_set = ({"string", 200, PesonClass()})

        out:'frozenset({<__main__.Person object at 0x0000025D0AC51010>, 3, 7, 'string', 6})'

* Receives one argument and try to convert this argument into a set, accepting just hashable types
        
        imutable_set = frozenset({7, 6, 3, "string", Person()})

        tuples_are_ok = frozenset({("tuple","collection","is","hashable","type")})
        frozenset_too = frozenset(imutable_set)

## Set Comprehension

* Set comprehension works like list comprehension and accepts the same syntax that list comprehension accepts
* Its a sofisticated and quick way to create sets based on loops with conditions

        expression one: {expression for item in iterable}
        expression two: {expression for item in iterable if condition}