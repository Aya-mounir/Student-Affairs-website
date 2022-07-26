//**************(Assign Page)***************** */



let assi = document.getElementById("sub")
 assi.onclick=function(){
      
 }
assi.addEventListener("click",function(event){ 
    let d=document.getElementById("sdep").value;
    let N=document.getElementById("search").value;
    
    
    if( d=='' ||  N=='' )
    {
        assi.type = "button";
        event.preventDefault();
        alert("You Must Enter your name or your id ");
    }
   

})

//**************(Assign Page)***************** */