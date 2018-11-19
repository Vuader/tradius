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

from luxon import db

def get_acct(domain=None, tenant_id=None, username=None):
    with db() as conn:
        query = 'SELECT' + \
                ' tradius_accounting.radacctid as radacctid,' + \
                ' tradius_accounting.acctsessionid as acctsessionid,' + \
                ' tradius_accounting.acctuniqueid as acctuniqueid,' + \
                ' tradius_accounting.username as username,' + \
                ' tradius_accounting.realm as realm,' + \
                ' tradius_accounting.nasipaddress as nasipaddress,' + \
                ' tradius_accounting.nasportid as nasportid,' + \
                ' tradius_accounting.acctstarttime as acctstarttime,' + \
                ' tradius_accounting.acctupdatetime as acctupdatetime,' + \
                ' tradius_accounting.acctstoptime as acctstoptime,' + \
                ' tradius_accounting.acctinterval as acctinterval,' + \
                ' tradius_accounting.acctsessiontime as acctsessiontime,' + \
                ' tradius_accounting.acctauthentic as acctauthentic,' + \
                ' tradius_accounting.connectinfo_start as connectinfo_start,' + \
                ' tradius_accounting.connectinfo_stop as connectinfo_stop,' + \
                ' tradius_accounting.acctinputoctets as acctinputoctets,' + \
                ' tradius_accounting.acctoutputoctets as acctoutputoctets,' + \
                ' tradius_accounting.calledstationid as calledstationid,' + \
                ' tradius_accounting.callingstationid  as callingstationid,' + \
                ' tradius_accounting.acctterminatecause as acctterminatecause,' + \
                ' tradius_accounting.servicetype as servicetype,' + \
                ' tradius_accounting.framedprotocol as framedprotocol,' + \
                ' tradius_accounting.framedipaddress as framedipaddress,' + \
                ' FROM' + \
                ' tradius_user_group LEFT JOIN tradius_group ON' + \
                ' tradius_user_group.group_id = tradius_group.id' + \
                ' WHERE tradius_user_group.user_id = %s'

        crsr = conn.execute(query, user_id)
        groups = crsr.fetchall()

    return groups

