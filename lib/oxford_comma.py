def oxford_comma(items):
    if len(items) == 2:
        print(items)
        comma_separated = ", ".join(items[:-1])
        print (comma_separated)
        c = f"{comma_separated} and {items[-1]}"
        print(c)
        return c
    if len(items) > 2:
        print(items)
        comma_separated = ", ".join(items[:-1])
        print (comma_separated)
        c = f"{comma_separated}, and {items[-1]}"
        print(c)
        return c
    else:
        return items[0]
