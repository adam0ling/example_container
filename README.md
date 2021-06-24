# How to use

Firstly check if your docker daemon is running and if not run it:

$ sudo dockerd

Then to build the docker image use command below inside example_container directory (..path to/example_image):

$ docker build -t you_image_name .

Then in the same directory you've built docker image use this to run the API (..path to/example_image):

$ docker run -p 80:80 you_image_name

Your API is running! Try using the example_call.py to get a response.

# Some important things

Dockerfile builds your container (a slimed down version of OS), you'll see that you need to install your packages for the image thorugh there (pip install package_1 ... package_n).

All your code is residing in /api directory. Add aditional py files there for additional functions. I suggest using a seperate file for seperate API route. Makes it easier to manage.

api.py controls how your API behaves. Add additional routes for additional things to do. 

We use 'POST' method for API routes as we post json data to it in a form of a dict. There are others methods as well, but POST should suffice for now.

You can use something like postman to play around with your API
