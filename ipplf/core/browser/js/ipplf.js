/*
script js for IPPLF projet
AFFINITIC MARS 2016
*/


function changementProprio(etat) {
    var demandeurProprio = document.querySelector('input[name = "demandeurProprio"]:checked').value;

    /* categorie individuelle => reduction_montant et reduction_modif */
    if (demandeurProprio == "True"){
        document.getElementById("proprio-demandeur").style="display:block";
        document.getElementById("motif-demande").style="display:block";
        document.getElementById("proprio-pas-demandeur").style="display:none";
    }
    else {
        document.getElementById("proprio-demandeur").style="display:none";
        document.getElementById("motif-demande").style="display:block";
        document.getElementById("proprio-pas-demandeur").style="display:block";
    }
}
