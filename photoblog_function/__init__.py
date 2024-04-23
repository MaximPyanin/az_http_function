<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
  <title>Document</title>
  <style>
  body {
  background-color: #333;
  color: white;
  font-family: "PT Sans", sans-serif;
  font-size: 0.875em;
  letter-spacing: 1px;
  line-height: 1.5em;
  margin: 0;
  padding: 0;
}

header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  height: 8%;
  align-items: center;
  border-bottom: 3px solid black;
}
header .logo {
  padding-left: 12px;
  color: gray;
}
header .logo .s {
  color: rgb(241, 180, 49);
}
header .buttons {
  padding-right: 10px;
}
header .buttons .b1 {
  color: #333333;
  background-color: white;
  border: 0;
  border-radius: 3px;
}
header .buttons .b2 {
  color: white;
  background-color: #ff3600;
  border: 0;
  border-radius: 3px;
}

main {
  position: relative;
  margin-left: auto;
  margin-right: auto;
  padding-top: 50px;
  width: 80%;
}
main .h {
  border-bottom: 3px solid black;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  -moz-column-gap: 10px;
       column-gap: 10px;
}
main .h .o .number {
  padding-left: 37px;
}
main .h .t .number {
  padding-left: 37px;
}
main .h .th .number {
  padding-left: 7px;
}

.main {
  padding-top: 30px;
  position: relative;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}
.main .small {
  display: flex;
  flex-direction: column;
  align-items: center;
  row-gap: 8px;
  border: 0;
  background-color: rgb(71, 68, 68);
  height: 270px;
  width: 280px;
  justify-self: end;
}
.main .small .oval {
  height: 120px;
  margin-top: 5px;
  margin-bottom: 5px;
  width: 120px;
  background-color: rgba(211, 211, 211, 0.541);
  border-radius: 100px;
}
.main .square {
  background-color: rgb(239, 228, 228);
  border: 0;
  height: 460px;
  width: 560px;
  margin-left: 200px;
}
.main p {
  display: flex;
  flex-direction: row;
  padding-left: 643px;
}
.main p .niew {
  font-weight: bold;
}
.main .str .fas:first-child {
  position: absolute;
  left: 140px;
  top: 215px;
}
.main .str .fas:nth-child(2) {
  position: absolute;
  top: 215px;
  left: 776px;
}
.main .str i {
  color: rgba(211, 211, 211, 0.541);
  background-color: rgba(111, 111, 111, 0.3);
  height: 79px;
  width: 45px;
  display: grid;
  align-items: center;
  justify-content: center;
  font-size: 29px;
}

.k {
  position: absolute;
  top: 150px;
  left: 125px;
  color: white;
  background-color: rgba(211, 211, 211, 0.541);
  height: 83px;
  width: 61px;
  border-radius: 10px;
}
.k p {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.aa {
  color: white;
  position: absolute;
  top: 240px;
  left: 125px;
  background-color: rgba(211, 211, 211, 0.541);
  height: 83px;
  width: 61px;
  border-radius: 10px;
}
.aa p {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.aa p .faj {
  font-weight: bold;
}

.small button {
  width: 90%;
  border-radius: 5px;
  border: 0;
  height: 24px;
  color: white;
  background-color: red;
}
.small .bb {
  background-color: white;
  color: black;
}
.small .buttons {
  display: flex;
  flex-direction: column;
  row-gap: 4px;
  align-self: flex-start;
  padding-left: 16px;
}/*# sourceMappingURL=photo.css.map */
  </style>
</head>
<body>
  <header>
<div class="logo">
  <h3>  A'laPhoto<span class="s">Blog.com</span></h3>
</div>
<div class="buttons">
<button class="b1">Login</button>
<button class="b2">Register</button>
</div>
  </header>
  <main>
    <div class="h">
<div class="o">
<p><span class="number">709</span><br>Subscribers</p>
</div>
<div class="t"><p><span class="number">125</span><br></p></div> 
<div class="th">
<p><span class="number">1605</span><br>Posts</p>
</div>
    </div>
    <div class="main">
  <div class="square">
  </div>
  <div class="small">
    <div class="oval"></div>
    <button><i class="fas fa-plus"></i>         Follow</button>
  <div class="buttons">
  <i class="fas fa-check"> Monika</i>
  <i class="fas fa-map-marker-alt"> Gdańsk</i>
</div>
  <button class="bb">About me</button>
  <button class="bb">Send message</button>
</div>
<p><span class="w">Views:</span> <span class="niew">1806</span></p>
<div class="str">
<i class="fas fa-chevron-left"></i>
<i class="fas fa-chevron-right"></i>
</div>
  </div>
  <div class="k">
    <p><span class="sty">Jan</span> <span class="8">8</span><span class="2016">2016</span></p>
  </div>
  <div class="aa">
    <p><span class="faj">Cool</span> <span class=233>232</span></p>
  </div>
  </main>
</body>
</html>
