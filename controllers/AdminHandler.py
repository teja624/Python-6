#  Copyright 2010 - 2012 Mark Finch
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not
#  use this file except in compliance with the License. You may obtain a copy
#  of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

#  Libraries
import webapp2
from google.appengine.api import users
from google.appengine.ext.webapp.util import login_required

# Import Views
from views.admin_view import display_admin

# Import Models
from models.EnvVars import update_vars
from models.EnvVars import tz_list
from models.EnvVars import env_vars

#  Homepage Request Handler Class
class AdminHandler(webapp2.RequestHandler):
    @login_required
    def get(self):
        values = {'logout_url': users.create_logout_url("/"),
                  'app_vars': env_vars(),
                  'time_zones': tz_list()}
        if users.is_current_user_admin():  # secure the page only admin can access
            display_admin(self, values)
        else:
            self.abort(401)

    def post(self):
        try:
            update_vars(self, 
                        adp=self.request.get('adp'),
                        dtz=self.request.get('default_tz'))
            self.redirect('/admin')
        except:
            self.abort(500)
