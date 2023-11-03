let music = new Audio("b.mp3");
let index= 0;
let progress = 0;
let playmain = document.querySelector("#btn_playmain");
var forward = document.querySelector("#btn_for");
let backward = document.querySelector("#btn_back");
let progressbar = document.getElementById("progressbar");
let play_songs = Array.from(
  document.getElementById("music").getElementsByTagName("button")
);
let music_album = Array.from(document.getElementsByClassName("music_blocks"));
let songs = [
  {
    name: "Give me some sunshine",
    path: "songs/Give Me Some Sunshine(MP3_160K).mp3",
    cover: "cover/1.jpg",
  },
  {
    name: "Hey Bhole Shankar Padhaaro",
    path: "songs/Hey Bhole Shankar Padhaaro [Full Song] I Shiv Mahima(M4A_128K).m4a",
    cover: "cover/2.jpg",
  },
  {
    name: "Hey shambhu baba mere bholenaath _ gulshan kumaar",
    path: "songs/Hey shambhu baba mere bholenaath _ gulshan kumaar _ shiv bhakti song _ remix _ T-Series _(MP3_160K).mp3",
    cover: "cover/3.jpg",
  },
  {
    name: "Karna vs Arjun_ The Battle of Destiny in Rashmirathi Pratham Sarg",
    path: "songs/Karna vs Arjun_ The Battle of Destiny in Rashmirathi Pratham Sarg(MP3_160K).mp3",
    cover: "cover/4.jpg",
  },
  {
    name: "Milta Hai Sachcha Sukh By Anuradha Paudwal",
    path: "songs/Milta Hai Sachcha Sukh By Anuradha Paudwal [Full Song] - Shiv Mahima Movie Song(M4A_128K).m4a",
    cover: "cover/5.jpg",
  },
  {
    name: "Subah Subah Le Shiv Ka Naam By Gulshan Kumar",
    path: "songs/Subah Subah Le Shiv Ka Naam By Gulshan Kumar_ Hariharan [Full Song] - Shiv Mahima(M4A_128K).m4a",
    cover: "cover/6.jpg",
  },
  {
    name: "I Aisi Subah Na Aaye I___ANURADHA PAUDWAL",
    path: "songs/सोमवार Special शिव भजन ऐसी सुबह ना आए I Aisi Subah Na Aaye I ANURADHA PAUDWAL I Morning Shiv Bhajan(MP3_160K).mp3",
    cover: "cover/7.jpg",
  },
  {
    name: "Meri Chokhat Pe Chal Ke Aaj Charo Dham Aaye Hai",
    path: "songs/Meri Chokhat Pe Chal Ke Aaj Charo Dham Aaye Hai Bajao Dhop Suagat _ Jubin Nautiyal _ New Song 2022(MP3_160K).mp3",
    cover: "cover/8.jpg",
  },
];

music_album.forEach((element, index) => {
  element.getElementsByTagName("h6")[0].innerText = songs[index].name;
  element.getElementsByClassName("img_music")[0].src = songs[index].cover;
});

playmain.addEventListener("click", () => {
  if (music.paused) {
    music.play();
  } else {
    music.pause();
  }
});

music.addEventListener("timeupdate", () => {
  progress = parseInt((music.currentTime / music.duration) * 100);
  progressbar.value = progress;
});

progressbar.addEventListener("change", () => {
  music.currentTime = (progressbar.value * music.duration) / 100;
});

play_songs.forEach((element) => {
  
  element.addEventListener("click", () => {
    index = play_songs.indexOf(element);
    music.src = songs[index].path;
    if (music.paused) {
      music.currentTime = 0;
      music.play();
    }});
    
    
});

forward.addEventListener('click', ()=>{
  if(index==7){
    index=0;
  }
  else{
    index +=1 ;
  }
  
  music.src = songs[index].path;
  if (music.paused) {
    music.currentTime = 0;
    music.play();
  }});


  backward.addEventListener('click', ()=>{
    if(index==0){
      index=7;
    }
    else{
      index -=1 ;
    }
    
    music.src = songs[index].path;
    if (music.paused) {
      music.currentTime = 0;
      music.play();
    }});
  