#!/usr/bin/env python3
# Conduct DNS Zone Transfer
# Author Yehia Elghaly

import dns.query
import dns.zone

fzone = 'nsztm1.digi.ninja'
szone = 'zonetransfer.me'

tr = dns.zone.from_xfr(dns.query.xfr(fzone, szone))
domain = tr.nodes.keys()
sorted(domain)

for n in domain:
    print(tr[n].to_text(n))