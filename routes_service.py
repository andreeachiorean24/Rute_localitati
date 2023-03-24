from typing import List

from Domain.route import Route
from Repository.repository import Repository
from ViewModel.RouteWithCities import RouteWithCities


class RoutesService:
    def __init__(self,
                 routes_repository: Repository,
                 city_repository: Repository):
        """
        Creeaza un service pentru rute.
        :param routes_repository: repository
               care retine rute.
        :param city_repository: repository
               pentru localitati
        """
        self.routes_repository = routes_repository
        self.city_repository = city_repository

    def add_route(self,
                  id_route: str,
                  id_start_city: str,
                  id_stop_city: str,
                  price: float,
                  return_route: bool):
        """

        :param id_start_city:
        :param id_stop_city:
        :param price:
        :param return_route:
        :return:
        """
        route = Route(id_route,
                      id_start_city,
                      id_stop_city,
                      price,
                      return_route)
        errors = []
        if self.city_repository.read(id_start_city) is None:
            errors.append(f'Nu exista oras cu id-ul {id_start_city}')
        if self.city_repository.read(id_stop_city) is None:
            errors.append(f'Nu exista oras cu id-ul {id_stop_city}')
        if id_stop_city == id_start_city:
            errors.append('id-urile oraselor de pornire si sosire '
                          'nu pot fi egale!')
        if errors:
            raise ValueError(errors)
        self.routes_repository.create(route)

    def get_all(self) -> List[Route]:
        """
        :return: o lista cu toate localitatile
        """
        return self.routes_repository.read()

    def get_cities_ordered_by_return_routes(self):
        """

        :return:
        """
        result = []
        lst_city = self.city_repository.read()
        lst_routes = self.routes_repository.read()
        for city in lst_city:
            routes_from_city = [route for route in lst_routes if
                                route.return_route and
                                route.id_start_city == city.id_entity]
            result.append((city, len(routes_from_city)))

        return sorted(result, key=lambda x: x[1])

    def routes_for_municipiu(self):
    #     Afișarea tuturor rutelor care se opresc într-o localitate minicipiu.
    #     Se vor afișa și denumirile localităților între care e definită ruta
        result = []
        for route in self.routes_repository.read():
            route_with_cities = RouteWithCities(
                route.id_entity,
                self.city_repository.read(route.id_start_city),
                self.city_repository.read(route.id_stop_city),
                route.price,
                route.return_route
            )
            if route_with_cities.stop_city.type == 'municipiu':
                result.append(route_with_cities)

        return result

