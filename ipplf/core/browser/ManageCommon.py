# -*- coding: utf-8 -*-

import datetime
from ManageMailer import Mailer
from Products.Five import BrowserView
from zope.interface import implements
from Products.CMFCore.utils import getToolByName
from interfaces import IManageCommon


class ManageCommon(BrowserView):
    """
    Methodes communes pour le projet IPPLF
    """

    implements(IManageCommon)

    def sendMail(self, sujet, message):
        """
        Envoi de mail
        """
        #mailer = Mailer("relay.skynet.be", "alain.meurant@affinitic.be")
        mailer = Mailer("localhost", "alain.meurant@affinitic.be")
        mailer.setSubject(sujet)
        mailer.setRecipients("alain.meurant@affinitic.be")
        mail = message
        mailer.sendAllMail(mail)

    def sendMailToDemandeur(self, sujet, message, emailDemandeur):
        """
        Envoi de mail au demandeur d'intervention
        """
        #mailer = Mailer("relay.skynet.be", emailDemandeur)
        mailer = Mailer("localhost", emailDemandeur)
        mailer.setSubject(sujet)
        recipients = "%s" % (emailDemandeur)
        mailer.setRecipients(recipients)
        mail = message
        mailer.sendAllMail(mail)

    def sendMailToIpplfForDemandeIntervention(self, sujet, message):
        """
        Envoi de mail à la personne qui a fait une demande d'inscription
        """
        #mailer = Mailer("relay.skynet.be", 'alain.meurant@affinitic.be')
        mailer = Mailer("localhost", 'alain.meurant@affinitic.be')
        mailer.setSubject(sujet)
        recipients = ','.join(['v.verstraete@ipplf.be', 'd.descamps@ipplf.be', 'alain.meurant@affinitic.be'])
        mailer.setRecipients(recipients)
        mail = message
        mailer.sendAllMail(mail)

    def getTimeStamp(self, aLaBelge):
        """
        Retourne la date stamp
        """
        timeStamp = datetime.datetime.now()
        if aLaBelge:
            return timeStamp.strftime('%d-%m-%Y %H:%M:%S')
        else:
            return timeStamp

    def getUserAuthenticated(self):
        """
        Retourne le nom du user loggué
        """
        pm = getToolByName(self, 'portal_membership')
        user = pm.getAuthenticatedMember()
        user = user.getUserName()
        return user

    def getRoleUserAuthenticated(self):
        """
        Retourne le nom du user loggué
        """
        pm = getToolByName(self.context, 'portal_membership')
        user = pm.getAuthenticatedMember()
        userRole = user.getRoles()
        return userRole
