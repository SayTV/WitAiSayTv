var vids = [];
var mainVid = null;
var maxDur = 0;

function websocketCallback(r) {
  var cmd = r.data;
  console.log("received command: " + cmd);
  if (cmd == "play") {
    writeInCorner("play");
  if(mainVid)   mainVid.play();
    console.log("video played");
  } else if (cmd == "pause") {
    writeInCorner("pause");
  if(mainVid)   mainVid.pause();
    console.log("video paused");
  } else if (cmd == "fullscreen") {
    writeInCorner("fullscreen");
    try {
    if(mainVid)   mainVid.requestFullScreen();
    } catch (e) {
      failedFullscreenMode();
    }
    console.log("video fullscreen");
  } else if (cmd == "window") {
    try {
    if(mainVid)   mainVid.webkitExitFullscreen();
    } catch (e) {
      if(mainVid) $(mainVid).removeClass("fullscreen");
    }
    console.log("video exit fullscreen");
  } else if (cmd == "exit") {
    writeInCorner("exiting..");
    chrome.runtime.sendMessage({ closeThis: true });
  } else {
    alert("unknown command recieved: " + cmd);
  }
};
var ws = new WebSocket("ws://localhost:8765");
ws.onmessage = websocketCallback;
$(document).ready(function () {
  var time = 1000 * 10;
  // setTimeout(tvHandler, time);
  var counter = 0;
  var interval = setInterval(function () {
    console.log("try number " + ++counter);
    if (!mainVid) {
      tvHandler();
    } else {
      clearInterval(interval);
    }
  }, 2000);
});

function failedFullscreenMode() {
  $(mainVid).addClass("fullscreen");
  $("nav,.nav,.navbar,footer,.footer").remove();
  var parents = $(mainVid).parents("*");
  $("*").css("opacity", "0");
  $(parents).css("opacity", "1");
}
function writeInCorner(text) {
  $("span.ext-top-label").remove();
  $("body").append('<span class="ext-top-label">' + text + "</span>");
  setTimeout(function () {
    $("span.ext-top-label").remove();
  }, 5000);
}
function tvHandler() {
  $("video").each(function (i, elm) {
    console.log(elm);
    vids.push(elm);
    if (maxDur < elm.duration) {
      mainVid = elm;
    }
  });
  console.log("finished");
  if (mainVid) {
    console.log("starting video (if not autostarted)..");
    mainVid.play();
    try {
      mainVid.muted=false
      mainVid.volume=1
      setInterval(function(){
        mainVid.muted=false
        mainVid.volume=1
      },1000)
      console.log("fullscreen request");
      mainVid.requestFullScreen();
      console.log("fullscreen success");
    } catch (e) {
      console.log(e);
      failedFullscreenMode();
      console.log("fullscreen fail, fullscreen by class");
    }
    console.log("connect to websocket");
    // var ws = new WebSocket("ws://localhost:8765");
    // ws.onmessage = websocketCallback
  }
}