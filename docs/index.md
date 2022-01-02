# How-To: Build generic crud functions with fastAPI

Here I will show you one way to massively reduce the ammount of boilerplate code in 
fastAPI for standard CRUD operations of database tables in a relational database.

I  was faced with writing an API for an app that had many database tables that were all related to one master table. None of them were connected to each other, but each had different columns, and some had different unique row constraints etc. So not stricly homogenous but also not a verz complicated data model.

I'm the kind of person that never likes to repeat themselves. And on my second copy-paste job I was already tired of that approach but I was under time pressure so pushed ahead and got the job done.

Some months later I needed to perform some work on the code again with implementing additional features for the website the API was serving and I was now facing the same copy-paste hell as before, except this time I had to be extra carefull not to break the small things that changed from one table to the next.

Naturally something like this should be easy to tackle with an abstract object class or two that then could be used as the buiding blocks for a general approach.  But I ran into an unforeseen obstacle in that fastAPI does not allow classess as scaffolds for router-functions out of the box.

After looking around and finding fastapi-utils and their [class based views](https://fastapi-utils.davidmontague.xyz/user-guide/class-based-views/) as well as reading [this](https://github.com/tiangolo/fastapi/issues/2625) discussion on fastAPI's github issue page on a similar topic I realized this is still far from being solved and would not be solved in the timeframe I would need it in. 

So a plan B wasS needed. Luckily in that github discussion above, Tiangolo had made a comment that would be the beginning of a perfect solution for this project in that it produced a workable solution that could be implemented without any changes to fastAPI and eased a lot of the copy-paste pain I was facing.

So I decided to pay this forward and share it with you dear reader.

Before jumping into the good bits I decided to give you some background information that might help you understand the code a bit better...
