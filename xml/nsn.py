# %%
import pandas as pd

# %%
df_lib = pd.read_xml('lib.xml',xpath='/lib')

# %%
df_lib

# %%
df_cor = pd.read_xml('lib.xml',xpath='/lib/corner')
df_cor

# %%
df_view = pd.read_xml('lib.xml',xpath='/lib/corner/view')
df_view

# %%
df_view2 = pd.read_xml('lib.xml',xpath='//view')
df_view2

# %%
df_cell = pd.read_xml('lib.xml',xpath='/lib/corner/view/cell')
df_cell

# %%
df_cell2 = pd.read_xml('lib.xml',xpath='//cell')
df_cell2

# %%
df_pin = pd.read_xml('lib.xml',xpath='/lib/corner/view/cell/pin')
df_pin

# %%
df_pin2 = pd.read_xml('lib.xml',xpath='//pin')
df_pin2

# %%
df_state = pd.read_xml('lib.xml',xpath='/lib/corner/view/cell/pin/state')
df_state

# %%
df_cell_cap = pd.read_xml('lib.xml',xpath='/lib/corner/view[@name="CAP"]/cell')
df_cell_cap

# %%
df_pin_cap = pd.read_xml('lib.xml',xpath='/lib/corner/view[@name="CAP"]//pin')
df_pin_cap

# %%
df_cell_cap = pd.read_xml('lib.xml',xpath='/lib/corner/view[@name="CAP"]//pin[@name="VDD"]//data')
print(df_cell_cap)


