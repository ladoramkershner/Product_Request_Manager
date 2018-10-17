
from product_request_gui import Product_Request #import the class that controls the gui

app = Product_Request()
app.mainloop()
parameters = app.outputs

print(parameters['Requestor Name'])
