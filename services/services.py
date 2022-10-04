from flask import Flask, request, jsonify

app = Flask("")

#possibile applicazione per prescriptor: Energy Smart Grid

@app.route("/saro", methods=["GET"])
def test_saro():
    # args = request.json.get('args')
    # print("ARGS",args)
    # json = request.json.get("value")
    # print("JSON",json)
    res = ["ciao", "ciao2", "bello", "casa"]
    return res#jsonify(dict(msg="Hello extensions!"))

@app.route("/", methods=["POST"])
def test():
    args = request.json.get('args')
    print("ARGS",args)
    json = request.json.get("value")
    print("JSON",json)
    return jsonify(dict(msg="Hello extensions!"))


@app.route("/files", methods=["POST"])
def test2():
    file = request.files['file']
    fname = file.filename
    print("You have uploaded a file called:",fname)
    return jsonify(dict(msg=f"Hello extensions, you have uploaded the file: {fname}!"))


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
