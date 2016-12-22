// fonction permettant de creer les differentes composantes de l'editeur wysiwyg
function cmd(nom, arg) {
  if (typeof(arg) == 'undefined') {
    arg = '';
  }

  // si l'utilisateur veut creer un lien
  if (nom === 'createLink') {
    arg = prompt("adresse du lien :");
  }

  // on execute la commande voulu par le client
  document.execCommand(nom, false, arg);

  // si l'utilisateur a demande le texte en gras
  if(document.queryCommandState("bold")) {
    document.getElementById("bouton_bold").className = "btn btn-success";
  } else{
    document.getElementById("bouton_bold").className = "btn btn-primary";
  }
  
  // si l'utilisateur a denande le texte en italic
  if(document.queryCommandState("italic")) {
    document.getElementById("bouton_it").className = "btn btn-success";
  } else{
    document.getElementById("bouton_it").className = "btn btn-primary";
  }  

  // si l'utlisateur a demande le texte en souligne'
  if(document.queryCommandState("underline")) {
    document.getElementById("bouton_und").className = "btn btn-success";
  } else{
    document.getElementById("bouton_und").className = "btn btn-primary";
  }
 
  // si l'utilisateur a demande le texte en barre
  if(document.queryCommandState("strikethrough")) {
    document.getElementById("bouton_stri").className = "btn btn-success";
  } else{
    document.getElementById("bouton_stri").className = "btn btn-primary";
  }
}


function result(){
  document.getElementById("hidden_content").value = document.getElementById("div_edit_art").innerHTML;
}