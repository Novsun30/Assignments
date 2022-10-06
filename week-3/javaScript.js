fetch(
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    let results = data.result.results;
    let divContainers = document.querySelectorAll("div.container");
    for (let i = 0; i < results.length; i++) {
      if (divContainers[i] == undefined) {
        break;
      }
      if (divContainers[i].classList.contains("added")) {
        continue;
      }
      for (let j = 0; j < results[i].file.length; j++) {
        let url = results[i].file.toLowerCase();
        if (url[j] == "j" && url[j + 1] == "p" && url[j + 2] == "g") {
          let firstPic = url.slice(0, j + 3);
          let img = document.createElement("img");
          img.src = firstPic;
          divContainers[i].appendChild(img);
          divContainers[i].classList.add("added"); // mark the container with img added
          break;
        }
      }
      let divTitle = document.createElement("div");
      let h3 = document.createElement("h3");
      divTitle.classList.add("title");
      divContainers[i].appendChild(divTitle);
      h3.innerText = results[i].stitle;
      divTitle.appendChild(h3);
    }
  });

function loadMore() {
  fetch(
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
  )
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      //----load new containers---
      let main = document.querySelector("main");
      let section = document.createElement("section");
      section.classList.add("bottom");
      let divContainer = document.createElement("div");
      divContainer.classList.add("container");
      main.appendChild(section);
      for (let i = 0; i < 8; i++) {
        section.appendChild(divContainer.cloneNode(true));
      }
      //------------------
      let results = data.result.results;
      let divContainers = document.querySelectorAll("div.container");
      for (let i = 0; i < results.length; i++) {
        if (divContainers[i] == undefined) {
          break;
        }
        if (divContainers[i].classList.contains("added")) {
          continue; //ignore the container with img added
        }
        for (let j = 0; j < results[i].file.length; j++) {
          let url = results[i].file.toLowerCase();
          if (url[j] == "j" && url[j + 1] == "p" && url[j + 2] == "g") {
            let firstPic = url.slice(0, j + 3);
            let img = document.createElement("img");
            img.src = firstPic;
            divContainers[i].appendChild(img);
            divContainers[i].classList.add("added"); // mark the container with img added
            break;
          }
        }
        let divTitle = document.createElement("div");
        let h3 = document.createElement("h3");
        divTitle.classList.add("title");
        divContainers[i].appendChild(divTitle);
        h3.innerText = results[i].stitle;
        divTitle.appendChild(h3);
      }
      //------remove button-----
      if (results.length == divContainers.length) {
        let button = document.querySelector("div.button");
        button.remove();
      }
      //-------------
    });
}
