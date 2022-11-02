function searchUsername(){
    let input = document.querySelector("input.search-input")
    fetch(`http://127.0.0.1:3000/api/member?username=${input.value}`)
        .then((response) => response.json())
        .then((data) => {
            if(document.querySelector("h2.search-result") == null){
                let searchContainer = document.querySelector("div.search-container");
                let result = document.createElement("h2");
                result.classList.add("search-result")
                searchContainer.appendChild(result);
            }
            if(data.data == null){
                let elementH2 = document.querySelector("h2.search-result")
                elementH2.innerText = "無此會員";
                return;
            }
            let elementH2 = document.querySelector("h2.search-result")
            elementH2.innerHTML = `<span class = "show-name">${data.data.name}</span> <span class = "parentheses">(</span><span class = "show-username">${data.data.username}</span><span class = "parentheses">)</span>`;
            return;
        });
    return;
}

function updateUsername(){
    input = document.querySelector("input.update-input")
    fetch("http://127.0.0.1:3000/api/member",{
        method:"PATCH",
        headers:{"content-type":"application/json"},
        body:JSON.stringify({"name":input.value})
    })
    .then((response)=>response.json())
    .then((data)=>{
        if (document.querySelector("h2.update-result") == null){
            let result = document.createElement("h2");
            let updateContainer = document.querySelector("div.update-container");
            result.classList.add("update-result");
            updateContainer.appendChild(result);
        }
        if(Object.keys(data) == "ok"){
            let result = document.querySelector("h2.update-result");
            result.innerText = "更新成功";
            let showName = document.querySelector("h2.show-name")
            showName.innerText = `${input.value}，歡迎登入`
            return;
        }
        let result = document.querySelector("h2.update-result");
        result.innerHTML = "更新失敗";
        return;
    });
}

let searchButton = document.querySelector("button.search-button");    
searchButton.addEventListener("click", searchUsername);

let updateButton = document.querySelector("button.update-button");
updateButton.addEventListener("click", updateUsername);
