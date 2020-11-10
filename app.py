import numpy as np
from flask import Flask, request,  render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model_depto.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #int_features = [int(x) for x in request.form.values()]
    comuna=request.form['comuna']
    
    zonas_rm={ 
    'Buin':	'satelite',
    'Calera de Tango':	'satelite',
    'Cerrillos':	'poniente',
    'Cerro Navia':	'norponiente',
    'Colina':	'satelite',
    'Conchalí':	'norponiente',
    'El Bosque':	'surponiente',
    'El Monte':	'satelite',
    'Estación Central':	'centro',
    'Huechuraba':	'norponiente',
    'Independencia':	'centro',
    'Isla de Maipo':	'satelite',
    'La Cisterna':	'surponiente',
    'La Florida':	'suroriente',
    'La Granja':	'surponiente',
    'La Pintana':	'suroriente',
    'La Reina':	'nororiente',
    'Lampa':	'satelite',
    'Las Condes':	'nororiente',
    'Lo Barnechea':	'nororiente',
    'Lo Espejo':	'surponiente',
    'Lo Prado':	'norponiente',
    'Macul':	'suroriente',
    'Maipú':	'surponiente',
    'Ñuñoa':	'nororiente',
    'Padre Hurtado':	'satelite',
    'Paine':	'satelite',
    'Pedro Aguirre Cerda':	'centro',
    'Peñaflor':	'satelite',
    'Peñalolén':	'suroriente',
    'Pirque':	'satelite',
    'Providencia':	'nororiente',
    'Pudahuel':	'norponiente',
    'Puente Alto':	'suroriente',
    'Quilicura':	'norponiente',
    'Quinta Normal':	'centro',
    'Recoleta':	'centro',
    'Renca':	'norponiente',
    'San Bernardo':	'surponiente',
    'San Joaquín':	'norponiente',
    'San José de Maipo':	'satelite',
    'San Miguel':	'centro',
    'San Ramón':	'surponiente',
    'Santiago':	'centro',
    'Talagante':	'satelite',
    'Vitacura':	'nororiente' 
     }
    zona=""
    for key,value in zonas_rm.items():
        if comuna== key:
            zona=value
        
    if zona=='centro':
        zona_nororiente=0
        zona_norponiente=0
        zona_satelite=0
        zona_suroriente=0
        zona_surponiente=0
    elif zona=='satelite':
        zona_nororiente=0
        zona_norponiente=0
        zona_satelite=1
        zona_suroriente=0
        zona_surponiente=0
    elif zona=='nororiente':
        zona_nororiente=1
        zona_norponiente=0
        zona_satelite=0
        zona_suroriente=0
        zona_surponiente=0
    elif zona=='norponiente':
        zona_nororiente=0
        zona_norponiente=1
        zona_satelite=0
        zona_suroriente=0
        zona_surponiente=0
    elif zona=='surponiente':
        zona_nororiente=0
        zona_norponiente=0
        zona_satelite=0
        zona_suroriente=0
        zona_surponiente=1
    elif zona=='suroriente':
        zona_nororiente=0
        zona_norponiente=0
        zona_satelite=0
        zona_suroriente=1
        zona_surponiente=0
    
    dormitorio=request.form['dormitorios']
    bano=request.form['banos']
    metros=request.form['metros']
    bodega=request.form['bodega']
    if bodega=='SI':
        bodega=1
    else:
        bodega=0
    estacionamiento=request.form['estacionamiento']
    if estacionamiento=='SI':
        estacionamiento=1
    else:
        estacionamiento=0
    metro=request.form['metro']
    if metro=='SI':
        metro=1
    else:
        metro=0
    piscina=request.form['piscina']
    if piscina=='SI':
        piscina=1
    else:
        piscina=0
    ocupacion=request.form['ocupacion']
    if ocupacion=='SI':
        ocupacion=1
    else:
        ocupacion=0
    loggia=request.form['loggia']
    if loggia=='SI':
        loggia=1
    else:
        loggia=0
    
    int_features=[bodega,
                  estacionamiento,
                  loggia,
                  piscina,
                  metro,
                  dormitorio,
                  bano,
                  metros,
                  ocupacion,
                  zona_nororiente,
                  zona_norponiente,
                  zona_satelite,
                  zona_suroriente,
                  zona_surponiente
                  ]
    
    
    
    final_features = [np.array(int_features)]
    
    prediction = model.predict(final_features)

    output = int(prediction[0])

    return render_template('index.html', prediction_text='Monto estimado:  $ {}'.format(output).replace(",", "@").replace(".", ",").replace("@", "."))

if __name__ == "__main__":
    app.run(debug=True)
    
    
