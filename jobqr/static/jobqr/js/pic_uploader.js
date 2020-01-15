const Uploader = {
  init() {
    this.startBtn = $('#add-pictures');
    this.uploader = $('#pictures');
    this.uploadBtn = $('#upload-pictures');
    this.files = $('#customFile');
    this.csrfInput = document.getElementsByName("csrfmiddlewaretoken");

    this.startBtn.on('click', () => {
      this.revealUploader()
    });
    this.uploadBtn.on('click', () => {
      this.startUploading();
    })
  },
  revealUploader() {
    this.uploader.toggleClass('d-none')
  },
  startUploading() {
    const filesToUpload = this.files[0].files;
    console.log(filesToUpload);
    const path = window.location.pathname;
    const url = `${path}pictures/`;
    const items = new FormData();
    $.each(filesToUpload, (i, file) => {
      items.append('images', file);
    });
    items.append('csrfmiddlewaretoken', this.csrfInput[0].value);
    console.log(items.getAll('images'));
    fetch(url, {method: 'POST', body: items}).then()
  }
};

$(document).ready(function () {
  bsCustomFileInput.init();
  Uploader.init();
});
