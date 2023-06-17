import sqlite3
import json
from enum import Enum  # TODO in 3.11 i can just use strenum


# these column names are going to change so it'll save me a bunch of time and typos later
class Column(Enum):
    NAME = "name"
    INGREDIENTS = "ingredients"
    TIMES_EATEN = "times_eaten"
    IN_CURRENT_LIST = "in_current_list"
    LAST_EATEN = "last_eaten"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


# could have been a global var since the scope is so small but the pun was too good to pass up
class DinnerTable:
    db: sqlite3.Connection

    def __init__(self):
        self.db = sqlite3.connect("dinner.db")
        self._create_table()

    def __del__(self):
        self.db.close()

    def _create_table(self):
        self.db.execute(
            f"""CREATE TABLE IF NOT EXISTS dinners(
                {Column.NAME} PRIMARY KEY, {Column.INGREDIENTS}, {Column.TIMES_EATEN}, {Column.IN_CURRENT_LIST}
                )"""
        )

    def _reset_table(self):
        """DROP TABLE convenience function. Use at your own peril"""
        self.db.execute("DROP TABLE dinners")
        self._create_table()

    def add_dinner(self, name: str, ingredients: list[str] | None = None):
        if ingredients and len(ingredients) >= 3:
            ingredients = str(ingredients)[1:-2].replace("'", "")
        else:
            ingredients = "none"

        data = (name, ingredients)
        self.db.execute("INSERT INTO dinners VALUES(?, ?, 0, FALSE)", data)
        self.db.commit()

    def remove_dinner(self, name: str):
        name = (name,)
        self.db.execute(f"DELETE FROM dinners WHERE {Column.NAME} IS ?", name)
        self.db.commit()

    def increment_count(self, name: str):
        name = (name,)
        self.db.execute(
            f"UPDATE dinners SET {Column.TIMES_EATEN} = {Column.TIMES_EATEN} + 1 WHERE {Column.NAME} IS ?", name
        )
        self.db.commit()

    def set_current(self, name: str):
        name = (name,)
        self.db.execute(f"UPDATE dinners SET {Column.IN_CURRENT_LIST} = TRUE WHERE {Column.NAME} IS ?", name)
        self.db.commit()

    def unset_current(self, name: str):
        name = (name,)
        self.db.execute(f"UPDATE dinners SET {Column.IN_CURRENT_LIST} = FALSE WHERE {Column.NAME} IS ?", name)
        self.db.commit()

    def filter_by(
        self,
        column: Column,
        contains: str,
        sort_by: Column = Column.NAME,
        ascending: bool = True,
    ) -> sqlite3.Cursor:
        return self.db.execute(
            f"SELECT * FROM dinners WHERE INSTR({column}, ?) > 0 ORDER BY {sort_by} {'ASC' if ascending else 'DESC'}",
            (contains,),
        )

    def edit(self, name: str, column: Column, new_value: str | int):
        self.db.execute(f"UPDATE dinners SET {column} = ? WHERE name IS ?", (new_value, name))
        self.db.commit()