# -*- coding: utf-8 -*-

from osv import fields, osv

from linkedin_base.utils import util_calllinkedin

class linkedin_position(osv.osv):
    _name = "linkedin.position"
    _inherit = "linkedin.position"

    _columns = {
        'contact_id': fields.many2one('res.partner.contact', 'Contact Id'),
    }

linkedin_position()

class linkedin_backlog(osv.osv):
    _name = "linkedin.backlog"
    _inherit = "linkedin.backlog"

    _columns = {
        'contact_id': fields.many2one('res.partner.contact', 'Contact Id'),
    }

    def copy_contact_profile(self, cr, uid, ids, context={}):
        try:
            _id = ids[0]
        except Exception, e:
            _id = ids
        this = self.browse(cr, uid, _id)
        if this.contact_id:
            cont = this.contact_id
            values = {
                'linkedin_profile_id': this.linkedin_profile_id,
                'linkedin_first_name': this.linkedin_first_name,
                'linkedin_last_name': this.linkedin_last_name,
                'linkedin_headline': this.linkedin_headline,
                'linkedin_specialties': this.linkedin_specialties,
                'linkedin_industry': this.linkedin_industry,
                'linkedin_honors': this.linkedin_honors,
                'linkedin_interests': this.linkedin_interests,
                'linkedin_languages': this.linkedin_languages,
                'linkedin_picture_url': this.linkedin_picture_url,
                'linkedin_skills': this.linkedin_skills,
                'linkedin_public_url': this.linkedin_public_url,
                'linkedin_location_country': this.linkedin_location_country,
                'linkedin_location': this.linkedin_location,
            }
            cont.write(values)
            val={}
            for pos in this.linkedin_positions:
                val['backlog_id'] = False
                val['contact_id'] = cont.id
                pos.write(val)
            backlog_ids = self.search(cr, uid, [('contact_id','=', cont.id)])
            backlogs = self.browse(cr, uid, backlog_ids)
            for back in backlogs:
                back.unlink()
        data_obj = self.pool.get('ir.model.data')
        id2 = data_obj._get_id(cr, uid, 'linkedin_base', 'linkedin_backlog_tree')
        if id2:
            id2 = data_obj.browse(cr, uid, id2, context=context).res_id
        return {
                'view_type': 'tree',
                'view_mode': 'tree',
                'res_model': 'linkedin.backlog',
                'view_id': id2,
                'type': 'ir.actions.act_window',
            }

linkedin_backlog()

class res_partner_contact(osv.osv):
    _name = "res.partner.contact"
    _description = "Contact"
    _inherit = "res.partner.contact"

    _columns = {
        'linkedin':fields.boolean('LinkedIn', help="If LinkedIn field is set to True, it will allow you to download the information from LinkedIn."),
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
        'linkedin_positions': fields.one2many('linkedin.position', 'contact_id', 'Positions'),
    }

    _defaults = {
        'linkedin' : lambda * a: False
    }

    def calllinkedin(self, cr, uid, ids, context={}):
        return util_calllinkedin(self, cr, uid, ids, context)

res_partner_contact()