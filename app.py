from flask import Flask, request

app = Flask(__name__)


# xử lý các request gửi tới
@app.route("/")
def root():
    return "Server is running"


@app.route("/test")
def test():
    user = {
        "name": "Hieu"
    }
    return user


@app.route("/update-cache")
def update_cache():
    return "update cache"


# Xử lý method GET và POST
@app.route("/asn", methods=["GET", "POST"])
def asn():
    method = request.method
    if method == "GET":
        return "Handling get method"
    if method == "POST":
        return "Handling post method"
    return "Default method"

###############################
# Nhận Input để xử lý dữ liệu #
###############################

# Nhận dữ liệu từ query parameter  
# Query param bắt đầu từ sau dấu ? được viết thành key=value
# nhiều biến thì ta sử dụng & để nối
# .../test-query?question=AAAAAAAA&name=Hieu
@app.route("/test-query", methods=["GET"])
def test_query():
    question = request.args.get("question", "default question")
    name = request.args.get("name", "default name")
    return f"""
    This is test method:
    Question: {question}
    Name: {name}
    """


if __name__ == "__main__":
    # debug=True => tự động reload lại code mà không cần chạy lại scripts
    app.run(host="0.0.0.0", port=5000, debug=True)