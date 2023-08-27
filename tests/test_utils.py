from src.utils import get_executed_operations,sorted_result_list, operation_details, date_to_str
import pytest


@pytest.fixture()
def sample_data():
    return  [
              {
                "id": 441945886,
                "state": "CANCELED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                  "amount": "31957.58",
                  "currency": {
                    "name": "руб.",
                    "code": "RUB"
                  }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
              },
              {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2023-07-03T18:35:29.512364",
                "operationAmount": {
                  "amount": "8221.37",
                  "currency": {
                    "name": "USD",
                    "code": "USD"
                  }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
              },
              {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                  "amount": "9824.07",
                  "currency": {
                    "name": "USD",
                    "code": "USD"
                  }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
              }
            ]
def test_get_executed_operations(sample_data):
    executed_list = get_executed_operations(sample_data)
    assert len(executed_list) == 2


# def test_date_time():
#    assert


def test_sorted_result_list(sample_data):
    sorted_list = sorted_result_list(sample_data)
    assert sorted_list[0]["id"] == 41428829
    assert sorted_list[-1]["id"] == 939719570



def test_operation_details():
    assert operation_details(None) == "Нет информации"
    assert operation_details("Счет 44812258784861134719") == "Счет **4719"
    assert operation_details("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_date_to_str():
    assert date_to_str({"date": "2018-04-04T17:33:34.701093"}) == "04.04.2018"
