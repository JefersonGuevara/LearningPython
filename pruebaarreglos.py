#[A J U S T E  D E  P O L I G O N A L  P O R  E L  M E T O D O  D E  L A  B R U J U L A]


import math

def gms2dec(angulo):
    grados = int(angulo)
    auxiliar = (angulo - grados) * 100
    minutos = int(auxiliar)
    segundos = (auxiliar - minutos)*100

    angulo_dec = grados + minutos / 60 + segundos / 3600

    return angulo_dec

#[ESTE BLOQUE CALCULA EL ACIMUT INICIAL]

def acimut_linea(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if dy != 0:
        rumbo = math.degrees(math.atan(dx/dy))

        if dx > 0 and dy > 0:
            acimut = rumbo
        elif dx > 0 and dy < 0:
            acimut = 180 + rumbo
        elif dx < 0 and dy < 0:
            acimut = 180 + rumbo
        elif dx < 0 and dy > 0:
            acimut = 360 + rumbo
        elif dx == 0 and dy > 0:
            acimut = 0
        elif dx == 0 and dy > 0:
            acimut = 180
    else:
        if dx > 0:
            acimut = 90
        elif dx < 0:
            acimut = 270
        else:
            acimut = -1
    
    return acimut

#[ESTE BLOQUE CONVIERTE EL ANGULO INGRESADO DE GRADOS DECIMALES A GGMMSS]
def dec2gms(angulo_dec):
    grados = int(angulo_dec)
    auxiliar = (angulo_dec - grados)*60
    minutos = int(auxiliar)
    segundos = round((auxiliar - minutos)*60,0)

    angulo_gms = '{:03d}'.format(grados) + '° ' + '{:02d}'.format(minutos) + "' " + '{:04.1f}'.format(segundos) + '"'

    return angulo_gms

#[CALCULA EL CONTRA ACIMUT Y RUMBO]
def acimut_poligonal(acimut_anterior, angulo_observ):
    if acimut_anterior >= 180:
        contra_acimut = acimut_anterior - 180
    else:
        contra_acimut = acimut_anterior + 180
    
    acimut = contra_acimut + angulo_observ

    if acimut >= 360:
        acimut = acimut - 360
    
    return acimut

#[CALCULA LAS PROYECCIONES]
def proyecciones(acimut, distancia):
    
    acimut = math.radians(acimut)

    valor_proyecciones = []
    valor_proyecciones.append(math.sin(acimut)*distancia)
    valor_proyecciones.append(math.cos(acimut)*distancia)

    return valor_proyecciones

#[SOLICTA NUMERO DE DELTAS Y QUE SE INDIQUE SI LOS ANGULOS SON INTERNOS Y EXTERNOS]
def main():

    print()
    print('='*173)
    print()
    print('{:^173}'.format('A J U S T E  D E  P O L I G O N A L  P O R  E L  M E T O D O  D E  L A  B R U J U L A'))
    print()
    print('='*173)
    print()

    deltas = int(input('Digite el numero de deltas en la poligonal: '))
    ang_externos = int(input('¿Angulos externos [1 = SI] [0 = NO]: '))

    #[AL DEFINIR ANGULOS INTERNOS Y EXTERNOS CALCULA SUMATORIA TEORICA DE ANGULO]
    if ang_externos == 1:
        suma_teorica_ang = (deltas + 2) *180
    else:
        suma_teorica_ang = (deltas - 2) *180

    #[SOLICITA LAS COORDENADAS DEL PUNTO DE ARMADA Y DEL PUNTO DE REFERENCIA]
    x_inicio = float(input('Digite la coordenada X (E) del punto de inicio: '))
    y_inicio = float(input('DIgite la coordenada Y (N) del punto de inicio: '))
    x_referencia = float(input('Digite la coordena X (E) del punto de referencia: '))
    y_referencia = float(input('Digite la coordena Y (N) del punto de referencia: '))

    #[IMPRIME EL ACIMUT DE REFERENCIA]
    acimut_ref = acimut_linea(x_inicio, y_inicio, x_referencia, y_referencia)
    print('\n', f'El acimut calculado es: {dec2gms(acimut_ref)}')

    #[IMPRIME LA SUMATORIA TEORICA DE ANGULOS]
    print(f'La sumatoria teórica de ángulos es: {suma_teorica_ang}°')

    #[ALMACENA LOS DATOS CAPTURADOS EN LISTAS]
    datos_medidos = []
    datos_medidos.append (['DELTA','ANG OBSER', 'DIST', 'ANG OBSERV DEC', 'ANG OBSER CORREG', 'AZIMUTH', 'PRY X', 'PRY Y', 'PRY X COREG', 'PRY Y COREG', 'COORD X', 'COORD Y'])

    j = 0
    sumang = 0.0
    sumdist = 0.0

    #[SOLICITA LOS DATOS DE CADA DELTA, NOMBRE, ANGULO Y DISTANCIA]
    # CON NUMERO DE DELTAS Y ANGULOS OBSERVADOS REALIZA LA SUMA DE ANGULOS
    # CALCULA EL ERROR ANGULAR Y LA CORRECCION ANGULAR
    # IMPRIME EL ERROR ANGULAR
    # IMPRIME LA CORRECCION ANGULAR
    
    for delta in (range(deltas+1)):
        print('='*80)

        nombre_delta = input(f'Digite el nombre del delta {delta+1}: ')
        ang_observado = float(input(f'Digite el angulo observado {delta+1}: '))
        distancia = float(input(f'Digite la dista de la linea {delta+1}: '))

        print('='*80)

        datos_linea = [nombre_delta, ang_observado, distancia, gms2dec(ang_observado)]
        datos_medidos.append(datos_linea.copy())

        if j != 0:
            sumdist = sumdist + distancia
            sumang = sumang + datos_linea[3]
            j += 1
        else:
            j += 1
    
    error_angular = suma_teorica_ang - sumang
    correccion_angular = error_angular / deltas
    
    print('El error angular es:', error_angular)
    print('La corrección angular es:', correccion_angular)

    datos_medidos[1].append(datos_medidos[1][3])
    datos_medidos[1].append(acimut_ref + datos_medidos[1][3])

    #[VARIABLES DE SUMA DE PROYECCIONES]
    i = 0
    suma_px = 0.0
    suma_py = 0.0
    proyec_punto = []

    #[CALCULA CORRECCIONES A ANGULO, ACIMUT Y PROYECCIONES ]
    for dato in datos_medidos:

        if i < 2:
            i += 1
            continue
        
        datos_medidos[i].append(datos_medidos[i][3] + correccion_angular)

        if datos_medidos[i-1][4] >= 180:
            acimut_deltas = datos_medidos[i-1][5] - 180 + datos_medidos[i][4]
        else:
            acimut_deltas = datos_medidos[i-1][5] + 180 + datos_medidos[i][4]
        
        if acimut_deltas >= 360:
            acimut_deltas -= 360

        datos_medidos[i].append(acimut_deltas)

        proyec_punto = proyecciones(acimut_deltas, datos_medidos[i][2])

        datos_medidos[i].append(proyec_punto[0])
        datos_medidos[i].append(proyec_punto[1])

        suma_px += datos_medidos[i][6]
        suma_py += datos_medidos[i][7]

        i += 1

    print()

    datos_medidos [1][:] += [0, 0, 0, 0, x_inicio, y_inicio]

    #[ALMACENA LAS PROYECCIONES CORREGIDAS EN LA LISTA]
    i = 0

    for dato in datos_medidos:

        if i < 2:
            i += 1
            continue

        #[CALCULA EL ERROR DE LAS PROYECCIONES]
        datos_medidos[i].append(datos_medidos[i][6] - (suma_px / sumdist)*datos_medidos[i][2])
        datos_medidos[i].append(datos_medidos[i][7] - (suma_py / sumdist)*datos_medidos[i][2])

        #[CALCULA COORDENADAS]
        datos_medidos[i].append(datos_medidos[i-1][10] + datos_medidos[i][8])
        datos_medidos[i].append(datos_medidos[i-1][11] + datos_medidos[i][9])

        i += 1

    #[IMPRIME DATOS CALCULADOS]
    print()

    print('='*173)
    print('{:^10}'.format('DELTA'), '{:^8}'.format('ANGULO'), '{:^8}'.format('DISTANC'), '{:^10}'.format('ANGULO'), '{:^10}'.format('AZIMUTH'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^11}'.format('COORDEN'), '{:^11}'.format('COORDEN'), sep='\t')

    print('{:^10}'.format(''), '{:^8}'.format('OBSERV'), '{:^8}'.format('(m)'), '{:^10}'.format('CORREGIDO'), '{:^10}'.format(''), '{:^10}'.format('X'), '{:^10}'.format('Y'), '{:^10}'.format('CORR X'), '{:^10}'.format('CORR Y'), '{:^11}'.format('X'), '{:^11}'.format('Y'), sep='\t')
    print('='*173)

    i = 0

    for dato in datos_medidos:
        if i == 0:
            i += 1
            continue

        print('{:^10}'.format(dato[0]),'{:8.4f}'.format(dato[1]), '{:8.4f}'.format(dato[2]), '{:10}'.format(dec2gms(dato[4])), '{:10}'.format(dec2gms(dato[5])), '{:+010.3f}'.format(dato[6]), '{:+010.3f}'.format(dato[7]), '{:+010.3f}'.format(dato[8]), '{:+010.3f}'.format(dato[9]), '{:11.3f}'.format(dato[10]), '{:11.3f}'.format(dato[11]), sep='\t')

        i += 1

    print('='*173)


if __name__ == '__main__':
    main()