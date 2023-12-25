from sqlite3 import connect
from plotly.express import scatter_mapbox
from pandas import DataFrame
from contextlib import closing

# creating connection with the sqilte database file
with closing(connect('data.db')) as connection:
  with closing(connection.cursor()) as cursor:
    # importing all data into the var rows
    cursor.execute("SELECT * FROM locations")
    rows = cursor.fetchall()

# adding the data from the rows into var data in prpoer format
data = {'location': [], 'latitude': [], 'longitude': [], 'value': []}
for row in rows[1:]:
  data['location'].append(row[0])
  data['latitude'].append(row[1])
  data['longitude'].append(row[2])
  data['value'].append(row[3])

# setting up the data frame using data
data_frame = DataFrame(data)

figure = scatter_mapbox(
  data_frame,
  lat="latitude",
  lon="longitude",
  color="value",
  color_continuous_scale="RdYlBu",
  size="value",
)
figure.update_layout(title="Custom Map of Sri Lanka", mapbox_style="open-street-map")
figure.show()
