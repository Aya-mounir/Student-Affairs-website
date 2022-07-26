//******(Add Page)***** *//

let sub = document.getElementById("Submit")
  sub.onclick=function(){
       

  }

 sub.addEventListener("click",function(event){
     let i=document.getElementById("Id").value;
     let g=document.getElementById("Gpa").value;
     let l=document.getElementById("slevel").value;
     let d=document.getElementById("depart").value;
     let E=document.getElementById("Email").value;
     let M=document.getElementById("Mobile").value;
     let D= document.getElementById("Date").value; 
     let N=document.getElementById("Name").value;
     let Em=document.getElementById("Email").value;

   
 if(i==''||g=='' ||l=='' || d==''|| E=='' ||M==''|| D==''||N==''||Em=='')
 {
     sub.type = "button";
     event.preventDefault();
     alert("You Must Enter Data First ");


 }
 if(l<1 || l>4){
    alert("level must be between 1 and 4");
}
 
 if(g<0 || g>4){
    alert("gpa must be between 0 and 4");
}
 
if(i.length<8){
    alert("id must be more than or equal 8");
}
 


 })
 
 function del()
 {
     confirm("Are You Sure You Want To Delete This");
 }
//******(Add Page)***** *//