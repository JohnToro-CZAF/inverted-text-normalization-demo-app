# inverted-text-normalization-demo-app
This is the demo of the application: converting spoken form to written form of the text.
![](/src/demo.png)

The project is built with react.js framework as the frontend and client server nginx. The typed text from the client will send a request to the python API - a wrapper around NeMo Language processing toolkit from Nvidia. Both client and api works with the help of Docker Compose.

Using the following command to start the docker containers.
```
docker compose up
```