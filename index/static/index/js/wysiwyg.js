function cmd(nom, arg) {
  if (typeof(arg) == 'undefined') {
    arg = '';
  }

  if (nom === 'createLink') {
    arg = prompt("adresse du lien :");
  }

  document.execCommand(nom, false, arg);

  if(document.queryCommandState("bold")) {
    document.getElementById("bouton_bold").className = "btn btn-success";
  } else{
    document.getElementById("bouton_bold").className = "btn btn-primary";
  }
  
  if(document.queryCommandState("italic")) {
    document.getElementById("bouton_it").className = "btn btn-success";
  } else{
    document.getElementById("bouton_it").className = "btn btn-primary";
  }  

  if(document.queryCommandState("underline")) {
    document.getElementById("bouton_und").className = "btn btn-success";
  } else{
    document.getElementById("bouton_und").className = "btn btn-primary";
  }
 
  if(document.queryCommandState("strikethrough")) {
    document.getElementById("bouton_stri").className = "btn btn-success";
  } else{
    document.getElementById("bouton_stri").className = "btn btn-primary";
  }
}


function result(){
  document.getElementById("hidden_content").value = document.getElementById("div_edit_art").innerHTML;
}