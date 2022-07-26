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
 if(!isNaN(i)){
    alert("id should not to be a string");
 }
if(N.length>15)
 {
     alert("Name Must be less than or equal 10 characters");
 }

 if (l<1 || l>4)
 {
     alert("Level Field Must Be 1 To 4");
 }
 

 
 if( g>4  || l>4)
 {
    alert("Gpa less than 4 ");
 }
 if( l>4)
 {
    alert(" Level less than or equal 4 ");
 }

if (g<0){
     
     alert("Gpa Must be 0 to 4 only ");
}


 

 })
 
 function del()
 {
     confirm("Are You Sure You Want To Delete This");
 }
//******(Add Page)***** *//