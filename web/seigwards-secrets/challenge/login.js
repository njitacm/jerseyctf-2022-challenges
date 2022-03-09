

function checkCreds(usr, pass){

    if(usr.includes("admin")){
        if(btoa(pass) === "amN0ZnsxTV9zMF8xTV81b19EeW40TWl0M18wOTI0Nzh9"){
            alert("My Secrets: 1. I count in my sleep, 2. I hav")
        }
        else{
            alert("nice try Derrick")   
        }
    }
    else{
         alert("You fool!")   
    }

}

function login(){
    usr = document.getElementById('form3Example3').value
    pass = document.getElementById('form3Example4').value
    checkCreds(usr,pass)
}