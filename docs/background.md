# Background

For you to follow this writeup I recomend to familarize yourself with the [SQL database howto](https://fastapi.tiangolo.com/tutorial/sql-databases/) on Tiangolo's documentation site for fastAPI.

Basically he builds a simple two table model, `users` and `items`, were each user can have more than one item, and each item belongs to one user.  Not that difficult to follow I hope but it shows the basic relationship I had going, except I had about 15 tables that all belonged to the user.


## Code layout

At the time of this writing the setup of the [bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) example found on the fastAPI documentation page is structured around having all routers in one folder, all pydantic schemas in another, etc.

Although there is nothing wrong with organizing your code in this way, the more database tables you have to build APIs for and the more the database tables are connected this rather understanable type of layout starts to become confusing. Example: am I working with the schema for a user or the database model? They both have the same file name, they are just located in different folders. Ok bad example but think of the situation when you are dealing with 15 or 20 database tables?

An alternative layout, keeping everything in one folder that is related to a single database table or logical object (if it makes sense e.g. to base that on more than one database table) starts to make more sense.  In this example where we are talking about reducing boilerplate code in CRUD routes for many tables it would also make sense to write up the example code using this second layout.

At least it makes sense to me.  Feel free to structure your code as makes most sense to you of course. It will not affect the basic principle of this write up.

So you will see a folder with the name `users` and a folder with the name `items`, that deal with users and items respectively.  Each folder will have a file name `router.py`, `schema.py` and `model.py` that deal with, you guessed it the routers, schemas and models for the users or items depending in which folder they are located.

Ok that was hopefully the complicated bits.  Now come the [good bits](./good_bits)....