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
from interfaces import IManageCaisseMusee
from boisduluc.db.pgsql.baseTypes import DemandeIntervention


class ManageDemandeIntervention(BrowserView):
    implements(IManageDemandeIntervention)

    def getAllDemandeIntervention(self):
        """
        recuperation de toutes les demande d'intervention
        """
        wrapper = getSAWrapper('ipplf')
        session = wrapper.session
        query = session.query(DemandeIntervention)
        query = query.order_by(DemandeIntervention.di_date_creation)
        allDemandeInterventions = query.all()
        return allDemandeInterventions


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
        operationTypePaiementFk = fields.get('operationTypePaiementFk', None)
        operationTypePaiementFk = fields.get('operationTypePaiementFk', None)
        operationTypePaiementFk = fields.get('operationTypePaiementFk', None)



        wrapper = getSAWrapper('boisduluc')
        session = wrapper.session
        insertOperation = wrapper.getMapper('operation')
        newEntry = insertOperation(di_nom_demandeur=nomDemandeur
                                   di_prenom_demandeur=prenomDemandeur
                                   di_gsm_demandeur=gsmDemandeur
                                   di_email_demandeur=emailDemandeur
                                   di_rue_demandeur=rueDemandeur
                                   di_cp_demandeur=cpDemandeur
                                   di_localite_demandeur=localiteDemandeur
                                   di_nom_non_locataire=nomNoLocataireDemandeur
                                   di_prenom_non_locataire=prenomNoLocataireDemandeur
                                   di_gsm_non_locataire=gsmNoLocataireDemandeur
                                   di_email_non_locataire=emailNoLocataireDemandeur
                                   di_rue_non_locataire=rueNoLocataireDemandeur
                                   di_cp_non_locataire=cpNoLocataireDemandeur
                                   di_localite_non_locataire=localiteNoLocataireDemandeur
                                   di_probleme_electrique_demandeur=problemeElectriqueDemandeur
                                   di_probleme_plomberie_demandeur=problemePlomberieDemandeur
                                   di_probleme_menuiserie_demandeur=problemeMenuiserieDemandeur
                                   di_probleme_toiture_demandeur=problemeToitureDemandeur
                                   di_probleme_chauffage_demandeur=problemeToitureDemandeur
                                   di_type_chauffage_demandeur=typeChauffageDemandeur
                                   di_probleme_eau_chaude_demandeur=problemeEauChaudeDemandeur
                                   di_probleme_chauffage_demandeur=problemeChauffageDemandeur
                                   di_probleme_wc_evacuation_demandeur=deboucherWcDemandeur
                                   di_deboucher_wc_demandeur=problemeWcEvacuationDemandeur
                                   di_probleme_horticol_demandeur=problemeHorticoleDemandeur
                                   di_probleme_humidite_demandeur=
                                   di_probleme_autre_motif_demandeur=
                                   di_commentaire_ipplf=
                                   di_etat_ipplf=
                                   )
        session.add(newEntry)
        session.flush()
        session.refresh(newEntry)
        operationPk = newEntry.operation_pk

        portalUrl = getToolByName(self.context, 'portal_url')()
        ploneUtils = getToolByName(self.context, 'plone_utils')
        message = u"Ok c'est dans la caisse !"
        ploneUtils.addPortalMessage(message, 'info')
        url = "%s/caisse-du-musee" % (portalUrl,)
        self.request.response.redirect(url)
        return ''



