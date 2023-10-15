var i = 0;
function progressing() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("progress");
    var width = 1;
    var id = setInterval(frame, 10);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
      } else {
        width++;
        elem.style.width = width + "%";
      }
    }
  }
}