const myStatus = document.getElementById('status');
fetch('/', {
    method: "POST",
    body: fd
  }).then(res => res.json())
    .then(data => {
      myStatus.innerHTML = data.Status;
      delete data.Status;

    })
