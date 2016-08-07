"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Model.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
Brand.query.filter((Brand.discontinued.isnot(None)) | (Brand.founded > 1950)).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    yrmods = db.session.query(Model.name, Brand.name,
                              Brand.headquarters).join(Brand).filter(Model.year == year).all()

    for name, brand_name, hq in yrmods:
        print name, brand_name, hq


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_mods = db.session.query(Brand.name, Model.name).join(Model).all()

    for name, model in brand_mods:
        print name, model

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
"""The returned value is a location in memory. It is a query object of the Brand class."""
# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
"""An association table is a table with foreign keys belonging to two or more different tables.
It manages an indirect but related relationship between different sets of data,
to connect an otherwise abstract many-to-many relationship(s)"""

# -------------------------------------------------------------------
# Part 3


def search_brands_by_name(mystr):
    """Returns list of brands with name containing/matching str parameter input."""
    # Design a function in python that takes in any string as parameter,
    # and returns a list of objects that are brands whose name contains or is equal to the input string.
    compare_str = {'mystr': mystr}

    similar_brands = db.session.query(Brand).filter(Brand.name.like('%{mystr}%'.format(**compare_str))).all()

    return similar_brands


def get_models_between(start_year, end_year):
    """Returns list of model objects produced between start yr (inclusive &
        end yr (exclusive)."""

    # I tried to accomplish the below with a dictionary, similar to
    # line 89 for search_brands function, but I couldn't get the formatting right.
    # Does this still santize the inputs?
    start = start_year
    end = end_year

    released_mods = db.session.query(Model).filter((Model.year >= start) & (Model.year < end)).all()

    return released_mods
