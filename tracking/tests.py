from django.test import TestCase
from rest_framework.test import APIRequestFactory
import json
from tracking.models import Ship, Position
from tracking.views import ships_list, ships_position


class ShipTestCase(TestCase):
    def setUp(self):
        Ship.objects.create(name="Mathilde Maersk", imo="9632179")
        Ship.objects.create(name="Australian Spirit", imo="9247455")

    def test_correct_ship_output(self):
        """ Tests the correct output of the model """
        mathilde = Ship.objects.get(imo="9632179")
        australian = Ship.objects.get(imo="9247455")
        self.assertEqual(str(mathilde), '9632179, Mathilde Maersk')
        self.assertEqual(str(australian), '9247455, Australian Spirit')


class PositionTestCase(TestCase):
    def setUp(self):
        Ship.objects.create(name="Mathilde Maersk", imo="9632179")
        self.ship = Ship.objects.get(imo="9632179")
        Position.objects.create(
            timestamp="2019-01-15T08:12:20Z", imo=self.ship,
            latitude="51.5519828796387", longitude="51.8737335205078")
        Position.objects.create(
            timestamp="2019-01-15T09:44:27Z", imo=self.ship,
            latitude="51.8737335205078", longitude="2.73133325576782")
        Position.objects.create(
            timestamp="2019-01-15T05:51:33Z", imo=self.ship,
            latitude="51.0502815246582", longitude="1.60008335113525")
        self.factory = APIRequestFactory()

    def test_correct_position_output(self):
        """ Tests the correct output of the model """
        position = Position.objects.filter(imo=self.ship.pk)
        self.assertEqual(
            str(position[1]), '9632179, Mathilde Maersk, 51.8737335205078, 2.73133325576782')

    def test_get_ship_list(self):
        """ Testing the ship list endpoint """
        request = self.factory.get('/api/ships')
        response = ships_list(request)
        response.render()
        self.assertEqual(json.loads(response.content), [
            {
                'name': "Mathilde Maersk",
                'imo': '9632179'
            }
        ])

    def test_get_positions_endpoint(self):
        """ Checking the endpoint is returning the correct data in the correct order"""
        expected_data = [
            {
                "ship": {
                    "imo": "9632179",
                    'name': "Mathilde Maersk",
                },
                "timestamp": "2019-01-15T09:44:27Z",
                "latitude": "51.8737335205078",
                "longitude": "2.73133325576782"
            },
            {
                "ship": {
                    "imo": "9632179",
                    'name': "Mathilde Maersk",
                },
                "timestamp": "2019-01-15T08:12:20Z",
                "latitude": "51.5519828796387",
                "longitude": "51.8737335205078"
            },
            {
                "ship": {
                    "imo": "9632179",
                    'name': "Mathilde Maersk",
                },
                "timestamp": "2019-01-15T05:51:33Z",
                "latitude": "51.0502815246582",
                "longitude": "1.60008335113525"
            },
        ]
        request = self.factory.get('/api/positions/9632179')
        response = ships_position(request, imo='9632179')
        response.render()
        self.assertEqual(json.loads(response.content), expected_data)

    def test_not_existentShip(self):
        """ Checking that an error message is returned when is requested
        a position of a non existing ship """
        expected_return = {"error": "Item '1111222' not found"}
        request = self.factory.get('/api/positions/1111222')
        response = ships_position(request, imo='1111222')
        response.render()
        self.assertEqual(json.loads(response.content), expected_return)
