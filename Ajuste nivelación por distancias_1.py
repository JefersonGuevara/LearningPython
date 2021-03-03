#nivelacion simple ajuste por número de cambios
import math
print()
print('='*173)
print()
print('{:^173}'.format('A J U S T E  D E  N I V E L A C I Ó N   P O R  D I S T A N C I A S'))
print()
print('='*173)
print()
BMS = int(input('Digite el número de BMS de la nivelación: '))
precisión = int(input('¿precisión del equipo [1 = 1mm] [0 = 2mm]: '))

#[AL DEFINIR PRECISIÓN CALCULA ERROR TEORICO PERMISIBLE DE LA NIVELACIÓN]
if precisión == 1:
    error_permitido = (BMS * 1)
else:
    error_permitido = (BMS * 2)
#[IMPRIME EL ERROR PERMITIDO DE ACUERDO CON LA PRECISIÓN DEL EQUIPO]
print(f'el error permitido de acuerdo con precisión del equipo es: {error_permitido}mm')
#[SOLICITA LA COTA DEL BM DE PARTIDA]
BM = float(input('Digite la cota del BM de inicio: '))
#VMAS_inicio = float(input('Digite la vista mas: '))
    
#[IMPRIME LA HI DE REFERENCIA]
#hi_ref = (BM + VMAS_inicio)
#print('\n', f'La ALTURA INSTRUMENTAL calculada es: {hi_ref}')
#[ALMACENA LOS DATOS CAPTURADOS EN LISTAS]
datos_medidos = []
j = 0
sumVMAS = 0.0
sumVMENOS = 0.0
sumdist_menos = 0.0
sumdist_mas = 0.0

#[SOLICITA LOS DATOS DE CADA BM, NOMBRE, VISTA +, VISTA - Y DISTANCIA]
# CON NUMERO DE BM´S Y DIST OBSERVADOS REALIZA LA SUMA DE ANGULOS
# CALCULA EL ERROR EN COTA Y LA CORRECCION 
# IMPRIME EL ERROR EN COTA
# IMPRIME LA CORRECCION EN COTA
    
for i in (range(BMS)):
    print('='*80)
    i=i+1
    punto = input(f'Digite el nombre del punto {i}: ')
    vistaMas = float(input(f'Digite la vista más observada {i}: '))
    distancia_mas = float(input(f'Digite la distancia más observada {i}: '))
    vistaMenos = float(input(f'Digite la vista menos observada {i}: '))
    distancia_menos = float(input(f'Digite la distacia menos observada {i}: '))
 

    print('='*80)

    datos_linea = [punto, vistaMas, distancia_mas, vistaMenos, distancia_menos]
    datos_medidos.append(datos_linea.copy())
    sumVMAS = sumVMAS + vistaMas
    sumVMENOS = sumVMENOS + vistaMenos
    sumdist_menos = sumdist_menos + distancia_menos
    sumdist_mas = sumdist_mas + distancia_mas
'''
datos_linea = ['BM1', 1.50, 15, 2, 10 ]
datos_medidos.append(datos_linea.copy())
datos_linea = ['BM2', 1.99, 15, 1.50, 10 ]
datos_medidos.append(datos_linea.copy())
sumVMAS=3.49
sumVMENOS=3.50
sumdist_mas=30
sumdist_menos=20
'''
error = round(sumVMAS -  sumVMENOS,8)

print(f'Error de cierre es: {error}')
sumatoria_total_distancia = sumdist_menos + sumdist_mas
print(f'Distancia Total es: {sumatoria_total_distancia}')
correccion = round(error / sumatoria_total_distancia,6)
print(f'Corrección es: {correccion}')

contador = 0
##calculamos ajuste vista +
for dato in  datos_medidos:
    calculado = correccion * dato[2]
    datos_medidos[contador].append(calculado)
    contador=contador+1;
contador = 0
##calculamos ajuste vista -
for dato in  datos_medidos:
    calculado = correccion * dato[4]
    datos_medidos[contador].append(calculado)
    contador=contador+1;

contador = 0
##calculamos v+ corregida
for dato in  datos_medidos:
    calculado = dato[1] - dato[5]
    datos_medidos[contador].append(calculado)
    contador=contador+1;
contador = 0
##calculamos v- corregida
for dato in  datos_medidos:
    calculado = dato[3] + dato[6]
    datos_medidos[contador].append(calculado)
    contador=contador+1;


calculado = BM + datos_medidos[0][7]
datos_medidos[0].append(calculado)
datos_medidos[0].append(BM)
contador = 1
##calculamos altura instrumental
for dato in  datos_medidos:
    if contador == BMS:
        continue
    cota_temporal = calculado - datos_medidos[contador-1][8]
    hi_temporal     = cota_temporal + datos_medidos[contador][7]
    
    datos_medidos[contador].append(hi_temporal)
    datos_medidos[contador].append(cota_temporal)
    contador=contador+1;
    
##Comprobación del cierre
comprobacion =math.ceil((datos_medidos[BMS-1][10] +  datos_medidos[BMS-1][7] ) - datos_medidos[BMS-1][8]) 
 
if comprobacion == BM:
    print(f'La comprobación  esta correcta por que: {comprobacion} es igual {BM}')

contador = 0
##imprimir 

print('='*173)
print('{:^10}'.format('PUNTO'), '{:^8}'.format('Vista+'), '{:^8}'.format('Distancia+'), '{:^10}'.format('Vista-'), '{:^10}'.format('Distancia-'), '{:^10}'.format('AjusteVista+'), '{:^10}'.format('AjusteVista-'), '{:^10}'.format('Vista+Corregida'), '{:^10}'.format('Vista-Corregida'), '{:^11}'.format('AlturaInstrumental'), '{:^11}'.format('Cota'), sep='\t')

for dato in datos_medidos:

        print('{:^10}'.format(dato[0]),'{:8.4f}'.format(dato[1]), '{:8.4f}'.format(dato[2]),'{:10}'.format(dato[3]), '{:10}'.format(dato[4]), '{:10}'.format(dato[5]), '{:+010.3f}'.format(dato[6]), '{:+010.3f}'.format(dato[7]), '{:+010.3f}'.format(dato[8]), '{:+010.3f}'.format(dato[9]), '{:11.3f}'.format(dato[10]), sep='\t')


print('='*173)
   