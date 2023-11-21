import requests

reqUrl = "https://cpd-aiops.apps.dexter.coc-ibm.com/aiops/api/issue-resolution/v1/incidents"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Authorization": "ZenApiKey YW5ndXMuamFtaWVzb246a2VlYTR1VE56Rm9pSUVUdHB2Y3JBYU80c3pVR3dBeDJOWWlnNEJQeg==" 
}


def getIncidents():
    payload = ""
    response = requests.request("GET", reqUrl, data=payload,  headers=headersList,verify=False)
    return response.text