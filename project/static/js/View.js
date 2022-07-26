//******(View Page)******* */

const active = document.getElementById("active")
const inActive = document.getElementById("inactive")
const all = document.getElementById("all")
const btn = document.getElementById("change")
const statuses = document.querySelectorAll(".status")

let arr = []
statuses.forEach(function(e){
     const id = document.getElementById

     const obj = {
        name : document.getElementById("name"+e.id).innerHTML,
        id : document.getElementById("id"+e.id).innerHTML

    }
    arr.push(obj)
    
})

btn.addEventListener("click", function(){
    let counter = 0;
    if(active.checked){
        (arr[counter].status == "Active")
        {
            const data = "<tr>"
        }
    }
        
})


//******(View Page)******* */