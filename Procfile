[[build.env]]
name = "GOOGLE_ENTRYPOINT"
value = "gunicorn --bind :$PORT --timeout 3600 -w 2 -k uvicorn.workers.UvicornWorker main:app"