
const dataForm = document.getElementById('data_form');

dataForm.onsubmit = function(e){
  const form = e.srcElement;
  const fd = new FormData(form);
  const myStatus = document.getElementById('status');
  fetch('/', {
      method: "POST",
      body: fd
    }).then(res => res.json())
      .then(data => {
        myStatus.innerHTML = data.Status;
        delete data.Status;
  })
  e.preventDefault();
}