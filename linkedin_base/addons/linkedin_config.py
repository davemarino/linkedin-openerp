# -*- coding: utf-8 -*-

from osv import fields, osv

class linkedin_configuration(osv.osv):
    _name = "linkedin.configuration"

    _columns = {
        'url': fields.char('Middleware URL', size=512),
    }

linkedin_configuration()

class linkedin_backlog(osv.osv):
    _name = "linkedin.backlog"

    _columns = {
        'linkedin_profile_id' : fields.char('Profile Id', size=64),
        'linkedin_first_name' : fields.char('First Name', size=1024),
        'linkedin_last_name' : fields.char('Last Name', size=1024),
        'linkedin_headline' : fields.char('Headline', size=1024),
        'linkedin_specialties' : fields.char('Specialties', size=1024),
        'linkedin_industry' : fields.char('Industry', size=1024),
        'linkedin_honors' : fields.char('Honors', size=1024),
        'linkedin_interests' : fields.char('Interests', size=1024),
        'linkedin_languages' : fields.char('Languages', size=1024),
        'linkedin_picture_url' : fields.char('Picture URL', size=1024),
        'linkedin_skills' : fields.char('Skills', size=1024),
        'linkedin_public_url' : fields.char('Public URL', size=1024),
        'linkedin_location' : fields.char('Location', size=1024),
        'linkedin_location_country' : fields.char('Location Country', size=1024),
        'linkedin_positions': fields.one2many('linkedin.position', 'backlog_id', 'Positions'),
    }

    def unlink(self, cr, uid, ids, context=None):
        for _id in ids:
            backlog = self.browse(cr, uid, _id)
            positions = backlog.linkedin_positions
            for pos in positions:
                pos.unlink(context=context)
            super(linkedin_backlog, self).unlink(cr, uid, _id, context=context)
        return True

linkedin_backlog()

class linkedin_position(osv.osv):
    _name = "linkedin.position"

    _columns = {
        'ref': fields.char('Position Id', size=64),
        'title': fields.char('Position Title', size=1024),
        'summary': fields.char('Position Summary', size=1024),
        'start_date': fields.datetime('Start date', size=1024),
        'end_date': fields.datetime('End date', size=1024),
        'company': fields.char('Company name', size=1024),
        'backlog_id': fields.many2one('linkedin.backlog', 'Backlog Id'),
    }

linkedin_position()