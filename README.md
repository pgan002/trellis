# trellis
Trellis.law coding challenge

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
