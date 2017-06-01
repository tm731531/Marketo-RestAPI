
# coding: utf-8

# In[40]:

url=url
client_id=client_id
client_secret=client_secret
date=date


# In[41]:

def sentreq(uri,method='GET'):
    import requests
    session = requests.Session() 
    req = requests.Request(method, uri).prepare()
    resp = session.send(req)
    return resp.json()
  


# In[42]:

access_token_uri="%sidentity/oauth/token?grant_type=client_credentials&client_id=%s&client_secret=%s" %(url,client_id,client_secret)
access_token_data=sentreq(access_token_uri)
access_token_data


# In[43]:


pageToken_uri=url+"rest/v1/activities/pagingtoken.json?sinceDatetime=%s&access_token=%s" %(date,access_token_data['access_token'])
pageToken_data=sentreq(pageToken_uri)
pageToken_data


# In[44]:

restlead_uri=url+"rest/v1/activities.json?activityTypeIds=12&access_token=%s&nextPageToken=%s" %(access_token_data['access_token'],pageToken_data['nextPageToken']);
restlead_data=sentreq(restlead_uri)
restlead_data


# In[51]:

for i in restlead_data['result']:
    print ("ID:%s leadId : %s"%(i['id'],i['leadId']))

