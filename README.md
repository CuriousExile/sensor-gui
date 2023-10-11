# Django PI Temperatur Sensor Web View

> Features: 

- ✅ `temperature graph of selected inerval`
- ✅ `check current temperature`

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone git@github.com:CuriousExile/sensor-gui.git
$ cd sensor-gui
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                            
   |    |-- settings.py   # Project Configuration  
   |    |-- urls.py       # Project Routing
   |
   |-- home/
   |    |-- views.py      # APP Views 
   |    |-- urls.py       # APP Routing
   |    |-- models.py     # APP Models 
   |    |-- tests.py      # Tests  
   |     
   |-- templates/
   |    |-- includes/     # UI components 
   |    |-- layouts/      # Masterpages
   |    |-- pages/        # Kit pages 
   |
   |-- static/   
   |    |-- css/                                   # CSS Files 
   |    |-- scss/                                  # SCSS Files 
   |         |-- soft-ui-dashboard/_variables.scss # File Used for Theme Styling
   |
   |-- requirements.txt   # Project Dependencies
   |
   |-- env.sample         # ENV Configuration (default values)
   |-- manage.py          # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## Recompile SCSS  

The SCSS/CSS files used to style the Ui are saved in the `static` directory. 
In order to update the Ui colors (primary, secondary) this procedure needs to be followed. 

```bash
$ yarn                                             # install modules
$ vi static/scss/soft-ui-dashboard/_variables.scss # edit variables 
$ gulp                                             # SCSS to CSS translation
```

The `_variables.scss` content defines the `primary` and `secondary` colors: 

```scss
$primary:       #cb0c9f !default;   // EDIT for customization 
$secondary:     #8392AB !default;   // EDIT for customization 
$info:          #17c1e8 !default;   // EDIT for customization 
$success:       #82d616 !default;   // EDIT for customization 
$warning:       #fbcf33 !default;   // EDIT for customization 
$danger:        #ea0606 !default;   // EDIT for customization 
```

<br />