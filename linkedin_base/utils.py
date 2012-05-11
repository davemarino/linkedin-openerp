# encoding: utf-8
from osv import osv
import urllib2
import webbrowser

def util_calllinkedin(self, cr, uid, ids, context={}):
	"""Call the linkedin redirect url"""
	config_id = self.pool.get('linkedin.configuration').search(cr, uid,[])
	try:
		_id = config_id[0]
	except:
		_id = config_id
	if _id:
		config = self.pool.get('linkedin.configuration').browse(cr, uid, _id)
		url = config.url
	try:
		response = urllib2.urlopen(url)
		url = response.geturl()
		webbrowser.open_new(url)
		return True
	except Exception, e:
		raise osv.except_osv("Error", "%s" % e)
		return False