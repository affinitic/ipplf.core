# -*- coding: utf-8 -*-

#import datetime
#import time
#import random
#from sqlalchemy import select, func
#from mailer import Mailer
#from LocalFS import LocalFS
# #from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget
#from Products.CMFPlone.utils import normalizeString
#from Products.CMFPlone import PloneMessageFactory as _
#from Products.Archetypes.atapi import LinesField
#from Products.Archetypes.Renderer import renderer
#from Products.Archetypes.atapi import BaseContent
#from collective.captcha.browser.captcha import Captcha
from Products.Five import BrowserView
from zope.interface import implements
from zope.component import getMultiAdapter
from z3c.sqlalchemy import getSAWrapper
from Products.CMFCore.utils import getToolByName
from interfaces import IManageDemandeIntervention
from ipplf.db.pgsql.baseTypes import DemandeIntervention


class ManageDemandeIntervention(BrowserView):
    """
    Methodes pour la gestion d'une demande d'intervention pour le projet IPPLF
    """

    implements(IManageDemandeIntervention)

    def getAllDemandeIntervention(self):
        """
        Recuperation de toutes les demande d'intervention
        """
        wrapper = getSAWrapper('ipplf')
        session = wrapper.session
        query = session.query(DemandeIntervention)
        query = query.order_by(DemandeIntervention.di_date_creation)
        allDemandeInterventions = query.all()
        return allDemandeInterventions

    def sendMailToDemandeurIntervention(self, prenomDemandeur, nomDemandeur, emailDemandeur):
        """
        Envoi d'un mail de confirmation au demandeur d'intervention
        """
        commonTools = getMultiAdapter((self.context, self.request), name="manageCommon")

        sujet = "IPPLF : confirmation de votre demande d'intervention"
        message = """
                  Bonjour %s %s,
                  <br /><br />
                  Votre demande d'intervention à bien été envoyée.
                  <br />
                  Vous recevrez une réponse sous peu.
                  <br /><br />
                  Bien à vous,
                  <br /><br />
                  L'équipe IPPLF.
                  """ % (prenomDemandeur, nomDemandeur)
        commonTools.sendMailToDemandeur(sujet, message, emailDemandeur)

    def sendMailToIPPLF(self, nomDemandeur,
                              prenomDemandeur,
                              gsmDemandeur,
                              emailDemandeur,
                              rueDemandeur,
                              cpDemandeur,
                              localiteDemandeur,
                              nomNoLocataireDemandeur,
                              prenomNoLocataireDemandeur,
                              gsmNoLocataireDemandeur,
                              emailNoLocataireDemandeur,
                              rueNoLocataireDemandeur,
                              cpNoLocataireDemandeur,
                              localiteNoLocataireDemandeur,
                              problemeElectriqueDemandeur,
                              problemePlomberieDemandeur,
                              problemeMenuiserieDemandeur,
                              problemeToitureDemandeur,
                              typeChauffageDemandeur,
                              problemeChauffageDemandeur,
                              problemeEauChaudeDemandeur,
                              deboucherWcDemandeur,
                              problemeWcEvacuationDemandeur,
                              problemeHorticoleDemandeur,
                              problemeHumiditeDemandeur,
                              problemeAutreMotifDemandeur):
        """
        Envoi d'un mail à l'équipe Ipplf lors d'une demande d'intervention
        """
        commonTools = getMultiAdapter((self.context, self.request), name="manageCommon")

        dateCreationDemandeIntervantion = commonTools.getTimeStamp(True)


        sujet = "IPPLF : demande d'intervention via le site"
        message = """
              <font color='#888888'>
              <font color='#FF0000'><b>:: DEMANDE D'INTERVENTION ::</b></font><br /><br />
              Date de la demande : <font color='#ff9c1b'><b>%s</b></font><br />
              <br />
              <font color='#00405e'>*** Coordonnées du demandeur ***</font>
              <br />
              Nom : <font color='#ff9c1b'><b>%s</b></font><br />
              Prénom : <font color='#ff9c1b'><b>%s</b></font><br />
              Adresse : <font color='#ff9c1b'><b>%s</b></font><br />
              Code Postal : <font color='#ff9c1b'><b>%s</b></font><br />
              Localité : <font color='#ff9c1b'><b>%s</b></font><br />
              GSM / Tel : <font color='#ff9c1b'><b>%s</b></font><br />
              E-mail : <font color='#ff9c1b'><b>%s</b></font><br />
              <br /><br />

              <font color='#00405e'>*** Le Demandeur n'est pas le locataire ***</font>
              <br />
              Nom : <font color='#ff9c1b'><b>%s</b></font><br />
              Prénom : <font color='#ff9c1b'><b>%s</b></font><br />
              Adresse : <font color='#ff9c1b'><b>%s</b></font><br />
              Code Postal : <font color='#ff9c1b'><b>%s</b></font><br />
              Localité : <font color='#ff9c1b'><b>%s</b></font><br />
              GSM / Tel : <font color='#ff9c1b'><b>%s</b></font><br />
              E-mail : <font color='#ff9c1b'><b>%s</b></font><br />
              <br /><br />

              <font color='#00405e'>*** PROBLEME ***</font>
              <br />
              Electricité : <font color='#ff9c1b'><b>%s</b></font><br />
              Plomberie : <font color='#ff9c1b'><b>%s</b></font><br />
              Menuiserie : <font color='#ff9c1b'><b>%s</b></font><br />
              Toiture : <font color='#ff9c1b'><b>%s</b></font><br />
              Chauffage :  <font color='#ff9c1b'><b>%s</b></font><br />
              &nbsp;&nbsp; &#8618; Type de chauffage : <font color='#ff9c1b'><b>%s</b></font><br />
              Eau chaude : <font color='#ff9c1b'><b>%s</b></font><br />
              WC : <font color='#ff9c1b'><b>%s</b></font><br />
              &nbsp;&nbsp; &#8618; Tentative de déboucher : <font color='#ff9c1b'><b>%s</b></font><br />
              Horticole : <font color='#ff9c1b'><b>%s</b></font><br />
              Humidité - Infiltation : <font color='#ff9c1b'><b>%s</b></font><br />
              Autre motif : <font color='#ff9c1b'><b>%s</b></font><br />
              </font>
              """ % (dateCreationDemandeIntervantion, nomDemandeur, prenomDemandeur, rueDemandeur,
                     cpDemandeur, localiteDemandeur, gsmDemandeur, emailDemandeur, nomNoLocataireDemandeur,
                     prenomNoLocataireDemandeur, rueNoLocataireDemandeur, cpNoLocataireDemandeur,
                     localiteNoLocataireDemandeur, gsmNoLocataireDemandeur, emailNoLocataireDemandeur,
                     problemeElectriqueDemandeur, problemePlomberieDemandeur, problemeMenuiserieDemandeur,
                     problemeToitureDemandeur, problemeChauffageDemandeur, typeChauffageDemandeur,
                     problemeEauChaudeDemandeur, deboucherWcDemandeur, problemeWcEvacuationDemandeur,
                     problemeHorticoleDemandeur, problemeHumiditeDemandeur, problemeAutreMotifDemandeur)

        commonTools.sendMailToIpplfForDemandeIntervention(sujet, message)


    def insertDemandeIntervention(self):
        """
        table pg demande d'intervention
        ajout d'une demande d'intervention
        """
        commonTools = getMultiAdapter((self.context, self.request), name="manageCommon")
        operationUser = commonTools.getUserAuthenticated()
        operationTypeCaisseFk = 1
        operationTotal = 22

        fields = self.request.form
        nomDemandeur = fields.get('nomDemandeur', None)
        prenomDemandeur = fields.get('prenomDemandeur', None)
        gsmDemandeur = fields.get('gsmDemandeur', None)
        emailDemandeur = fields.get('emailDemandeur', None)
        rueDemandeur = fields.get('rueDemandeur', None)
        cpDemandeur = fields.get('cpDemandeur', None)
        localiteDemandeur = fields.get('localiteDemandeur', None)
        nomNoLocataireDemandeur = fields.get('nomNoLocataireDemandeur', None)
        prenomNoLocataireDemandeur = fields.get('prenomNoLocataireDemandeur', None)
        gsmNoLocataireDemandeur = fields.get('gsmNoLocataireDemandeur', None)
        emailNoLocataireDemandeur = fields.get('emailNoLocataireDemandeur', None)
        rueNoLocataireDemandeur = fields.get('rueNoLocataireDemandeur', None)
        cpNoLocataireDemandeur = fields.get('cpNoLocataireDemandeur', None)
        localiteNoLocataireDemandeur = fields.get('localiteNoLocataireDemandeur', None)
        problemeElectriqueDemandeur = fields.get('problemeElectriqueDemandeur', None)
        problemePlomberieDemandeur = fields.get('problemePlomberieDemandeur', None)
        problemeMenuiserieDemandeur = fields.get('problemeMenuiserieDemandeur', None)
        problemeToitureDemandeur = fields.get('problemeToitureDemandeur', None)
        typeChauffageDemandeur = fields.get('typeChauffageDemandeur', None)
        problemeChauffageDemandeur = fields.get('problemeChauffageDemandeur', None)
        problemeEauChaudeDemandeur = fields.get('problemeEauChaudeDemandeur', None)
        deboucherWcDemandeur = fields.get('deboucherWcDemandeur', None)
        problemeWcEvacuationDemandeur = fields.get('problemeWcEvacuationDemandeur', None)
        problemeHorticoleDemandeur = fields.get('problemeHorticoleDemandeur', None)
        problemeHumiditeDemandeur = fields.get('problemeHumiditeDemandeur', None)
        problemeAutreMotifDemandeur = fields.get('problemeAutreMotifDemandeur', None)

        commentaireIpplf = ""
        etatIpplf = True

        wrapper = getSAWrapper('ipplf')
        session = wrapper.session
        insertOperation = wrapper.getMapper('demande_intervention')
        newEntry = insertOperation(di_nom_demandeur=nomDemandeur,
                                   di_prenom_demandeur=prenomDemandeur,
                                   di_gsm_demandeur=gsmDemandeur,
                                   di_email_demandeur=emailDemandeur,
                                   di_rue_demandeur=rueDemandeur,
                                   di_cp_demandeur=cpDemandeur,
                                   di_localite_demandeur=localiteDemandeur,
                                   di_nom_non_locataire=nomNoLocataireDemandeur,
                                   di_prenom_non_locataire=prenomNoLocataireDemandeur,
                                   di_gsm_non_locataire=gsmNoLocataireDemandeur,
                                   di_email_non_locataire=emailNoLocataireDemandeur,
                                   di_rue_non_locataire=rueNoLocataireDemandeur,
                                   di_cp_non_locataire=cpNoLocataireDemandeur,
                                   di_localite_non_locataire=localiteNoLocataireDemandeur,
                                   di_probleme_electrique_demandeur=problemeElectriqueDemandeur,
                                   di_probleme_plomberie_demandeur=problemePlomberieDemandeur,
                                   di_probleme_menuiserie_demandeur=problemeMenuiserieDemandeur,
                                   di_probleme_toiture_demandeur=problemeToitureDemandeur,
                                   di_probleme_chauffage_demandeur=problemeChauffageDemandeur,
                                   di_type_chauffage_demandeur=typeChauffageDemandeur,
                                   di_probleme_eau_chaude_demandeur=problemeEauChaudeDemandeur,
                                   di_probleme_wc_evacuation_demandeur=problemeWcEvacuationDemandeur,
                                   di_deboucher_wc_demandeur=deboucherWcDemandeur,
                                   di_probleme_horticol_demandeur=problemeHorticoleDemandeur,
                                   di_probleme_humidite_demandeur=problemeHumiditeDemandeur,
                                   di_probleme_autre_motif_demandeur=problemeAutreMotifDemandeur)
        session.add(newEntry)
        session.flush()
        session.refresh(newEntry)
        operationPk = newEntry.di_pk

        self.sendMailToDemandeurIntervention(prenomDemandeur, nomDemandeur, emailDemandeur)

        self.sendMailToIPPLF(nomDemandeur,
                             prenomDemandeur,
                             gsmDemandeur,
                             emailDemandeur,
                             rueDemandeur,
                             cpDemandeur,
                             localiteDemandeur,
                             nomNoLocataireDemandeur,
                             prenomNoLocataireDemandeur,
                             gsmNoLocataireDemandeur,
                             emailNoLocataireDemandeur,
                             rueNoLocataireDemandeur,
                             cpNoLocataireDemandeur,
                             localiteNoLocataireDemandeur,
                             problemeElectriqueDemandeur,
                             problemePlomberieDemandeur,
                             problemeMenuiserieDemandeur,
                             problemeToitureDemandeur,
                             typeChauffageDemandeur,
                             problemeChauffageDemandeur,
                             problemeEauChaudeDemandeur,
                             deboucherWcDemandeur,
                             problemeWcEvacuationDemandeur,
                             problemeHorticoleDemandeur,
                             problemeHumiditeDemandeur,
                             problemeAutreMotifDemandeur)

        portalUrl = getToolByName(self.context, 'portal_url')()
        ploneUtils = getToolByName(self.context, 'plone_utils')
        message = u"Demande d'intervention envoyée !"
        ploneUtils.addPortalMessage(message, 'info')
        url = "%s/" % (portalUrl,)
        self.request.response.redirect(url)
        return ''



