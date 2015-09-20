import os
import sys
app_root = os.path.dirname(__file__) 
sys.path.insert(0,'site_packages')
import re
import requests as req
import sae

raw_cookies='pz4N_2132_nofavfid=1; pz4N_2132_lastvisit=1441106478; pz4N_2132_lastcheckfeed=34184%7C1441110116; pz4N_2132_blueidea_login=1; pz4N_2132_atarget=1; pz4N_2132_st_t=34184%7C1442647038%7C64764c90ef88feb4596aa2792cd72858; pz4N_2132_forum_lastvisit=D_50_1441624561D_2_1442647038; gsScrollPos=; pz4N_2132_ulastactivity=1442730236%7C0; pz4N_2132_sendmail=1; pz4N_2132_noticeTitle=1; pz4N_2132_visitedfid=48D2D43D50D42D44; pz4N_2132_smile=1D1; pz4N_2132_st_p=34184%7C1442730400%7Cc9aabd1f371bf22d4a9bb16640039d22; pz4N_2132_viewid=tid_21284; pz4N_2132_lastact=1442730466%09forum.php%09'
cookies={}
for line in raw_cookies.split(';'):
	key,value=line.split('=',1)
	cookies[key]=value


url='http://www.wndflb.com'
checkIn='http://www.wndflb.com/plugin.php?id=fx_checkin:checkin&formhash='



def qiandao(cookies):
	s=req.get(url,cookies=cookies)
	formhash=re.findall('checkin&formhash=(.*?)&',s.content)[0]
	urls=checkIn+formhash
	ss=req.get(urls,cookies=cookies)
	return ss
	
def app(environ, start_response):
	start_response('200 ok', [('content-type', 'text/plain')])
	qiandao(cookies)
	return ['Hello, SAE!']
		
application=sae.create_wsgi_app(app)   
