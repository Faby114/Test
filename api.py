from fastapi import FastAPI,HTTPException,Form
import uvicorn,requests,uuid,json,random,re,hashlib,time
from bs4 import BeautifulSoup as bs
from pydantic import BaseModel
from typing import Optional,Union
app=FastAPI()
liste=[]
def generate_ua():
	ua_wind='Mozilla/5.0 (Windows NT %s.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s.%s.%s.%s Safari/537.36'%(random.choice(['10','11']),random.randrange(110,201),random.randint(0,10),random.randint(0,10),random.randint(0,10))
	return ua_wind
class Gen(BaseModel):
	cooks:Union[str,int]
class User(BaseModel):
	email:Union[int,str]
	pwd:Union[int,str]
class Add(BaseModel):
	name:str
	pwd:Union[str,int]
	email:Union[str,int]
class Update1(BaseModel):
	user_id:str
	new_name:str
@app.get("/")
async def fonc():
	return "Hello,C'est L'Api de Faby"
@app.get("/composant/{uid}")
async def fonc1(uid):
	return {"Composant":uid}
@app.get("/login/uid={uid}&pwd={pwd}")
async def fonc2(uid,pwd):
	head = {'Host':'b-graph.facebook.com','X-Fb-Connection-Quality':'EXCELLENT','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; RMX3740 Build/QP1A.190711.020) [FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/480086274;FBCR/Corporation Tbk;FBMF/realme;FBBD/realme;FBDV/RMX3740;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.0,width=540,height=960};FB_FW/1;FBRV/483172840;]','X-Tigon-Is-Retry':'false','X-Fb-Friendly-Name':'authenticate','X-Fb-Connection-Bandwidth':str(random.randrange(70000000,80000000)),'Zero-Rated':'0','X-Fb-Net-Hni':str(random.randrange(50000,60000)),'X-Fb-Sim-Hni':str(random.randrange(50000,60000)),'X-Fb-Request-Analytics-Tags':'{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}','Content-Type':'application/x-www-form-urlencoded','X-Fb-Connection-Type':'WIFI','X-Fb-Device-Group':str(random.randrange(4700,5000)),'Priority':'u=3,i','Accept-Encoding':'gzip, deflate','X-Fb-Http-Engine':'Liger','X-Fb-Client-Ip':'true','X-Fb-Server-Cluster':'true','Content-Length':str(random.randrange(1500,2000))}
	data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':uid,'password':'#PWD_FB4A:0:{}:{}'.format(str(time.time())[:10], pwd),'generate_analytics_claim':'1','community_id':'','linked_guest_account_userid':'','cpl':True,'try_num':'1','family_device_id':str(uuid.uuid4()),'secure_family_device_id':str(uuid.uuid4()),'credentials_type':'password','account_switcher_uids':[],'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3','fb4a_shared_phone_cpl_group':'enable_v3_at_risk','enroll_misauth':False,'generate_session_cookies':'1','error_detail_type':'button_with_disabled','source':'login','machine_id':str(''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(24)])),'jazoest':str(random.randrange(22000,23000)),'meta_inf_fbmeta':'V2_UNTAGGED','advertiser_id':str(uuid.uuid4()),'encrypted_msisdn':'','currently_logged_in_userid':'0','locale':'fr_FR','client_country_code':'fr','fb_api_req_friendly_name':'authenticate','fb_api_caller_class':'Fb4aAuthHandler','api_key':'882a8490361da98702bf97a021ddc14d','sig':str(hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:32]),'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
	rq1=requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
	if "session_key" in rq1:
		user=rq1['uid']
		token=rq1['access_token']
		cooks=''.join(['{}={};'.format(i['name'],i['value']) for i in rq1['session_cookies']])
		var={
		"user_id":user,
		"token":token,
		'cookie':cooks}
		return var
	else:
		return rq1
@app.post("/cookie2/")
async def fonc3(cooks:Union[str,int]=Form(...)):
	gen=Gen(cooks=cooks)
	cookie=gen.cooks
	rq=requests.Session()
	url="https://web.facebook.com"
	header= {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'light','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':generate_ua()}
	rq1=rq.get(url,headers=header,cookies={'cookie':cookie})
	rp1=bs(rq1.text,'html.parser')
	try:
		return {"av":re.search('"actorID":"(.*?)"',str(rp1)).group(1),"__aaid":"0","__user":re.search('"actorID":"(.*?)"',str(rp1)).group(1),"__a":"1","__req":"14",'__hs':re.search('"haste_session":"(.*?)",',str(rp1)).group(1),'__dpr':'2','__ccg':'GOOD','__rev':re.search('{"rev":(.*?)}',str(rp1)).group(1),'__hsi':re.search('"hsi":"(.*?)",',str(rp1)).group(1),'__comet_req':'15','fb_dtsg':re.search(r'"DTSGInitialData",\[\],{"token":"(.*?)"',str(rp1)).group(1),'jazoest':re.search('&jazoest=(.*?)",',str(rp1)).group(1),'lsd':re.search(r'"LSD",\[\],{"token":"(.*?)"',str(rp1)).group(1),'__spin_r':re.search('"__spin_r":(.*?),',str(rp1)).group(1),'__spin_b':'trunk','__spin_t':re.search('"__spin_t":(.*?),',str(rp1)).group(1),'fb_api_caller_class':'RelayModern'}
	except Exception as e:
		return {"error_msg":"Cookie Invalid or Expired,please verify your cookie and try again"}
@app.post('/login/')
async def fonc4(email:Union[int,str]=Form(...),pwd:Union[int,str]=Form(...)):
	user=User(email=email,pwd=pwd)
	pas=user.pwd
	num=user.email
	head = {'Host':'b-graph.facebook.com','X-Fb-Connection-Quality':'EXCELLENT','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; RMX3740 Build/QP1A.190711.020) [FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/480086274;FBCR/Corporation Tbk;FBMF/realme;FBBD/realme;FBDV/RMX3740;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.0,width=540,height=960};FB_FW/1;FBRV/483172840;]','X-Tigon-Is-Retry':'false','X-Fb-Friendly-Name':'authenticate','X-Fb-Connection-Bandwidth':str(random.randrange(70000000,80000000)),'Zero-Rated':'0','X-Fb-Net-Hni':str(random.randrange(50000,60000)),'X-Fb-Sim-Hni':str(random.randrange(50000,60000)),'X-Fb-Request-Analytics-Tags':'{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}','Content-Type':'application/x-www-form-urlencoded','X-Fb-Connection-Type':'WIFI','X-Fb-Device-Group':str(random.randrange(4700,5000)),'Priority':'u=3,i','Accept-Encoding':'gzip, deflate','X-Fb-Http-Engine':'Liger','X-Fb-Client-Ip':'true','X-Fb-Server-Cluster':'true','Content-Length':str(random.randrange(1500,2000))}
	data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':num,'password':'#PWD_FB4A:0:{}:{}'.format(str(time.time())[:10], pas),'generate_analytics_claim':'1','community_id':'','linked_guest_account_userid':'','cpl':True,'try_num':'1','family_device_id':str(uuid.uuid4()),'secure_family_device_id':str(uuid.uuid4()),'credentials_type':'password','account_switcher_uids':[],'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3','fb4a_shared_phone_cpl_group':'enable_v3_at_risk','enroll_misauth':False,'generate_session_cookies':'1','error_detail_type':'button_with_disabled','source':'login','machine_id':str(''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(24)])),'jazoest':str(random.randrange(22000,23000)),'meta_inf_fbmeta':'V2_UNTAGGED','advertiser_id':str(uuid.uuid4()),'encrypted_msisdn':'','currently_logged_in_userid':'0','locale':'fr_FR','client_country_code':'fr','fb_api_req_friendly_name':'authenticate','fb_api_caller_class':'Fb4aAuthHandler','api_key':'882a8490361da98702bf97a021ddc14d','sig':str(hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:32]),'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
	rq1=requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
	if "session_key" in rq1:
		user=rq1["uid"]
		token=rq1["access_token"]
		cooks=''.join(['{}={};'.format(i['name'],i['value']) for i in rq1['session_cookies']])
		return {
		"user_id":user,
		"token":token,
		"cookie":cooks}
	else:
		return rq1
@app.post("/add_user/")
async def fonc5(name:str=Form(...),pwd:Union[int,str]=Form(...),email:Union[str,int]=Form(...)):
	add=Add(name=name,pwd=pwd,email=email)
	user_id="user"+str(random.randrange(1000,9999))
	liste.append(f"{add.name}|{add.pwd}|{add.email}|{user_id}")
	return {"message":"Registration Success","user_info":{"user_name":f"{add.name}","user_id":user_id}}

@app.get("/all_users/")
async def fonc6():
	return liste
@app.put("/update_name/")
async def fonc7(user_id:str=Form(...),new_name:str=Form(...)):
	update=Update1(user_id=user_id,new_name=new_name)
	uid=update.user_id
	n_name=update.new_name
	liste1=[]
	try:
		for x in liste:
			id=x.split("|")[3]
			liste1.append(id)
	except:
		raise HTTPException(status_code=404,detail="User Not Found")
	if uid in liste1:
		index=liste1.index(uid)
		old_info=liste[index]
		name,pwd,email,user_id=old_info.split("|")
		liste[index]=f"{n_name}|{pwd}|{email}|{user_id}"
		return {"message":"Name has been edited Successfuly","user_info":{"name":n_name,"user_id":uid}}
	else:
		raise HTTPException(status_code=404,detail="User Not Found")
