import requests
from calendar import monthrange

meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
ano = '2019'

for mes in meses:
    dias_mes = monthrange(int(ano), int(mes))[1]
    for dia in range(1,dias_mes+1):
        if dia < 10:  
            url = 'http://sdro.ons.org.br/SDRO/DIARIO/' + ano + '_' + mes + '_0'+ str(dia) +'/HTML/14_CargaHorariaSub_0'+ str(dia) +'-'+ mes +'-' + ano + '.xlsx'
            r = requests.get(url, allow_redirects=True)
            open('dados'+mes+'_'+str(dia)+ '_'+ ano +'.xlsx', 'wb').write(r.content)
        else:
            url = 'http://sdro.ons.org.br/SDRO/DIARIO/' + ano + '_' + mes + '_'+ str(dia) +'/HTML/14_CargaHorariaSub_'+ str(dia) +'-'+ mes +'-' + ano + '.xlsx'
            r = requests.get(url, allow_redirects=True)
            open('dados'+mes+'_'+str(dia)+ '_'+ ano +'.xlsx', 'wb').write(r.content)