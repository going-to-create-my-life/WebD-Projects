let img = document.getElementsByTagName("img")[0];
let enemy = document.getElementById("enemy");
let left = 0;

document.getElementById("main").addEventListener("click", () => {
  img.style.animation = "jump 1s ease-in-out 0s 1";
});

document.getElementById("main").addEventListener("animationend", () => {
  img.style.animation = "";
});

let i = 0;
setInterval(() => {
  let enemy_x = parseInt(
    window.getComputedStyle(enemy, null).getPropertyValue("right")
  );
  let player_x = parseInt(
    window.getComputedStyle(img, null).getPropertyValue("right")
  );
  let enemy_y = parseInt(
    window.getComputedStyle(enemy, null).getPropertyValue("top")
  );
  let player_y = parseInt(
    window.getComputedStyle(img, null).getPropertyValue("top")
  );
  let y = enemy_y - player_y;
  let x = enemy_x - player_x;
  console.log(x);
  if (x >= 1050 && x <= 1500 && y <= 182) {
    enemy.style.animation = "none";
    document.getElementById("score").style.visibility = "hidden";
    let j = i;
    document.getElementById("game_over").style.display = "block";
    document.getElementById("game_over").innerText = "GAME OVER  YOUR SCORE:" + j;
  } else {
    i++;
    document.getElementById("score").innerText = "SCORE:" + i;
  }
}, 100);

document.onkeydown = function (element) {
  if (element.keyCode == 39) {
    left += 20;
    img.style.left = left + "px";
  } else if (element.keyCode == 37) {
    left -= 20;
    img.style.left = left + "px";
  } else if (element.keyCode == 38) {
    img.style.animation = "jump 1s ease-in-out 0s 1";
  }
};
