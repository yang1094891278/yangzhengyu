#flask  web开发框架
from flask import Flask,jsonify

app =Flask(__name__)

#创建一个路由
@app.route("/")  #装饰器
def index():
    indexhtml =  """
    <!DOCTYPE html>
<html>
<head>
  <title>Bootstrap 实例</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://cdn.staticfile.org/popper.js/1.15.0/umd/popper.min.js"></script>
  <script src="https://cdn.staticfile.org/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center">
  <h1>我的第一个 Bootstrap 页面</h1>
  <p>重置浏览器大小查看效果!</p> 
</div>
 
<div class="container">
  <div class="row">
    <div class="col-sm-4">
      <h3>第一列</h3>
      <p>菜鸟教程</p>
      <p>学的不仅是技术，更是梦想！！！</p>
    </div>
    <div class="col-sm-4">
      <h3>第二列</h3>
      <p>菜鸟教程..</p>
      <p>学的不仅是技术，更是梦想！！！</p>
    </div>
    <div class="col-sm-4">
      <h3>第三列</h3> 
      <p>菜鸟教程..</p>
      <p>学的不仅是技术，更是梦想！！！</p>
    </div>
  </div>
</div>

</body>
</html>
"""
    return indexhtml

@app.route("/userinfo")
def getuserinfo():
    hdict = {
        "name" : "yanzghengyu",
        "age" : 20,
        "high" : 200,
        "work" : "xuesheng",
        "phone" : "123456789",
        "weixin" : "yang"
    }
    return jsonify(hdict) 

if __name__ == "__main__":
    app.run(debug=True)