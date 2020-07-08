# This is the plan on how the iDataAnalyse processing section will be made

This program has several legs.
They are

Image to dictionary:

{img.png} --> <[1, 2, 5, x, 6]>

Push info to database:

{1, 2, 5, x, 6} PY --> {1, 2, 5, x, 6} JSON

Pull data from database:

{1, 2, 5, x, 6} JSON --> {1, 2, 5, x, 6} PY