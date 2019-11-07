const App = {
  init() {
    this.addBtn = document.getElementById("start_adding_items");
    this.addSection = document.getElementById("add_items");
    this.addForm = document.getElementById('add_form');
    this.qrLinkInput = document.getElementById('qr_link');
    this.csrfInput = document.getElementsByName("csrfmiddlewaretoken");
    this.currentItemsUl = document.getElementById("current_items");
    this.currentItems = [];
    this.initCurrentItems();
    this.addBtn.addEventListener('click', this.detectQr.bind(this));
    this.addForm.addEventListener('submit', this.addFormListener.bind(this));
  },
  addFormListener(ev) {

    const item = this.qrLinkInput.value;

    const items = new FormData();

    items.append('csrfmiddlewaretoken', this.csrfInput[0].value);
    items.append('scanned_url', item);

    fetch('', {method: 'POST', body: items})
      .then(response => response.json())
      .then(() => {
        this.initCurrentItems();
      });

    ev.preventDefault();
    return false;

  },
  initCurrentItems() {
    const url = '/api' + window.location.pathname;

    fetch(url).then(res => res.json()).then(({current_items}) => {
      this.updateCurrentItems(current_items);
    });
  },
  updateCurrentItems(items) {
    this.currentItems = items;

    this.currentItemsUl.innerHTML = this.currentItems.map(item => {
      return `<tr>
                <td>${item.pk}</td>
                <td>${item.name}</td>
                <td><button type="button" class="btn btn-danger" onclick="App.untrackItem(this)" value="${item.pk}">Remove</button></td>
              </tr>`;
    }).join('');
  },
  untrackItem(item) {
    const data = new FormData();
    data.append('csrfmiddlewaretoken', this.csrfInput[0].value);
    fetch(window.location.pathname + 'untrack/' + item.value + '/', {method: 'POST', body: data})
      .then(res => res.json())
      .then(json => {
        console.log(json);
        App.initCurrentItems();
      })
  },
  detectQr() {
    this.addSection.hidden = false;
    const video = document.createElement("video");
    const canvasElement = document.getElementById("canvas");
    const canvas = canvasElement.getContext("2d");
    const loadingMessage = document.getElementById("loadingMessage");
    const outputContainer = document.getElementById("output");
    const outputMessage = document.getElementById("outputMessage");
    const outputData = document.getElementById("outputData");

    function drawLine(begin, end, color) {
      canvas.beginPath();
      canvas.moveTo(begin.x, begin.y);
      canvas.lineTo(end.x, end.y);
      canvas.lineWidth = 4;
      canvas.strokeStyle = color;
      canvas.stroke();
    }

    // Use facingMode: environment to attemt to get the front camera on phones
    navigator.mediaDevices.getUserMedia({video: {facingMode: "environment"}}).then(function (stream) {
      video.srcObject = stream;
      video.setAttribute("playsinline", 'true'); // required to tell iOS safari we don't want fullscreen
      video.play();
      requestAnimationFrame(tick);
    });

    function tick() {
      loadingMessage.innerText = "⌛ Loading video...";
      if (video.readyState === video.HAVE_ENOUGH_DATA) {
        loadingMessage.hidden = true;
        canvasElement.hidden = false;
        outputContainer.hidden = false;
        canvasElement.height = video.videoHeight;
        canvasElement.width = video.videoWidth;
        canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);
        const imageData = canvas.getImageData(0, 0, canvasElement.width, canvasElement.height);
        const code = jsQR(imageData.data, imageData.width, imageData.height, {
          inversionAttempts: "dontInvert",
        });
        if (code) {
          drawLine(code.location.topLeftCorner, code.location.topRightCorner, "#FF3B58");
          drawLine(code.location.topRightCorner, code.location.bottomRightCorner, "#FF3B58");
          drawLine(code.location.bottomRightCorner, code.location.bottomLeftCorner, "#FF3B58");
          drawLine(code.location.bottomLeftCorner, code.location.topLeftCorner, "#FF3B58");
          outputMessage.hidden = true;
          outputData.parentElement.hidden = false;
          outputData.innerText = code.data;
          App.qrLinkInput.setAttribute('value', code.data);

        } else {
          outputMessage.hidden = false;
          outputData.parentElement.hidden = true;
        }
      }
      requestAnimationFrame(tick);
    }
  }
};
App.init();