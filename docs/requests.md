## How is the request object defined naturally without any additional middleware?
The natural request object coming from the browser contains the following parameters and we need 
to add additional middleware, JWT and CSRF tokens to facilitate production quality features and 
we need to configure them through Starlette as Starlette encapsulates all functionalities of 
FastAPI
Starlette middleware docs can be found [here](https://www.starlette.io/authentication/)
Request objects:
 -  Type
 -  Asgi
 -  http_version
 -  server
 -  client
 -  scheme
 -  method
 -  root_path
 -  path
 -  path
 -  raw_path
 -  query_string
 -  headers
 - fastapi_astack
 - app
 - router
 - endpoint
 - path_params
 
Starlette middleware docs can be found [here](https://www.starlette.io/authentication/)