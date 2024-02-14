import azure.functions as func


def main(req:func.HttpRequest) -> func.HttpResponse:
    if req.method == "GET":
        return func.HttpResponse(
            body='''<!DOCTYPE html>
                 <html lang="en">
                 <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="с.css">
  <title>Document</title>
</head>
<body>
<header>
<img src="logo.svg" class="logo">
<div class="menu">
<a href="#">Components</a>
<a href="#">Blocks</a>
<a href="#">Designer</a>
<a href="#">Templates</a>
</div>
<div class="icons">
  <i class="fa-brands fa-github"></i>
  <i class="fa-brands fa-discord"></i>
  <i class="fa-regular fa-moon"></i>
</div>
</header>
<main>
<div class="items">
<div class="item1">
<img src="icon1.svg">
<h3>Templates</h3>
<p>Spectacular designer</p>
</div>
<div class="item2">
  <img src="icon2.svg">
  <h3>Open Source</h3>
  <p>90+ UI Components</p>
</div>
<div class="item3">
  <img src="icon3.svg">
  <h3>Prime Blocks</h3>
  <p>400+ UI Blocks</p>
</div>
<div class="item4">
  <img src="icon4.svg">
  <h3>NEXT-GEN</h3>
  <p>ANGULAR UI</p>
</div>
<div class="item5">
  <img src="icon5.svg">
  <h3>Theme Designer</h3>
  <p>Create Your Own</p>
</div>
<div class="item6">
  <img src="icon6.svg">
  <h3>CSS Utilities</h3>
  <p>PrimeFlex CSS</p>
</div>
<div class="item7">
  <img src="icon7.svg">
  <h3>Icon Libraey</h3>
  <p>200+ Icons</p>
</div>
</div>
<div class="line"></div>
</main>
<div class="buttons">
<button class="b1">Get Started</button>
<button class="b2">npm i primeng</button>
</div>
</body>
</html>''',
        status_code=200,
        mimetype='text/html'
        )
