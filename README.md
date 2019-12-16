# trellis
Trellis.law coding challenge

This is a web application that converts integer numbers expressed in digits to
English words.

It has one endpoint:

    GET /num_to_english?number=

Example:

    GET /num_to_english?number=12345678

Result:

HTTP status: `200`. Response body:

    {
      "status": "ok",
      "num_in_english": "twelve million three hundred forty five thousand six hundred seventy eight"
    }

The endpoint takes query parameters as required for a standard HTTP GET method, 
instead of JSON request body as suggested by the task description.

We do not implement models because Django models are intended to store data, 
this app does not store any data.

To run unit tests:

    pytest app/en.py app/large_int.py 


_What are the things you would do to allow other engineers to use your
endpoint?_

We need to publish the API documentation, but I do not know Django well enough 
to use its doc-generating facilities.


## Task

Create a Python Django application that exposes an endpoint:
`GET /num_to_english`
```
{
  "number": "12345678"
}
```

This endpoint will convert any number given to it into the english words that describe that
number. For example the above request should return:
```
{
  "status": "ok",
  "num_in_english": "twelve million three hundred forty five thousand six hundred seventy eight"
}
```
Status is reserved for messaging back if the process succeeded or failed. Make sure to use that
when handling errors.
Requirements:
1. Python is a must
2. Django is preferable but if not then use any framework you are comfortable with but do
use a framework.
3. Treat this as a production endpoint you would publish.How would you organize it to be
production ready? What are the things you would do to allow other engineers to use your
endpoint?
