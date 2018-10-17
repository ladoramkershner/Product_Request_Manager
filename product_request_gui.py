
import tkinter as tk

class Product_Request(tk.Tk): #make Product Request a child of tk.Tk
    def __init__(self):
        tk.Tk.__init__(self) #initialize parent class
        rw = 0 #variable row dim; iterated after each entry field group
        wl = 52 #width of long entry fields
        small_font = ("Times New Roman",12)
        header_font = ("Times New Roman",16)
        self.title("Product Request")
        self.geometry("415x550")

        #-----------------------------
        ##REQUIRED INPUTS##
        tk.Label(text="Required Inputs", font=header_font).grid(columnspan=4, row=rw)
        rw+=1

        #Name
        tk.Label(self, text="Your Name", font=small_font).grid(column=0, row=rw, sticky="E")
        self.name_entry = tk.Entry(self,width=wl)
        self.name_entry.grid(column=1, row=rw, columnspan=3, sticky="W")
        rw+=1

        #Project
        tk.Label(self, text="Project Name", font=small_font).grid(column=0, row=rw, sticky="E")
        self.project_entry = tk.Entry(width=wl)
        self.project_entry.grid(column=1, row=rw, columnspan=3, sticky="W")
        rw+=1

        #Target
        tk.Label(self, text="Target Name", font=small_font).grid(column=0, row=rw, sticky="E")
        self.target_entry = tk.Entry(width=wl)
        self.target_entry.grid(column=1, row=rw, columnspan=3, sticky="W")
        rw+=1

        #Latitude
        tk.Label(self, text="Latitude", font=small_font).grid(columnspan=4, row=rw)
        rw+=1
        tk.Label(self, text="Minimum", font=small_font).grid(column=0, row=rw, sticky="E")
        self.lat_min_entry = tk.Entry()
        self.lat_min_entry.grid(column=1, row=rw, sticky="W")
        tk.Label(self, text="Maximum", font=small_font).grid(column=2, row=rw, sticky="E")
        self.lat_max_entry = tk.Entry()
        self.lat_max_entry.grid(column=3, row=rw, sticky="W")
        rw+=1

        #Longitude
        tk.Label(self, text="Longitude", font=small_font).grid(columnspan=4, row=rw)
        rw+=1
        tk.Label(self, text="Minimum", font=small_font).grid(column=0, row=rw, sticky="E")
        self.lon_min_entry = tk.Entry()
        self.lon_min_entry.grid(column=1, row=rw, sticky="W")
        tk.Label(self, text="Maximum", font=small_font).grid(column=2, row=rw, sticky="E")
        self.lon_max_entry = tk.Entry()
        self.lon_max_entry.grid(column=3, row=rw, sticky="W")
        rw+=1

        #Stereo
        tk.Label(self, text="Stereo Pair? ", font=small_font).grid(column=0, row=rw, sticky="E")
        self.stereo = tk.BooleanVar()
        self.stereo_entry = tk.Checkbutton(variable=self.stereo, onvalue=True, offvalue=False)
        self.stereo_entry.grid(column=1, row=rw, sticky="W")
        rw+=1

        #-----------------------------
        ##OPTIONAL INPUTS##
        tk.Label(self, text="Optional Inputs", font=header_font).grid(columnspan=4, row=rw)
        rw+=1

        #Emission Angle
        tk.Label(self, text="Emission Angle", font=small_font).grid(columnspan=4, row=rw)
        rw+=1
        tk.Label(self, text="Minimum", font=small_font).grid(column=0, row=rw, sticky="E")
        self.ema_min_entry = tk.Entry()
        self.ema_min_entry.grid(column=1, row=rw, sticky="W")
        tk.Label(self, text="Maximum", font=small_font).grid(column=2, row=rw, sticky="E")
        self.ema_max_entry = tk.Entry()
        self.ema_max_entry.grid(column=3, row=rw, sticky="W")
        rw+=1

        #Incidence Angle
        tk.Label(self, text="Incidence Angle", font=small_font).grid(columnspan=4, row=rw)
        rw+=1
        tk.Label(self, text="Minimum", font=small_font).grid(column=0, row=rw, sticky="E")
        self.ina_min_entry = tk.Entry()
        self.ina_min_entry.grid(column=1, row=rw, sticky="W")
        tk.Label(self, text="Maximum", font=small_font).grid(column=2, row=rw, sticky="E")
        self.ina_max_entry = tk.Entry()
        self.ina_max_entry.grid(column=3, row=rw, sticky="W")
        rw+=1

        #Phase Angle
        tk.Label(self, text="Phase Angle", font=small_font).grid(columnspan=4, row=rw)
        rw+=1
        tk.Label(self, text="Minimum", font=small_font).grid(column=0, row=rw, sticky="E")
        self.pha_min_entry = tk.Entry()
        self.pha_min_entry.grid(column=1, row=rw, sticky="W")
        tk.Label(self, text="Maximum", font=small_font).grid(column=2, row=rw, sticky="E")
        self.pha_max_entry = tk.Entry()
        self.pha_max_entry.grid(column=3, row=rw, sticky="W")
        rw+=1

        #Mean Ground Resolution
        tk.Label(self, text="Mean Ground Resolution", font=small_font).grid(columnspan=4, row=rw)
        rw+=1
        tk.Label(self, text="Minimum", font=small_font).grid(column=0, row=rw, sticky="E")
        self.mgr_min_entry = tk.Entry()
        self.mgr_min_entry.grid(column=1, row=rw, sticky="W")
        tk.Label(self, text="Maximum", font=small_font).grid(column=2, row=rw, sticky="E")
        self.mgr_max_entry = tk.Entry()
        self.mgr_max_entry.grid(column=3, row=rw, sticky="W")
        rw+=1

        #Solar Longitude
        tk.Label(self, text="Solar Longitude", font=small_font).grid(columnspan=4, row=rw)
        rw+=1
        tk.Label(self, text="Minimum", font=small_font).grid(column=0, row=rw, sticky="E")
        self.solar_lon_min_entry = tk.Entry()
        self.solar_lon_min_entry.grid(column=1, row=rw, sticky="W")
        tk.Label(self, text="Maximum", font=small_font).grid(column=2, row=rw, sticky="E")
        self.solar_lon_max_entry = tk.Entry()
        self.solar_lon_max_entry.grid(column=3, row=rw, sticky="W")
        rw+=1

        #Start Time
        tk.Label(self, text="Start Date", font=small_font).grid(columnspan=4, row=rw)
        rw+=1
        tk.Label(self, text="Earliest", font=small_font).grid(column=0, row=rw, sticky="E")
        self.start_date_min_entry = tk.Entry()
        self.start_date_min_entry.grid(column=1, row=rw, sticky="W")
        tk.Label(self, text="Latest", font=small_font).grid(column=2, row=rw, sticky="E")
        self.start_date_max_entry = tk.Entry()
        self.start_date_max_entry.grid(column=3, row=rw, sticky="W")
        rw+=1

        ##SUBMIT BUTTON##
        self.submit_button = tk.Button(self, text="Submit Request", font=small_font, command=self.submit).grid(column=3, row=rw, sticky="E")

    def submit(self):
        required_outputs = {'Requestor Name': self.name_entry.get(), 'Project Name': self.project_entry.get(), 'Target Name': self.target_entry.get(),
        'Minimum Latitude': self.lat_min_entry.get(), 'Maximum Latitude': self.lat_max_entry.get(), 'Minimum Longitude': self.lon_min_entry.get(),
        'Maximum Longitude': self.lon_max_entry.get(), 'Stereo Boolean': self.stereo.get()}

        optional_outputs = {'Minimum Emission': self.ema_min_entry.get(), 'Maximum Emission': self.ema_max_entry.get(),
        'Minimum Incidence': self.ina_min_entry.get(), 'Maximum Incidence': self.ina_max_entry.get(), 'Minimum Phase': self.pha_min_entry.get(),
        'Maximum Phase': self.pha_max_entry.get(), 'Minimum Mean Ground Resolution': self.mgr_min_entry.get(),
        'Maximum Mean Ground Resolution': self.mgr_max_entry.get(), 'Minimum Solar Longitude': self.solar_lon_min_entry.get(),
        'Maximum Solar Longitude': self.solar_lon_max_entry.get(), 'Minimum Start Date': self.start_date_min_entry.get(),
        'Maximum Start Date': self.start_date_max_entry.get()}

        self.quit() #close the window, when the submit button is hit
        self.outputs = {**required_outputs, **optional_outputs} #create class variable from concatenated dictionaries
