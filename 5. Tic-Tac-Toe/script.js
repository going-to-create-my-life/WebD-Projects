let boxes = Array.from(document.getElementsByClassName("box"));
let turn = "X";
// CHANGE TURN
change_turn = () => {
  if (turn == "X") {
    turn = "O";
  } else {
    turn = "X";
  }
};

// GAME LOGIC
boxes.forEach((element) => {
  element.addEventListener("click", () => {
    let index = boxes.indexOf(element) + 1;
    document.getElementById("box" + index).innerText = turn;
    change_turn();
    document
      .getElementById("side_items")
      .getElementsByTagName("h3")[0].innerText = "TURN FOR " + `"${turn}"`;
    check_win();
  });
});

// RESET ALL
document.getElementById("btn_reset").addEventListener("click", () => {
  boxes.forEach((element) => {
    element.innerText = "";
  });
  document
    .getElementById("side_items")
    .getElementsByTagName("h3")[0].innerText = ` TURN FOR "X" `;
  document.getElementById("side_items").getElementsByTagName("h3")[0].style = "";
  turn = "X";
});

// WINING LOGIC
check_win = () => {
  if ( 
    document.getElementById("box1").innerText ===
      document.getElementById("box2").innerText &&
    document.getElementById("box1").innerText ===
      document.getElementById("box3").innerText &&
    document.getElementById("box1").innerText !== "" ||
    document.getElementById("box4").innerText ===
      document.getElementById("box5").innerText &&
    document.getElementById("box4").innerText ===
      document.getElementById("box6").innerText &&
    document.getElementById("box4").innerText !== "" ||
    document.getElementById("box7").innerText ===
      document.getElementById("box8").innerText &&
    document.getElementById("box7").innerText ===
      document.getElementById("box9").innerText &&
    document.getElementById("box7").innerText !== "" ||
    document.getElementById("box1").innerText ===
      document.getElementById("box4").innerText &&
    document.getElementById("box1").innerText ===
      document.getElementById("box7").innerText &&
    document.getElementById("box1").innerText !== "" ||
    document.getElementById("box2").innerText ===
      document.getElementById("box5").innerText &&
    document.getElementById("box2").innerText ===
      document.getElementById("box8").innerText &&
    document.getElementById("box2").innerText !== "" ||
    document.getElementById("box3").innerText ===
      document.getElementById("box6").innerText &&
    document.getElementById("box3").innerText ===
      document.getElementById("box9").innerText &&
    document.getElementById("box3").innerText !== "" ||
    document.getElementById("box1").innerText ===
      document.getElementById("box5").innerText &&
    document.getElementById("box1").innerText ===
      document.getElementById("box9").innerText &&
    document.getElementById("box1").innerText !== "" ||
    document.getElementById("box3").innerText ===
      document.getElementById("box5").innerText &&
    document.getElementById("box3").innerText ===
      document.getElementById("box7").innerText &&
    document.getElementById("box3").innerText !== ""
  ) {
    change_turn();
    document
      .getElementById("side_items")
      .getElementsByTagName("h3")[0].innerText =
      turn + " WON THE GAME";

    document.getElementById("side_items").getElementsByTagName("h3")[0].style =
      " font-size : 60px; color: red;";
  }
  else if( document.getElementById("box1").innerText !== "" && document.getElementById("box2").innerText !== "" && document.getElementById("box3").innerText !== "" && document.getElementById("box4").innerText !== "" && document.getElementById("box5").innerText !== "" && document.getElementById("box6").innerText !== "" && document.getElementById("box7").innerText !== "" && document.getElementById("box8").innerText !== "" && document.getElementById("box9").innerText !== ""){
    document
    .getElementById("side_items")
    .getElementsByTagName("h3")[0].innerText = `NO ONE WON, CLICK ON RESET TO START AGAIN`;
  document.getElementById("side_items").getElementsByTagName("h3")[0].style = " font-size : 40px; color: red;";
  }
};
