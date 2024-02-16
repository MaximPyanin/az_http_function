import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == 'GET':
        return func.HttpResponse(
            body='''
            <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mikro Unsplash</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" />
    <style>
    body {
  font-family: BlinkMacSystemFont, San Francisco, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Segoe UI, Arial, sans-serif;
  font-size: 1em;
  font-weight: 400;
  line-height: 1.6;
  color: rgb(118, 118, 118);
}

footer {
  padding-bottom: 25px;
  margin-right: auto;
  margin-left: auto;
  width: 80%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  border-top: 3px solid rgb(232, 222, 222);
}
footer .left-section {
  padding-top: 10px;
  display: flex;
  flex-direction: row;
  -moz-column-gap: 12px;
       column-gap: 12px;
}
footer .left-section a {
  color: gray;
  font-size: small;
  text-decoration: none;
}
footer .right-section {
  padding-top: 10px;
  display: flex;
  flex-direction: row;
  -moz-column-gap: 15px;
       column-gap: 15px;
}
footer .right-section a {
  color: gray;
  font-size: medium;
}

.toczki {
  display: flex;
  flex-direction: row;
  justify-content: center;
  padding-bottom: 40px;
}
.toczki button {
  border: 0;
  width: 34px;
  height: 34px;
  font-size: larger;
}

#search-section {
  width: 100%;
  background-color: rgb(46, 46, 104);
  height: 370px;
  border: 0;
}
#search-section .content {
  display: flex;
  flex-direction: column;
  align-items: center;
  row-gap: 9px;
  padding-top: 124px;
  width: 51%;
  margin-left: auto;
  margin-right: auto;
}
#search-section .content div {
  align-self: flex-start;
}
#search-section .content span {
  color: white;
  font-weight: bold;
  font-size: medium;
}
#search-section .content .header {
  align-self: flex-start;
  color: white;
  font-weight: bold;
  font-size: 30px;
  padding-right: 430px;
}
#search-section .content .trending {
  color: white;
}
#search-section .content .search {
  position: relative;
  background-color: white;
  border: 0;
  border-radius: 10px;
  width: 100%;
  height: 30px;
  font-size: medium;
}
#search-section .content .search .search {
  display: flex;
  flex-direction: row;
}
#search-section .content .search .search i {
  color: gray;
  padding-left: 3px;
  padding-top: 7px;
}
#search-section .content .search #search {
  position: absolute;
  top: 5px;
  left: 35px;
  border: 0;
  border-radius: 10px;
  color: gray;
  font-size: medium;
}

.main {
  width: 80%;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  -moz-column-gap: 19px;
       column-gap: 19px;
  padding-top: 37px;
  padding-bottom: 17px;
  margin-left: auto;
  margin-right: auto;
}
.main .first-column {
  display: grid;
  row-gap: 15px;
}
.main .second-column {
  display: grid;
  row-gap: 15px;
}
.main .third-column {
  display: grid;
  row-gap: 15px;
}
.main .pic {
  background-color: rgb(237, 215, 186);
}/*# sourceMappingURL=unsplash.css.map */
    </style>
  </head>
  <body>
    <header>
      <div class="logo">Logo</div>
      <input type="text" name="search" id="search" placeholder="Search free high-resolution photos" />
      <button>Explore</button>
      <button>Advertise</button>
      <button>Blog</button>
      <div class="separator"></div>
      <button>Log&nbsp;In</button>
      <button id="submit">Submit&nbsp;a&nbsp;photo</button>
      <button>
        <i class="fas fa-bars"></i>
      </button>
    </header>
    <nav>
      <button class="active">Editorial</button>
      <div class="separator"></div>
      <button>Holidays</button>
      <button>Blockchain</button>
      <button>Wallpapers</button>
      <button>3D Renders</button>
      <button>Textures & Patterns</button>
      <button>Architecture</button>
      <button>Experimental</button>
      <button>Nature</button>
      <button>Business & Work</button>
      <button>Fashion</button>
      <button>Film</button>
      <button>Food & Drink</button>
      <button>Health & Wellness</button>
    </nav>
    <div id="search-section">
      <div class="content">
        <div class="header">Unsplash</div>
        <div>
          <span>The internet’s source of freely-usable images.<br></span>
          <span>Powered by creators everywhere.</span>
        </div>
        <div class="search">
          <button class="search">
            <i class="fas fa-search"></i>
          </button>
          <input type="text" name="search" id="search" placeholder="Szukaj" />
        </div>
        <div class="trending">
          <span>Trending:</span>
          flower, wallpapers, backgrounds, happy, love
        </div>
      </div>
    </div>
    <div class="main">
      <div class="first-column">
        <div class="pic" style="height: 450px">
          <div class="pic-info">
            <div class="top">
              <button>
                <i class="fas fa-plus"></i>
              </button>
              <button>
                <i class="fas fa-heart"></i>
              </button>
            </div>
            <div class="bottom">
              <div class="person">
                <div class="logo"></div>
                <div class="name">Jan Kowalski</div>
              </div>
              <button>
                <i class="fas fa-arrow-down"></i>
              </button>
            </div>
          </div>
        </div>
        <div class="pic" style="height: 400px">
          <div class="pic-info">
            <div class="top">
              <button>
                <i class="fas fa-plus"></i>
              </button>
              <button>
                <i class="fas fa-heart"></i>
              </button>
            </div>
            <div class="bottom">
              <div class="person">
                <div class="logo"></div>
                <div class="name">Jan Kowalski</div>
              </div>
              <button>
                <i class="fas fa-arrow-down"></i>
              </button>
            </div>
          </div>
        </div>
        <div class="pic" style="height: 400px">
          <div class="pic-info">
            <div class="top">
              <button>
                <i class="fas fa-plus"></i>
              </button>
              <button>
                <i class="fas fa-heart"></i>
              </button>
            </div>
            <div class="bottom">
              <div class="person">
                <div class="logo"></div>
                <div class="name">Jan Kowalski</div>
              </div>
              <button>
                <i class="fas fa-arrow-down"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="second-column">
        <div class="pic" style="height: 400px">
          <div class="pic-info">
            <div class="top">
              <button>
                <i class="fas fa-plus"></i>
              </button>
              <button>
                <i class="fas fa-heart"></i>
              </button>
            </div>
            <div class="bottom">
              <div class="person">
                <div class="logo"></div>
                <div class="name">Jan Kowalski</div>
              </div>
              <button>
                <i class="fas fa-arrow-down"></i>
              </button>
            </div>
          </div>
        </div>
        <div class="pic" style="height: 350px">
          <div class="pic-info">
            <div class="top">
              <button>
                <i class="fas fa-plus"></i>
              </button>
              <button>
                <i class="fas fa-heart"></i>
              </button>
            </div>
            <div class="bottom">
              <div class="person">
                <div class="logo"></div>
                <div class="name">Jan Kowalski</div>
              </div>
              <button>
                <i class="fas fa-arrow-down"></i>
              </button>
            </div>
          </div>
        </div>
        <div class="pic" style="height: 450px">
          <div class="pic-info">
            <div class="top">
              <button>
                <i class="fas fa-plus"></i>
              </button>
              <button>
                <i class="fas fa-heart"></i>
              </button>
            </div>
            <div class="bottom">
              <div class="person">
                <div class="logo"></div>
                <div class="name">Jan Kowalski</div>
              </div>
              <button>
                <i class="fas fa-arrow-down"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="third-column">
        <div class="pic" style="height: 400px">
          <div class="pic-info">
            <div class="top">
              <button>
                <i class="fas fa-plus"></i>
              </button>
              <button>
                <i class="fas fa-heart"></i>
              </button>
            </div>
            <div class="bottom">
              <div class="person">
                <div class="logo"></div>
                <div class="name">Jan Kowalski</div>
              </div>
              <button>
                <i class="fas fa-arrow-down"></i>
              </button>
            </div>
          </div>
        </div>
        <div class="pic" style="height: 450px">
          <div class="pic-info">
            <div class="top">
              <button>
                <i class="fas fa-plus"></i>
              </button>
              <button>
                <i class="fas fa-heart"></i>
              </button>
            </div>
            <div class="bottom">
              <div class="person">
                <div class="logo"></div>
                <div class="name">Jan Kowalski</div>
              </div>
              <button>
                <i class="fas fa-arrow-down"></i>
              </button>
            </div>
          </div>
        </div>
        <div class="pic" style="height: 450px">
          <div class="pic-info">
            <div class="top">
              <button>
                <i class="fas fa-plus"></i>
              </button>
              <button>
                <i class="fas fa-heart"></i>
              </button>
            </div>
            <div class="bottom">
              <div class="person">
                <div class="logo"></div>
                <div class="name">Jan Kowalski</div>
              </div>
              <button>
                <i class="fas fa-arrow-down"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="toczki">
      <button>...</button>
    </div>
    <footer>
      <div class="left-section">
        <a href="#">Privacy Policy</a>
        <a href="#">Terms</a>
        <a href="#">Security</a>
      </div>
      <div class="right-section">
        <a href="#"><i class="fab fa-twitter"></i></a>
        <a href="#"><i class="fab fa-facebook"></i></a>
        <a href="#"><i class="fab fa-instagram"></i></a>
      </div>
    </footer>
  </body>
</html>

            ''',
            status_code=200,
            mimetype='text/html'
        )