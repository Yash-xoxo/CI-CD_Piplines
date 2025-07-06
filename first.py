def lw_sum(x, y):
    return x + y

def lw_mul(x, y):
    return x * y

#@app.route("/info")
def get_info():
    return "Hello from the APP"

def lwinfo():
    return {"author": "Yash", "language": "Python"}
