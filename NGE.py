import marshal
with open("ng", "rb") as f:
    code = marshal.loads(f.read())
exec(code)
