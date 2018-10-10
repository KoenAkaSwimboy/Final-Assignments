def inlezen_beginstation(stations):
    bs = input('Wat is uw beginstation? ')
    while bs not in stations:
      print('Het station wat u heeft opgegeven komt niet voor in dit traject')
      bs = input('Wat is uw beginstation? ')

    return bs


def inlezen_eindstation(stations, beginstation):
    es = input('Wat is uw eindstation? ')
    if es == beginstation:
        print('Wat? Beste persoon u kunt niet in en uitstappen in het zelfde station denk na manmanman')
        exit()
    while es not in stations:
      print('Het station wat u heeft opgegeven komt niet voor in dit traject')
      es = input('Wat is uw eindstation? ')

    while stations.index(es) < stations.index(beginstation):
        print('Het eindstation kan niet voor het beginstation komen')
        es = input('Wat is uw eindstation? ')
    return es

def omroepen_reis(stations, beginstation, eindstation):
    print('Het beginstation ', beginstation, 'is het ', stations.index(beginstation) + 1 , 'e ', 'station in dit traject')
    print('Het eindstation ', eindstation, 'is het ', stations.index(eindstation) + 1, 'e ', 'station in dit traject')
    begin = stations.index(beginstation)
    eind = stations.index(eindstation)
    aantal =  eind - begin
    print('De afstand bedraagt', aantal, 'station(s)')
    prijs = aantal * 5
    print('De prijs van het kaartje is', prijs, 'euro \n')
    print('Jij stapt in de trein in: ', beginstation)
    lijst = stations[begin+1:eind]
    for x in lijst:
        print('- ' + x)
    print('Jij stapt uit de trein in: ', eindstation)
stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)



