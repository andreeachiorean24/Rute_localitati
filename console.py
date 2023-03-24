from datetime import date

from Service.city_service import CityService
from Service.routes_service import RoutesService


class Console:
    def __init__(self,
                 city_service: CityService,
                 routes_service: RoutesService):
        self.city_service = city_service
        self.routes_service = routes_service

    def show_menu(self):
        print('1.Adauga localitate')
        print('2.Adauga ruta')
        print('sl. Afiseaza localitatiile')
        print('sr. Afiseaza rutele')
        print('3.Afișarea loc ordonate crescător după numărul'
              ' de rute dus-întors care pornesc din ele.')
        print('4. Afișarea tuturor rutelor care se opresc'
              ' într-o localitate minicipiu.')
        print('5. Export JSON.')
        print('6. Iesire')

    def run_console(self):
        while True:
            self.show_menu()
            opt = input('Optiunea aleasa:')
            if opt == '1':
                self.handle_add_city()
            elif opt == '2':
                self.handle_add_route()
            elif opt == 'sl':
                self.handle_show_all(self.city_service.get_all())
            elif opt == 'sr':
                self.handle_show_all(self.routes_service.get_all())
            elif opt == '3':
                self.handle_show_all(
                    self.routes_service.get_cities_ordered_by_return_routes())
            elif opt == '4':
                self.handle_show_all(self.routes_service.routes_for_municipiu())
            elif opt == '6':
                break
            else:
                print('Optiune invalida')

    def handle_add_city(self):
        try:
            id_city = input('Id-ul localitatii: ')
            name = input('Numele localitatii: ')
            type = input('Tipul localitatii (sat, oras, municipiu): ')

            self.city_service.add_city(id_city, name, type)
        except ValueError as ve:
            print('Eroare validare:', ve)
        except KeyError as ke:
            print('Eroare ID:', ke)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_add_route(self):
        try:
            id_route = input('Id-ul rutei: ')
            id_start_city = input('Id-ul orasului de pornire: ')
            id_stop_city = input('Id-ul orasului de sosire: ')
            price = float(input('Pretul: '))
            return_route = input('Dus intors? da / nu')

            if return_route == 'da':
                return_route = True
            else:
                return_route = False

            self.routes_service.add_route(id_route,
                                          id_start_city,
                                          id_stop_city,
                                          price,
                                          return_route)
        except ValueError as ve:
            print('Eroare validare:', ve)
        except KeyError as ke:
            print('Eroare ID:', ke)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_show_all(self, entities):
        for entity in entities:
            print(entity)

    def readDate(self):
        givenString = input('Dati data, cu elem separate printr-o liniuta: ')
        numbersAsString = givenString.split('-')
        year = int(numbersAsString[0])
        month = int(numbersAsString[1])
        day = int(numbersAsString[2])
        return date(year, month, day)

