Place these files into your repo root.

Run:
  uvicorn app.main:app --reload --port 8000

Test:
  http://127.0.0.1:8000/ui/text?message=hello
  POST /ui/message
