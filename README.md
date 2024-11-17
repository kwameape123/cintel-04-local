# cintel-04-local
## Author: Arnold Atchoe
## Date: 11/15/2024

## Project Description
    The goal of this project is to create an interactive dashboard app that allows users to analyze and 
    visualize the ** Palmer Penguins ** dataset. This project made use of shiny for python and GitHub 
    pages to achieve its goal.

## Data Description
   Dataset contains facts about three species of penguins observed on three island in **Palmer Archipelago, 
   Antarctica**. The data has been made available by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER, 
   a member of the Long Term Ecological Research Network.

    Column names for the penguins dataset include:

    ** species **: penguin species (Chinstrap, Adelie, or Gentoo)
    ** island **: island name (Dream, Torgersen, or Biscoe) in the Palmer Archipelago
    ** bill_length_mm **: length of the bill in millimeters
    ** bill_depth_mm **: depth of the bill in millimeters
    ** flipper_length_mm **: length of the flipper in millimeters
    ** body_mass_g **: body mass in grams
    ** sex **: MALE or FEMALE

## Data Cleaning and transformation
    Dataset has some missing values. To ensure accurate analysis, rows with at least one column of missing data 
    is deleted.

## Project Execution

### Prep Development Environment
Determine and prepare the tools require to execute project successfully.

1. Install latest version of python.
2. Install latest version of Git for version control.
3. Install VS Code as a Code editor.
4. Download and enable python and shiny extension for VS Code.
5. Create and activate python project virtual environment(.venv). Virtual enivroment keep
project dependencies exclusive.
```py -m venv .venv```
```.venv\Scripts\activate```
6. Install project dependencies and libraries.
```py -m pip install -r requirements.txt```
The requirements.txt file contains a list of all projedct dependencies to allow for easy installation.

#### Notes(In terminal):
1. Configure git with username and email used in github with the following lines of code;
```git config --global user.name "Your Name"```
```git config --global user.email "youremail@example.com"```
2. Check python version, Git version and confriguration with following lines of code;
 ```py --version```
```git --version```
 ```git config user.name```
 ```git config user.email```

### Run App
    Launch app in web browser by running ```shiny run --reload --launch-browser penguins/app.py``` in terminal. Terminal becomes occupied after running this code hence another terminal must be used for other tasks.

### Build App to Docs folder and Test locally.
    Keep virtual environment active for this step.
    1. Remove any existing static assets using terminal command ```shiny static-assets remove```,
    2. Export the contents of penguins folder to docs folder to build a web app using shinylive export. Docs folder is created if it does not exist. Terminal command used is 
```shinylive export penguins docs```
    3. Edit index.html file to modify web app browser tab to include custom title and favicon.Favicon used was generate on [text](https://favicon.io/).[text](https://favicon.io/) provides instructions on implement favicons. Section of index.html edited is shown below;
```<title>Arnold Atchoe-Palmer Penguins</title>```
```<link rel="icon" type="image/x-icon" href="./favicon.ico">```
    4.Test app in browser using the link generated by terminal command
 ```py -m http.server --directory docs --bind localhost 8008```.
 
### Publish App with GitHub Pages
GitHub pages hosts this web application. An initial confriguration is done to setup pages for repository containing the web app.
After, any subsequent update pushed to repository will be reflected in the web application.

    1. Go the settings tab of the web app repository.
    2. Scroll to the bottom of the page and click the pages section.
    3. Select branch main as the source for the site.
    4. Change from the root folder to the docs folder as publishing source.
    5. Click Save and wait for the site to build.
    6. Edit the "About" section of the repository to include a link to the live app.

## Resoruces  

Palmer Penguins published in:

Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer Archipelago (Antarctica) penguin data. R package version 0.1.0. https://allisonhorst.github.io/palmerpenguins/. doi: 10.5281/zenodo.3960218.

Data originally published in:

Gorman KB, Williams TD, Fraser WR (2014). Ecological sexual dimorphism and environmental variability within a community of Antarctic penguins (genus Pygoscelis). PLoS ONE 9(3):e90081. https://doi.org/10.1371/journal.pone.0090081
The Shiny development team. Shiny for Python [Computer software]. https://github.com/posit-dev/py-shiny

