const App = {
  init() {
    this.videoSection = document.getElementById("video_section");
    this.cancellationId = 0;
    this.startDetection();
  },
  startDetection() {
    this.videoSection.hidden = false;
    const video = document.createElement("video");
    const canvasElement = document.getElementById("canvas");
    const ctx = canvasElement.getContext("2d");
    const loadingMessage = document.getElementById("loadingMessage");
    const outputContainer = document.getElementById("output");

    function drawLine(begin, end, color) {
      ctx.beginPath();
      ctx.moveTo(begin.x, begin.y);
      ctx.lineTo(end.x, end.y);
      ctx.lineWidth = 4;
      ctx.strokeStyle = color;
      ctx.stroke();
    }

    const width = Orientation.dimensions.width - 32;
    const height = Orientation.dimensions.height - 128;

    navigator.mediaDevices.getUserMedia({
      video: {
        facingMode: "environment",
        width: width,
        height: height
      }
    }).then(function (stream) {
      video.srcObject = stream;
      video.setAttribute("playsinline", "true");
      video.play();
      App.cancellationId = requestAnimationFrame(tick);
    });

    function tick() {
      loadingMessage.innerText = "⌛ Loading video...";
      if (video.readyState === video.HAVE_ENOUGH_DATA) {
        loadingMessage.hidden = true;
        canvasElement.hidden = false;
        outputContainer.hidden = false;
        canvasElement.height = video.videoHeight;
        canvasElement.width = video.videoWidth;
        ctx.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);
        const imageData = ctx.getImageData(0, 0, canvasElement.width, canvasElement.height);
        const code = jsQR(imageData.data, imageData.width, imageData.height, {inverse: 'dontInvert'});
        if (code) {
          drawLine(code.location.topLeftCorner, code.location.topRightCorner, "#5cff4e");
          drawLine(code.location.topRightCorner, code.location.bottomRightCorner, "#5CFF4E");
          drawLine(code.location.bottomRightCorner, code.location.bottomLeftCorner, "#5CFF4E");
          drawLine(code.location.bottomLeftCorner, code.location.topLeftCorner, "#5CFF4E");
          outputMessage.hidden = true;
          cancelAnimationFrame(App.cancellationId);
          App.initForm(code.data);
          return;
        } else {
          drawLine({x: 0, y: 0}, {x: 0, y: canvasElement.height}, "#FF3B58");
          drawLine({x: 0, y: canvasElement.height}, {x: canvasElement.width, y: canvasElement.height}, "#FF3B58");
          drawLine({x: canvasElement.width, y: canvasElement.height}, {x: canvasElement.width, y: 0}, "#FF3B58");
          drawLine({x: canvasElement.width, y: 0}, {x: 0, y: 0}, "#FF3B58");
        }
      }
      App.cancellationId = requestAnimationFrame(tick);
    }
  },
  initForm(data) {
    console.log(data);
    $("#inputItemUrl").val(data);
    $("#itemModal").modal('show');
  }
};
$(document).ready(function () {
  App.init();
});
