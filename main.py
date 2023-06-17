from dinnerlist.table import DinnerTable, Column

db = DinnerTable()
# db._reset_table()
# db.add_dinner("stir fry")
# db.add_dinner("spaghetti", ["pasta", "red sauce", "ground beef"])
db.remove_dinner("burgers")
db.add_dinner("burger", ["ground beef", "buns", "onion", "ketchup", "fries"])

db.edit("stir fry", Column.TIMES_EATEN, 1)

thing = db.filter_by(Column.NAME, "s")

for row in thing:
    print(row)


pass
