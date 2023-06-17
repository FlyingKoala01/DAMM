# Implementation

Below you will see some technical details, in case you are trying to understand
the project, in order to make some changes by yourself.

## Database structure

You will see a file in this folder with the E/R diagram. Just some details:
- `Valoracion` contains the Google reviews.
- Nota contains the grades.

The rest of the things are quite intuitive.

## Grade system

As you can imagine, rankings may change every now and then, as well as reviews.
That's why a bar has multiple grades: one per month. The same happens with
`valoracion`.

In the `Establecimiento` table, the last two grades are stored, so the
webpage visits are performed faster.

Inside the utils folder you will find all the functions to add more samples.

## Web scrapping

The data from Google is retrieved via web-scrapping. The `get_geckodriver.sh`
downloads the firefox adapter for python, compatible with linux 64. It won't
work with other systems, but it's easy to find tutorials for other systems
and browsers.
