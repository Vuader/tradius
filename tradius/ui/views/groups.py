# -*- coding: utf-8 -*-
# Copyright (c) 2018 Christiaan Frans Rademan.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holders nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
from luxon import g
from luxon import router
from luxon import register
from luxon import render_template
from luxon.utils.bootstrap4 import form

from tradius.lib.ops import ops
from tradius.ui.models.groups import tradius_group

g.nav_menu.add('/Infrastructure/Radius/Groups',
               href='/infrastructure/radius/group',
               tag='services',
               feather='package')


@register.resources()
class Groups():
    def __init__(self):
        router.add('GET',
                   '/infrastructure/radius/group',
                   self.list,
                   tag='services')

        router.add('GET',
                   '/infrastructure/radius/group/{id}',
                   self.view,
                   tag='services')

        router.add('GET',
                   '/infrastructure/radius/group/delete/{id}',
                   self.delete,
                   tag='services')

        router.add(('GET', 'POST',),
                   '/infrastructure/radius/group/add',
                   self.add,
                   tag='services')

        router.add(('GET', 'POST',),
                   '/infrastructure/radius/group/edit/{id}',
                   self.edit,
                   tag='services')

        router.add('POST',
                   '/infrastructure/radius/group/add_attr/{id}',
                   self.add_attr,
                   tag='services')

        router.add('GET',
                   '/infrastructure/radius/group/rm_attr/{id}',
                   self.rm_attr,
                   tag='services')

    def list(self, req, resp):
        return render_template('tradius.ui/groups/list.html',
                               view='Subscriber Groups')

    def delete(self, req, resp, id):
        req.context.api.execute('DELETE', '/v1/group/%s' % id,
                                endpoint='radius')

    def view(self, req, resp, id):
        vr = req.context.api.execute('GET', '/v1/group/%s' % id,
                                     endpoint='radius')
        html_form = form(tradius_group, vr.json, readonly=True)
        return render_template('tradius.ui/groups/view.html',
                               view='View Subscriber Group',
                               form=html_form,
                               id=id)

    def edit(self, req, resp, id):
        if req.method == 'POST':
            req.context.api.execute('PUT', '/v1/group/%s' % id,
                                    data=req.form_dict,
                                    endpoint='radius')
            return self.view(req, resp, id)
        else:
            domain = req.context.api.execute('GET', '/v1/group/%s' % id,
                                             endpoint='radius')
            html_form = form(tradius_group, domain.json)
            return render_template('tradius.ui/groups/edit.html',
                                   view='Edit Subscriber Group',
                                   form=html_form,
                                   id=id,
                                   ops=ops)

    def add(self, req, resp):
        if req.method == 'POST':
            response = req.context.api.execute('POST', '/v1/group',
                                               data=req.form_dict,
                                               endpoint='radius')
            return self.view(req, resp, response.json['id'])
        else:
            html_form = form(tradius_group)
            return render_template('tradius.ui/groups/add.html',
                                   view='Add Subscriber Group',
                                   form=html_form)

    def add_attr(self, req, resp, id):
        data = req.form_dict

        uri = '/v1/group/%s/attrs' % id

        response = req.context.api.execute('POST', uri, data=data,
                                           endpoint='radius')

    def rm_attr(self, req, resp, id):
        uri = '/v1/group/%s/attrs' % id
        response = req.context.api.execute('DELETE', uri, endpoint='radius') 
