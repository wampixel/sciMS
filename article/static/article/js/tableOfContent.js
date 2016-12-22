/**
 * Générer le sommaire de l'article scientifique dynamiquement
 */
function generateSummary() {
    // Liste des éléments à rechercher
    list_tags = ["H1", "H2", "H3", "H4", "H5", "H6"];

    // Section parent de l'article dont ses fils sont à analyser
    tag_section = "DIV";

    // Chercher <article> dans la page
    var article = document.getElementsByTagName("article")[0];

    // Chercher le sommaire dans la page
    var summary = document.getElementById("summary");

    // Compter les liens du sommaire (pour les ancres)
    lien = 1;

    // Créer la navigation <nav>
    navigation = document.createElement("nav");

    // Créer le premier <ul> pour la fonction récursive
    list = document.createElement("ul");

    // Compléter la navigation à l'aide du retour de la fonction récursive
    navigation.appendChild(generateNavigationSummary(article, list));

    // Ajouter le nouveau sommaire généré dans la navigation
    summary.appendChild(navigation);
}

/**
 * Générer le sommaire récursivement
 * Arguments : tree (arbre DOM), list (future navigation)
 * Retourner : <ul> liste de navigation
 */
function generateNavigationSummary(tree, list) {
    // Parcourir les enfants du noeud courant de l'arbre DOM
    for (var i = 0; i < tree.childNodes.length; ++i) {
        // Si le DOM est une balise (HTML) (élimination des noeuds "fantômes")
        if (tree.childNodes[i].nodeType == 1) {
            // Si une balise section est rencontrée et si elle possède des enfants
            if (tree.childNodes[i].tagName == tag_section && tree.hasChildNodes()) {
                // Créer une nouvelle liste <ul> avec notre nouvelle élément
                var ul = document.createElement("ul");
                var li = document.createElement("li");

                // Poursuivre la récursivité et compléter notre nouvelle liste <ul> avec le retour
                list.appendChild(generateNavigationSummary(tree.childNodes[i], ul));

                // Compléter notre liste principale <ul> avec notre dernière liste
                li.appendChild(ul);
                list.appendChild(li);
            }
            // Si le noeud n'est pas <section> ou ne possède pas d'enfants
            else {
                // Le noeud courant appartient-il à la liste des tags à copier ?
                for (j = 0; j < list_tags.length; ++j) {
                    // Si le noeud courant appartient à la liste des tags à copier
                    if (tree.childNodes[i].tagName == list_tags[j]) {
                        // Création de <li> et <a>
                        var li = document.createElement("li");
                        var a = document.createElement("a");

                        // Définition de l'ancre pour <a>
                        a.setAttribute("href", "#" + lien);
                        a.appendChild(document.createTextNode(tree.childNodes[i].textContent));

                        // Ajouter le lien <a> à notre nouvel élément <li> de liste
                        li.appendChild(a);

                        // Ajouter l'élément à la liste principale <ul>
                        list.appendChild(li);

                        // Modifier le noeud de l'article pour lui ajouter un identifiant
                        tree.childNodes[i].setAttribute("id", lien);

                        // Incrémenter le nombre de lien de navigation
                        ++lien;
                    }
                }
            }
        }
    }

    return list;
}

/* FIN DU CHARGEMENT DE LA PAGE */
window.onload = generateSummary;
