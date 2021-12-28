# How-To: Build generic crud functions with fastAPI

Here I will show you one way to massively reduce the ammount of boilerplate code in 
fastAPI for standard CRUD operations of database tables in a relational database.

I  was faced with writing an API for an app that some database tables that were all related to one master table. Meaning a single entry in the master table could have one or more related entries in any of the other tables.

## backstory

For our example let's say that the master table contained user information. And one of these related tables contained items the user owned and another one contained the users todo list. The two related tables did not have any direct conections with each other as they contained lists of completely different nature. 

Each would need a typical Create and Read API. Well that's not a problem you say and start coding away... Nothing to it, you finish coding for one table and realize that you can pretty much copy and paste the code for table number two, change a few schema and model references and voila, second table API is done in record time.

Ah but then there's a third list of things the user needs to keep track of, their grocery shopping list... oh and their top 3 favorite movies, and so the list grows for a while.

But you grow with task and copying and pasting your boilerplate code doesn't take all that much time anyway so all is good in the world, project done and delivered!  

Not so fast... now the users are so happy with what you delivered that they come up with some new and crazy ideas they want to have as well, what about update? that would be so great to be able to update some of those things, oh.. oh.. and delete, just to be able to clean up some of these lists... I mean who has heard of a todo list where you couldn't update the status or delete old things off the list?

Aaand the create should also be able to deal with not just single create requests but a list of new entries. Multiple updates could also come in handy...

And soon you realize that the nearest future will involve some quality time copying and pasting again.

Good times!

Of course that is not what you should do, give your ctlr-C fingers a bit of a rest and let me show you a better way.  It is by far not the only way but I do think this way will limit your boilerplate code to something reasonable, like a single line or so.

## Prepare to be dassled

In order for you to quickly understand the basic concept I followed the example Tiangolo used for his [SQL database howto](https://fastapi.tiangolo.com/tutorial/sql-databases/)
If you are not familiar with his code you should skip over there and read it, it is not comlicated but both covers some of the basics of working with databases and fastAPI plus we will be using (and expanding) the datamodel that he introduces there.  So jump over there and take a look.  I'll wait here until you are back, don't worry.
## Code layout

At the time of this writing the setup of the [bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) example found on the fastAPI documentation page is structured around having all routers in one folder, all pydantic schemas in another, etc.

Although there is nothing wrong with organizing your code in this way, the more database tables you have to build APIs for and the more the database tables are connected this rather understanable type of layout starts to become confusing. Example: am I working with the schema for a user or the database model? They both have the same file name, they are just located in different folders. Ok bad example but think of the situation when you are dealing with 15 or 20 database tables?

An alternative layout, keeping everything in one folder that is related to a single database table or logical object (if it makes sense e.g. to base that on more than one database table) starts to make more sense.  In this example where we are talking about reducing boilerplate code in CRUD routes for many tables it would also make sense to write up the example code using this second layout.

At least it makes sense to me.  Feel free to structure your code as makes most sense to you of course. It will not affect the basic principle of this write up.

So you will see a folder with the name `users` and a folder with the name `items`, that deal with users and items respectively.  Each folder will have a file name `router.py`, `schema.py` and `model.py` that deal with, you guessed it the routers, schemas and models for the users or items depending in which folder they are located.

With me so far? Good, that was the complicated part.  Now comes the easy part.  Let's fill these files with some life shall we?

