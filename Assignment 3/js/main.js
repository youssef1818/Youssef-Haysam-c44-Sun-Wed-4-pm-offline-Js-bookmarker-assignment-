var inputName = document.getElementById('siteName');
var inputUrl = document.getElementById('siteUrl');
var sitesArray = [];
if (localStorage.getItem('sites') != null) {
    sitesArray = JSON.parse(localStorage.getItem('sites'))
    display();
}
function addSite() {

    if (validationForm(inputName) && validationForm(inputUrl)) {
      
        var site = {
            name: inputName.value,
            URL: inputUrl.value,
        }
        sitesArray.push(site);
        display();
        localStorage.setItem('sites', JSON.stringify(sitesArray))
        clearInput();
    } 
       
   
}
function display() {
    var cartona = "";
    for (var i = 0; i < sitesArray.length; i++) {
        cartona += `<div class=" siteDisplay d-flex align-items-baseline justify-content-center bg-white py-2 border-top  ">
                
                <div class="col-3">
                    <p class="mb-0 text-center ">${i + 1}</p>
                </div >
                <div class="col-3">
                    <p class="mb-0 text-center">${sitesArray[i].name}</p>
                </div>
                <div class="col-3 text-center">
                   <a href="${sitesArray[i].URL}"> <button type="button " class="btn btn-success "> <i class="fa-regular fa-eye"></i> Visit</button></a>
                </div>
                <div class="col-3 text-center">
                    <button type="button " class="btn btn-danger" onclick="Delete(${i})"><i class="fa-solid fa-trash"></i> Delete</button>
                </div>
                
            </div>`
    }
    document.getElementById('special').innerHTML = cartona;
}
function clearInput() {
    inputName.value = null;
    inputUrl.value = null;
}
function Delete(i) {
    sitesArray.splice(i, 1);
    localStorage.setItem('sites', JSON.stringify(sitesArray));
    display();
}
function validationForm(ele) {
    var regex = {
        siteName:  /^[a-zA-Z0-9_]{3,}$/,
        siteUrl: /(www.([a-z]|[A-Z]|[0-9]){2,})|(.com)$/
    }
    if (regex[ele.id].test(ele.value)) {
        ele.classList.remove("is-invalid")
        ele.classList.add("is-valid")
        ele.nextElementSibling.classList.add("d-none")
        return true
        
    } else {
        ele.nextElementSibling.classList.remove("d-none")
        
        ele.classList.remove("is-valid")
        ele.classList.add("is-invalid")
        return false

    }
}
