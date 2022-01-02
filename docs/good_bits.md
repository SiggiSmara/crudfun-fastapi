# The good bits

The basic idea is to write a function that takes as it's parameters the router object, the database table model and the pydantic models.  Inside of that function you define subfunctions that act as the CRUD paths for your router and you decorate them as usuall with the router that is given as a parameter.

With that approach you can then define basically instanciate an instance of this function with all the information it needs to build up a functioning CRUD path for you.

Doesn't matter if you have one or fifteen tables, they all instanciate their own version of the same function with their specific database models and pydantic schemas and voila, if you ever need to go back to the code and say implement a route for not only saving a single incoming object but a list of incoming objects you build that logic once and it will be automatically available for all of your tables the next time you run your fastAPI code.

Now if your are curious about the ins and outs you can read all about them in the next section, or if that is enough for you and you just want to see the code then head over to the [github repository](https://github.com/SiggiSmara/crudfun-fastapi)
