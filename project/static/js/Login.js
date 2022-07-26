//******************(Login Page)************************/
function login(event){

    var n = document.getElementById("name").value;
    var p = document.getElementById("pass").value;

    if(n==false||p==false)
    {
        return false;
    }

     else if(n=="Nehal" && p=="20200251"){
        location.href = "{% url 'home' %}";
    }
    
    else{
        
       alert("username or password is incorrect")
       return false;

    }
  
}

//******************(Login Page)************************/
