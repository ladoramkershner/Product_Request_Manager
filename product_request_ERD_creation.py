
from product_request_gui import Product_Request #import the class that controls the gui

app = Product_Request()
app.mainloop()
parameters = app.outputs
'''parameters dictionary keys include:
(REQUIRED)
Requestor Name
Project Name
Target Name
Product Description
Deadline
Minimum Latitude and Maximum Latitude
Minimum Longitude and Maximum Longitude
Stereo Boolean
(OPTIONAL)
Minimum Emission and Maximum Emission
Minimum Incidence and Maximum Incidence
Minimum Phase and Maximum Phase
Minimum Mean Ground Resolution and Maximum Mean Ground Resolution
Minimum Solar Longitude and Maximum Solar Longitude
Minimum Start Date and Maximum Start Date
'''
#query upc database download
#create ERD and add table with product request information
