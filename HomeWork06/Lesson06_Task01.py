def count_and_show_variables_size(variables_list, include_varlist_size=False):
    def namestr(obj, namespace):
        return [name for name in namespace if namespace[name] is obj]

    def show_size(x, level=0, include_level_0=False):
        import sys
        if include_level_0 is False:
            if level != 0:
                size_count = sys.getsizeof(x)
                print("\t" * level,
                      "Имя переменной = %s; тип = %s; размер = %d; содержимое = " % (namestr(x, globals()),
                                                                                     type(x), sys.getsizeof(x)),
                      x)
            else:
                size_count = 0
        else:
            size_count = sys.getsizeof(x)
            print("\t" * level,
                  "Имя переменной = %s; тип = %s; размер = %d; содержимое = " % (namestr(x, globals()), type(x),
                                                                                 sys.getsizeof(x)), x)
        if hasattr(x, "__iter__") and not isinstance(x, str):
            if hasattr(x, "items"):
                for key, value in x.items():
                    size_count += show_size(key, level + 1)
                    size_count += show_size(value, level + 1)
            else:
                for item in x:
                    size_count += show_size(item, level + 1)
        return size_count

    size_of_border_line_ = 80
    print("=" * size_of_border_line_)
    print("Данные о переменных:")
    total_size = show_size(variables_list, include_level_0=include_varlist_size)
    print("=" * size_of_border_line_)
    print("Суммарный размер всех переменных из списка:", total_size)


a = 111
b = "Hello, Alex Petrenko!"
c = "This is homework 06"
d = ["It's a nice day today. Beautiful snow is falling on the street."]
e = {"e_a": 4332, "e_b": 5454, "e_d": False, "e_e": 1}

count_and_show_variables_size([a, b, c, d, e])



# /Volumes/ARHIV/PYTHON/Algoritm_dannye/HomeWork/venv/bin/python /Volumes/ARHIV/PYTHON/Algoritm_dannye/HomeWork/HW06/Lesson06_Task01.py
# ================================================================================
# Данные о переменных:
# 	 Имя переменной = ['a']; тип = <class 'int'>; размер = 28; содержимое =  111
# 	 Имя переменной = ['b']; тип = <class 'str'>; размер = 70; содержимое =  Hello, Alex Petrenko!
# 	 Имя переменной = ['c']; тип = <class 'str'>; размер = 68; содержимое =  This is homework 06
# 	 Имя переменной = ['d']; тип = <class 'list'>; размер = 80; содержимое =  ["It's a nice day today. Beautiful snow is falling on the street."]
# 		 Имя переменной = []; тип = <class 'str'>; размер = 112; содержимое =  It's a nice day today. Beautiful snow is falling on the street.
# 	 Имя переменной = ['e']; тип = <class 'dict'>; размер = 248; содержимое =  {'e_a': 4332, 'e_b': 5454, 'e_d': False, 'e_e': 1}
# 		 Имя переменной = []; тип = <class 'str'>; размер = 52; содержимое =  e_a
# 		 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  4332
# 		 Имя переменной = []; тип = <class 'str'>; размер = 52; содержимое =  e_b
# 		 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  5454
# 		 Имя переменной = []; тип = <class 'str'>; размер = 52; содержимое =  e_d
# 		 Имя переменной = []; тип = <class 'bool'>; размер = 24; содержимое =  False
# 		 Имя переменной = []; тип = <class 'str'>; размер = 52; содержимое =  e_e
# 		 Имя переменной = []; тип = <class 'int'>; размер = 28; содержимое =  1
# ================================================================================
# Суммарный размер всех переменных из списка: 922