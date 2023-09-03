val = [1, 2, 3, 4, 5]
thing = str(val)
thing2 = list([int(x) for x in thing if x != ',' and x != '[' and x != "]" and x != ' '])

print(thing)
print(thing2)


# from dinnertable.table import DinnerTable, Column

# db = DinnerTable()
# # db._reset_table()
# # db.add_dinner("stir fry")
# # db.add_dinner("spaghetti", ["pasta", "red sauce", "ground beef"])
# db.remove_dinner("burgers")

# thing = db.filter_by(Column.NAME, "s")

# for row in thing:
#     print(row)


# pass
