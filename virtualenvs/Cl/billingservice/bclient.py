from zeep import Client
from zeep import xsd
from datetime import date, datetime
#from collections import defaultdict
import json

currentMonth = datetime.now().month
print(currentMonth)

wsdl = "http://clvmweb.clyfsa.com:81/SEP2WebServices/ManagementService.svc?singleWsdl"
client = Client(wsdl)

request_data ={
    "groupReference": {
      "Name": "PDS EXCLUSIVOS Activos",
    } 
  }
response = client.service.QueryGroupMembers(**request_data)
request_data_amt ={
    "groupReference": {
      "Name": "Active-AM550-T",
    }
  }
responseamt = client.service.QueryGroupMembers(**request_data_amt)
request_data_amm ={
    "groupReference": {
      "Name": "Active-AM550-E",
    }
  }
responseamm = client.service.QueryGroupMembers(**request_data_amm)
#print (response)
#Here 'request_data' is the request parameter dictionary.
#Assuming that the operation named 'sendData' is defined in the passed wsdl.
#print (response)
lim = len(response["Devices"]["DeviceReference"])
limamt = len(responseamt["Devices"]["DeviceReference"])
limamm = len(responseamm["Devices"]["DeviceReference"])
flim=lim+limamm+limamt
devices_all= []
for j in range (lim):
	devices_all.append(response["Devices"]["DeviceReference"][j]["Name"])
for k in range (limamt):
	devices_all.append(responseamt["Devices"]["DeviceReference"][k]["Name"])
for l in range (limamm):
	devices_all.append(responseamm["Devices"]["DeviceReference"][l]["Name"])
lim = len(devices_all)
alldvcs=[]
ddvcs=[]
print(lim)
#lim=20
#def myconverter(o):
#    if isinstance(o, datetime.datetime):
#        return o.__str__()
 

ddd=0
for x in range (lim):
	arequest_data ={
        "deviceReference": {
          "Name": devices_all[x],
        },
        "queryAll": "false",
        "attributeReferences": {
          "AttributeReferencesByGroup": [
            {
              "AttributeGroupType": "DeviceParameters",
              "AttributeReferences": {
                "AttributeReference": {
                  "Name": "Numero de Medidor"
                }
              },
              "AllAttributes": "false"
            }
          ]
        }
      }
	#print(response["Devices"]["DeviceReference"][x]["Name"])  
	#print(x)
	
	#aresponse = client.service.QueryDeviceAttributes(**arequest_data)
	bwsdl = "http://clvmweb.clyfsa.com:81/SEP2WebServices/DataService.svc?singleWsdl"
	bclient = Client(bwsdl)

	brequest_data ={
	    "measurementPointResultTypes": {
	      "MeasurementPointResultTypeReferences": {
	        "MeasurementPointName": devices_all[x],
	        "AgencyId": "0",
	        "ResultTypeNames":  "AbsoluteEnergy_T0_BP1",
	        
	      }
	    },
	    "intervalStart": "2022-01-02T00:00:00",
	    "intervalEnd": "2022-12-02T00:00:00",
	    "statusFilter": "null",
	    "sourceFilter": {
	      "Measured": "true",
	      "Manual": "false",
	      "Aggregated": "false",
	      "Imported": "false",
	      "Estimated": "false"
	    },
	    "resultOrigin": "PreferRaw",
	    "lastResultOnly": "true"
	  }

	#bresponse = bclient.service.QueryResults(**brequest_data)
	#print(brequest_data)
	crequest_data ={
	    "measurementPointResultTypes": {
	      "MeasurementPointResultTypeReferences": {
	        "MeasurementPointName": devices_all[x],
	        "AgencyId": "0",
	        "ResultTypeNames": "AbsoluteEnergy_T1_BP1"
	      }
	    },
	    "intervalStart": "2022-01-02T00:00:00",
	    "intervalEnd": "2022-12-02T00:00:00",
	    "statusFilter": "null",
	    "sourceFilter": {
	      "Measured": "true",
	      "Manual": "false",
	      "Aggregated": "false",
	      "Imported": "false",
	      "Estimated": "false"
	    },
	    "resultOrigin": "PreferRaw",
	    "lastResultOnly": "true"
	  }

	#cresponse = bclient.service.QueryResults(**crequest_data)
	drequest_data ={
	    "measurementPointResultTypes": {
	      "MeasurementPointResultTypeReferences": {
	        "MeasurementPointName": devices_all[x],
	        "AgencyId": "0",
	        "ResultTypeNames": "AbsoluteEnergy_T2_BP1"
	      }
	    },
	    "intervalStart": "2022-01-02T00:00:00",
	    "intervalEnd": "2022-12-02T00:00:00",
	    "statusFilter": "null",
	    "sourceFilter": {
	      "Measured": "true",
	      "Manual": "false",
	      "Aggregated": "false",
	      "Imported": "false",
	      "Estimated": "false"
	    },
	    "resultOrigin": "PreferRaw",
	    "lastResultOnly": "true"
	  }
	#dresponse = bclient.service.QueryResults(**drequest_data)
	#alldvcs.append(cresponse)
	erequest_data ={
	    "measurementPointResultTypes": {
	      "MeasurementPointResultTypeReferences": {
	        "MeasurementPointName": devices_all[x],
	        "AgencyId": "0",
	        "ResultTypeNames": "ReactiveEnergyPlus_CUM_T0_BP1"
	      }
	    },
	    "intervalStart": "2022-01-02T00:00:00",
	    "intervalEnd": "2022-12-02T00:00:00",
	    "statusFilter": "null",
	    "sourceFilter": {
	      "Measured": "true",
	      "Manual": "false",
	      "Aggregated": "false",
	      "Imported": "false",
	      "Estimated": "false"
	    },
	    "resultOrigin": "PreferRaw",
	    "lastResultOnly": "true"
	  }
	frequest_data ={
		"measurementPointResultTypes": {
		  "MeasurementPointResultTypeReferences": {
		    "MeasurementPointName": devices_all[x],
		    "AgencyId": "0",
		    "ResultTypeNames": "AbsoluteMaxDemand_T0_BP1"
		  }
		},
		"intervalStart": "2022-01-02T00:00:00",
		"intervalEnd": "2022-12-02T00:00:00",
		"statusFilter": "null",
		"sourceFilter": {
		  "Measured": "true",
		  "Manual": "false",
		  "Aggregated": "false",
		  "Imported": "false",
		  "Estimated": "false"
		},
		"resultOrigin": "PreferRaw",
		"lastResultOnly": "true"
	  }
	grequest_data ={
		"measurementPointResultTypes": {
		  "MeasurementPointResultTypeReferences": {
		    "MeasurementPointName": devices_all[x],
		    "AgencyId": "0",
		    "ResultTypeNames": "AbsoluteMaxDemand_T1_BP1"
		  }
		},
		"intervalStart": "2022-01-02T00:00:00",
		"intervalEnd": "2022-12-02T00:00:00",
		"statusFilter": "null",
		"sourceFilter": {
		  "Measured": "true",
		  "Manual": "false",
		  "Aggregated": "false",
		  "Imported": "false",
		  "Estimated": "false"
		},
		"resultOrigin": "PreferRaw",
		"lastResultOnly": "true"
	  }
	hrequest_data ={
		"measurementPointResultTypes": {
		  "MeasurementPointResultTypeReferences": {
		    "MeasurementPointName": devices_all[x],
		    "AgencyId": "0",
		    "ResultTypeNames": "AbsoluteMaxDemand_T2_BP1"
		  }
		},
		"intervalStart": "2022-01-02T00:00:00",
		"intervalEnd": "2022-12-02T00:00:00",
		"statusFilter": "null",
		"sourceFilter": {
		  "Measured": "true",
		  "Manual": "false",
		  "Aggregated": "false",
		  "Imported": "false",
		  "Estimated": "false"
		},
		"resultOrigin": "PreferRaw",
		"lastResultOnly": "true"
	  }
	#aresponse = client.service.QueryDeviceAttributes(**arequest_data)
	aresponse = client.service.QueryDeviceAttributes(**arequest_data)
	bresponse = bclient.service.QueryResults(**brequest_data)
	cresponse = bclient.service.QueryResults(**crequest_data)
	dresponse = bclient.service.QueryResults(**drequest_data)
	eresponse = bclient.service.QueryResults(**erequest_data)
	fresponse = bclient.service.QueryResults(**frequest_data)
	gresponse = bclient.service.QueryResults(**grequest_data)
	hresponse = bclient.service.QueryResults(**hrequest_data)
	#alldvcs.append(aresponse)
	#alldvcs.append(bresponse)
	#alldvcs.append(cresponse)
	#alldvcs.append(dresponse)
	#alldvcs.append(eresponse)
	print(x)
	print(aresponse, bresponse, cresponse, dresponse, eresponse, fresponse, gresponse, hresponse)
	#print(response["Devices"]["DeviceReference"][x])
	alldvcs.append({'MeterName':devices_all[x]})
	#alldvcs.append({'DeviceId':bresponse[0].MeasurementPointId})
	
	#alldvcs[x]["id"]=bresponse[0].MeasurementPointId
	if hasattr(aresponse[0].Attributes, 'AttributeInfo'):
		alldvcs[x]["id"]=aresponse[0].Attributes.AttributeInfo[0].Value.Value
	else:
		alldvcs[x]["id"]='n/a'
	if hasattr(bresponse[0].ResultsByResultType, 'ResultTypeResults'):
		if hasattr(bresponse[0].ResultsByResultType.ResultTypeResults[0], 'Results'):
			if hasattr(bresponse[0].ResultsByResultType.ResultTypeResults[0].Results, 'Result'):
				
				alldvcs[x]["EnergiaActTotal"]=bresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Value.Value
			else:
				alldvcs[x]["EnergiaActTotal"]='n/a'
		else:
			alldvcs[x]["EnergiaActTotal"]='n/a'
	else:
		alldvcs[x]["EnergiaActTotal"]='n/a'				
	if hasattr(cresponse[0].ResultsByResultType, 'ResultTypeResults'):
		if hasattr(cresponse[0].ResultsByResultType.ResultTypeResults[0], 'Results'):
			if hasattr(cresponse[0].ResultsByResultType.ResultTypeResults[0].Results, 'Result'):
				
				alldvcs[x]["EnergiaActFPC"]=cresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Value.Value
			else:
				alldvcs[x]["EnergiaActFPC"]='n/a'
		else:
			alldvcs[x]["EnergiaActFPC"]='n/a'
	else:
		alldvcs[x]["EnergiaActFPC"]='n/a'
	if hasattr(dresponse[0].ResultsByResultType, 'ResultTypeResults'):
		if hasattr(dresponse[0].ResultsByResultType.ResultTypeResults[0], 'Results'):
			if hasattr(dresponse[0].ResultsByResultType.ResultTypeResults[0].Results, 'Result'):

				alldvcs[x]["EnergiaActPC"]=dresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Value.Value
			else:
				alldvcs[x]["EnergiaActPC"]='n/a'
		else:
			alldvcs[x]["EnergiaActPC"]='n/a'
	else:
		alldvcs[x]["EnergiaActPC"]='n/a'
	if hasattr(eresponse[0].ResultsByResultType, 'ResultTypeResults'):
		if hasattr(eresponse[0].ResultsByResultType.ResultTypeResults[0], 'Results'):
			if hasattr(eresponse[0].ResultsByResultType.ResultTypeResults[0].Results, 'Result'):
				
				alldvcs[x]["EnergiaReact"]=eresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Value.Value
			else:
				alldvcs[x]["EnergiaReact"]='n/a'
		else:
			alldvcs[x]["EnergiaReact"]='n/a'
	else:
		alldvcs[x]["EnergiaReact"]='n/a'		
	if hasattr(fresponse[0].ResultsByResultType, 'ResultTypeResults'):
		if hasattr(fresponse[0].ResultsByResultType.ResultTypeResults[0], 'Results'):
			if hasattr(fresponse[0].ResultsByResultType.ResultTypeResults[0].Results, 'Result'):
				
				alldvcs[x]["DemandaMaxTotal"]=fresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Value.Value
			else:
				alldvcs[x]["DemandaMaxTotal"]='n/a'
		else:
			alldvcs[x]["DemandaMaxTotal"]='n/a'
	else:
		alldvcs[x]["DemandaMaxTotal"]='n/a'
	if hasattr(gresponse[0].ResultsByResultType, 'ResultTypeResults'):
		if hasattr(gresponse[0].ResultsByResultType.ResultTypeResults[0], 'Results'):
			if hasattr(gresponse[0].ResultsByResultType.ResultTypeResults[0].Results, 'Result'):
				
				alldvcs[x]["DemandaMaxFPC"]=gresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Value.Value
			else:
				alldvcs[x]["DemandaMaxFPC"]='n/a'
		else:
			alldvcs[x]["DemandaMaxFPC"]='n/a'
	else:
		alldvcs[x]["DemandaMaxFPC"]='n/a'
	if hasattr(hresponse[0].ResultsByResultType, 'ResultTypeResults'):
		if hasattr(hresponse[0].ResultsByResultType.ResultTypeResults[0], 'Results'):
			if hasattr(hresponse[0].ResultsByResultType.ResultTypeResults[0].Results, 'Result'):
				
				alldvcs[x]["DemandaMaxPC"]=hresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Value.Value
			else:
				alldvcs[x]["DemandaMaxPC"]='n/a'
		else:
			alldvcs[x]["DemandaMaxPC"]='n/a'
	else:
		alldvcs[x]["DemandaMaxPC"]='n/a'
	if hasattr(bresponse[0].ResultsByResultType, 'ResultTypeResults'):
		if hasattr(bresponse[0].ResultsByResultType.ResultTypeResults[0], 'Results'):
			if hasattr(bresponse[0].ResultsByResultType.ResultTypeResults[0].Results, 'Result'):
				
				billdate=bresponse[0].ResultsByResultType.ResultTypeResults[0].Results.Result[0].Timestamp
				billdate= str(billdate)
				print('Date:', billdate)
				alldvcs[x]["Fecha_de_cierre"]=billdate
			else:
				alldvcs[x]["Fecha_de_cierre"]='n/a'
		else:
			alldvcs[x]["Fecha_de_cierre"]='n/a'
	else:
		alldvcs[x]["Fecha_de_cierre"]='n/a'			
	#alldvcs.append(aresponse[0]['Attributes']['AttributeInfo'][0]['Value']['Value'])
	
	#print(bresponse[0]["ResultsByResultType"]["ResultTypeResults"][0]["Results"]["Result"][0]["Value"]["Value"])
	#alldvcs.append('NOPE')
	#ele = (input("Name : ")) 
    #d = json.loads(s)
#print (alldvcs)

with open('/var/www/html/virtualenvs/Cl/billingservice/billing/billing.json', 'w', encoding='utf-8') as f:
    json.dump(alldvcs, f, ensure_ascii=False, indent=4)

	# prints [1,3,5]    
#aresponse = aclient.service.QueryDeviceAttributes(**raequest_data)

print (alldvcs)
