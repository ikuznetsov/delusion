from gi.repository import WebKit as webkit
import urllib
from os import system
import base64

class Browser(webkit.WebView):
    def __init__(self):
        webkit.WebView.__init__(self)

        #Allow to load local json files
        settings = self.get_settings()
        settings.props.enable_file_access_from_file_uris=True
        settings.props.enable_universal_access_from_file_uris=True
        self.set_settings(settings)
        self.connect("navigation-policy-decision-requested",self._nav_request_policy_decision_cb)
        self.l_uri=None

    def _nav_request_policy_decision_cb(self,view,frame,net_req,nav_act,pol_dec):
        uri=net_req.get_uri()
        if uri==self.l_uri:
            pol_dec.use()
            return True
        if uri.startswith('xdg:'):
            try:
                system("xdg-open %s" % base64.b64decode(uri[4:]))
            except:
                pass
            return True
        if uri.startswith('exec:'):
            try:
                system("%s" % base64.b64decode(uri[4:]))
            except:
                pass
            return True
 
        self.l_uri=uri
        page=urllib.urlopen(uri)
        frame.load_string(page.read(),"text/html","iso-8859-15",page.geturl())
        pol_dec.ignore()
        return True
