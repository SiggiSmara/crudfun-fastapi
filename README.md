# crudfun-fastapi
How-To: Build generic crud functions with fastAPI

## Base

This repository is reflecting the setup of the [bigger applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) example found on the fastAPI documentation page.

At the time of this tutorial the layout was build in a way that all routers were in one folder with individual files named after the object it was building routes for.

Expanding that to a setup with an SQL database and pydantic models would mean all schemas (pydantic models) would be in its own folder, all database models would be in another folder and all crud operations in yet another one.  This is reflected in this repository.





