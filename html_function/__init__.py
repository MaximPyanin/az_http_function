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
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  padding: 0;
}

.content .column > .pic {
  background-color: #a2a285;
  border-radius: 1.5625rem;
}
.content .column:first-of-type > .pic:first-of-type {
  height: 14rem;
}
.content .column:first-of-type > .pic:nth-of-type(2) {
  height: 20rem;
}
.content .column:first-of-type > .pic:nth-of-type(3) {
  height: 23rem;
}
.content .column:first-of-type > .pic:nth-of-type(4) {
  height: 17rem;
}
.content .column:first-of-type > .pic:nth-of-type(5) {
  height: 19rem;
}
.content .column:first-of-type > .pic:nth-of-type(6) {
  height: 16rem;
}
.content .column:nth-of-type(2) > .pic:first-of-type {
  height: 18rem;
}
.content .column:nth-of-type(2) > .pic:nth-of-type(2) {
  height: 20rem;
}
.content .column:nth-of-type(2) > .pic:nth-of-type(3) {
  height: 18rem;
}
.content .column:nth-of-type(2) > .pic:nth-of-type(4) {
  height: 19rem;
}
.content .column:nth-of-type(2) > .pic:nth-of-type(5) {
  height: 16rem;
}
.content .column:nth-of-type(2) > .pic:nth-of-type(6) {
  height: 20rem;
}
.content .column:nth-of-type(3) > .pic:first-of-type {
  height: 17rem;
}
.content .column:nth-of-type(3) > .pic:nth-of-type(2) {
  height: 23rem;
}
.content .column:nth-of-type(3) > .pic:nth-of-type(3) {
  height: 16rem;
}
.content .column:nth-of-type(3) > .pic:nth-of-type(4) {
  height: 18rem;
}
.content .column:nth-of-type(3) > .pic:nth-of-type(5) {
  height: 14rem;
}
.content .column:nth-of-type(3) > .pic:nth-of-type(6) {
  height: 20rem;
}
.content .column:nth-of-type(4) > .pic:first-of-type {
  height: 19rem;
}
.content .column:nth-of-type(4) > .pic:nth-of-type(2) {
  height: 16rem;
}
.content .column:nth-of-type(4) > .pic:nth-of-type(3) {
  height: 17rem;
}
.content .column:nth-of-type(4) > .pic:nth-of-type(4) {
  height: 19rem;
}
.content .column:nth-of-type(4) > .pic:nth-of-type(5) {
  height: 16rem;
}
.content .column:nth-of-type(4) > .pic:nth-of-type(6) {
  height: 17rem;
}
.content .column:nth-of-type(5) > .pic:first-of-type {
  height: 17rem;
}
.content .column:nth-of-type(5) > .pic:nth-of-type(2) {
  height: 19rem;
}
.content .column:nth-of-type(5) > .pic:nth-of-type(3) {
  height: 18rem;
}
.content .column:nth-of-type(5) > .pic:nth-of-type(4) {
  height: 14rem;
}
.content .column:nth-of-type(5) > .pic:nth-of-type(5) {
  height: 15rem;
}
.content .column:nth-of-type(5) > .pic:nth-of-type(6) {
  height: 17rem;
}
.content .column:nth-of-type(6) > .pic:first-of-type {
  height: 15rem;
}
.content .column:nth-of-type(6) > .pic:nth-of-type(2) {
  height: 17rem;
}
.content .column:nth-of-type(6) > .pic:nth-of-type(3) {
  height: 19rem;
}
.content .column:nth-of-type(6) > .pic:nth-of-type(4) {
  height: 14rem;
}
.content .column:nth-of-type(6) > .pic:nth-of-type(5) {
  height: 20rem;
}
.content .column:nth-of-type(6) > .pic:nth-of-type(6) {
  height: 18rem;
}

header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  border-bottom: 2px solid grey;
  display: flex;
  height: 7%;
  flex-direction: row;
  align-items: center;
  -moz-column-gap: 10px;
       column-gap: 10px;
}

form {
  padding-left: 20px;
  width: 1200px;
  border-radius: 10px;
  background-color: grey;
}
form input {
  background-color: grey;
  color: black;
  border: 0;
  width: 100px;
}

header .fab {
  margin-left: 12px;
  background-color: white;
  color: red;
  border-radius: 12px;
}

header button {
  color: white;
  background-color: black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
}

header .right {
  display: flex;
  flex-direction: row;
  -moz-column-gap: 14px;
       column-gap: 14px;
}
header .right i {
  color: rgba(79, 77, 77, 0.699);
}

.header2 {
  display: flex;
  flex-direction: row;
  align-items: center;
  border-radius: 10px;
  -moz-column-gap: 15px;
       column-gap: 15px;
  border: 2px solid gray;
  margin-top: 80px;
  margin-left: auto;
  margin-right: auto;
  width: 90%;
}
.header2 button {
  border-radius: 10px;
  height: 45px;
  width: 140px;
  color: black;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  font-size: smaller;
  border: 0;
}
.header2 p {
  padding-left: 9px;
}
.header2 p a {
  text-decoration: none;
  color: black;
  font-weight: bold;
}

.content {
  padding-top: 55px;
  padding-left: 95px;
  padding-right: 95px;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  -moz-column-gap: 18px;
       column-gap: 18px;
}
.content .column {
  display: grid;
  row-gap: 9px;
}/*# sourceMappingURL=style (2).css.map */
 </style>
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
  <title>Document</title>
</head>
<header>
    <i class="fab fa-pinterest"></i>
    <button>Glowna Strona</button>
    
    <form action="/search" method="get">
      <input type="search" name="q" placeholder="szukaj">
    </form>
 
    <div class="right">
      <i class="fa-solid fa-bell"></i>
      <i class="fa-solid fa-comment"></i>
    </div>
  </header>
<main>
<div class="header2">
<p>Używamy plików cookie, aby wyświetlać spersonalizowane reklamy i treści oraz analizować ruch w naszej witrynie. Więcej<br> informacji znajdziesz w naszym dokumencie <a href="#">Zasady dotyczące plików cookie.</a>
</p>
  <button>Zaakceptuj wszystkie</button>
  <button>Odrzuć wszystkie</button>
  <button>Chcę wybrać samodzielnie</button>  
</div>
<div class="content">
  <div class="column">
   <div class="pic">
   </div>
   <div class="pic">
   </div>
   <div class="pic">
  </div>
  <div class="pic">
  </div>
  <div class="pic">
  </div>
  <div class="pic">
  </div>
  </div>
  <div class="column">
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
  </div>
  <div class="column">
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
  </div>
  <div class="column">
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
  </div>
  <div class="column">
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
  </div>
  <div class="column">
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
    <div class="pic">
    </div>
  </div>
</div>
</main>
</body>
</html>''',
        status_code=200,
        mimetype='text/html'
        )
