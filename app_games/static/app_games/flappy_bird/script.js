// Variables
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var score = 0;
var intervalId;
var pipes = [];
var bird = {
  x: 50,
  y: canvas.height / 2,
  width: 40,
  height: 30,
  speed: 0,
  gravity: 0.3,
  jumpForce: 6,
  draw: function() {
    ctx.fillStyle = "#FF6A6A";
    ctx.fillRect(this.x, this.y, this.width, this.height);
  },
  jump: function() {
    this.speed = -this.jumpForce;
  },
  update: function() {
    this.speed += this.gravity;
    this.y += this.speed;
  }
};

// Functions
function drawBackground() {
  ctx.fillStyle = "#70C5CE";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function drawScore() {
  ctx.fillStyle = "#000";
  ctx.font = "24px Arial";
  ctx.fillText("Score: " + score, 10, 30);
}

function drawPipes() {
  for (var i = 0; i < pipes.length; i++) {
    var pipe = pipes[i];
    ctx.fillStyle = "#2ECC71";
    ctx.fillRect(pipe.x, 0, pipe.width, pipe.heightTop);
    ctx.fillRect(pipe.x, pipe.yBottom, pipe.width, pipe.heightBottom);
    pipe.x -= 2;
    if (pipe.x + pipe.width < 0) {
      pipes.splice(i, 1);
    }
    if (pipe.x + pipe.width == bird.x) {
      score++;
    }
  }
}

function generatePipes() {
  var pipeSpace = 100;
  var minHeightTop = 50;
  var maxHeightTop = canvas.height - pipeSpace - minHeightTop;
  var heightTop = Math.floor(Math.random() * (maxHeightTop - minHeightTop + 1)) + minHeightTop;
  var heightBottom = canvas.height - heightTop - pipeSpace;
  var pipe = {
    x: canvas.width,
    yBottom: canvas.height - heightBottom,
    width: 60,
    heightTop: heightTop,
    heightBottom: heightBottom
  };
  pipes.push