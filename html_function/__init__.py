import azure.functions as func


def main(req:func.HttpRequest) -> func.HttpResponse:
    if req.method == "GET":
        return func.HttpResponse(
            body='''<!DOCTYPE html>
                 <html lang="en">
                 <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style> 
  body {
  background-color: #edf5ff;
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, Segoe UI Symbol;
  font-size: 14px;
}

header {
  width: 1280px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.logo {
  width: 140px;
  height: 35px;
}

.menu {
  font-weight: bold;
  font-size: medium;
  padding-left: 315px;
  display: flex;
  flex-direction: row;
  -moz-column-gap: 25px;
       column-gap: 25px;
}
.menu a {
  text-decoration: none;
  color: #191919;
}
.menu a:hover {
  color: #1876d1;
}

.icons {
  display: flex;
  flex-direction: row;
  -moz-column-gap: 12px;
       column-gap: 12px;
}
.icons i:hover {
  background-color: black;
}
.icons i {
  background-color: white;
  border: 1px solid grey;
  border-radius: 8px;
  height: 25px;
  width: 20px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.buttons {
  padding-top: 14px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  -moz-column-gap: 10px;
       column-gap: 10px;
}

.b1 {
  background-color: blue;
  color: white;
  border-radius: 10px;
  height: 47px;
  width: 120px;
  border: 0;
  font-weight: bold;
}

.b2 {
  border-radius: 10px;
  height: 47px;
  width: 120px;
  background-color: #edf5ff;
  color: #191919;
  font-weight: bold;
  border: 1px solid grey;
}

.item1 {
  height: 170px;
  width: 170px;
  background-color: white;
  border: 1px solid black;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.item1 p {
  margin: 0;
}

.item1:hover {
  background-color: #e3f0ff;
}

.item2 {
  height: 170px;
  width: 170px;
  background-color: white;
  border: 1px solid black;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.item2 p {
  margin: 0;
}

.item2:hover {
  background-color: #e3f0ff;
}

.item3 {
  height: 170px;
  width: 170px;
  background-color: white;
  border: 1px solid black;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.item3 p {
  margin: 0;
}

.item3:hover {
  background-color: #e3f0ff;
}

.item4 {
  height: 170px;
  width: 170px;
  background-color: white;
  border: 1px solid black;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.item4 p {
  margin: 0;
}

.item4:hover {
  background-color: #e3f0ff;
}

.item5 {
  height: 170px;
  width: 170px;
  background-color: white;
  border: 1px solid black;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.item5 p {
  margin: 0;
}

.item5:hover {
  background-color: #e3f0ff;
}

.item6 {
  height: 170px;
  width: 170px;
  background-color: white;
  border: 1px solid black;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.item6 p {
  margin: 0;
}

.item6:hover {
  background-color: #e3f0ff;
}

.item7 {
  height: 170px;
  width: 170px;
  background-color: white;
  border: 1px solid black;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.item7 p {
  margin: 0;
}

.item7:hover {
  background-color: #e3f0ff;
}

.items {
  padding-left: 450px;
  padding-top: 50px;
  padding-right: 400px;
}

main {
  position: relative;
}

.line {
  position: absolute;
  z-index: -1;
  background-color: #73879e;
  width: 100%;
  top: 340px;
  height: 100px;
}

.items {
  display: grid;
  -moz-column-gap: 20px;
       column-gap: 20px;
  row-gap: 20px;
  grid-template-areas: ". b ." "a b c" "a d c" "f d e" "f g e" ". g .";
}

.item1 {
  grid-area: a;
}

.item2 {
  grid-area: b;
}

.item3 {
  grid-area: c;
}

.item4 {
  grid-area: d;
}

.item5 {
  grid-area: e;
}

.item6 {
  grid-area: f;
}

.item7 {
  grid-area: g;
}
 </style>
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
