import dearpygui.dearpygui as dpg
from dinnerlist.table import DinnerTable, Column
from dinnerlist.callbacks import sort_callback, add_dinner_callback

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

db = DinnerTable()
items = db.get_all()

dpg.create_context()

with dpg.window(tag="add_dinner", show=False, modal=True, label="Add Dinner", min_size=[300, 100]):
    with dpg.table(
        header_row=False,
        row_background=True,
        borders_innerH=True,
        borders_outerH=True,
        borders_innerV=True,
        borders_outerV=True,
        user_data=db,
    ):
        # use add_table_column to add columns to the table,
        # table columns use child slot 0
        dpg.add_table_column(label="Name")
        dpg.add_table_column(label="Ingredients")
        dpg.add_table_column(label="In Current List", width_fixed=True, tag="curr_list")

        with dpg.table_row():
            dpg.add_input_text(
                label="Name",
            )
            dpg.add_input_text(label="Ingredients")
            dpg.add_checkbox(label="Current List")

with dpg.window(tag="Primary Window"):
    dpg.add_button(label="Add Dinner", callback=add_dinner_callback)
    with dpg.table(
        header_row=True,
        row_background=True,
        borders_innerH=True,
        borders_outerH=True,
        borders_innerV=True,
        borders_outerV=True,
        sortable=True,
        callback=sort_callback,
    ):
        # use add_table_column to add columns to the table,
        # table columns use child slot 0
        dpg.add_table_column(label="Name", default_sort=True)
        dpg.add_table_column(label="Ingredients")
        dpg.add_table_column(label="Times Eaten", width_fixed=True)
        dpg.add_table_column(label="In Current List", width_fixed=True)

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        for i, item in enumerate(items):
            with dpg.table_row():
                dpg.add_text(f"{item[0]}")
                dpg.add_text(f"{item[1]}")
                dpg.add_text(f"{int(item[2])}")
                dpg.add_checkbox(default_value=bool(item[3]))


dpg.create_viewport(title="Dinner Table", width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
