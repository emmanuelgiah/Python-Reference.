# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 22:46:50 2019

@author: Emmanuel
"""

import webbrowser;
import requests as rq;

res = rq.get("https://thispersondoesnotexist.com");
print(type(res));