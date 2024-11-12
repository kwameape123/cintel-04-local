# This is an interactive data application that features a dashboard displaying a data table, two histograms and two scatterplots 
# for selected datasets. 

# Users can modify specific aspects of the visuals and see the results in real-time. 

# This data application consists of two components: the user interface and the server section. 

# The user interface enables users to issue commands that are executed on the server side.

# Import required dependencies
import seaborn as sns
import plotly.express as px
import palmerpenguins # This package provides palmer penguin dataset.
from shiny import reactive
from shiny.express import input, ui,render
from shinywidgets import render_plotly

##############################
# Get dataset to be presented and load into pandas dataframe
###############################
# Dataset Description
###############################
# species: penguin species (Chinstrap, Adelie, or Gentoo)
# island: island name (Dream, Torgersen, or Biscoe) in the Palmer Archipelago
# bill_length_mm: length of the bill in millimeters
# bill_depth_mm: depth of the bill in millimeters
# flipper_length_mm: length of the flipper in millimeters
# body_mass_g: body mass in grams
# sex: MALE or FEMALE

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

# Function to handle NaN Errors
# This function with get rid of rows in a dataframe with NaN values in any column
def clean_dataframe(df):
    # Drop rows where any column contains NaN
    return df.dropna()

###########################
#Define and Design our user interface.
############################

# Create a title for webpage
ui.page_opts(title="Arnold Atchoe- Palmer Peguins", fillable=True)

# Create a sidebar for user input and interaction.
# Siderbar has the following features:
# Header for the sidebar.
# A selector that has 3 options and is currently not linked to any output.
# An input box that takes only numbers and specify the number of bins for the bill lenght histogram.
# An input slider that is used to specify the number of bins for the body mass histogram.
# A list of species of penguins with checkbox to filter the first table.
# A horizontal line(ui.hr) to separate sections of the side bar.
# A link to the project github repository named "GitHub"
# Note that the input value indicate in user interface components indicate the default value of these components when we run the program.


with ui.sidebar(open="open"):
    ui.h2("Sidebar")
    ui.input_selectize("Selected_attribute","Select Attribute",["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"])
    ui.input_numeric("plotly_bin_count","Number of Plotly Bins",value=6)
    ui.input_slider("seaborn_bin_count","Number of Seaborn Bins",value=6,min=4,max=20)
    ui.input_checkbox_group("selected_species_list","Select Species",["Adelie", "Gentoo", "Chinstrap"],selected=["Adelie"],inline=True)
    ui.input_checkbox_group("selected_island_list","Select Island",["Biscoe","Dream","Torgersen"])
    ui.hr()
    ui.a("GitHub",href="https://github.com/kwameape123/cintel-02-data",target="_blank")

############################
# Render the desired charts and visuals
############################

# Render DataTable and Datagrid within the same layout column.
with ui.layout_columns():
# the reactive.event decorator allows for the filtering of data in data table using the options of the checkbox.  
    with ui.card(full_screen=True):
        ui.card_header("Data Table for Palmer Penguins")
        @reactive.event(input.selected_species_list)
        def species_data():
            return penguins_df[penguins_df['species'].isin(input.selected_species_list())]
# this render.data_frame decorator returns filtered data 
        @render.data_frame
        def table():
           return species_data() 
            
    with ui.card(full_screen=True):
        ui.card_header("Data Grid for Palmer Penguins")
        @render.data_frame
        def grid():
           return render.DataGrid(data=filtered_data())

# Render plotly and seaborn histogram within the same layout column.
            
with ui.layout_columns():
     with ui.card(full_screen=True):
        ui.card_header("Distribution of Penguins bill length")
        @render_plotly
        def plot1():
            return px.histogram(filtered_data(), x="bill_length_mm",nbins=input.plotly_bin_count())
            
     with ui.card(full_screen=True):
        ui.card_header("Distribution of Penguins body mass")
        @render.plot
        def plot2():
            return sns.histplot(data=filtered_data(), x="body_mass_g")

# Render plotly and seaborn scatterplot within the same layout column.
            
with ui.layout_columns(height="1000px"):
     with ui.card(full_screen=True):
        ui.card_header("Relationship between bill length and body mass(Plotly)")
        @render_plotly
        def plot3():
         return px.scatter(data_frame=filtered_data(),x="bill_length_mm", y="body_mass_g",color="species",hover_name="island",symbol="sex")

     with ui.card(full_screen=True):
        ui.card_header("Relationship between bill length and body mass(Seaborn)")
        @render.plot
        def plot4():
         return sns.scatterplot(data=filtered_data(),x="bill_length_mm", y="body_mass_g",hue="species")

# --------------------------------------------------------
# Reactive calculations and effects
# --------------------------------------------------------

# Add a reactive calculation to filter the data with respect to species and island
# By decorating the function with @reactive, we can use the function to filter the data
# The function will be called whenever an input functions used to generate that output changes.
# Any output that depends on the reactive function (filtered_data()) will be updated when the data changes.

@reactive.calc
def filtered_data():
    Speciesmatch=penguins_df["species"].isin(input.selected_species_list())
    Islandmatch= penguins_df["island"].isin(input.selected_island_list())
    filtered_data=penguins_df[Speciesmatch & Islandmatch]
    return clean_dataframe(filtered_data)
