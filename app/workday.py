import workday


client = workday.WorkdayClient()
#client = workday.WorkdayClient(
#    wsdls={'talent': 'https://workday.com/tenant/434$sd.xml'},
#    authentication=WsSecurityCredentialAuthentication('lmcneil', 'LWWUw5Gw-cDDs0K'),
 #   )

#print(client.talent.Get_Languages().data)